[app]
# نام اپلیکیشن
title = Graphical Calculator
# نام پکیج (یونیک باشه)
package.name = calculator
package.domain = org.example

# فایل اصلی پروژه
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# نسخه اپلیکیشن
version = 0.1

# نیازمندی‌ها (کتابخانه‌ها)
requirements = python3,kivy

# آیکون اپلیکیشن (اختیاری)
icon.filename = %(source.dir)s/icon.png

# مجوزهای اندروید (اگر لازم داری اضافه کن)
android.permissions = INTERNET

# حالت اجرا
fullscreen = 0

[buildozer]
# هدف ساخت
log_level = 2
warn_on_root = 1

# پلتفرم هدف
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = armeabi-v7a

# خروجی
android.debug = True
