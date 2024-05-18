import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email information
sender_email = 'your_email@example.com'
receiver_email = 'recipient_email@example.com'
password = 'your_email_password'
subject = 'Subject Line'
body = 'Email Body'

# Create message object
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Add body to message
message.attach(MIMEText(body, 'plain'))

# Create SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)

# Send email
text = message.as_string()
server.sendmail(sender_email, receiver_email, text)

# Close SMTP session
server.quit()
