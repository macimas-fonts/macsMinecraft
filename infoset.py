ff = fontforge

temp_dir = "./temp/"
fonts_list = str.split(sys.argv[1], "|")
version = float(sys.argv[2])

for i, font in enumerate(fonts_list):
	fonts_list[i] = tuple(str.split(font, "/"))


for pack_id, pack_name, full_name, style in fonts_list:
	font_dir = temp_dir + full_name + ".ttf"
	font = ff.open(font_dir)

	font.fontname = pack_id
	font.familyname = pack_name
	font.sfntRevision = version
	font.copyright = "macimas"

	font.appendSFNTName("English (US)", "Fullname", full_name)
	font.appendSFNTName("English (US)", "UniqueID", pack_name)
	font.appendSFNTName("English (US)", "Version", "Version " + str(version))
	font.appendSFNTName("English (US)", "Copyright", "© macimas")
	font.appendSFNTName("English (US)", "Descriptor", "a rough 1:1 recreation of the Minecraft font")
	
	font.generate(font_dir)