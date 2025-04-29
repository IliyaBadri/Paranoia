# Paranoia - Privacy First Text Encryption App

**Paranoia** is an Android app designed for privacy-conscious users who need a simple, secure, and lightweight tool for text encryption and decryption. It uses AES CBC 256 encryption with a password-based key to secure your sensitive data.

## Features

-   **AES CBC 256 Encryption**: Securely encrypts and decrypts text using a strong encryption standard (AES 256-bit in CBC mode).
    
-   **Password-Based**: Only the correct password can decrypt your encrypted text. No need for complicated setups or key management.
    
-   **Lightweight & Simple**: No unnecessary features. Just the essentials for privacy, keeping the app small and easy to use.
    
-   **Old-School UI**: Designed using Kivy, the app has a straightforward, retro-style interface that's functional and focused on privacy.
    

## Requirements

-   **Linux machine** (on your local device or a virtual machine or WSL)
    
-   **Python3** (tested on: v3.11.12) (must work on v3.11.x)
    
-   **Other dependencies**: These are some but not all of the dependencies you will need if you are on Debian/Ubuntu:
    
    ```bash
    sudo apt install git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
    ```
    

## Installation

1.  **Clone the repository**:
    
    ```bash
    git clone https://github.com/IliyaBadri/Paranoia.git
    ```
    
    ```bash
    cd Paranoia
    ```
    
2.  **Create a Python Virtual Environment** (Optional but recommended):
    
    -   To avoid cluttering your system's Python installation, it's better to create a virtual environment:
        
        ```bash
        python3 -m venv venv
        ```
        
    -   Now activate the virtual environment:
        
        ```bash
        source venv/bin/activate
        ```
        
3.  **Install dependencies**:
    
    -   You will need to have Python, Kivy, and Buildozer installed.
        
    -   Installing the `requirements.txt` will handle the installation of dependencies:
        
        ```bash
        pip install -r requirements.txt
        ```
        
4.  **Build the APK**:
    
    -   Inside the app directory, run the following command to generate the APK:
        
        ```bash
        buildozer android release
        ```
        
    -   The APK will be located in the `bin/` folder after the build process completes.
        
5.  **Install the APK on your Android device**:
    
    -   Once the APK is generated, you can install it on your device using:
        
        ```bash
        adb install bin/paranoia-*.apk
        ```
        

## Usage

-   Open the app, and you'll be presented with three fields:
    
    -   The first field is for your encryption password. For two individuals who want to encrypt and decrypt each other's data, they will need to have the same encryption password.
        
    -   The second field is for the plain text. The encryption functionality takes input from this field, and the decryption functionality of the app writes output to this field.
        
    -   The third field is for the encrypted text. The decryption functionality takes input from this field, and the encryption functionality of the app writes output to this field.
        
-   You can use the `Encrypt` and `Decrypt` buttons to perform each function, respectively.
    

## Security Warning

-   The strength of your encryption depends on the strength of your password. A strong, unique password is highly recommended.
    
-   **Do not forget your password**, as the app does not store or recover it.
    

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

-   **Kivy**: The app was built using the Kivy framework for Python, which makes it easy to develop cross-platform applications.
    
-   **Python**: The app is developed in Python, ensuring a clean and readable codebase.
