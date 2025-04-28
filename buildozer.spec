[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (can be anything you like)
package.domain = org.example

# (str) Source code directory (where your main.py is located)
source.dir = .

# (str) Main .py file
source.main = main.py

# (str) Version number (MUST set it!)
version = 0.1

# (list) Supported orientations (portrait, landscape, etc.)
orientation = portrait

# (list) List of permissions you need (optional)
# Example: permissions = INTERNET,ACCESS_FINE_LOCATION
permissions = INTERNET

# (str) Presplash screen image (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (list) Icon of your app (optional)
# icon.filename = %(source.dir)s/data/icon.png

# (list) Application requirements
requirements = python3,kivy

# (str) Custom source folders for requirements (leave empty normally)
# requirements.source =

# (str) Supported android architectures
# If not set, defaults to armeabi-v7a
android.archs = armeabi-v7a

# (bool) Indicate if the app should be fullscreen or not
fullscreen = 0

# (bool) Android: prevent APK expansion file generation
android.disable_expansion = True

# (str) Android entry point, default is ok
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is 'import android' if not set
# android.theme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project (no .git etc)
# source.include_exts = py,png,jpg,kv,atlas

# (str) Path to a custom android manifest file (optional)
# android.manifest = ./AndroidManifest.xml

# (str) Path to a custom Java file (optional)
# android.add_src = 

# (str) Path to a custom Java classes (optional)
# android.add_jars =

# (list) Gradle dependencies (if needed)
# android.gradle_dependencies =

# (bool) Copy library instead of linking (for windows)
copy_libs = 1

# (bool) Android: want to force compile Python to .pyo files?
# (pyo is deprecated now, so skip it)
# android.pyo = 0

# (bool) Want to build a release APK?
# (You will need to sign it manually)
# android.release = 0
