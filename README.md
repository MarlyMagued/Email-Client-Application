
# Email Application

This project is a simple GUI-based email application built using Python and Tkinter. It allows users to send and receive emails using the SMTP and IMAP protocols.

## Features
- Send emails using SMTP (Gmail as the provider).
- Receive the latest email using IMAP (Yahoo as the provider).
- Simple and interactive GUI using Tkinter.
- Notifications for new emails.
- Test functionality with hardcoded values for quick testing.

## Prerequisites
- Python 3.x
- Libraries: 
  - tkinter
  - smtplib
  - imaplib
  - email
  - subprocess (for notifications)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MarlyMagued/Email-Client-Application.git
   ```
2. Install the required libraries (if not already installed):
   ```bash
   pip install tkinter
   ```

## Usage
### Sending Emails
1. Run the `send_email.py` script:
   ```bash
   python send_email.py
   ```
2. Enter your email, password, recipient's email, subject, and message body.
3. Click "Send Email" to send the message.

### Receiving Emails
1. Run the `receive_email.py` script:
   ```bash
   python receive_email.py
   ```
2. Enter your email and password.
3. Click "Check Email" to receive the latest message.

### Test Mode
For demonstration purposes, both applications include a test button that automatically fills in sample data.

## Security Notice
Avoid hardcoding sensitive information (like email credentials) in the code. Use environment variables or secure credential storage practices.

## Troubleshooting
- Make sure to enable "Less secure app access" in your email provider's settings.
- Check for any firewall or network restrictions that might block SMTP/IMAP ports.

## Acknowledgments
- Tkinter for GUI support.
- SMTP and IMAP for email handling.
