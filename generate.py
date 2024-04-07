import os
import json
import random
import re
import zipfile
ff = fontforge

config = json.load(open("config/font.json"))
quotes = json.load(open("config/quotes.json"))

license = open(config["license_file"])
license = license.read()

base_dir = config["base_dir"]
temp_dir = config["temp_dir"]

if not os.path.isdir(temp_dir):
	os.mkdir(temp_dir)

styles = [ "Regular", "Bold", "Italic", "Bold Italic" ]
stylemap = {
	"Regular":     0x40,
	"Italic":      0x01,
	"Bold":        0x20,
	"Bold Italic": 0x21
}

def style_it(pack_name, pack_config, style):
	font = ff.open(base_dir + "basis.ttf")
	is_bold   = style == "Bold"   or style == "Bold Italic"
	is_italic = style == "Italic" or style == "Bold Italic"

	space = font["space"]

	if is_bold:
		space.width = 640
	else:
		space.width = 512

	for component in pack_config["basis"]:
		if component == "_":
			component = pack_name

		regular_font = base_dir + component + "/Regular.ttf"
		bold_font    = base_dir + component + "/Bold.ttf"
		italic_font  = base_dir + component + "/Italic.ttf"

		if is_bold and os.path.isfile(bold_font):
			font.mergeFonts(bold_font)

		if not is_bold and os.path.isfile(regular_font):
			font.mergeFonts(regular_font)

	if is_italic:
		font.selection.all()
		font.transform(psMat.skew(0.20944))

	def appendSFNTName(string_id, value):
		font.appendSFNTName("English (US)", string_id, value)

	id_name = f'{config["id"]}-{pack_name}'
	full_name = f'{config["name"]} {pack_name} {style}'

	font.fontname = id_name
	font.os2_stylemap = stylemap[style]
	font.sfntRevision = config["version"]

	if pack_name == "Main":
		font.familyname = config["name"]
	else:
		font.familyname = f'{config["name"]} {pack_name}'

	appendSFNTName("Fullname", full_name)
	appendSFNTName("UniqueID", id_name)
	appendSFNTName("Version", "Version " + str(config["version"]))
	appendSFNTName("SubFamily", style)
	appendSFNTName("Descriptor", config["description"]["default"])
	appendSFNTName("Copyright", "© macimas")
	appendSFNTName("License", license)

	for glyph in font.selection.all().byGlyphs:
		if glyph.foreground.isEmpty():
			if glyph.glyphname not in ["space", ".notdef", ".null", "uni000D"]:
				font.removeGlyph(glyph)

	for export in config["exports"]:
		zip_main_name = re.sub(config["name_filter"], "", config["name"])
		zip_style = re.sub(config["name_filter"], "", style)
		
		if pack_name == "Main":
			zip_pack_name = ""
		else:
			zip_pack_name = re.sub(config["name_filter"], "", pack_name)

		pack_dir = f'{temp_dir}/{zip_main_name}{zip_pack_name}+{export}'

		if (not os.path.isdir(pack_dir)):
			os.mkdir(pack_dir)

		font.generate(f'{pack_dir}/{zip_main_name}{zip_pack_name}-{zip_style}.{export}')

	font.close()


for pack_name, pack_config in config["packs"].items():
	print(f'(🐔) working on {pack_name}...')

	for style in styles:
		style_it(pack_name, pack_config, style)

		print(f'-- (🐣) {random.choice(quotes).format(style)}')

	print(f'(🛖) {pack_name} is done!')

print('(🤐) zipping...')


for font_dir in os.listdir(temp_dir):
	font_dir = temp_dir + font_dir;
	if os.path.isdir(font_dir):
		zip = zipfile.ZipFile(font_dir + ".zip", mode="w")
		
		for f in os.listdir(font_dir):
			zip.write(font_dir + "/" + f, arcname=f);
		
		zip.close();
		
		print(f'-- (📂) zipped {font_dir}')

print('(🗃️) done!!!')