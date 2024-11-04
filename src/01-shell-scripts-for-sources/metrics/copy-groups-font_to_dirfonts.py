'''
    Usage:

    python "<path>/copy-groups-font_to_dirfonts.py" "<path>/<font>.ufo" <dir/to/copy/to>

    Required argument: UFO path to copy kerning & groups from

    Optional argument: Dir path of UFOs to copy to, if separate

    Assumptions: 
        - You have a single group of UFOs
        - The UFO path you feed in contains both groups.plist and kerning.plist
        - You wish to exactly copy groups.plist from the UFO path to all other UFOs in the same directory
'''

import sys
import os
import shutil

try:
    ufoToCopyFrom = sys.argv[1]
except IndexError:
    print("At least one arg required: path of UFO to copy from")

try:
    if sys.argv[2]:
        print("Copying from UFO to UFOs in another Directory")
        dirToCopyTo = sys.argv[2]
        ufosToCopyTo = next(os.walk(dirToCopyTo))[1]

        head, tail = dirToCopyTo, os.path.split(ufoToCopyFrom)[1]
except IndexError:
    print("Copying from UFO to UFOs in the same Directory")
    head, tail = os.path.split(ufoToCopyFrom)
    ufosToCopyTo = next(os.walk(head))[1]

groupsPath = f"{ufoToCopyFrom}/groups.plist"

for ufo in sorted(ufosToCopyTo):
    ufoPath = f"{head}/{ufo}"
    
    if ufoPath != ufoToCopyFrom and '.ufo' in ufoPath and 'sparse' not in ufoPath:
        print(ufoPath)
        groupsDest = f"{ufoPath}/groups.plist"
        shutil.copyfile(groupsPath, groupsDest)
