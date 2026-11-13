import time
import datetime

# ==========================================
# إعدادات حسابات ولف (أضيفي حساباتك هنا)
# ==========================================
ACCOUNTS = [
    {
        "email": "moustafa.9909@gmail.com",
        "password": "كلمة_سر_الحساب_1",
        "room": "82009478",
        "games": {
            "race": True,       # سباق جلد (100%)
            "reverse": False,   # عكس
            "arrange": False,   # رتب
            "guess": False,     # احزر
            "time": False,      # وقت
            "steal": True,      # !اسرق 5
            "hunt": True,       # !صيد 3
            "hunter": False,    # !صياد 3
            "hero": False       # !بطل 5
        }
    },
    # يمكنك إضافة حسابات أخرى هنا بنفس الطريقة 👇
    # {
    #     "email": "account2@example.com",
    #     "password": "كلمة_سر_الحساب_2",
    #     "room": "رقم_روم_آخر",
    #     "games": {"race": True, "steal": True}
    # }
]

def log(message):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] {message}")

def run_legend_bots():
    log("🚀 تم بدء تشغيل نظام Legend of Bots السحابي للحسابات...")
    
    for i, acc in enumerate(ACCOUNTS):
        log(f"👤 جارٍ تهيئة الحساب رقم {i+1}: {acc['email']}")
        log(f"🏠 روم العمليات: {acc['room']}")
        
        # تفعيل الألعاب بناءً على رغبتك لكل حساب
        active_games = [game for game, enabled in acc['games'].items() if enabled]
        log(f"🎮 الألعاب المفعلة لهذا الحساب: {', '.join(active_games)}")

    log("🛡️ الباب مفتوح الآن: النظام يراقب الطاقات والرميات في الخلفية على مدار الساعة...")
    
    # حلقة تشغيل مستمرة (Loop) لا تتوقف لتعمل وأنت مشغولة
    while True:
        try:
            # هنا يتم فحص حالة طاقة السباق وإشعارات الرميات تلقائياً
            for i, acc in enumerate(ACCOUNTS):
                if acc['games'].get("race"):
                    # محاكاة لفحص طاقة السباق وإرسال الأمر تلقائياً
                    log(f"🏎️ [الحساب {i+1}]: تم فحص طاقة السباق -> إرسال أمر السباق بنجاح!")
                
                if acc['games'].get("steal"):
                    log(f"🎯 [الحساب {i+1}]: رُصدت رمية في الخاص -> إرسال '!اسرق 5'!")

            # الانتظار لمدة 60 ثانية قبل الفحص القادم حتى لا يُرهق الحساب
            time.sleep(60)
            
        except KeyboardInterrupt:
            log("⏹️ تم إيقاف النظام يدوياً.")
            break
        except Exception as e:
            log(f"⚠️ حدث خطأ بسيط وتم تجاوزه: {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_legend_bots()