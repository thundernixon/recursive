from vanilla.dialogs import *
from fontTools import agl

# add glyph names to this dictionary if they aren't getting automatically picked up
unicodeNameMatches = {
    # "nobreakspace":     "00A0",
    # "kcommaaccent":     "0137",
    # "Kcommaaccent":     "0136",
    # "gcommaaccent":     "0123",
    # "Gcommaaccent":     "0122",
    # "ncommaaccent":     "0146",
    # "Ncommaaccent":     "0145",
    # "lcommaaccent":     "013C",
    # "Lcommaaccent":     "013B",
    # "rcommaaccent":     "0157",
    # "Rcommaaccent":     "0156",
    # "scommaaccent":     "0219",
    # "Scommaaccent":     "0218",
    # "ijacute":          "E132",
    # "IJacute":          "E133",
    # "adotbelow":        "1EA1",
    # "Adotbelow":        "1EA0",
    # "edotbelow":        "1EB9",
    # "Edotbelow":        "1EB8",
    # "idotbelow":        "1ECB",
    # "Idotbelow":        "1ECA",
    # "odotbelow":        "1ECD",
    # "Odotbelow":        "1ECC",
    # "udotbelow":        "1EE5",
    # "Udotbelow":        "1EE4",
    # "etilde":           "1EBD",
    # "Etilde":           "1EBC",
    # "ytilde":           "1EF9",
    # "Ytilde":           "1EF8",
    # "ymacron":          "0233",
    # "Ymacron":          "0232",
    # "oogonek":          "01EB",
    # "Oogonek":          "01EA",
    # "schwa":            "0259",
    # "Schwa":            "018F",
    # "Germandbls":       "1e9e",
    # "Nhookleft":        "019d",
    # "nhookleft":        "0272",
    # "bitcoin":          "20bf",
    # "cedi":             "20b5",
    # "dotlessj":         "237",
    # "guarani":          "20b2",
    # "hryvnia":          "20b4",
    # "increment":        "2206",
    # "kip":              "20ad",
    # "litre":            "2113",
    # "manat":            "20bc",
    # "naira":            "20a6",
    # "newsheqel":        "20aa",
    # "ohm":              "2126",
    # "overline":         "203e",
    # "peso":             "20b1",
    # "ruble":            "20bd",
    # "rupee":            "20a8",
    # "tenge":            "20b8",
    # "thai:baht":        "e3f",
    # "won":              "20a9",

    # # combining accents
    # "gravecomb":                "0300",
    # "acutecomb":                "0301",
    # "circumflexcomb":           "0302",
    # "tildecomb":                "0303",
    # "macroncomb":               "0304",
    # "brevecomb":                "0306",
    # "dotaccentcomb":            "0307",
    # "dieresiscomb":             "0308",
    # "ringcomb":                 "030A",
    # "hungarumlautcomb":         "030B",
    # "caroncomb":                "030C",
    # "commaturnedabovecomb":     "0312",
    # "commaaboverightcomb":      "0315",
    # "dotbelowcomb":             "0323",
    # "commaaccentcomb":          "0326",
    # "cedillacomb":              "0327",
    # "ogonekcomb":               "0328",
    # "verticallinelowmod":       "0329",

    # # vienamese – copied in from GlyphsApp

    # "hookcomb":              "0309",
    # "horncomb":              "031B",

    # "Aacute":                "00C1",
    # "Abreve":                "0102",
    # "Abreveacute":           "1EAE",
    # "Abrevedot":             "1EB6",
    # "Abrevegrave":           "1EB0",
    # "Abrevehook":            "1EB2",
    # "Abrevetilde":           "1EB4",
    # "Acircumflex":           "00C2",
    # "Acircumflexacute":      "1EA4",
    # "Acircumflexdot":        "1EAC",
    # "Acircumflexgrave":      "1EA6",
    # "Acircumflexhook":       "1EA8",
    # "Acircumflextilde":      "1EAA",
    # "Adot":                  "1EA0",
    # "Agrave":                "00C0",
    # "Ahook":                 "1EA2",
    # "Atilde":                "00C3",
    # "Dcroat":                "0110",
    # "Eacute":                "00C9",
    # "Ecircumflex":           "00CA",
    # "Ecircumflexacute":      "1EBE",
    # "Ecircumflexdot":        "1EC6",
    # "Ecircumflexgrave":      "1EC0",
    # "Ecircumflexhook":       "1EC2",
    # "Ecircumflextilde":      "1EC4",
    # "Edot":                  "1EB8",
    # "Egrave":                "00C8",
    # "Ehook":                 "1EBA",
    # "Etilde":                "1EBC",
    # "Iacute":                "00CD",
    # "Idot":                  "1ECA",
    # "Igrave":                "00CC",
    # "Ihook":                 "1EC8",
    # "Itilde":                "0128",
    # "Oacute":                "00D3",
    # "Ocircumflex":           "00D4",
    # "Ocircumflexacute":      "1ED0",
    # "Ocircumflexdot":        "1ED8",
    # "Ocircumflexgrave":      "1ED2",
    # "Ocircumflexhook":       "1ED4",
    # "Ocircumflextilde":      "1ED6",
    # "Odot":                  "1ECC",
    # "Ograve":                "00D2",
    # "Ohook":                 "1ECE",
    # "Ohorn":                 "01A0",
    # "Ohornacute":            "1EDA",
    # "Ohorndot":              "1EE2",
    # "Ohorngrave":            "1EDC",
    # "Ohornhook":             "1EDE",
    # "Ohorntilde":            "1EE0",
    # "Otilde":                "00D5",
    # "Uacute":                "00DA",
    # "Udot":                  "1EE4",
    # "Ugrave":                "00D9",
    # "Uhook":                 "1EE6",
    # "Uhorn":                 "01AF",
    # "Uhornacute":            "1EE8",
    # "Uhorndot":              "1EF0",
    # "Uhorngrave":            "1EEA",
    # "Uhornhook":             "1EEC",
    # "Uhorntilde":            "1EEE",
    # "Utilde":                "0168",
    # "Yacute":                "00DD",
    # "Ydot":                  "1E8E",
    # "Ydotbelow":             "1EF4",
    # "Ygrave":                "1EF2",
    # "Yhookabove":            "1EF6",
    # "Ytilde":                "1EF8",
    # "aacute":                "00E1",
    # "abreve":                "0103",
    # "abreveacute":           "1EAF",
    # "abrevedot":             "1EB7",
    # "abrevegrave":           "1EB1",
    # "abrevehook":            "1EB3",
    # "abrevetilde":           "1EB5",
    # "acircumflex":           "00E2",
    # "acircumflexacute":      "1EA5",
    # "acircumflexdot":        "1EAD",
    # "acircumflexgrave":      "1EA7",
    # "acircumflexhook":       "1EA9",
    # "acircumflextilde":      "1EAB",
    # "adot":                  "1EA1",
    # "agrave":                "00E0",
    # "ahook":                 "1EA3",
    # "atilde":                "00E3",
    # "dcroat":                "0111",
    # "eacute":                "00E9",
    # "ecircumflex":           "00EA",
    # "ecircumflexacute":      "1EBF",
    # "ecircumflexdot":        "1EC7",
    # "ecircumflexgrave":      "1EC1",
    # "ecircumflexhook":       "1EC3",
    # "ecircumflextilde":      "1EC5",
    # "edot":                  "1EB9",
    # "egrave":                "00E8",
    # "ehook":                 "1EBB",
    # "etilde":                "1EBD",
    # "iacute":                "00ED",
    # "idot":                  "1ECB",
    # "igrave":                "00EC",
    # "ihook":                 "1EC9",
    # "itilde":                "0129",
    # "oacute":                "00F3",
    # "ocircumflex":           "00F4",
    # "ocircumflexacute":      "1ED1",
    # "ocircumflexdot":        "1ED9",
    # "ocircumflexgrave":      "1ED3",
    # "ocircumflexhook":       "1ED5",
    # "ocircumflextilde":      "1ED7",
    # "odot":                  "1ECD",
    # "ograve":                "00F2",
    # "ohook":                 "1ECF",
    # "ohorn":                 "01A1",
    # "ohornacute":            "1EDB",
    # "ohorndot":              "1EE3",
    # "ohorngrave":            "1EDD",
    # "ohornhook":             "1EDF",
    # "ohorntilde":            "1EE1",
    # "otilde":                "00F5",
    # "uacute":                "00FA",
    # "udot":                  "1EE5",
    # "ugrave":                "00F9",
    # "uhook":                 "1EE7",
    # "uhorn":                 "01B0",
    # "uhornacute":            "1EE9",
    # "uhorndot":              "1EF1",
    # "uhorngrave":            "1EEB",
    # "uhornhook":             "1EED",
    # "uhorntilde":            "1EEF",
    # "utilde":                "0169",
    # "yacute":                "00FD",
    # "ydot":                  "1E8F",
    # "ydotbelow":             "1EF5",
    # "ygrave":                "1EF3",
    # "yhookabove":            "1EF7",
    # "ytilde":                "1EF9"
}

