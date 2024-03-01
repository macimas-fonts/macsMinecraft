from os import mkdir
from os.path import isdir

print(" (🌟) exporting...")

ff = fontforge

temp_dir = "./temp/"
fonts_list = str.split(sys.argv[1], "|")
exports = str.split(sys.argv[2], "|")
version = float(sys.argv[3])
license = open("LICENSE")
license = license.read()

for (i, font) in enumerate(fonts_list):
	fonts_list[i] = tuple(str.split(font, "/"))

for (pack_id, pack_name, full_name, style) in fonts_list:
	font_hand = temp_dir + full_name
	font = ff.open(font_hand + ".ttf")

	def appendSFNTName(string_id, value):
		font.appendSFNTName("English (US)", string_id, value)

	font.fontname = pack_id
	font.familyname = pack_name
	font.sfntRevision = version

	appendSFNTName("Fullname", full_name)
	appendSFNTName("UniqueID", pack_name)
	appendSFNTName("Version", "Version " + str(version))
	appendSFNTName("SubFamily", style)
	appendSFNTName("Descriptor", "a rough 1:1 recreation of the Minecraft font")
	appendSFNTName("Copyright", "© macimas")
	appendSFNTName("License", license)

	for export in exports:
		pack_dir = f'{temp_dir}/{pack_name} {export}'

		if (not isdir(pack_dir)):
			mkdir(pack_dir)

		font.generate(f'{pack_dir}/{full_name}.{export}')

	print(f'  -- (🌠) exported {full_name}!')

print(" (🌄) finished!")
print()