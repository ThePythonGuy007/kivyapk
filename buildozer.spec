[app]

title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.11,kivy==2.2.1

orientation = portrait

#
# Android specific
#
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

#
# Buildozer specific
#
[buildozer]
log_level = 2
warn_on_root = 1
