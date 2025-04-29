from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from p_cryptography import encrypt, decrypt

class ParanoiaApp(App):
    def build(self):
        self.layout = BoxLayout(
            orientation='vertical', 
            padding=10, 
            spacing=10
            )
        
        self.key_input = TextInput(
            hint_text='Enter encryption password', 
            password=True
            )
        self.layout.add_widget(self.key_input)

        self.text_input = TextInput(
            hint_text='Enter text to encrypt'
            )
        self.layout.add_widget(self.text_input)

        self.encrypt_button = Button(text='Encrypt')
        self.encrypt_button.bind(on_press=self.encrypt_text)
        self.layout.add_widget(self.encrypt_button)

        self.decrypt_button = Button(text='Decrypt')
        self.decrypt_button.bind(on_press=self.decrypt_text)
        self.layout.add_widget(self.decrypt_button)

        self.output_label = Label(text='Result will appear here')
        self.layout.add_widget(self.output_label)

        return self.layout
    
    def handle_encrypt(self, instance):
        password = self.key_input.text
        text = self.text_input.text
        if password and text:
            encrypted = encrypt(text, password)
            self.output_label.text = f'Encrypted: {encrypted}'
        else:
            self.output_label.text = 'Please provide password and text.'

    def handle_decrypt(self, instance):
        password = self.key_input.text
        text = self.text_input.text
        if password and text:
            try:
                decrypted = decrypt(text, password)
                self.output_label.text = f'Decrypted: {decrypted}'
            except Exception as e:
                self.output_label.text = f'Error: {str(e)}'
        else:
            self.output_label.text = 'Please provide password and text.'


if __name__ == "__main__":
    ParanoiaApp().run()
