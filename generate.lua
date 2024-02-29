local config = require("config")
local quotes = config.quotes
local styles = { "Regular", "Bold", "Italic", "Bold Italic" }

-- do the generating stuff

local fonts_list = {}

for i, pack in ipairs(config.packs) do
	local id = table.concat({ config.id, pack.id }, "-")
	
	local basis = pack.basis
	table.sort(basis, function (a, b); return a > b; end)

	if (basis[1] == "_") then
		basis[1] = pack.id
	end

	print(string.format(" (🐔) working on %s...", pack.id))

	for i, style in ipairs(styles) do
		local name = table.concat({ config.name, pack.id }, " ")
		local full_name = table.concat({ name, style }, " ")

		local generate_cli = string.format(
			'fontforge generate.ff "%s" "%s" "%s" &> /dev/null',
			full_name, style, table.concat(basis, "|")
		)

		local result = os.execute(generate_cli) or os.exit(1)

		print(string.format(
			"  ^^ (🐣) %s%s",
			style, quotes[math.random(#quotes)]
		))

		table.insert(fonts_list, { id, name, full_name, style })
	end
end

-- info set

for i, font in ipairs(fonts_list) do
	fonts_list[i] = table.concat(font, "/")
end

fonts_list = table.concat(fonts_list, "|")

os.execute(string.format(
	'fontforge --quiet --script infoset.py "%s" "%s"',
	fonts_list, config.version
))

print(" (🛖) finished!")