import os
import json
ff = fontforge

config = json.load(open("config/font.json"))
quotes = json.load(open("config/quotes.json"))

license = open("LICENSE")
license = license.read()

base_dir = "variants/"
temp_dir = "TEMP/"

styles = [ "Regular", "Bold", "Italic", "Bold Italic" ]

def style_it(pack_name, pack_config, style):
	font = ff.open(base_dir + "basis.ttf")
	is_bold   = style == "Bold"   or style == "Bold Italic"
	is_italic = style == "Italic" or style == "Bold Italic"

	space = font["space"]

	if is_bold:
		space.width = 640
	else:
		space.width = 512
	#if

	for component in pack_config["basis"]:
		if component == "_":
			component = pack_name

		print(f'{component} for {pack_name}')

		regular_font = base_dir + component + "/Regular.ttf"
		bold_font    = base_dir + component + "/Bold.ttf"
		italic_font  = base_dir + component + "/Italic.ttf"

		if is_bold and os.path.isfile(bold_font):
			print("merge bold")
			font.mergeFonts(bold_font)
		#if

		if not is_bold and os.path.isfile(regular_font):
			print("merge regular")
			font.mergeFonts(regular_font)
		#if
	#for

	if is_italic:
		font.selection.all()
		font.transform(psMat.skew(0.20944))
	#if

	def appendSFNTName(string_id, value):
		font.appendSFNTName("English (US)", string_id, value)
	#def

	id_name = f'{config["id"]}-{pack_name}'
	full_name = f'{config["name"]} {pack_name} {style}'

	font.fontname = id_name
	font.familyname = full_name
	font.sfntRevision = config["version"]

	appendSFNTName("Fullname", full_name)
	appendSFNTName("UniqueID", id_name)
	appendSFNTName("Version", "Version " + str(config["version"]))
	appendSFNTName("SubFamily", style)
	appendSFNTName("Descriptor", config["description"]["default"])
	appendSFNTName("Copyright", "© macimas")
	appendSFNTName("License", license)

	for export in config["exports"]:
		pack_dir = f'{temp_dir}/{pack_name} {export}'

		if (not os.path.isdir(pack_dir)):
			os.mkdir(pack_dir)
		#if

		font.generate(f'{pack_dir}/{full_name}.{export}')
	#for

	font.close()
#def

for pack_name, pack_config in config["packs"].items():
	for style in styles:
		style_it(pack_name, pack_config, style)
	#for
#for