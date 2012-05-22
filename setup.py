#!/usr/bin/env python
"""Setup script for building prosail's python bindings"""

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(parent_package,top_path)
    config.add_extension('prosail', ['prosail/dataSpec_P5B.f90', \
        "prosail/dladgen.f", "prosail/LIDF.f90", "prosail/MODULE_PRO4SAIL.f90", \
        "prosail/PRO4SAIL.f90", "prosail/prospect_5B.f90", \
        "prosail/run_prosail.f90","prosail/tav_abs.f90", \
        "prosail/volscatt.f90","prosail/prosail.pyf"] )
    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    # Global variables for this extension:
    name         = "prosail"  # name of the generated python extension (.so)
    description  = "PRO4SAIL python wrappers"
    author       = "J Gomez-Dans/NCEO & University College London"
    author_email = "j.gomez-dans@ucl.ac.uk"
    
    setup( name=name,\
        description=description, \
        author=author, \
        author_email = author_email, \
        configuration = configuration, version="1.0.1",\
        packages=["prosail"])
