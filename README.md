# hoi4-superiority

**Superiority: Ultima Ratio** is a mod for Hearts of Iron IV that improves upon vanilla, including various improvements and fixes.

Built against game version **1.19.3**.

## Features

- Hand-picked country colours
- Germany: the "Danzig for Slovakia" deal also gives Germany Poznan and Katowice
- Germany: historical German names for focuses famous for Germany, such as "Danzig oder Krieg", "Vierjahresplan" and "Wunderwaffen"

## What this mod changes

| File | Our change |
|------|------------|
| `common/countries/colors.txt` | Hand-picked colours for AFG, AUS, BUL, CHI, CZE, ENG, FRA, HUN, INS, IRE, ITA, PAK, PER, PHI, POL, ROM, TIB and YUG. DIP (Indian Partisans) and PSR (Second Philippine Republic) are recoloured so they don't clash with ENG and INS. Every other tag has its vanilla colour. |
| `common/countries/cosmetic.txt` | Hand-picked colours for HUN_EMPIRE and INS_HOL. Every other tag has its vanilla colour. |
| `events/Germany.txt` | In the "Danzig for Slovakia" deal (`germany.80`/`germany.81`), Poland also cedes Poznan (state 86) and Katowice (state 762) to Germany, and Germany gets cores on them. Each state only moves if Poland still owns it. |
| `localisation/english/replace/superiority_l_english.yml` | German names: Danzig oder Krieg, Vierjahresplan, Wunderwaffen, Autarkiepolitik, U-Boot-Waffe, Unternehmen Tannenbaum, Rückkehr des Kaisers. |
| `gfx/leaders/GER/portrait_GER_adolf_hitler.dds` | Custom Hitler portrait. |

## Publishing to the Steam Workshop

Workshop item: [3471446814](https://steamcommunity.com/sharedfiles/filedetails/?id=3471446814).

1. Register this folder as a local mod. Create `Documents/Paradox Interactive/Hearts of Iron IV/mod/superiority.mod` with the contents of `descriptor.mod`, plus `path="C:/Users/jerry/Documents/hoi4-superiority"`.
2. To test, open the Paradox Launcher and make a playset with the local `Superiority: Ultima Ratio` instead of the subscribed Workshop one.
3. To upload, go to Launcher → **Mods** → **Mod Tools** → **Upload a mod**. Pick `Superiority: Ultima Ratio` and add a change note.
