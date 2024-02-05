<img align="left" src="GITHUB/bennett.png" alt="strange grass block">

# mac's Minecraft

a rough 1:1 recreation of Minecraft font

kudos to [YellowAfterlife's pixel font converter](https://yal.cc/r/20/pixelfont/)


<img align="right" src="./GITHUB/mmm... font!.png">

## packages

<p>
	<img src="./GITHUB/main%20package.png" alt="main">
	<br>
	→ <i>Minecraft font with bold and italic styles</i>
	<br>
	( 📥 ← 
		<a href="https://github.com/macimas/macsMinecraft/raw/main/build/mac's%20Minecraft%20ttf.zip"><code>ttf</code></a> 
		<a href="https://github.com/macimas/macsMinecraft/raw/main/build/mac's%20Minecraft%20otf.zip"><code>otf</code></a> 
		<a href="https://github.com/macimas/macsMinecraft/raw/main/build/mac's%20Minecraft%20woff2.zip"><code>woff2</code></a> 
	)
</p>

this is most likely what you're looking for! it should cover almost every character in respect to Minecraft Java 1.20.x

<details>
	<summary>previews</summary>
	some sample text
	<br>
	<img src="./GITHUB/main preview 1.png">
	<hr>
	bold and italic styles, with bold being strange as ever
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

<p>
	<img src="./GITHUB/tweaked%20package.png" alt="tweaked">
	<br>
	→ <i>tweaks characters in main package</i>
	<br>
	( 📥 ← 
		<a href="https://github.com/macimas/macsMinecraft/raw/main/build/mac's%20Tweaked%20Minecraft%20ttf.zip"><code>ttf</code></a> 
		<a href="https://github.com/macimas/macsMinecraft/raw/main/build/mac's%20Tweaked%20Minecraft%20otf.zip"><code>otf</code></a> 
		<a href="https://github.com/macimas/macsMinecraft/raw/main/build/mac's%20Tweaked%20Minecraft%20woff2.zip"><code>woff2</code></a> 
	)
</p>

tweakity with no regard if it actually makes it better. let me know if bad in Issues page

<details>
	<summary>previews</summary>
	tweaks some things, i guess..
	<br>
	<img src="./GITHUB/tweaked preview 1.png">
	<hr>
	bold style should be more readable
	<br>
	<img src="./GITHUB/tweaked preview 2.png">
	<hr>
	some characters will not be bolden in bold style, for reasons!
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

<p>
	<img src="./GITHUB/extended%20package.png" alt="extended">
	<br>
	→ <i>adds more characters to main package</i>
	<br>
	( 📥 ← 
		<a href="https://github.com/macimas/macsMinecraft/raw/main/build/mac's%20Extended%20Minecraft%20ttf.zip"><code>ttf</code></a> 
		<a href="https://github.com/macimas/macsMinecraft/raw/main/build/mac's%20Extended%20Minecraft%20otf.zip"><code>otf</code></a> 
		<a href="https://github.com/macimas/macsMinecraft/raw/main/build/mac's%20Extended%20Minecraft%20woff2.zip"><code>woff2</code></a> 
	)
</p>

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


## license
fonts are under [SIL Open Font License](./LICENSE)

feel free and open source to use these fonts freely, for personal and commercial purposes! `:D`


## vague plans

- fix kerning issue with italic styles
- somehow make the process of working on font a bit better?
- tweaked + extended package?


## how to build?
uhmmm not sure why you need to do that but here's some prerequisites:

- Linux (sorry...)
- other things (`lua`, `fontforge`, `findutils`, `zip`)

then run the script `lua generate.lua`

it should generate fonts in `temp/`, and zip those fonts into their respective packages in `build/`

## some boring background info

i started this back in around December 2022 when i couldn't find a nice Minecraft font. they were either not pixel-perfect, outdated, or were quite lacking or weird looking

initial attempt only contained Basic Latin and some other characters i needed. was pretty satisfied with it and kept it as is for an entire year, until i revisited the font in December 2023

was pretty bored in christmas break and thought "wat if i make a mc font that's 1:1 used ingame for funsies"

"no way in hell i'm gonna be able to do that" i said, but tried anyway, making this my most ambitious font recreation yet

also this was previously released as "mdt's Minecraft" only on github, but decided to rename it and release it as separate font for terrible reasons `:v` the previous version is still up in my fonts repo, but i'd rather not you find it `>:(` 