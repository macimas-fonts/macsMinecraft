-- this script is probably bad

packages = {
	{"macimas-Minecraft", "mac's Minecraft", "1.0", 0, 0},
	{"macimas-Extended-Minecraft", "mac's Extended Minecraft", "1.0", 1, 0},
	{"macimas-Tweaked-Minecraft", "mac's Tweaked Minecraft", "1.0", 1, 1}
}
exports = {
	"ttf",
	"otf",
	"woff2"
}
quotes = {
	" is ready!",
	" has been baked!",
	" is feelin ready!",
	" is feelin good!",
	", the legendary warrior, appears!",
	" has joined the server!",
}


print(">>> generating…")
os.execute("mkdir temp; mkdir build")

ff_packages = {}

for i, pack in ipairs(packages) do
	ff_packages[i] = table.concat(pack, "…")
end

ff_packages = table.concat(ff_packages, "|")
ff_exports = table.concat(exports, "|")
ff_quotes = table.concat(quotes, "|")

build_exec = string.format(
	'fontforge -quiet generate.ff "%s" "%s" "%s"',
	ff_packages, ff_exports, ff_quotes
)

build = os.execute(build_exec)

if (not build) then os.exit(1) end
print(">>> done generating!")


print(">>> zipping…")

zip_exec = 'find temp -name "%s*.%s" -print0 | xargs -0 zip -q -j "build/%s %s.zip" || exit 1'
for i, pack in pairs(packages) do
	local pack = pack[2]
	for i, export in pairs(exports) do
		local exec = string.format(zip_exec, pack, export, pack, export)
		os.execute(exec)
		print(string.format("--- zipped %s %s!", pack, export))
	end
end

print(">>> done zipping!")