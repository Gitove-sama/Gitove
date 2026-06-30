[app]
title = My Clock App
package.name = myclockapp
package.domain = org.test
source.main = main.py
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
version = 0.1
orientation = portrait
fullscreen = 1

# --- إعدادات توافق هامة ---
android.sdk = 33
android.build_tools_version = 33.0.0
android.api = 33
android.ndk = 25b
android.archs = arm64-v8a
