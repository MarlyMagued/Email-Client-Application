
import tkinter as tk
from tkinter import messagebox
import imaplib
import email
from email.header import decode_header
import subprocess

IMAP_SERVER = "imap.mail.yahoo.com"  # According to the email provider
IMAP_PORT = 993


def notify(title, message):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])


def receive_email():
    email_address = email_entry.get()
    password = password_entry.get()

    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)  # Connect to the IMAP server
        mail.login(email_address, password)  # Login to email account
        mail.select("inbox")  # Select the mailbox (default is "INBOX")

        # Search for all emails
        status, messages = mail.search(None, "ALL")
        if status != "OK" or not messages[0]:
            messagebox.showinfo("Info", "No emails found.")
            return

        latest_email_id = messages[0].split()[-1]  # Get the latest email ID
        status, data = mail.fetch(latest_email_id, "(RFC822)")

        if status != "OK":
            messagebox.showerror("Error", "Failed to fetch email.")
            return

        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])  # Convert raw email to readable format
                subject, encoding = decode_header(msg["Subject"])[0]  # Decode subject 

                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8")  # Default to UTF-8

                notify("New Email Received", f"Subject: {subject}")
                messagebox.showinfo("New Email", f"📩 Subject: {subject}")

        mail.logout()

    except Exception as e:
        messagebox.showerror("Error", f"Failed to receive email: {e}")


# Test function with hardcoded values
def test_receive_email():
    email_entry.insert(0, "")
    password_entry.insert(0, "")  # Use a test password
    receive_email()  # Call the receive function


# GUI Setup
root = tk.Tk()
root.title("Email Receiver")

tk.Label(root, text="Your Email:").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack()

receive_button = tk.Button(root, text="Check Email", command=receive_email)
receive_button.pack()

# Test button to run the hardcoded test case
test_button = tk.Button(root, text="Run Test Case", command=test_receive_email)
test_button.pack()

root.mainloop()

