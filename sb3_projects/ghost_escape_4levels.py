"""
لعبة الهروب من الشبح 👻 - ٤ مستويات
Ben يحاول النجاة. الشبح يتحرك ببطء نحوه.
الطالب يبني الكود بنفسه قبل أن يصل الشبح!

المستويات (تلقائية - اضغط العلم الأخضر للبدء من ١):
  ١ الغابة: اهرب إلى النجمة ← تصل للنجمة تنتقل للمدينة
  ٢ المدينة: ابتعد عن الشبح ← تصمد ١٥ ثانية تنتقل للبحر
  ٣ البحر: الحق النجمة المتحركة ← تمسكها تنتقل للفضاء
  ٤ الفضاء: النهاية ← المس النجمة لتفوز باللعبة

ملاحظة للمدرس: كود Ben فارغ عن قصد (TODO فقط).
كود Ghost و Star جاهز. النصوص قصيرة بالفصحى.
لا يذكر أي أمر سكراتش - الطالب يختار بحرية.
"""
import json
from scratch import transpile_to_json, save_sb3
from scratch.dsl import *


class Ben:
    def when_flag_clicked(self):
        switch_backdrop("backdrop1")

    def when_backdrop_backdrop1(self):
        go_to_xy(-170, -20)
        point_in_direction(90)
        play_sound("Pop")
        say_for_secs("المستوى ١: اهرب إلى النجمة ⭐", 2)
        # ---------------------------------------------
        # مهمة الطالب - المستوى ١
        # الهدف: الوصول إلى النجمة.
        # (ممنوع كتابة الحل هنا)
        # ---------------------------------------------
        wait(1)
        say("هيا! 🏃")

    def when_backdrop_level2(self):
        go_to_xy(-170, -60)
        point_in_direction(90)
        play_sound("Pop")
        say_for_secs("المستوى ٢: ابتعد عن الشبح 👻", 2)
        # ---------------------------------------------
        # مهمة الطالب - المستوى ٢
        # الهدف: البقاء بعيدا عن الشبح.
        # الفوز لا يحتاج لمس النجمة.
        # (ممنوع كتابة الحل هنا)
        # ---------------------------------------------
        wait(1)
        say("احذر! 🏃")

    def when_backdrop_level3(self):
        go_to_xy(-170, 40)
        point_in_direction(90)
        play_sound("Pop")
        say_for_secs("المستوى ٣: الحق النجمة ⭐", 2)
        # ---------------------------------------------
        # مهمة الطالب - المستوى ٣
        # الهدف: اللحاق بالنجمة المتحركة.
        # (ممنوع كتابة الحل هنا)
        # ---------------------------------------------
        wait(1)
        say("أسرع! 🏊")

    def when_backdrop_level4(self):
        go_to_xy(-170, 0)
        point_in_direction(90)
        play_sound("Pop")
        say_for_secs("المستوى ٤: النهاية 🚀", 2)
        # ---------------------------------------------
        # مهمة الطالب - المستوى ٤
        # الهدف: الفوز في النهاية.
        # لك حرية الاختيار.
        # (ممنوع كتابة الحل هنا)
        # ---------------------------------------------
        wait(1)
        say("هيا! 🏆")


class Ghost:
    def when_flag_clicked(self):
        go_to_xy(-210, 100)
        play_sound("Scream1")
        say_for_secs("أنا قادم! 👻", 2)
        while True:
            point_towards("Ben")
            move(2)
            wait(0.35)
            if touching("Ben"):
                play_sound_until_done("Drum Buzz")
                say("مسكتك! اضغط العلم وحاول مجددا 👻")
                stop("all")

    def when_backdrop_backdrop1(self):
        go_to_xy(-210, 100)
        say("أنا بطيء... 👻")

    def when_backdrop_level2(self):
        go_to_xy(-170, 10)
        say("أنا أسرع! 👻")

    def when_backdrop_level3(self):
        go_to_xy(-150, 90)
        say("أنا قريب! 👻")

    def when_backdrop_level4(self):
        go_to_xy(-120, 60)
        say("النهاية قريبة! 👻")


class Star:
    def when_flag_clicked(self):
        go_to_xy(180, 0)
        say("تعال إلي ⭐")
        while True:
            if touching("Ben"):
                if backdrop_name() == "backdrop1":
                    play_sound("collect")
                    say_for_secs("أحسنت! المستوى التالي ➡️", 2)
                    switch_backdrop("level2")
                elif backdrop_name() == "level2":
                    play_sound("collect")
                    say("أحسنت! استمر! ⭐")
                    wait(2)
                elif backdrop_name() == "level3":
                    play_sound("collect")
                    say_for_secs("رائع! المستوى التالي ➡️", 2)
                    switch_backdrop("level4")
                elif backdrop_name() == "level4":
                    play_sound_until_done("Splash Cymbal")
                    say("فزت باللعبة! 🏆")
                    stop("all")
            wait(0.2)

    def when_backdrop_backdrop1(self):
        go_to_xy(180, 0)
        say("أنا هنا ⭐")

    def when_backdrop_level2(self):
        go_to_xy(180, -30)
        say("اثبت مكانك! ⭐")
        wait(15)
        if backdrop_name() == "level2":
            play_sound("Clapping")
            say_for_secs("نجوت! المستوى التالي ➡️", 2)
            switch_backdrop("level3")

    def when_backdrop_level3(self):
        go_to_xy(170, 50)
        play_sound("Bubbles")
        say("الحقني! ⭐")
        while True:
            if backdrop_name() == "level3":
                change_y(50)
                wait(1)
                change_y(-50)
                wait(1)
            else:
                stop("this script")

    def when_backdrop_level4(self):
        go_to_xy(180, 20)
        say("النهاية هنا 🏆")


