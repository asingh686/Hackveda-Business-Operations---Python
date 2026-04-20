# 🤖 Lead Generation & Email Automation – Python Project

This project was developed  to automate lead generation and Email outreach for Digital Marketing using Python.  
It combines a Google search crawler with an email notification system — streamlining repetitive digital marketing tasks.

---

## 🧠 Project Overview

Manual digital outreach can be time-consuming and error-prone.  
This system automates two key operations:

1. **Crawling Google Search results** to gather potential leads.
2. **Sending personalized emails** to those leads using Gmail’s secure SMTP.

---
## 📜 Requirements

This project uses both external and built-in Python libraries:

### 🔹 Install via pip:
- `googlesearch-python` – to fetch search results from Google
- `pandas` – to create and manage the leads CSV

Install with:
```bash
pip install googlesearch-python pandas

```

## 🚀 Features

### 🔍 Google Crawler

- Prompts the user to enter a keyword (e.g., `"top Python blogs"`)
- Fetches the **top 5 Google results** using `googlesearch-python`
- Creates a formatted table using `pandas` with:
  - Result Name (e.g., `Result 1`)
  - URL
  - Blank fields for Name and Email
- Saves all data to `leads.csv` for use in email automation

➡️ **Purpose:** Save hours of manual copy-paste work from Google.

---

### 📬 Email Notifier

- Reads `leads.csv` entries
- Prompts for Gmail address + Gmail **App Password**
- Sends **personalized emails** using:
  - Recipient Name
  - Associated Link
- Skips rows with missing or blank emails to avoid errors
- Uses Python’s built-in `smtplib` and `ssl` for secure delivery

➡️ **Purpose:** Automates follow-up emails with custom messages — safely and reliably.

---

## 🔄 Workflow Summary

```text
Step 1: Run google_crawler.py
→ Enter keyword like “best Python blogs”
→ Script fetches links, saves to leads.csv

Step 2: Open leads.csv
→ Manually fill in names and email addresses

Step 3: Run email_notifier.py
→ Enter Gmail & App Password
→ Emails sent one by one, with name & link included
```





## 💡 Future Improvements

- 🔍 Automatically extract email addresses from websites using regex or scraping
- 🧠 Integrate natural language models to personalize email body per topic
- 📊 Add analytics: open rate, bounce detection, etc.
- 🖥 Create a simple GUI using Tkinter or PyQt for non-technical users


## 🛡️ Security Note

This script uses Gmail App Passwords, not your actual Gmail password.

To enable:

Turn on 2-Step Verification in Gmail

Create an App Password here:
👉 https://myaccount.google.com/apppasswords

Generate an App Password for “Mail” + “Windows Computer”

## ✍️ Author : 

 **Aryan Raj**

🔗 YouTube – @MindSketcher2

💼 LinkedIn – (https://linkedin.com/in/iamaryanraj)

💻 GitHub: asingh686

📬 Email: as1121aryan@gmail.com

## 🏁 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute it with attribution.



