import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class FB_NotificationsManager:
    def __init__(self):
        self.fromEmail = os.getenv("EMAIL_USER")
        self.password = os.getenv("EMAIL_PASS")
        self.smtpServer = os.getenv("SMTP_SERVER")
        self.smtpPort = int(os.getenv("SMTP_PORT"))
        self.toEmail = os.getenv("TO_EMAIL_USER")
    def confirmEnvVariables(self):
        print(f"From Email: {self.fromEmail}")
        print(f"Password: {self.password}")  # Be careful about printing sensitive information
        print(f"SMTP Server: {self.smtpServer}")
        print(f"SMTP Port: {self.smtpPort}")
        print(f"To Email: {self.toEmail}")

    def testServerConnection(self):
        try:
            with smtplib.SMTP(self.smtpServer, self.smtpPort) as server:
                server.starttls()
                server.login(self.fromEmail, self.password)
                print("Successfully connected to the SMTP server.")
        except Exception as e:
            print(f"Failed to connect to the SMTP server: {e}")
    def createEmailContent(self, goodDeals):
        subject = "Good Deals from FB Marketplace Scraper"
        text = "Here are the good deals found by the FB Marketplace Scraper:"
        html = """
        <html>
        <body>
            <h2>Potentially Good Dealsr</h2>
            <table border="1">
                <tr>
                    <th>Primary Key</th>
                    <th>Year</th>
                    <th>Price</th>
                    <th>Mileage</th>
                    <th>Description</th>
                    <th>Location</th>
                    <th>Link</th>
                </tr>
        """

        for key, details in goodDeals.items():
            html += f"""
            <tr>
                <td>{key}</td>
                <td>{details['year']}</td>
                <td>{details['price']}</td>
                <td>{details['mileage']}</td>
                <td>{details['description']}</td>
                <td>{details['location']}</td>
                <td><a href="{details['link']}">View Listing</a></td>
            </tr>
            """
        
        html += """
            </table>
        </body>
        </html>
        """

        return subject, text, html

    def sendEmail(self, toEmail, subject, text, html):
        # Create the email message
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.fromEmail
        message["To"] = toEmail

        # Attach the text and HTML parts to the message
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)

        # Send the email
        with smtplib.SMTP(self.smtpServer, self.smtpPort) as server:
            server.starttls()
            server.login(self.fromEmail, self.password)
            server.sendmail(self.fromEmail, toEmail, message.as_string())

    def sendGoodDealsEmail(self, goodDeals):
        subject, text, html = self.createEmailContent(goodDeals)
        self.sendEmail(self.toEmail, subject, text, html)