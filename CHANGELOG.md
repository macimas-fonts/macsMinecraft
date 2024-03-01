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
<small><i>please do not look at the code, thank you</i></small>

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
