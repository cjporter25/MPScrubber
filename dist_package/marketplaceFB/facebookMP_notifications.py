import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

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
                server.set_debuglevel(1)  # Enable debugging output
                server.starttls()
                server.login(self.fromEmail, self.password)
                print("Successfully connected to the SMTP server.")
        except Exception as e:
            print(f"Failed to connect to the SMTP server: {e}")
    def createEmailContent(self, goodDeals):
        subject = "Good Deals - Facebook MarketPlace"
        text = "Chrysler, Jeep, Dodge:"
        html = """
        <html>
        <body>
            <h2>Potentially Good Deals - Chrysler, Jeep, Dodge</h2>
            <table border="1">
                <tr>
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
        sender = self.fromEmail
        senderPW = self.password
        recipient = toEmail
        server = self.smtpServer
        port = self.smtpPort
        
        
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
        try:
            with smtplib.SMTP_SSL(server, port) as smtp_server:
                smtp_server.login(sender, senderPW)
                smtp_server.sendmail(sender, recipient, message.as_string())
                print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def sendGoodDealsEmail(self, goodDeals):
        subject, text, html = self.createEmailContent(goodDeals)
        self.sendEmail(self.toEmail, subject, text, html)