if __name__ == "__main__":
    with open(__file__) as f:
        source = f.read()
    json_str = transpile_to_json(source)
    data = json.loads(json_str)

    # حماية: scratch.mit.edu لا يشغّل أصوات ADPCM (يفشل تحميل المشروع).
    # استخدم أصوات WAV عادية فقط - راجع dataFormat في sounds_library.
    bad = [(t["name"], s["name"]) for t in data["targets"] for s in t.get("sounds", []) if s.get("dataFormat") == "adpcm"]
    if bad:
        raise SystemExit(f"ADPCM sounds break scratch.mit.edu upload, replace them: {bad}")

    # خلفيات ملونة حقيقية (SVG) - مختلفة لكل مستوى
    svg_forest = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360"><rect width="480" height="360" fill="#8FD694"/><circle cx="420" cy="50" r="30" fill="#FFEB3B"/><rect x="60" y="200" width="20" height="60" fill="#795548"/><polygon points="70,120 30,210 110,210" fill="#2E7D32"/><rect x="200" y="210" width="20" height="60" fill="#795548"/><polygon points="210,130 170,220 250,220" fill="#388E3C"/><rect x="340" y="200" width="20" height="60" fill="#795548"/><polygon points="350,120 310,210 390,210" fill="#2E7D32"/><rect y="260" width="480" height="100" fill="#558B2F"/><circle cx="150" cy="300" r="8" fill="#FF5252"/><circle cx="300" cy="310" r="8" fill="#FF5252"/><circle cx="100" cy="320" r="8" fill="#FFFFFF"/></svg>'''
    svg_city = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360"><rect width="480" height="360" fill="#87CEEB"/><rect x="40" y="100" width="90" height="180" fill="#78909C"/><rect x="150" y="60" width="110" height="220" fill="#90A4AE"/><rect x="280" y="120" width="80" height="160" fill="#78909C"/><rect x="380" y="80" width="70" height="200" fill="#90A4AE"/><rect x="55" y="120" width="20" height="20" fill="#FFEB3B"/><rect x="85" y="120" width="20" height="20" fill="#FFEB3B"/><rect x="55" y="160" width="20" height="20" fill="#FFEB3B"/><rect x="165" y="80" width="20" height="20" fill="#FFEB3B"/><rect x="195" y="80" width="20" height="20" fill="#FFEB3B"/><rect x="225" y="80" width="20" height="20" fill="#FFEB3B"/><rect y="280" width="480" height="80" fill="#455A64"/><rect x="0" y="312" width="480" height="8" fill="#FFFFFF"/></svg>'''
    svg_sea = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360"><rect width="480" height="360" fill="#0288D1"/><rect y="240" width="480" height="120" fill="#01579B"/><path d="M0,240 Q30,220 60,240 T120,240 T180,240 T240,240 T300,240 T360,240 T420,240 T480,240 L480,260 L0,260 Z" fill="#4FC3F7"/><ellipse cx="150" cy="150" rx="40" ry="20" fill="#FF9800"/><polygon points="190,150 215,135 215,165" fill="#FF9800"/><circle cx="140" cy="148" r="4" fill="black"/><circle cx="300" cy="100" r="6" fill="none" stroke="white" stroke-width="2"/><circle cx="320" cy="70" r="8" fill="none" stroke="white" stroke-width="2"/><circle cx="250" cy="280" r="6" fill="none" stroke="white" stroke-width="2"/><polygon points="350,280 370,280 360,300" fill="#4CAF50"/><rect x="355" y="250" width="10" height="35" fill="#4CAF50"/></svg>'''
    svg_space = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360"><rect width="480" height="360" fill="#0B0B3B"/><circle cx="50" cy="40" r="3" fill="white"/><circle cx="120" cy="90" r="2" fill="white"/><circle cx="200" cy="30" r="3" fill="white"/><circle cx="300" cy="70" r="2" fill="white"/><circle cx="400" cy="40" r="3" fill="white"/><circle cx="450" cy="120" r="2" fill="white"/><circle cx="80" cy="200" r="2" fill="white"/><circle cx="250" cy="150" r="2" fill="white"/><circle cx="350" cy="200" r="3" fill="white"/><circle cx="150" cy="250" r="2" fill="white"/><circle cx="350" cy="120" r="35" fill="#9C27B0"/><ellipse cx="350" cy="120" rx="60" ry="15" fill="none" stroke="#FFEB3B" stroke-width="4"/><circle cx="100" cy="280" r="25" fill="#B0BEC5"/><circle cx="92" cy="272" r="6" fill="#90A4AE"/><circle cx="108" cy="288" r="4" fill="#90A4AE"/></svg>'''

    import hashlib
    import scratch.transpiler as T

    customs = [
        ("backdrop1", svg_forest),
        ("level2", svg_city),
        ("level3", svg_sea),
        ("level4", svg_space),
    ]
    stage = data["targets"][0]
    stage["costumes"] = []
    for name, svg in customs:
        h = hashlib.md5(svg.encode()).hexdigest()
        stage["costumes"].append({
            "name": name,
            "dataFormat": "svg",
            "assetId": h,
            "md5ext": f"{h}.svg",
            "rotationCenterX": 240,
            "rotationCenterY": 180,
        })
        # سجلها كأصل مضمن حتى يحفظها save_sb3 بدون إنترنت
        T.EMBEDDED_COSTUMES[name] = svg
        T.ASSET_ID_TO_EMBEDDED[h] = name

    json_str = json.dumps(data)
    save_sb3(json_str, "ghost_escape_4levels.sb3")
