# hoi4-superiority

**Superiority: Ultima Ratio** is a mod for Hearts of Iron IV that improves upon vanilla, including various improvements and fixes.

Built against game version **1.19.3** (`supported_version` in `descriptor.mod`).

## Features

- Hand-picked country colours
- Germany: the "Danzig for Slovakia" deal also gives Germany Poznan and Katowice
- Germany: historical German names for focuses famous for Germany, such as "Danzig oder Krieg", "Vierjahresplan" and "Wunderwaffen"

## What this mod changes

HOI4 can't patch part of a script file. A mod file with the same path as a vanilla file replaces the vanilla file completely. Any file listed below as a **full copy** therefore has to be re-copied from the new game version after every patch, and our edits applied to it again.

| File | Kind | Our change |
|------|------|------------|
| `common/countries/colors.txt` | Full copy | Hand-picked: AFG, AUS, BUL, CHI, CZE, ENG, FRA, HUN, INS, IRE, ITA, PAK, PER, PHI, POL, ROM, TIB, YUG. DIP (Indian Partisans) and PSR (Second Philippine Republic) are recoloured so they don't clash with ENG and INS. Every other tag has its vanilla colour. |
| `common/countries/cosmetic.txt` | Full copy | Hand-picked: HUN_EMPIRE, INS_HOL. Every other tag has its vanilla colour. |
| `events/Germany.txt` | Full copy | Two blocks marked `# superiority:`. In `germany.81` ("Danzig Ceded for Slovakia"), Poland also cedes states 86 (Poznan) and 762 (Katowice) to Germany, and Germany gets cores on them. `germany.80` ("Danzig for Slovakia", Poland's choice) shows the same thing in its tooltip. Each state only moves if Poland still owns it. |
| `localisation/english/replace/superiority_l_english.yml` | Override (own keys only) | German names for German focuses (Danzig oder Krieg, Vierjahresplan, Wunderwaffen, Autarkiepolitik, U-Boot-Waffe, Unternehmen Tannenbaum, Rückkehr des Kaisers). Files under `replace/` override single keys, so a patch can't break this file. Only rename focuses that are historically unique to Germany, not generic programmes. After a patch, check the keys are still focus IDs in `common/national_focus/germany.txt`: Paradox renames them when it reworks the tree, and an old key silently stops showing. |
| `gfx/leaders/GER/portrait_GER_adolf_hitler.dds` | Replacement image | Custom Hitler portrait. It only works while the filename matches the vanilla one, so check `interface/_leader_portraits.gfx` if it stops showing. |

## Updating to a new game version

`$GAME` is the game folder, e.g. `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`.

1. **Colours.** Merge our colours onto the new vanilla files. Vanilla's layout and any new tags are kept; our colour wins for every tag we define:

   ```bash
   python tools/merge_colors.py "$GAME/common/countries/colors.txt" common/countries/colors.txt common/countries/colors.txt
   python tools/merge_colors.py "$GAME/common/countries/cosmetic.txt" common/countries/cosmetic.txt common/countries/cosmetic.txt
   ```

   The script prints the tags that are in our file but no longer in vanilla (`mod-only`). Those are usually renamed or removed tags: rename ours to match, or delete them.
2. **Germany events.** Copy `$GAME/events/Germany.txt` over `events/Germany.txt`. Then `git diff events/Germany.txt` shows the two `# superiority:` blocks as removed lines, among Paradox's own changes. Re-add those blocks. Check that `germany.80`/`germany.81` still hand Poland's states over in the same way, and that states 86/762 still exist with the same IDs.
3. **Portrait.** Check that the vanilla filename in `$GAME/gfx/leaders/GER/` hasn't changed.
4. **Descriptor.** Bump `version` and `supported_version` in `descriptor.mod`.
5. Start the game with only this mod enabled and check `Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log` for errors from our files.

## Publishing to the Steam Workshop

Workshop item: [3471446814](https://steamcommunity.com/sharedfiles/filedetails/?id=3471446814). `remote_file_id` in `descriptor.mod` ties uploads to that item. Without it, an upload creates a brand-new Workshop item.

1. Register this folder as a local mod. Create `Documents/Paradox Interactive/Hearts of Iron IV/mod/superiority.mod` with the contents of `descriptor.mod`, plus `path="C:/Users/jerry/Documents/hoi4-superiority"`.
2. To test, open the Paradox Launcher and make a playset with the local `Superiority: Ultima Ratio` instead of the subscribed Workshop one. Both show up with the same name.
3. To upload, go to Launcher → **Mods** → **Mod Tools** → **Upload a mod**. Pick `Superiority: Ultima Ratio` and add a change note.

The upload sends the whole folder, `.git` and `tools/` included.

Never add a full copy of a vanilla file without listing it in the table above. Unlisted copies go stale silently and overwrite newer vanilla content. That happened to the old Germany focus tree after 1.16.
