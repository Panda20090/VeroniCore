# alert_manager.py
# This script monitors the system for critical errors or security breaches and triggers alerts to the user or admin for immediate action.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

class AlertManager:
    def __init__(self, admin_email, smtp_server, smtp_port, smtp_user, smtp_password):
        self.admin_email = admin_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password
        self.logger = logging.getLogger('VeroniCoreAlertManager')

    def send_email_alert(self, subject, message):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.smtp_user
            msg['To'] = self.admin_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            text = msg.as_string()
            server.sendmail(self.smtp_user, self.admin_email, text)
            server.quit()
            self.logger.info(f"Alert sent to {self.admin_email}: {subject}")
        except Exception as e:
            self.logger.error(f"Failed to send alert: {e}")

    def log_and_alert(self, severity, message):
        if severity == 'critical':
            self.logger.critical(message)
            self.send_email_alert("Critical Alert", message)
        elif severity == 'error':
            self.logger.error(message)
        elif severity == 'warning':
            self.logger.warning(message)
        else:
            self.logger.info(message)

if __name__ == "__main__":
    # Example usage of AlertManager
    alert_manager = AlertManager(
        admin_email="admin@example.com",
        smtp_server="smtp.example.com",
        smtp_port=587,
        smtp_user="your_email@example.com",
        smtp_password="your_password"
    )

    # Test alert
    alert_manager.log_and_alert('critical', 'Test critical alert: System failure detected.')
    