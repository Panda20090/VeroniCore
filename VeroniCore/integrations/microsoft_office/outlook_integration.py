
# outlook_integration.py
# This script manages the integration of Microsoft Outlook with VeroniCore.
# It handles operations such as sending emails, managing calendars, and syncing contacts.

import win32com.client as win32

class OutlookIntegration:
    def __init__(self):
        self.outlook = win32.Dispatch("Outlook.Application")
        self.namespace = self.outlook.GetNamespace("MAPI")

    def send_email(self, subject, body, to_recipients):
        mail = self.outlook.CreateItem(0)  # 0: olMailItem
        mail.Subject = subject
        mail.Body = body
        mail.To = ";".join(to_recipients)
        mail.Send()

    def get_calendar_appointments(self):
        calendar = self.namespace.GetDefaultFolder(9)  # 9: olFolderCalendar
        appointments = calendar.Items
        appointments.Sort("[Start]")
        appointments.IncludeRecurrences = True
        return appointments

    def sync_contacts(self):
        contacts_folder = self.namespace.GetDefaultFolder(10)  # 10: olFolderContacts
        contacts = contacts_folder.Items
        contacts_list = []
        for contact in contacts:
            contacts_list.append({
                "FullName": contact.FullName,
                "Email": contact.Email1Address,
                "BusinessPhone": contact.BusinessTelephoneNumber
            })
        return contacts_list

if __name__ == "__main__":
    # Example usage of the OutlookIntegration class
    outlook_integration = OutlookIntegration()

    # Sending an email
    outlook_integration.send_email(
        subject="Test Email",
        body="This is a test email from VeroniCore.",
        to_recipients=["example@example.com"]
    )

    # Retrieving calendar appointments
    appointments = outlook_integration.get_calendar_appointments()
    print(f"Retrieved {len(appointments)} appointments.")

    # Syncing contacts
    contacts = outlook_integration.sync_contacts()
    print(f"Synced {len(contacts)} contacts.")
    