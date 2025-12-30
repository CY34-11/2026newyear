import time
import random
from math import sin, cos, pi

try:
    import androidhelper as android
    droid = android.Android()
    HAS_ANDROID = True
except ImportError:
    HAS_ANDROID = False

# 目标时间：2026年1月1日0点
TARGET_TIME = time.mktime((2026, 1, 1, 0, 0, 0, 0, 0, 0))

# 专属祝福库
WISHES = {
    "default": ["新岁启幕，万事顺意！", "2026，暴富暴美暴好运！", "烟火向星辰，所愿皆成真~"],
    "彩蛋": ["今年会有超棒的奇遇哦！", "偷偷告诉你，你是2026的幸运儿✨", "已为你加载好全年好运buff！"]
}

# 幸运签
LUCKY_SIGNS = ["事业腾飞签", "桃花朵朵签", "财运亨通签", "健康无忧签", "心想事成签"]

def clear_screen():
    print("\033c", end="")

def get_name():
    name = input("✨ 请输入你的名字，领取专属跨年祝福：")
    return name if name else "亲爱的朋友"

def show_countdown(remaining, name):
    days = remaining // 86400
    hours = (remaining % 86400) // 3600
    minutes = (remaining % 3600) // 60
    seconds = remaining % 60
    print(f"💖 {name}专属跨年倒计时 💖\n")
    print(f"⏰ {days}天 {hours:02d}时 {minutes:02d}分 {seconds:02d}秒 ⏰\n")
    print("——————✨ 期待值拉满ing ✨——————")

def fireworks(name):
    clear_screen()
    wish = random.choice(WISHES["default"])
    if random.random() < 0.3:  # 30%概率触发彩蛋
        wish = random.choice(WISHES["彩蛋"])
    sign = random.choice(LUCKY_SIGNS)
    print(f"\n\n🎉🎉🎉 {name}！新年快乐！🎉🎉🎉")
    print(f"\n🌟 {wish} 🌟")
    print(f"\n🎐 你的2026幸运签：{sign} 🎐\n")
    
    # 动态烟花
    width, height = 35, 18
    colors = ["\033[91m", "\033[93m", "\033[92m", "\033[94m", "\033[95m", "\033[96m"]
    for round in range(10):
        x = random.randint(5, width-5)
        y = random.randint(2, height-2)
        color = random.choice(colors)
        radius = random.randint(2, 5)
        frame = [[" " for _ in range(width)] for __ in range(height)]
        # 烟花爆炸效果
        for angle in range(360):
            rad = angle * pi / 180
            fx = int(x + radius * cos(rad) * (1 - round/10))
            fy = int(y + radius * sin(rad) * (1 - round/10))
            if 0 <= fx < width and 0 <= fy < height:
                frame[fy][fx] = color + "*" + "\033[0m"
        # 流星点缀
        if round % 3 == 0:
            mx = random.randint(0, width-10)
            my = random.randint(0, height//2)
            for i in range(10):
                if mx+i < width and my+i < height:
                    frame[my+i][mx+i] = "\033[97m" + "★" + "\033[0m"
        for row in frame:
            print("".join(row))
        time.sleep(0.2)
        clear_screen()
    
    print(f"\n💪 {name}，新的一年一起冲鸭！💪\n")
    if HAS_ANDROID:
        droid.makeToast(f"{name}！2026新年快乐！")

if _name_ == "_main_":
    try:
        clear_screen()
        name = get_name()
        while True:
            now = time.time()
            remaining = int(TARGET_TIME - now)
            if remaining <= 0:
                fireworks(name)
                break
            clear_screen()
            show_countdown(remaining, name)
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n💫 {name}，提前祝你跨年快乐~下次见！")