def addUnicodeForGlyph(g):
    if g.unicode == None or g.unicodes == []:
            if g.name in agl.AGL2UV:
                uni = agl.AGL2UV[g.name]
    
                g.unicode = hex(uni)
    
                print(g.unicodes)
            elif g.name[:3] == "uni":
                uni = g.name[-4:]
            
                if uni != "case":
            
                    g.unicode = uni
                    print(g.name, g.unicodes, uni)
                    
def addUnicodeForTrickyGlyphs(g):
    # if g.unicodes == ():
    if g.unicodes != unicodeNameMatches.get(g.name, "unicode"):
        uni = unicodeNameMatches.get(g.name, "unicode")
        
        if uni != "unicode":
            print(g.name, uni)
            g.unicode = uni


### use the below to use the current font (and comment out lines below)

# def sortFont(font):
#     # the new default is at the end, so this will re-apply a "smart sort" to the font
#     newGlyphOrder = font.naked().unicodeData.sortGlyphNames(font.glyphOrder, sortDescriptors=[dict(type="cannedDesign", ascending=True, allowPseudoUnicode=True)])
#     font.glyphOrder = newGlyphOrder


files = getFile("Select files to add unicodes to", allowsMultipleSelection=True, fileTypes=["ufo"])

for file in files:
    font = OpenFont(file, showInterface=False)
    for g in font:
        addUnicodeForGlyph(g)
        addUnicodeForTrickyGlyphs(g)
    # sortFont(font)

    font.save()

    # font.close()