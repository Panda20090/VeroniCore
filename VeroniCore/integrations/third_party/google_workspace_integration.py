from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

class GoogleWorkspaceIntegration:
    def __init__(self, credentials_json, scopes):
        self.creds = service_account.Credentials.from_service_account_file(credentials_json, scopes=scopes)

    def send_email(self, sender, recipient, subject, body):
        """
        Sends an email using the Gmail API.
        """
        try:
            service = build('gmail', 'v1', credentials=self.creds)
            message = {
                'raw': self.create_message(sender, recipient, subject, body)
            }
            send_message = service.users().messages().send(userId="me", body=message).execute()
            print(f"Message Id: {send_message['id']}")
            return send_message
        except Exception as e:
            print(f"Error sending email: {e}")
            return None

    def create_message(self, sender, to, subject, message_text):
        """
        Creates a message for an email.
        """
        from email.mime.text import MIMEText
        import base64

        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return base64.urlsafe_b64encode(message.as_bytes()).decode()

    def upload_file_to_drive(self, file_path, folder_id=None):
        """
        Uploads a file to Google Drive.
        """
        try:
            service = build('drive', 'v3', credentials=self.creds)
            file_metadata = {'name': os.path.basename(file_path)}
            if folder_id:
                file_metadata['parents'] = [folder_id]

            media = MediaFileUpload(file_path, resumable=True)
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f"File ID: {file.get('id')}")
            return file.get('id')
        except Exception as e:
            print(f"Error uploading file: {e}")
            return None

    def read_google_sheet(self, spreadsheet_id, range_name):
        """
        Reads data from a Google Sheet.
        """
        try:
            service = build('sheets', 'v4', credentials=self.creds)
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
            values = result.get('values', [])
            return values
        except Exception as e:
            print(f"Error reading Google Sheet: {e}")
            return None

    def write_to_google_sheet(self, spreadsheet_id, range_name, values):
        """
        Writes data to a Google Sheet.
        """
        try:
            service = build('sheets', 'v4', credentials=self.creds)
            body = {'values': values}
            result = service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id, range=range_name,
                valueInputOption="RAW", body=body).execute()
            print(f"{result.get('updatedCells')} cells updated.")
            return result
        except Exception as e:
            print(f"Error writing to Google Sheet: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    scopes = [
        'https://www.googleapis.com/auth/gmail.send',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/spreadsheets'
    ]
    credentials_json = "path_to_your_service_account_credentials.json"
    google_workspace = GoogleWorkspaceIntegration(credentials_json, scopes)

    # Send an email using Gmail
    google_workspace.send_email(
        sender="your_email@example.com",
        recipient="recipient@example.com",
        subject="Test Email",
        body="This is a test email sent from Python using the Gmail API."
    )

    # Upload a file to Google Drive
    google_workspace.upload_file_to_drive("path_to_your_file.txt")

    # Read data from a Google Sheet
    sheet_data = google_workspace.read_google_sheet(
        spreadsheet_id="your_spreadsheet_id",
        range_name="Sheet1!A1:C10"
    )
    print("Google Sheet Data:")
    print(sheet_data)

    # Write data to a Google Sheet
    google_workspace.write_to_google_sheet(
        spreadsheet_id="your_spreadsheet_id",
        range_name="Sheet1!A1",
        values=[
            ["Name", "Age", "Occupation"],
            ["John Doe", "30", "Software Engineer"]
        ]
    )
