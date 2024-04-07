## 1.03 - April 8, 2024
this release should fix most parity issues between Main and Minecraft's font

oh yeah i call them fonts instead of packages now, for reasons `:v`

- new fonts: Amalgam
  - combines Extended and Tweaked fonts, of course!
- Illageralt fonts are now based on Main fonts
- Illageralt Tweaked fonts are now based on Tweaked fonts
- use `✘` instead of `✗` in Main and Tweaked fonts
- add characters in Main and Tweaked fonts
  - Cyrillic
`Ӽ Ӿ ӽ ӿ ӻ`
  - Spacing Modifier Letters
`ʻ ˌ ˙`
  - Basic Latin
`/`
  - General Punctuation
`… ‽`
  - Geometric Shapes
`◘`
  - Latin-1 Supplement
` ̧`
  - Miscellaneous Mathematical Symbols-A
`⟘`
- add characters in Extended fonts
  - Emoticons
`😀 😁 😂 😃 😄 😅 😆 😇 😈 😉 😊 😋 😌 😍 😎 😏 😐 😑 😒 😓 😔 😕 😖 😗 😘 😙 😚 😛 😜 😝 😞 😟
😠 😡 😢 😣 😤 😥 😦 😧 😨 😩 😪 😫 😬 😭 😮 😯 😰 😱 😲 😳 😴 😵 😶 😷 😸 😹 😺 😻 😼 😽 😾 😿
🙀 🙁 🙂 🙃 🙄 🙅 🙆 🙇 🙈 🙉 🙊`
- tweak characters in Main fonts
  - Greek Extended
`ἄ Ὰ Ά ᾄ ᾎ ᾏ ἥ Ἦ ᾕ ᾞ ἰ Ἲ Ἴ Ἶ Ὅ Ὗ Ὤ Ὥ ᾬ ᾭ Ἆ Ἱ`
  - Cyrillic
`Ў ё ђ ћ Ҕ ӫ ӱ ӯ ӳ Ӹ Ҋ Ӊ Ҥ ҋ ӎ Р ө ѳ`
  - Latin Extended Additional
`ḥ Ỉ ỉ Ḧ ḧ Ḩ ḩ Ḥ ṅ Ṥ ṥ ẞ`
  - Latin Extended-B
`Ǵ Ǧ Ǥ Ɯ ƣ ȿ Ƚ ƻ Ƀ ư Ƕ ȗ`
  - IPA Extensions
`ʥ ʨ ʬ ʭ ɯ ɼ ɐ ʄ`
  - Armenian
`Դ ե ճ ն ՟ ֊`
  - Runic
`ᚯ ᚰ ᚾ ᛅ ᛧ ᛴ`
  - Miscellaneous Symbols
`☮ ♯ ⛏ ☔ ⚗`
  - Cyrillic Supplement
`Ԇ ԇ ԗ Ԅ`
  - Georgian
`Ⴇ დ ე Ⴥ`
  - Basic Latin
`7 @ ^`
  - Latin Extended-A
`Đ ļ Ľ`
  - Gothic
`𐌱 𐌲`
  - Greek and Coptic
`ϓ η`
  - Phonetic Extensions Supplement
`ᶈ ᶋ`
  - Latin Extended-D
`ꜿ`
  - Phonetic Extensions
`ᵫ`
  - Arrows
`⇄`
  - Currency Symbols
`₾`
  - Cyrillic Extended-B
`ꚗ`
  - General Punctuation
`‱`
  - Georgian Supplement
`ⴈ`
  - Geometric Shapes
`◎`
  - Latin-1 Supplement
`£`
  - Miscellaneous Symbols and Pictographs
`🏹`
  - Runic
`ᛟ`
  - Superscripts and Subscripts
`⁵₅`
  - Supplemental Arrows-B
`⥝`
- tweak characters in Tweaked fonts
  - mostly inherits changes from Main
  - Box Drawing
`─ ┌ └ ┬ ┴ ├ ┼ ╒ ╘ ╥ ╨ ╞ ╪ ═ ╔ ╚ ╦ ╩ ╠ ╬ ╓ ╙ ╤ ╧ ╟ ╫`
<br>(horizontal lines are 1px longer)
  - Georgian
`ჵ`
  - IPA Extensions
`ʣ`

i also redid font generation again :p

## 1.02 - March 1, 2024
this release mostly contains technical changes, for terrible reasons!

- fix characters
  - `U+0440 р` - stem was 1 pixel longer
  - `U+1E06 Ḇ`, `U+1E07 ḇ` - wasn't bold in tweaked
- new package: Illageralt
- new package: Illageralt Tweaked
- embed license into fonts
- change versioning to `M.mm`
- sfnt revision is now also set to font version
- change package naming
  - tweaked: `mac's Tweaked Minecraft` → `mac's Minecraft Tweaked`
  - extended: `mac's Extended Minecraft` → `mac's Minecraft Extended`

i also redid font generation. it's slightly more cleaner and lets me do things i wasn't able to do before. am mostly satisfied with it! 👍️
~~*please do not look at the code, thank you*~~

## 1.1 - February 28, 2024
- fix characters `p q`
  - their stems were 1 pixel longer due to oversight

## 1.0 - February 5, 2024
- initial release for main, tweaked, and extended packages

<hr>

this font was previously released as "mdt's Minecraft", but for stupid reasons decided to rename it and made it as a separate font

here's changelog between main 1.0 and mdt's 1.1:

- add Gothic block and other characters `❄ 🎣 🛡`
- fix some characters `@ ─ ╫ ´ ƞ Ҧ ҧ Ӂ ӝ Ӡ ԭ Ὶ Ί ῠ ῡ ῢ ΰ ῤ ῥ ῦ ῧ Ῠ Ῡ Ὺ Ύ Ῥ ῲ ῳ ῴ ῶ ῷ Ὸ Ό Ὼ Ώ ῼ`
	- `@` wasn't in the font due to oversight

and here's changelog from the previous font:

## mdt's 1.1 (December 23, 2023)
- should now cover entire Basic Multilingual Plane
- fixed some symbols not being 1:1 `₃ ⅞ ⅟ ↉`
- adds `✗` (i missed it previously)

## mdt's 1.0 (December 21, 2023)
- initial release. should cover most of Basic Multilingual Plane + some mix of symbols. has 2,271 symbols :)
