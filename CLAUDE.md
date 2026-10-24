# Superiority: Ultima Ratio (HOI4 mod)

A small vanilla+ mod for Hearts of Iron IV, built against **1.19.3**. The README's "What this mod changes" table lists every file the mod ships and why it's there. Keep that table in sync with what the mod actually ships.

The game is installed at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV` (`$GAME` below). Check its version in `$GAME/launcher-settings.json`.

## Rules

- **Full copies go stale.** HOI4 can't patch part of a script file: a mod file with the same path as a vanilla file replaces it completely. So every full copy has to be re-copied from vanilla after each patch, with our edits applied again. Avoid adding full copies. Prefer our own new files: decisions, events with our own IDs, ideas, scripted effects, `on_actions` (they merge), single-value overrides in `common/defines/`, and `localisation/english/replace/`. If a full copy is unavoidable, list it in the README table and mark our edits in it with `# superiority:` comments. This went wrong after 1.16: unlisted copies of Germany's focus tree and events silently overwrote newer vanilla content.
- **Events load only from `events/`.** A file in `common/events/` is ignored without any error.
- **Colours are hand-picked.** Only the tags listed in the README table differ from vanilla. Don't recolour those without asking. New vanilla tags keep their vanilla colour, unless one clashes with a hand-picked colour.
- **Focus renames.** `localisation/english/replace/superiority_l_english.yml` only renames focuses that are historically unique to, or famous for, Germany, such as Vierjahresplan or Wunderwaffen. Never rename generic programmes like Coal Liquidization. A rename only works while its key is still a focus `id` in `$GAME/common/national_focus/germany.txt`. Paradox renames IDs when it reworks a tree, and a stale key silently stops showing.
- **Portrait.** The portrait in `gfx/leaders/GER/` only overrides vanilla while its filename matches `$GAME/interface/_leader_portraits.gfx`.
- No new focus trees, and no Britain work for now: the maintainer has ruled both out.

## Updating to a new game version

1. **Colours.** Re-merge our colours onto the new vanilla files. Vanilla's layout and any new tags are kept; our colour wins for every tag in our file:

   ```bash
   python tools/merge_colors.py "$GAME/common/countries/colors.txt" common/countries/colors.txt common/countries/colors.txt
   python tools/merge_colors.py "$GAME/common/countries/cosmetic.txt" common/countries/cosmetic.txt common/countries/cosmetic.txt
   ```

   The script lists tags in our file that are missing from vanilla (`mod-only`). Those are renamed or removed tags: rename ours to match, or delete them. Then check new vanilla tags for clashes with the hand-picked colours.
2. **Germany events.** Copy `$GAME/events/Germany.txt` over `events/Germany.txt`. `git diff events/Germany.txt` then shows our `# superiority:` blocks as removed lines, among Paradox's changes. Re-add them. Check that `germany.80`/`germany.81` still hand Poland's states over in the same way, and that states 86 (Poznan) and 762 (Katowice) still exist with those IDs (`$GAME/history/states/`).
3. **Focus renames and portrait.** Check both as described under Rules.
4. **Descriptor.** Bump `version` and `supported_version` in `descriptor.mod`.
5. **Test.** You can't playtest, so ask the maintainer to start the game with the local mod and check `Documents/Paradox Interactive/Hearts of Iron IV/logs/error.log`.

## Publishing

- `remote_file_id="3471446814"` in `descriptor.mod` ties uploads to the existing Workshop item. Never remove it: without it, an upload creates a new Workshop item.
- The local launcher registration is `Documents/Paradox Interactive/Hearts of Iron IV/mod/superiority.mod`. It mirrors `descriptor.mod` plus a `path` line, so keep the `name` in both files in sync.
- The upload sends the whole folder, `.git` and `tools/` included.
