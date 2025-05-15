from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox

SMTP_SERVER = "smtp.gmail.com"  # according to the email provider
SMTP_PORT = 587  # Uses TLS encryption for security


def send_email():
    sender_email = sender_email_entry.get()
    password = password_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", tk.END)

    try:
        server = SMTP(SMTP_SERVER, SMTP_PORT)  # Connect to the SMTP server
        server.starttls()  # Upgrade connection to secure TLS
        server.login(sender_email, password)  # Login to email account

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server.sendmail(sender_email, recipient_email, msg.as_string())  # Send the email
        server.quit()  # Close the SMTP connection

        messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")


# Test function with hardcoded values
def test_send_email():
    sender_email_entry.insert(0, "") #insert your email
    password_entry.insert(0, "")  #insert your password
    recipient_email_entry.insert(0, "") #insert the recepient email
    subject_entry.insert(0, "Test Email")
    body_entry.insert("1.0", "This is a test email.")

    send_email()  # Call the send function


# GUI Setup
root = tk.Tk()
root.title("Email Sender")

tk.Label(root, text="Your Email:").pack()
sender_email_entry = tk.Entry(root, width=40)
sender_email_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack()

tk.Label(root, text="Recipient Email:").pack()
recipient_email_entry = tk.Entry(root, width=40)
recipient_email_entry.pack()

tk.Label(root, text="Subject:").pack()
subject_entry = tk.Entry(root, width=40)
subject_entry.pack()

tk.Label(root, text="Body:").pack()
body_entry = tk.Text(root, height=10, width=50)
body_entry.pack()

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack()

# Test button to run the hardcoded test case
test_button = tk.Button(root, text="Run Test Case", command=test_send_email)
test_button.pack()

root.mainloop()

    
