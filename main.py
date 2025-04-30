import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

APP_NAME = 'Paranoia'
APP_VERSION = 'v0.2'

from p_cryptography import encrypt, decrypt

class ParanoiaApp(App):
    def build(self):

        root_scroll_view = ScrollView()
        root_scroll_view.do_scroll_x = False
        root_scroll_view.do_scroll_y = False
        root_scroll_view.size_hint_x = 1
        root_scroll_view.size_hint_y = 1

        DEFAULT_ELEMENT_COUNT = 1 + 1 + 1 + 4 + 1 + 4 + 1
        DEFAULT_ELEMENT_HEIGHT = 1 / DEFAULT_ELEMENT_COUNT
        
        root_box_layout = BoxLayout()
        root_box_layout.orientation = 'vertical'
        root_box_layout.size_hint_x = 1
        root_box_layout.size_hint_y = 1
        root_box_layout.padding = 10
        root_box_layout.spacing = 10
        root_box_layout.bind(minimum_height=root_scroll_view.setter('height'))
        root_scroll_view.add_widget(root_box_layout)

        title_label = Label()
        title_label.text = f'{APP_NAME} - {APP_VERSION}'
        title_label.size_hint_x = 1 
        title_label.size_hint_y = DEFAULT_ELEMENT_HEIGHT
        root_box_layout.add_widget(title_label)
        
        self.password_input = TextInput()
        self.password_input.hint_text = 'Encryption Password'
        self.password_input.multiline = False
        self.password_input.password = True
        self.password_input.size_hint_x = 1
        self.password_input.size_hint_y = DEFAULT_ELEMENT_HEIGHT
        root_box_layout.add_widget(self.password_input)

        password_controls_box_layout = BoxLayout()
        password_controls_box_layout.orientation = 'horizontal'
        password_controls_box_layout.size_hint_x = 1
        password_controls_box_layout.size_hint_y = DEFAULT_ELEMENT_HEIGHT
        password_controls_box_layout.padding = 10
        password_controls_box_layout.spacing = 20
        root_box_layout.add_widget(password_controls_box_layout)

        password_copy_button= Button()
        password_copy_button.text = 'Copy'
        password_copy_button.size_hint_x = 0.5
        password_copy_button.size_hint_y = 1
        password_copy_button.bind(on_press=self.handle_password_copy)
        password_controls_box_layout.add_widget(password_copy_button)

        password_paste_button= Button()
        password_paste_button.text = 'Paste'
        password_paste_button.size_hint_x = 0.5
        password_paste_button.size_hint_y = 1
        password_paste_button.bind(on_press=self.handle_password_paste)
        password_controls_box_layout.add_widget(password_paste_button)


        self.plain_text_input = TextInput()
        self.plain_text_input.hint_text = 'Plain Text'
        self.plain_text_input.size_hint_x = 1
        self.plain_text_input.size_hint_y = DEFAULT_ELEMENT_HEIGHT * 4
        root_box_layout.add_widget(self.plain_text_input)

        plain_text_controls_box_layout = BoxLayout()
        plain_text_controls_box_layout.orientation = 'horizontal'
        plain_text_controls_box_layout.size_hint_x = 1
        plain_text_controls_box_layout.size_hint_y = DEFAULT_ELEMENT_HEIGHT
        plain_text_controls_box_layout.padding = 10
        plain_text_controls_box_layout.spacing = 20
        root_box_layout.add_widget(plain_text_controls_box_layout)

        plain_text_copy_button = Button()
        plain_text_copy_button.text = 'Copy'
        plain_text_copy_button.size_hint_x = 0.25
        plain_text_copy_button.size_hint_y = 1
        plain_text_copy_button.bind(on_press=self.handle_plain_text_copy)
        plain_text_controls_box_layout.add_widget(plain_text_copy_button)

        plain_text_paste_button= Button()
        plain_text_paste_button.text = 'Paste'
        plain_text_paste_button.size_hint_x = 0.25
        plain_text_paste_button.size_hint_y = 1
        plain_text_paste_button.bind(on_press=self.handle_plain_text_paste)
        plain_text_controls_box_layout.add_widget(plain_text_paste_button)

        self.encrypt_button = Button()
        self.encrypt_button.text = 'Encrypt'
        self.encrypt_button.size_hint_x = 0.25
        self.encrypt_button.size_hint_y = 1
        self.encrypt_button.bind(on_press=self.handle_encrypt)
        plain_text_controls_box_layout.add_widget(self.encrypt_button)

        

        self.encrypted_text_input = TextInput()
        self.encrypted_text_input.hint_text = 'Encrypted text'
        self.encrypted_text_input.size_hint_x = 1
        self.encrypted_text_input.size_hint_y = DEFAULT_ELEMENT_HEIGHT * 4
        root_box_layout.add_widget(self.encrypted_text_input)

        encrypted_text_controls_box_layout = BoxLayout()
        encrypted_text_controls_box_layout.orientation = 'horizontal'
        encrypted_text_controls_box_layout.size_hint_x = 1
        encrypted_text_controls_box_layout.size_hint_y = DEFAULT_ELEMENT_HEIGHT
        encrypted_text_controls_box_layout.padding = 10
        encrypted_text_controls_box_layout.spacing = 20
        root_box_layout.add_widget(encrypted_text_controls_box_layout)

        encrypted_text_copy_button = Button()
        encrypted_text_copy_button.text = 'Copy'
        encrypted_text_copy_button.size_hint_x = 0.25
        encrypted_text_copy_button.size_hint_y = 1
        encrypted_text_copy_button.bind(on_press=self.handle_encrypted_text_copy)
        encrypted_text_controls_box_layout.add_widget(encrypted_text_copy_button)

        encrypted_text_paste_button= Button()
        encrypted_text_paste_button.text = 'Paste'
        encrypted_text_paste_button.size_hint_x = 0.25
        encrypted_text_paste_button.size_hint_y = 1
        encrypted_text_paste_button.bind(on_press=self.handle_encrypted_text_paste)
        encrypted_text_controls_box_layout.add_widget(encrypted_text_paste_button)

        self.decrypt_button = Button()
        self.decrypt_button.text = 'Decrypt'
        self.decrypt_button.size_hint_x = 0.25
        self.decrypt_button.size_hint_y = 1
        self.decrypt_button.bind(on_press=self.handle_decrypt)
        encrypted_text_controls_box_layout.add_widget(self.decrypt_button)

        dummy_layout = BoxLayout()
        dummy_layout.orientation = 'vertical'
        dummy_layout.size_hint_x = 1
        dummy_layout.size_hint_y = 0.5
        
        root_box_layout.add_widget(dummy_layout)

        return root_scroll_view
    
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

    def handle_password_copy(self, instance):
        self.password_input.copy(self.password_input.text)

    def handle_password_paste(self, instance):
        self.password_input.text = ''
        self.password_input.paste()

    def handle_plain_text_copy(self, instance):
        self.plain_text_input.copy(self.plain_text_input.text)

    def handle_plain_text_paste(self, instance):
        self.plain_text_input.text = ''
        self.plain_text_input.paste()

    def handle_encrypted_text_copy(self, instance):
        self.encrypted_text_input.copy(self.encrypted_text_input.text)

    def handle_encrypted_text_paste(self, instance):
        self.encrypted_text_input.text = ''
        self.encrypted_text_input.paste()
    
    def handle_encrypt(self, instance):
        self.encrypt_button.set_disabled(True)
        password = self.password_input.text
        text = self.plain_text_input.text
        if password and text:
            encrypted = encrypt(text, password)
            self.encrypted_text_input.text = encrypted
        else:
            self.show_alert(instance, 'Invalid Input', 'Please provide a password and a plain text.')
        self.encrypt_button.set_disabled(False)

    def handle_decrypt(self, instance):
        self.decrypt_button.set_disabled(True)
        password = self.password_input.text
        text = self.encrypted_text_input.text
        if password and text:
            try:
                decrypted = decrypt(text, password)
                self.plain_text_input.text = decrypted
            except Exception as e:
                self.show_alert(instance, 'Error', str(e)) 
        else:
            self.show_alert(instance, 'Invalid Input', 'Please provide a password and an encrypted text.')
        self.decrypt_button.set_disabled(False)

    


if __name__ == "__main__":
    ParanoiaApp().run()
