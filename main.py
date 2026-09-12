from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # استخدام FloatLayout لتركيب الخلفية ووضع الأزرار فوقها
        layout = FloatLayout()
        
        # 1. إضافة صورة خلفية سونيك للمشروع
        bg = Image(source='sonic_bg.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg)
        
        # صندوق واجهة النصوص والأزرار باللون الشفاف فوق الخلفية
        content = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(0.9, 0.8), pos_hint={'x': 0.05, 'y': 0.1})
        
        title = Label(text="مدرسة الهكر الأخلاقي 🛡️", font_size='28sp', bold=True, color=(1, 1, 1, 1))
        content.add_widget(title)
        
        desc = Label(text="تعلم حماية الأنظمة واختبار الاختراق بصورة آمنة", font_size='16sp', color=(1, 1, 1, 1))
        content.add_widget(desc)
        
        start_btn = Button(text="ابدأ الدرس الأول 🚀", size_hint=(1, 0.2), background_color=(0, 0.6, 0.3, 1), font_size='20sp')
        start_btn.bind(on_press=self.go_to_lesson)
        content.add_widget(start_btn)
        
        layout.add_widget(content)
        self.add_widget(layout)

    def go_to_lesson(self, instance):
        self.manager.current = 'lesson'

class LessonScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        bg = Image(source='sonic_bg.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg)
        
        content = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint=(0.9, 0.8), pos_hint={'x': 0.05, 'y': 0.1})
        
        lesson_title = Label(text="الدرس الأول: الهندسة الاجتماعية", font_size='22sp', bold=True)
        content.add_widget(lesson_title)
        
        lesson_content = Label(
            text="الهندسة الاجتماعية هي فن خداع البشر واختراق عقولهم\nللحصول على معلومات سرية (مثل كلمة المرور)\nدون الحاجة لأدوات اختراق معقدة.\n\nأشهر أنواعها: التصيد الاحتيالي (Phishing).",
            font_size='16sp', halign='center'
        )
        content.add_widget(lesson_content)
        
        quiz_btn = Button(text="الانتقال إلى الاختبار 📝", size_hint=(1, 0.2), background_color=(0.1, 0.5, 0.8, 1))
        quiz_btn.bind(on_press=self.go_to_quiz)
        content.add_widget(quiz_btn)
        
        layout.add_widget(content)
        self.add_widget(layout)

    def go_to_quiz(self, instance):
        self.manager.current = 'quiz'

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        
        bg = Image(source='sonic_bg.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg)
        
        content = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint=(0.9, 0.8), pos_hint={'x': 0.05, 'y': 0.1})
        
        self.question = Label(text="سؤال: ما هو هدف الهندسة الاجتماعية الأساسي؟", font_size='18sp', bold=True)
        content.add_widget(self.question)
        
        self.ans1 = Button(text="أ) اختراق أجهزة التوجيه (Router)", size_hint=(1, 0.15))
        self.ans2 = Button(text="ب) خداع البشر للحصول على معلوماتهم", size_hint=(1, 0.15))
        self.ans3 = Button(text="ج) تشفير الملفات وطلب فدية", size_hint=(1, 0.15))
        
        self.ans1.bind(on_press=self.check_wrong)
        self.ans2.bind(on_press=self.check_correct)
        self.ans3.bind(on_press=self.check_wrong)
        
        content.add_widget(self.ans1)
        content.add_widget(self.ans2)
        content.add_widget(self.ans3)
        
        self.result = Label(text="", font_size='18sp', bold=True)
        content.add_widget(self.result)
        
        layout.add_widget(content)
        self.add_widget(layout)

    def check_correct(self, instance):
        self.result.text = "إجابة صحيحة! 🎉 أحسنت يا بطل الأمن السيبراني."
        self.result.color = (0, 1, 0, 1)

    def check_wrong(self, instance):
        self.result.text = "إجابة خاطئة! ❌ راجع الدرس وحاول مرة أخرى."
        self.result.color = (1, 0, 0, 1)

class CyberSecurityApp(App):
    def build(self):
        # تشغيل أغنية سونيك في الخلفية تلقائياً فور فتح التطبيق
        self.sound = SoundLoader.load('sonic_song.mp3')
        if self.sound:
            self.sound.loop = True  # تكرار الأغنية تلقائياً
            self.sound.play()
            
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(LessonScreen(name='lesson'))
        sm.add_widget(QuizScreen(name='quiz'))
        return sm

if __name__ == '__main__':
    CyberSecurityApp().run()

