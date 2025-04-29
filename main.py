import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

APP_NAME = 'Paranoia'
APP_VERSION = 'v0.1'

from p_cryptography import encrypt, decrypt

class ParanoiaApp(App):
    def build(self):
        self.scroll_view = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True,
            size_hint_x=1,
            size_hint_y=1
            )
        
        self.layout = BoxLayout(
            orientation='vertical', 
            size_hint_y=2,
            size_hint_x=1,
            padding=10, 
            spacing=20
            )

        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.scroll_view.add_widget(self.layout)

        self.title_lable = Label(
            text=f'{APP_NAME} - {APP_VERSION}',
            size_hint_y=0.05,
            size_hint_x=1,
        )
        self.layout.add_widget(self.title_lable)
        
        self.key_input = TextInput(
            hint_text='Enter encryption password', 
            multiline=False,
            password=True,
            size_hint_y=0.05
            )
        self.layout.add_widget(self.key_input)

        self.text_input = TextInput(
            hint_text='Plain text',
            size_hint_y=0.15
            )
        self.layout.add_widget(self.text_input)

        self.encrypt_button = Button(
            text='Encrypt',
            size_hint_y=0.05
            )
        self.encrypt_button.bind(on_press=self.handle_encrypt)
        self.layout.add_widget(self.encrypt_button)

        self.decrypt_button = Button(
            text='Decrypt',
            size_hint_y=0.05
            )
        self.decrypt_button.bind(on_press=self.handle_decrypt)
        self.layout.add_widget(self.decrypt_button)

        self.encrypted_text_input = TextInput(
            hint_text='Encrypted text',
            size_hint_y=0.15
            )
        self.layout.add_widget(self.encrypted_text_input)

        self.dummy_layout = BoxLayout(
            orientation='vertical', 
            size_hint_y=1,
            size_hint_x=1
            )
        
        self.layout.add_widget(self.dummy_layout)

        return self.scroll_view
    
    def show_alert(self, instance, title='Alert', message='This is a default message'):
        alert_label = Label(text=message)

        self.popup = Popup(
            title=title, 
            content=alert_label,
            size_hint_x=0.9, 
            size_hint_y=0.5,
            auto_dismiss=True
            )
        self.popup.open()

    
    def handle_encrypt(self, instance):
        password = self.key_input.text
        text = self.text_input.text
        if password and text:
            encrypted = encrypt(text, password)
            self.encrypted_text_input.text = encrypted
        else:
            self.show_alert(instance, 'Invalid Input', 'Please provide a password and a plain text.')

    def handle_decrypt(self, instance):
        password = self.key_input.text
        text = self.encrypted_text_input.text
        if password and text:
            try:
                decrypted = decrypt(text, password)
                self.text_input.text = decrypted
            except Exception as e:
                self.show_alert(instance, 'Error', str(e)) 
        else:
            self.show_alert(instance, 'Invalid Input', 'Please provide a password and an encrypted text.')

    


if __name__ == "__main__":
    ParanoiaApp().run()
