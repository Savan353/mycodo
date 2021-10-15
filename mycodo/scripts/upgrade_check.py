# -*- coding: utf-8 -*-
# Perform checks used during install/upgrade

import os
import sys

sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))

from mycodo.config_maintenance import MAINTENANCE_MODE

if __name__ == "__main__": #https://www.youtube.com/watch?v=Gy74MjEpnYw&ab_channel=CodeWithHarry
    try:
        if sys.argv[1] == '--min_python_version': # sys.argv [1] https://www.youtube.com/watch?v=Qi-8zaBfRWI

            if not sys.version_info.major >= int(sys.argv[2].split('.')[0]): #sys.version_info.major https://stackoverflow.com/questions/44249513/python-version-check-major-attribute
                sys.exit(1)
            if not sys.version_info.minor >= int(sys.argv[2].split('.')[1]):
                sys.exit(1)

        elif sys.argv[1] == '--maintenance_mode': # to check https://github.com/kizniche/Mycodo/blob/master/install/setup.sh to maintence mode

            if not MAINTENANCE_MODE:
                sys.exit(1)

    except:
        sys.exit(1)
