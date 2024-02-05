<img align="left" src="GITHUB/bennett.png" alt="strange grass block">

<h1>mac's Minecraft</h2>

a rough 1:1 recreation of Minecraft font

kudos to [YellowAfterlife's pixel font converter](https://yal.cc/r/20/pixelfont/)


<h2>packages</h2>

<img align="right" src="./GITHUB/mmm... font!.png">

<img align="center" src="./GITHUB/main%20package.png" alt="main">
<br>
→ *Minecraft font with bold and italic variants*
<br>
( 📥 ← [`ttf`][m ttf] [`otf`][m otf] [`woff2`][m woff2] )

[m ttf]: https://github.com/macimas/mac's%20Minecraft/raw/main/mac's%20Minecraft%20ttf.zip
[m otf]: https://github.com/macimas/mac's%20Minecraft/raw/main/mac's%20Minecraft%20otf.zip
[m woff2]: https://github.com/macimas/mac's%20Minecraft/raw/main/mac's%20Minecraft%20woff2.zip

this is most likely what you're looking for! it should cover almost every character in respect to Minecraft Java 1.20.x

<details>
	<summary>previews</summary>
	some sample text
	<br>
	<img src="./GITHUB/main preview 1.png">
	<hr>
	bold and italic variants, with bold being strange as ever
	<br>
	please note that italic has a little kerning issue that i do not know how to fix yet. sorry
	<img src="./GITHUB/main preview 2.png">
	<hr>
	a boring little story
	<br>
	<img src="./GITHUB/main preview 3.png">
	<hr>
	some goofy thing i wrote for some odd reason
	<br>
	<img src="./GITHUB/main preview 4.png">
</details>

<details>
	<summary>glyph table</summary>
	<img src="./base/mac's Minecraft/table.png">
</details>

<hr>

<img align="center" src="./GITHUB/tweaked%20package.png" alt="tweaked">
<br>
→ *tweaks characters in main package*
<br>
( 📥 ← [`ttf`][t ttf] [`otf`][t otf] [`woff2`][t woff2] )

[t ttf]: https://github.com/macimas/mac's%20Minecraft/raw/main/mac's%20Tweaked%20Minecraft%20ttf.zip
[t otf]: https://github.com/macimas/mac's%20Minecraft/raw/main/mac's%20Tweaked%20Minecraft%20otf.zip
[t woff2]: https://github.com/macimas/mac's%20Minecraft/raw/main/mac's%20Tweaked%20Minecraft%20woff2.zip

tweakity with no regard if it actually makes it better. let me know if bad in Issues page

<details>
	<summary>previews</summary>
	tweaks some things, i guess..
	<br>
	<img src="./GITHUB/tweaked preview 1.png">
	<hr>
	bold variant should be more readable
	<br>
	<img src="./GITHUB/tweaked preview 2.png">
	<hr>
	some characters will not be bolden, for reasons!
	<br>
	<img src="./GITHUB/tweaked preview 3.png">
</details>

<details>
	<summary>glyph table</summary>
	<img src="./base/mac's Tweaked Minecraft/table.png">
	<br>
	<img src="./base/mac's Tweaked Minecraft/Bold/table.png">
</details>

<hr>

<img align="center" src="./GITHUB/extended%20package.png" alt="extended">
<br>
→ *adds more characters to main package*
<br>
( 📥 ← [`ttf`][e ttf] [`otf`][e otf] [`woff2`][e woff2] )

[e ttf]: https://github.com/macimas/mac's%20Minecraft/raw/main/mac's%20Extended%20Minecraft%20ttf.zip
[e otf]: https://github.com/macimas/mac's%20Minecraft/raw/main/mac's%20Extended%20Minecraft%20otf.zip
[e woff2]: https://github.com/macimas/mac's%20Minecraft/raw/main/mac's%20Extended%20Minecraft%20woff2.zip

a little experiment. i dont really like most of it turned out. i may add more and polish this up in later versions, but for now it just exists `:p`

<details>
	<summary>previews</summary>
	a little arrowy and sparkly preview, with (most likely) bonked Shavian sentence
	<br>
	<img src="./GITHUB/extended preview 1.png">
	<br>
	please note that some characters aren't built properly due to the converter i use. it does provide a fix but filesize triples and im too stubborn, so yeah. i dont realy care for now since you probably dont really need to use this package anyway
	<br>
	<img src="./GITHUB/extended preview 2.png">
</details>

<details>
	<summary>glyph table</summary>
	<img src="./base/mac's Extended Minecraft/table.png">
</details>

<hr>

**note:** these fonts haven't been thoroughly tested. feel free to let me know in Issues page if you have suggestion or issue with these packages `:)`


# license
fonts are under [SIL Open Font License](./LICENSE)

feel free and open source to use these fonts freely, in personal and commercial projects! `:D`


# vague plans

- fix kerning issue with italic variants
- somehow make the process of working on font a bit better?
- tweaked + extended package?


# how to build?
uhmmm not sure why you need to do that but here's some prerequisites:

- Linux (sorry...)
- other things (`lua`, `fontforge`, `findutils`, `zip`)

then run the script `lua generate.lua`

it should generate fonts in `temp/`, and zip those fonts into their respective packages in `build/`

# some boring background info

i started this back in around December 2022 when i couldn't find a nice Minecraft font. they were either not pixel-perfect, outdated, or were quite lacking or weird looking

initial attempt only contained Basic Latin and some other characters i needed. was pretty satisfied with it and kept it as is for an entire year, until i revisited the font in December 2023

was pretty bored in christmas break and thought "wat if i make a mc font that's 1:1 used ingame for funsies"

"no way in hell i'm gonna be able to do that" i said, but tried anyway, making this my most ambitious font recreation yet

also this was previously released as "mdt's Minecraft" only on github, but decided to rename it and release it as separate font for terrible reasons `:v` the previous version is still up in my fonts repo, but i'd rather not you find it `>:(` 