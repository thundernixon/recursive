from vanilla.dialogs import *
from mojo.UI import OutputWindow
import metricsMachine

## use if you want to select different files
files = getFile(
    "Select files to add blank kerning to",
    allowsMultipleSelection=True,
    fileTypes=["ufo"],
)

## uncomment if you wish to see output window
OutputWindow().show()
OutputWindow().clear()

for fontPath in files:
    f = OpenFont(fontPath, showInterface=False)

    if len(f.kerning) == 0:
        f.kerning[("A", "A")] = 0
        f.kerning[("pi", "pi")] = 0
        # del f.kerning[("A","A")]

    print(f.info.styleName)
    print("groups: " + str(len(f.groups)))
    print("\n")

    f.save()
    f.close()


# common_keys_vals = [(key, [dict[key] for dict in components.keys()])]
