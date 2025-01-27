

# '''
#     Make listed glyphs default, and give current defaults new suffix

# '''

import typing
from typing import Any, Dict, List, Mapping, Set, Tuple, Union
import ufoLib2
from fontParts.world import *

import sys
import os


oldNames = "l.sans lcaron.sans lacute.sans lcommaaccent.sans ldotbelow.sans llinebelow.sans lslash.sans".split()
newSuffix = ""


try:
    if sys.argv[1]:
        print("Swapping glyph names!")
        dirToUpdate = sys.argv[1]
        subDirs = next(os.walk(dirToUpdate))[1]
        ufosToAdjust = [ path for path in subDirs if path.endswith(".ufo")]
        head = dirToUpdate

except IndexError:
    print("Please include directory containing UFOs")



# from https://github.com/googlefonts/fontmake/blob/a5529377219a13f5685f38bcefb248150704ff5e/Lib/fontmake/instantiator.py#L556
def swap_glyph_names(font: ufoLib2.Font, name_old: str, name_new: str):
    """Swap two existing glyphs in the default layer of a font (outlines,
    width, component references, kerning references, group membership).
    The idea behind swapping instead of overwriting is explained in
    https://github.com/fonttools/fonttools/tree/master/Doc/source/designspaceLib#ufo-instances.
    We need to keep the old glyph around in case any other glyph references
    it; glyphs that are not explicitly substituted by rules should not be
    affected by the rule application.
    The .unicodes are not swapped. The rules mechanism is supposed to swap
    glyphs, not characters.
    """

    if name_old not in font or name_new not in font:
        print(f"Cannot swap glyphs '{name_old}' and '{name_new}', as either or both are "
            "missing.")
        return
        # raise InstantiatorError(
        #     f"Cannot swap glyphs '{name_old}' and '{name_new}', as either or both are "
        #     "missing."
        # )

    # 1. Swap outlines and glyph width. Ignore lib content and other properties.
    glyph_swap = ufoLib2.objects.Glyph(name="temporary_swap_glyph")
    glyph_old = font[name_old]
    glyph_new = font[name_new]

    p = glyph_swap.getPointPen()
    glyph_old.drawPoints(p)
    glyph_swap.width = glyph_old.width
    for a in glyph_old.anchors:
        glyph_swap.anchors.appendAnchor(a.copy(), a.position)

    glyph_old.clear()
    p = glyph_old.getPointPen()
    glyph_new.drawPoints(p)
    glyph_old.width = glyph_new.width
    for a in glyph_new.anchors:
        glyph_old.anchors.appendAnchor(a.copy(), a.position)

    glyph_new.clear()
    p = glyph_new.getPointPen()
    glyph_swap.drawPoints(p)
    glyph_new.width = glyph_swap.width
    for a in glyph_swap.anchors:
        glyph_new.anchors.appendAnchor(a.copy(), a.position)

    # 2. Remap components.
    for g in font:
        for c in g.components:
            if c.baseGlyph == name_old:
                c.baseGlyph = name_new
            elif c.baseGlyph == name_new:
                c.baseGlyph = name_old

    # 3. Swap literal names in kerning.
    kerning_new = {}
    for first, second in font.kerning.keys():
        value = font.kerning[(first, second)]
        if first == name_old:
            first = name_new
        elif first == name_new:
            first = name_old
        if second == name_old:
            second = name_new
        elif second == name_new:
            second = name_old
        kerning_new[(first, second)] = value
    # font.kerning = kerning_new
    font.kerning.update(kerning_new)

    # 4. Swap names in groups.
    for group_name, group_members in font.groups.items():
        group_members_new = []
        for name in group_members:
            if name == name_old:
                group_members_new.append(name_new)
            elif name == name_new:
                group_members_new.append(name_old)
            else:
                group_members_new.append(name)
        font.groups[group_name] = group_members_new


for ufo in sorted(ufosToAdjust):
    ufoPath = f"{head}/{ufo}"
    font = OpenFont(ufoPath, showInterface=True)

    for glyphName in oldNames:

        if newSuffix != "":
            newName = glyphName.split(".")[0] + '.' + newSuffix
        else:
            newName = glyphName.split(".")[0]

        print(newName)

        swap_glyph_names(font, glyphName, newName)

        # TODO: remove old glyphName

    # font.save()
    # font.close()


