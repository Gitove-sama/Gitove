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

# (list) الملفات التي يجب تضمينها (تأكد من وجود png)
source.include_exts = py,png,jpg,kv,atlas

# (list) المكتبات المطلوبة (أضف هنا أي مكتبة تستخدمها مثل kivy أو pygame)
requirements = python3,kivy

# (str) إصدار التطبيق
version = 0.1

# (list) اتجاه الشاشة (портрет = portrait)
orientation = portrait

# (bool) ملء الشاشة
fullscreen = 1

# (str) أيقونة التطبيق (اختياري)
# icon.filename = %(source.dir)s/data/icon.png

[buildozer]
# (int) مستوى السجلات (0 = خطأ، 1 = معلومات، 2 = تصحيح)
log_level = 2
warn_on_root = 1