local JSON = require("lunajson")

local pack_id = arg[1] or error "no id?"
local dir = "variants/"..pack_id.."/"
local f = io.open("variants/basis.json", "r")
io.input(f)
local base_font_json = JSON.decode(io.read("*all"))
f:close()

function get_parts(style)
	local texts = {}
	local bitmaps = {}

	local dir = dir..style
	local cli = string.format('cd "%s"; find . -maxdepth 1 -name "*.txt"', dir)
	
	for text in io.popen(cli):lines() do
		text   = dir.."/"..string.sub(text, 3)
		bitmap = string.sub(text, 0, -4).."png"
		bitmap = '"'..bitmap..'"'
		table.insert(texts, text)
		table.insert(bitmaps, bitmap)
	end

	bitmaps = table.concat(bitmaps, " ")

	return { texts, bitmaps }
end

function combine(style)
	local parts = get_parts(style, dir)
	local text_files = parts[1]
	local bitmap_files = parts[2]
	local characters = {}

	for i, text_file in ipairs(text_files) do
		local f = io.open(text_file, "r")
		io.input(f)
		characters[i] = io.read("*all")
		f:close()
	end

	characters = table.concat(characters, "\n \n")
	
	local lines = {}
	local font_json = base_font_json
	for str in string.gmatch(characters, "([^\n]+)") do
		table.insert(lines, str)
	end

	font_json["in-glyphs"] = lines
	font_json["font-name"] = style

	local f = io.open(dir..style..".json", "w")
	io.output(f)
	io.write(JSON.encode(font_json))
	f:close()

	local cli = string.format(
		'convert -background black -smush 15 %s "png24:%s.png"',
		bitmap_files, dir..style
	)

	os.execute(cli)

	print("exported "..style)
end

local cli = string.format(
	'cd "%s"; find . -maxdepth 1 -type d',
	dir
)

for dir in io.popen(cli):lines() do
	local style = string.sub(dir, 3)

	if not (style == "") then
		combine(style)
	end
end