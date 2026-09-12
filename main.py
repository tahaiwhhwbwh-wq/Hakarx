from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

class MyFirstApp(App):
    def build(self):
        # تصميم واجهة رأسية للتطبيق
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # إضافة نص ترحيبي
        self.my_label = Label(text="مرحباً بك في تطبيقي الأول!", font_size='24sp')
        layout.add_widget(self.my_label)
        
        # إضافة زر تفاعلي
        btn = Button(text="اضغط هنا لتغيير الخلفية", size_hint=(1, 0.3), background_color=(0, 0.7, 0.9, 1))
        btn.bind(on_press=self.change_color)
        layout.add_widget(btn)
        
        return layout

    def change_color(self, instance):
        # تغيير نص الترحيب عند الضغط على الزر
        self.my_label.text = "تم الضغط بنجاح! 🚀"

if __name__ == '__main__':
    MyFirstApp().run()
