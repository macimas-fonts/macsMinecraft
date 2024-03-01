local config = require("config")
local quotes = config.quotes
local styles = { "Regular", "Bold", "Italic", "Bold Italic" }

os.execute("mkdir temp; mkdir base")

-- do the generating stuff

local fonts_list = {}

for i, pack in ipairs(config.packs) do
	local id = table.concat({ config.id, pack.id }, "-")

	local basis = pack.basis
	table.sort(basis, function (a, b); return a > b; end)

	if (basis[1] == "_") then
		basis[1] = pack.id
	end

	print()
	print(string.format(" (🐔) working on %s...", pack.id))

	for i, style in ipairs(styles) do
		local name_table = { config.name }
		if not (pack.id == "Main") then
			name_table[2] = pack.id
		end

		local name = table.concat(name_table, " ")
		local full_name = table.concat({ name, style }, " ")

		local generate_cli = string.format(
			'fontforge generate.ff "%s" "%s" "%s" &> /dev/null',
			full_name, style, table.concat(basis, "|")
		)

		local result = os.execute(generate_cli)
		local result = result or os.exit(1)

		print(string.format(
			"  -- (🐣) %s%s",
			style, quotes[math.random(#quotes)]
		))

		table.insert(fonts_list, { id, name, full_name, style })
	end
end

print(" (🛖) finished!")
print()

-- export

for i, font in ipairs(fonts_list) do
	fonts_list[i] = table.concat(font, "/")
end

fonts_list = table.concat(fonts_list, "|")

local infoset_cli = string.format(
	'fontforge --quiet --script export.py "%s" "%s" "%s"',
	fonts_list, table.concat(config.exports, "|"), config.version
)

local result = os.execute(infoset_cli)
local result = result or os.exit(1)

-- zip them up

print(" (📥️) zipping...")

for i, pack in ipairs(config.packs) do
	for i, export in ipairs(config.exports) do
		local pack_name_table = { config.name, export }

		if not (pack.id == "Main") then
			table.insert(pack_name_table, 2, pack.id)
		end

		local pack_name = table.concat(pack_name_table, " ")
		local zip_cli = string.format(
			'find "temp/%s" -print0 | xargs -0 zip -q -j "build/%s.zip" || exit 1',
			pack_name, pack_name
		)

		local result = os.execute(zip_cli)
		local result = result or os.exit(1)

		print(string.format("  -- (📦) zipped %s!", pack_name))
	end
end

print(" (📬) finished!")
print()