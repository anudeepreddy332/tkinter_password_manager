🔒 Password Manager (Tkinter)
  A simple GUI-based Password Manager built with Python and Tkinter. It generates strong random passwords, saves them to a file, and copies them to the clipboard.

🚀 Features
  Generate secure passwords with letters, numbers, and symbols.
  Save passwords locally in data.txt (format: Website | Email | Password).
  Auto-copy passwords to clipboard using pyperclip.
  Input validation to ensure no empty fields are submitted.

🖥️ How to Use
  Enter a website name (e.g., google.com).
  Your email/username is auto-filled (editable).
  Click "Generate Password" to create a random password.
  Click "Add" to save the entry to data.txt.
  The password is automatically copied to your clipboard.

⚠️ Note
  Security: This is a local-only tool. For real-world use, consider:
  Encrypting data.txt (e.g., with cryptography).
  Using a database (SQLite) instead of a plain text file.
  .gitignore: Add data.txt to avoid committing sensitive data.

📜 License
  MIT License (Free for personal use).
