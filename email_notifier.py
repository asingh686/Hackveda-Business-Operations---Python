import pandas as pd
import smtplib
import ssl
from email.message import EmailMessage
import getpass

# Load leads
try:
    df = pd.read_csv("sample_data/leads.csv")
except FileNotFoundError:
    print("leads.csv not found in sample_data/")
    exit()

# Gmail login
print("Gmail Login")
sender_email = input("Enter your Gmail address: ").strip()
password = getpass.getpass("Enter your Gmail App Password: ").strip()

# Email setup
subject = "Collaboration Opportunity with Hackveda"

body_template = """Hi {name},

I came across your website ({link}) while researching digital opportunities in the Python/AI education space.

My name is Aryan Raj, and I’m currently working on automation tasks at Hackveda. I’d love to explore if there’s a way we can connect or collaborate on tech internships, education programs, or outreach.

Let me know what you think!

Regards,  
Aryan Raj  
Intern, Hackveda  
"""

# Setup secure SMTP server
try:
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_email, password)
    print("Login successful.\n")
except Exception as e:
    print("Gmail login failed:", e)
    exit()

# Send emails
for idx, row in df.iterrows():
    name = str(row.get('Name', 'Team')).strip()
    recipient_email = str(row.get('Email', '')).strip()
    link = str(row.get('Link', '')).strip()

    # Skip if email is missing or invalid
    if pd.isna(recipient_email) or recipient_email == "":
        print(f"Skipped row {idx+1} — no email provided.")
        continue

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.set_content(body_template.format(name=name, link=link))

    try:
        server.send_message(msg)
        int(f"Email sent to: {name} <{recipient_email}>")
    except Exception as e:
        print(f"Failed to send to {recipient_email}: {e}")

server.quit()
print("\n All emails processed.")
