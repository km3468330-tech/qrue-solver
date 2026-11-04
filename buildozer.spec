[app]
title = QRUE SOLVER
package.name = qruesolver
package.domain = org.egyptianhacker
source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 1.0
requirements = python3,kivy,android
orientation = portrait
fullscreen = 0
icon.filename = icon.png
android.permissions = INTERNET

android.api = 31
android.min_api = 21
android.sdk = 33
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
