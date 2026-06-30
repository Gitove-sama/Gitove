[app]
# (str) عنوان تطبيقك
title = My Clock App

# (str) اسم الحزمة (يجب أن يكون فريداً)
package.name = myclockapp
package.domain = org.test

# (str) الملف الرئيسي لتطبيقك
source.main = main.py

# (str) المجلد الذي يحتوي على الكود والصور
source.dir = .

# (list) الملفات التي يجب تضمينها
source.include_exts = py,png,jpg,kv,atlas

# (list) المكتبات المطلوبة
requirements = python3,kivy

# (str) إصدار التطبيق
version = 0.1

# (list) اتجاه الشاشة
orientation = portrait

# (bool) ملء الشاشة
fullscreen = 1

# --- إعدادات التوافق مع GitHub Actions ---
# تحديد الإصدارات لضمان الاستقرار وعدم الفشل أثناء البناء
android.sdk = 34
android.build_tools_version = 34.0.0
android.api = 34
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
# (int) مستوى السجلات (2 = تصحيح أخطاء)
log_level = 2
warn_on_root = 1
