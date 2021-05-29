from distutils.core import setup
import py2exe
import sys
sys.stderr = sys.stdout

setup(
    options = {'py2exe': {'bundle_files': 2, 'compressed': True}},
    windows = [
        {
            "script": "PicFinder.py",
            "icon_resources": [(1, "PicFinderIco.ico")]
        }
    ],
    zipfile = None,
    version = "1.0.1"
    
)