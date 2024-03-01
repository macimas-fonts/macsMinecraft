local config = {
	id      = "macimas-Minecraft",
	name    = "mac's Minecraft",
	version = 1.02,

	packs = {
		{ id = "Main",     basis = { "_" } },
		{ id = "Tweaked",  basis = { "_", "Main" } },
		{ id = "Extended", basis = { "_", "Main" } },

		{ id = "Illageralt",         basis = { "_" } },
		{ id = "Illageralt Tweaked", basis = { "_", "Illageralt" }}
	},

	quotes = {
		" is ready!",
		" has been baked!",
		" is feelin ready!",
		" is feelin good!",
		", the legendary warrior, appears!",
		" has joined the server!",
		" has arrived!",
		" is here!",
		" has brought pizza!"
	}
}

return config