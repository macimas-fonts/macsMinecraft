import os
import math
import json
import random
import re
import zipfile
ff = fontforge

config = json.load(open("config/font.json"))
config_glyphs = json.load(open("config/glyphs.json"))
quotes = json.load(open("config/quotes.json"))

config["font_skew"] = psMat.skew(math.radians(config["font_skew"]))

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
	font.uwidth = 128

	is_bold   = style == "Bold"   or style == "Bold Italic"
	is_italic = style == "Italic" or style == "Bold Italic"

	for component in pack_config["basis"]:
		if component == "_":
			name = pack_name
		else:
			name = component

		regular_font = base_dir + name + "/Regular.ttf"
		bold_font    = base_dir + name + "/Bold.ttf"

		if is_bold and os.path.isfile(bold_font):
			font.mergeFonts(bold_font)

		if not is_bold and os.path.isfile(regular_font):
			font.mergeFonts(regular_font)

	for glyph in font.selection.all().byGlyphs:
		if glyph.foreground.isEmpty():
			if glyph.glyphname not in ["space", ".notdef", ".null", "uni000D"]:
				font.removeGlyph(glyph)

	for component in pack_config["basis"]:
		logs = []
		for pattern in config_glyphs:
			if component == "_":
				name = pack_name
			else:
				name = component

			if name not in pattern["fonts"]:
				if component not in pattern["fonts"]:
					continue

			for glyph in list(pattern["glyphs"]):
				for glyph in font.selection.select(ord(glyph)).byGlyphs:
					props = pattern["props"]

					def set_prop(prop, value):
						if not hasattr(glyph, prop):
							return

						if prop in props:
							setattr(glyph, prop, value)

					def get_value(values):
						if is_bold:
							return values["Bold"]
						else:
							return values["Regular"]

					set_prop("width", get_value(props["width"]))

			logs.append(pattern)

			if logs:
				print(f'\033[93m   [💛] set glyphs in {name} [[{pattern["glyphs"]}]]\033[0m')
				print(f'\033[93m        props: {pattern["props"]}\033[0m')

	if is_italic:
		font.selection.all()
		font.transform(config["font_skew"])

	if is_bold:
		font.os2_weight = config["os2_weight"]["Bold"]
	else:
		font.os2_weight = config["os2_weight"]["Regular"]

	id_name = f'{config["id"]}-{pack_name}'
	full_name = f'{config["name"]} {pack_name} {style}'

	font.fontname = id_name
	font.os2_stylemap = stylemap[style]
	font.sfntRevision = config["version"]

	if pack_name == "Main":
		font.familyname = config["name"]
	else:
		font.familyname = f'{config["name"]} {pack_name}'

	def appendSFNTName(string_id, value):
		font.appendSFNTName("English (US)", string_id, value)

	appendSFNTName("Fullname", full_name)
	appendSFNTName("UniqueID", id_name)
	appendSFNTName("Version", "Version " + str(config["version"]))
	appendSFNTName("SubFamily", style)
	appendSFNTName("Descriptor", config["description"])
	appendSFNTName("Copyright", config["copyright"])
	appendSFNTName("License", license)

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


for pack_name, pack_config in config["fonts"].items():
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