import pygame
import sys
import datetime

# 1. إعدادات النافذة الديناميكية
pygame.init()

# الحصول على أبعاد شاشة الجهاز
info = pygame.display.Info()
# نجعل النافذة مربعة لتناسب تصميم الساعة وتأخذ عرض الشاشة
SIZE = min(info.current_w, info.current_h)
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Steampunk Clock - Responsive")
clock = pygame.time.Clock()
CENTER = (SIZE // 2, SIZE // 2)

# 2. دالة مساعدة لتحجيم الصور (Responsive Scaling)
def load_and_scale(name, factor):
    img = pygame.image.load(name).convert_alpha()
    w, h = img.get_size()
    # نحسب الحجم الجديد بناءً على نسبة مئوية من حجم الشاشة
    new_w = int(SIZE * factor)
    new_h = int(h * (new_w / w)) # الحفاظ على نسبة العرض للارتفاع
    return pygame.transform.smoothscale(img, (new_w, new_h))

try:
    # تحميل الصور مع تحجيمها (عدل الـ factor حسب حجم صورك الأصلي)
    clock_face = pygame.transform.smoothscale(pygame.image.load("image_5.png").convert_alpha(), (SIZE, SIZE))
    hour_hand = load_and_scale("image_6.png", 0.5)
    minute_hand = load_and_scale("image_7.png", 0.6)
    second_hand = load_and_scale("image_8.png", 0.6)
except pygame.error as e:
    print(f"خطأ في تحميل الصور: {e}")
    sys.exit()

def blit_rotate(surf, image, pos, origin_pos, angle):
    rotated_image = pygame.transform.rotate(image, -angle)
    # حساب نقطة الارتكاز بناءً على حجم الصورة الحالي
    image_center = pygame.math.Vector2(origin_pos) - pygame.math.Vector2(image.get_rect().center)
    rotated_image_center = image_center.rotate(angle)
    rect = rotated_image.get_rect(center=pos - rotated_image_center)
    surf.blit(rotated_image, rect)

# 3. حلقة التشغيل
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    now = datetime.datetime.now()
    ms = now.microsecond / 1000000.0
    
    sec_angle = ((now.second + ms) * 6)
    min_angle = ((now.minute + now.second / 60.0) * 6)
    hour_angle = (((now.hour % 12) + now.minute / 60.0) * 30)

    # نقاط الارتكاز (تُحسب كنسبة من أبعاد الصورة)
    hour_pivot = (hour_hand.get_width() // 2, hour_hand.get_height() * 0.663)
    minute_pivot = (minute_hand.get_width() // 2, minute_hand.get_height() * 0.5)
    second_pivot = (second_hand.get_width() // 2, second_hand.get_height() * 0.5)

    # الرسم
    screen.blit(clock_face, (0, 0))
    blit_rotate(screen, minute_hand, CENTER, minute_pivot, min_angle)
    blit_rotate(screen, hour_hand, CENTER, hour_pivot, hour_angle)
    blit_rotate(screen, second_hand, CENTER, second_pivot, sec_angle)

    pygame.display.flip()
    clock.tick(60)