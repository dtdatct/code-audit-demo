import smtplib

SMTP_USER = "shoplite@example.com"
SMTP_PASSWORD = "Sup3rS3cret!"  # hardcoded SMTP password


def send_receipt(to, body):
    server = smtplib.SMTP("smtp.example.com", 25)  # plaintext, no STARTTLS
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.sendmail(SMTP_USER, to, "Subject: Receipt\n\n" + body)
    server.quit()
