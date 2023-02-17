import smtplib
from email.mime.text import MIMEText

def send_happiness():
    # Replace these variables with your own email credentials and message
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"
    message = "Wishing you a happy day! :)"
    
    # Set up the SMTP server and login
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    # Create the email message and send it to everyone in your contact list
    recipients = ["friend1@example.com", "friend2@example.com", "friend3@example.com"]
    for recipient in recipients:
        email_message = MIMEText(message)
        email_message['Subject'] = 'Sending you some happiness!'
        email_message['From'] = sender_email
        email_message['To'] = recipient
        smtp_server.sendmail(sender_email, recipient, email_message.as_string())

    # Close the SMTP server connection
    smtp_server.quit()

if __name__ == '__main__':
    send_happiness()

