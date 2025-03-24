# 🚀 Reverse Shell - Directory Navigation & File Transfer 🔥

## 📝 Description
This project is a Python-based **reverse shell** that allows remote command execution, directory navigation, and file transfer. The client connects to an attacker's machine and executes received commands. It is useful for ethical hacking and penetration testing purposes. 🛡️

## 🌟 Features
- 📂 Remote directory navigation (`cd` command support)
- 📤 File transfer from the client to the attacker (`grab*filename` command)
- 💻 Remote command execution
- ❌ Ability to terminate the session remotely

## ⚙️ Requirements
- 🐍 Python 3.x
- 🌐 A network connection between the client and the attacker

## 🚀 Installation & Usage
1. **Set up the listener on the attacker's machine:**
   ```bash
   nc -lvp 80
   ```
2. **Run the client script on the target machine:**
   ```bash
   python backdoor.py
   ```
3. **Available Commands:**
   - 📂 `cd <directory>` → Change working directory
   - 📤 `grab*<filepath>` → Transfer a file from the client to the server
   - ⚡ `<any system command>` → Execute a shell command remotely
   - ❌ `terminate` → Close the connection

## ⚠️ Disclaimer
This tool is for **educational and ethical hacking purposes only**. 🚨 Unauthorized use of this script on systems without permission is **illegal** and may lead to legal consequences. 🚫

