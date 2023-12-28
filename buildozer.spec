[app]

# (str) Title of your application
title = TVPlotGenerator

# (str) Package name
package.name = tvplotgenerator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.tvplotgenerator

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd

[buildozer]

# (list) Application source code
source.include_exts = py,png,jpg,kv,atlas

# (list) Garden requirements (optional)
garden_requirements = kivymd

# (list) List of inclusions using pattern matching
include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
include_patterns = assets/*,images/*.png

# (str) Application versioning (method 1)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (str) Application versioning (method 2)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd

# (str) Custom source folders for requirements
source.include_exts = py,png,jpg,kv,atlas
