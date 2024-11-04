from vanilla.dialogs import *
from mojo.UI import AskString
from mojo.UI import OutputWindow
import pprint

# TODO: ignore glyphs marked as "experimental" with robofont marx
# TODO: allow user to paste space-separated string of glyphs to limit check to

### SET THIS TO IGNORE GLYPHS YOU WANT TO LEAVE ALONE (e.g. experimental glyphs) ###

glyphsToIgnore = ""

# R.trap Z.noserif ampersand.code_experimental_2 ampersand.code_experimental_3 ampersand.crossbar at.simple at.short at.replaced_with_prop dagger.daggery g.extra g.long_desc g.longtail g.ss01 onehalf.v1 perthousand r.simple_italic sterling.replaced_with_flat two.replaced_with_rounder zero.ss01 one.flatflag

####################################################################################

debug = False # will print full dictionaries

files = getFile("Select files to check for unicodes similarity", allowsMultipleSelection=True, fileTypes=["ufo"])

fonts = []
unicodesDict = {}

OutputWindow().show()
OutputWindow().clear()

print("\nCOMPATIBILITY CHECK: UNICODES\n\n")

for file in files:
    font = OpenFont(file, showInterface=False)

    # fontName = (font.info.styleName).transl ate({ord(c): None for c in 'aeiou'}) # remove vowels to shorten
    fontName = (font.info.styleName)

    fonts.append(fontName)

    for glyph in font:
        if glyph.name not in unicodesDict:
            unicodesDict[glyph.name] = {}
        
        if fontName not in unicodesDict[glyph.name]:
            unicodesDict[glyph.name][fontName] = ()

        unicodesDict[glyph.name][fontName] = glyph.unicodes

    font.close()

print("Checking fonts:")
for fontName in fonts:
    print("• ", fontName)
print("")

if debug:
    pp = pprint.PrettyPrinter(indent=2, width=200)
    pp.pprint(unicodesDict)

glyphsNotInAllFonts = []

for glyphName in unicodesDict.keys():
    if len(unicodesDict[glyphName]) < len(fonts):
        if glyphName not in glyphsNotInAllFonts and glyphName not in glyphsToIgnore.split(" "):
            glyphsNotInAllFonts.append(glyphName)

glyphsWithUnevenUnicodes = []

for glyphName in unicodesDict.keys():
    if len(set(unicodesDict[glyphName].values())) > 1:
        if glyphName not in glyphsWithUnevenUnicodes and glyphName not in glyphsToIgnore.split(" "):
            glyphsWithUnevenUnicodes.append(glyphName)
            
maxFontNameLength = len(max(fonts, key=len))


alertEmoji = "🍇 🥑 🍉 🍊 🍑 🍌 🍒 🌽 🍈 🐶 🐱 🐭 🐰 🦊 🐻 🐯 🦁 🐮 🐷 🐸 🐵 🐔 🐣".split(" ")
iconDict = {}

for glyphName in sorted(glyphsWithUnevenUnicodes):
    iconDict[glyphName] = {}
    # for font with this glyph
    for fontName in unicodesDict[glyphName].keys():
        # if glyph point count not already in icon dict under glyph
        if unicodesDict[glyphName][fontName] not in iconDict[glyphName].keys():
            count  = str(unicodesDict[glyphName][fontName])
            iconDict[glyphName][count] = ""

    # go through each glyph:font combo in iconDict and assing emoji to diff counts
    for index,unicodeTupple in enumerate(iconDict[glyphName].keys()):
        iconDict[glyphName][unicodeTupple] = alertEmoji[index]


if debug:
    pp = pprint.PrettyPrinter(indent=2, width=200)
    pp.pprint(iconDict)

problemGlyphs = glyphsNotInAllFonts + glyphsWithUnevenUnicodes

unicodePadding = 9

for glyphName in sorted(problemGlyphs):
    print("\n--------------------------------------------------------------\n")
    print(f"{glyphName}\n")

    # If glyph has different point counts in different fonts, report
    # if len(set(unicodesDict[glyphName].keys())) != 1:
    if glyphName in glyphsWithUnevenUnicodes:

        print(f"\t{'Font'.ljust(maxFontNameLength + 1)} |  {'Unicodes'.rjust(unicodePadding)} | 📊") # add contour count? segment count?
        print(f"\t{''.ljust(maxFontNameLength + 1, '-')} | {''.rjust(unicodePadding,'-')} | --")

        for fontName in unicodesDict[glyphName].keys():
            
            unicodeTupple = str(unicodesDict[glyphName][fontName])
            print(f"\t{fontName.ljust(maxFontNameLength + 1)} | {str(unicodesDict[glyphName][fontName]).rjust(unicodePadding)} | {iconDict[glyphName][unicodeTupple]}")
            
        print("")

    # # If glyph is not in all fonts, report
    # # if len(unicodesDict[glyphName]) != len(fonts):
    # if glyphName in glyphsNotInAllFonts:
    #     # print("\tGlyph is not in all fonts.\n")
    #     print("\tIs in:\n\t------------------")
    #     for fontName in sorted(fonts):
    #         if fontName in unicodesDict[glyphName]:
    #             print("\t",fontName)
        
    #     print("\n")

    #     print("\tNot in:\n\t------------------")
    #     for fontName in sorted(fonts):
    #         if fontName not in unicodesDict[glyphName]:
    #             print("\t",fontName)

if len(glyphsWithUnevenUnicodes) >= 1:
    print("️\n\nGlyphs with unequal unicodes between fonts:\n")
    print("\t", end=" ")
    for glyphName in sorted(glyphsWithUnevenUnicodes):
        # print(" - [ ] ", glyphName)
        print(glyphName, end=" ")
    print("")


if len(glyphsNotInAllFonts) >= 1:
    print("\n\nGlyphs that aren't in all fonts:\n")
    print("\t", end=" ")
    for glyphName in sorted(glyphsNotInAllFonts):
        # print(" - [ ] ", glyphName)
        print(glyphName, end=" ")
    print("")

if len(problemGlyphs) is 0:
    print("🤖🤖🤖\n")
    print("Looks like all glyphs have the same unicodes – nice work! \n")
    print("🎉🎉🎉\n")


if glyphsToIgnore is not "" and len(glyphsToIgnore.split(" ")) > 0:
    print("\n--------------------------------------------------------------\n")
    print("NOTE: ignored the following glyphs (they are experiments or currently low-priority)")
    print("(edit script to adjust these)")
    for name in glyphsToIgnore.split(" "):
        print(name, end=" ")

print("\n")