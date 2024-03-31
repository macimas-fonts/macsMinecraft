local pack_id = arg[1]
	or error "no id?"
local dir = string.format("fonts/%s/", pack_id)
local regular_dir = dir.."Regular/"
local bold_dir = dir.."Bold/"
local cli = 'cd "'..bold_dir..'"; find -maxdepth 1 -name "*.png" -printf "%P\n"'

os.execute('rm -rf "'..bold_dir..'"')
os.execute('cp -r "'..regular_dir..'" "'..bold_dir..'"')

local components = {}
for component in io.popen(cli):lines() do
	table.insert(components, component)
end

for i, name in ipairs(components) do
	local file = '"'..bold_dir..name..'"'
	local cli = "magick "..file.." -background none -repage +1+0 -flatten -fill none +opaque white -flatten "
		..file.." +swap -compose ATop -composite png24:"..file
	local result = os.execute(cli)
		or error ("cant bolden "..name)

	print("boldened "..name)
end
