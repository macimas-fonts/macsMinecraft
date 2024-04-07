<h1 align="center">
	<img src="GITHUB/bennett.png" alt="strange grass block">
	<br>
	mac's Minecraft
</h1>
<p align="center">
	a rough 1:1 recreation of the Minecraft font
	<br>
	<small>kudos to <a href="https://yal.cc/r/20/pixelfont">YellowAfterlife's pixel font converter</a></small>
</p>

<img align="right" src="./GITHUB/mmm... font!.png">

## fonts

> ![](./GITHUB/little%20notice.png)
> <br>
> these fonts are incompetently made, so expect some issues!!
><br>
> feel free to let me know in Issues page if you have issue or suggestion with these packages `:)`

for downloads, check [Releases page](https://github.com/macimas-fonts/macsMinecraft/releases)


<hr>

![main](./GITHUB/header/Main.png)
<br>
*→ Minecraft font with bold and italic styles*

this is most likely what you're looking for!
<br>
it should cover almost every character in respect to Minecraft Java 1.20.4

<details>
	<summary>previews</summary>
	some sample text
	<br>
	<img src="./GITHUB/preview/main_1.png">
	<hr>
	bold and italic styles, with bold being strange as ever
	<br>
	<img src="./GITHUB/preview/main_2.gif">
	<hr>
	a boring little story
	<br>
	<img src="./GITHUB/preview/main_3.png">
	<hr>
	some goofy thing i wrote for some odd reason
	<br>
	<img src="./GITHUB/preview/main_4.png">
</details>

<details>
	<summary>glyph table</summary>
	Regular
	<br>
	<img src="./fonts/Main/Regular.png">
	<br>
	Bold
	<br>
	<img src="./fonts/Main/Bold.png">
</details>

<hr>

![](./GITHUB/header/Tweaked.png)
<br>
*→ tweaks characters in Main fonts*


tweakity with no regard if it actually makes it better. let me know if bad in Issues page

<details>
	<summary>previews</summary>
	tweaks some things, i guess..
	<br>
	<img src="./GITHUB/preview/tweaked_1.gif">
	<hr>
	bold style should be more readable
	<br>
	<img src="./GITHUB/preview/tweaked_2.gif">
	<hr>
	some characters will not be bolden in bold style, for reasons!
	<br>
	<img src="./GITHUB/preview/tweaked_3.gif">
</details>

<details>
	<summary>glyph table</summary>
	Regular
	<br>
	<img src="./fonts/Tweaked/Regular.png">
	<br>
	Bold
	<br>
	<img src="./fonts/Tweaked/Bold.png">
</details>

<hr>

![](./GITHUB/header/Extended.png)
<br>
*→ adds more characters to Main fonts*

a little experiment. i dont really like most of it turned out. i may add more and polish this up in later versions, but for now it just exists `:p`

<details>
	<summary>previews</summary>
	a little arrowy and sparkly preview, with (most likely) bonked Shavian sentence
	<br>
	<img src="./GITHUB/preview/extended_1.png">
	<br>
	please note that some characters aren't built properly due to the converter i use. it does provide a fix but filesize triples and im too stubborn, so yeah. i dont realy care for now since you probably dont really need to use these fonts anyway
	<br>
	<img src="./GITHUB/preview/extended_2.png">
	<br>
	an attempt to do emoticons
	<br>
	<img src="./GITHUB/preview/extended_3.png">
</details>

<details>
	<summary>glyph table</summary>
	Regular
	<br>
	<img src="./fonts/Extended/Regular.png">
	<br>
	Bold
	<br>
	<img src="./fonts/Extended/Bold.png">
</details>

<hr>

![](./GITHUB/header/Amalgam.png)
<br>
*→ simply Main + Tweaked + Extended fonts*

quick n dirty

<details>
	<summary>previews</summary>
	refer to their dedicated sections
</details>

<details>
	<summary>glyph table</summary>
	Bold
	<br>
	<img src="./fonts/Amalgam/Bold.png">
</details>

<hr>

![](./GITHUB/header/Illageralt.png)
<br>
*→ it's that secret font in Java and the runic font in Dungeons*

yep!

<details>
	<summary>previews</summary>
	the fonts! with Main fonts for comparison
	<br>
	<img src="./GITHUB/preview/illageralt_1.gif">
</details>

<details>
	<summary>glyph table</summary>
	Regular
	<br>
	<img src="./fonts/Illageralt/Regular.png">
	<br>
	Bold
	<br>
	<img src="./fonts/Illageralt/Bold.png">
</details>

<hr>

![](./GITHUB/header/IllageraltTweaked.png)
<br>
*→ simply bold more readable*

yep!

<details>
	<summary>previews</summary>
	bold is most likely more readable, maybe
	<br>
	<img src="./GITHUB/preview/illageralt_tweaked_1.gif">
</details>

<details>
	<summary>glyph table</summary>
	Bold
	<br>
	<img src="./fonts/Illageralt Tweaked/Bold.png">
</details>

<hr>


## license
fonts are under [SIL Open Font License](./LICENSE)

feel free and open source to use these fonts freely, for personal and commercial purposes! `:D`


## some boring background info

i started this back in around December 2022 when i couldn't find a nice Minecraft font. they were either not pixel-perfect, outdated, or were quite lacking or weird looking (i am quite nitpicky)

initial attempt only contained Basic Latin and some other characters i needed. was pretty satisfied with it and kept it as is for an entire year, until i revisited the font in December 2023

was pretty bored in christmas break and thought "wat if i make a mc font that's 1:1 used ingame for funsies"

"no way in hell i'm gonna be able to do that" i said, but tried anyway, making this my most ambitious font recreation yet

also this was previously released as "mdt's Minecraft" only on github, but decided to rename it and release it as separate font for terrible reasons `:v` the previous version is still up in my fonts repo, but i'd rather not you find it `>:(`


## how to build?
uhmmm not sure why you need to do that but here's some prerequisites:

- Linux (not sure if it works on Windows)
- FontForge

then run the script `fontforge -quiet -script generate.py`

it should put generated fonts in `TEMP/`