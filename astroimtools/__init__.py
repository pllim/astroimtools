# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
This is an Astropy affiliated package.
"""

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

# For egg_info test builds to pass, put package imports here.
if not _ASTROPY_SETUP_:
    from .arithmetic import *
    from .cutout_tools import *
    from .filtering import *
    from .lupton_rgb import *
    from .nddata_adapters import *
    from .scripts import imarith, imstats
    from .stats import *
    from .utils import *
