import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackIntegration:
    def __init__(self, token):
        self.client = WebClient(token=token)

    def send_message(self, channel, text):
        """
        Sends a message to a Slack channel.
        """
        try:
            response = self.client.chat_postMessage(channel=channel, text=text)
            print(f"Message sent to {channel}: {text}")
            return response
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")
            return None

    def upload_file(self, channel, file_path, initial_comment=None):
        """
        Uploads a file to a Slack channel.
        """
        try:
            response = self.client.files_upload(
                channels=channel,
                file=file_path,
                initial_comment=initial_comment
            )
            print(f"File uploaded to {channel}: {file_path}")
            return response
        except SlackApiError as e:
            print(f"Error uploading file: {e.response['error']}")
            return None

    def list_channels(self):
        """
        Lists all channels in the Slack workspace.
        """
        try:
            response = self.client.conversations_list()
            channels = response.get('channels', [])
            for channel in channels:
                print(f"Channel: {channel['name']} (ID: {channel['id']})")
            return channels
        except SlackApiError as e:
            print(f"Error listing channels: {e.response['error']}")
            return None

if __name__ == "__main__":
    # Example usage
    slack_token = "your_slack_token_here"
    slack = SlackIntegration(slack_token)

    # Send a message to a channel
    slack.send_message(channel="#general", text="Hello from Python!")

    # Upload a file to a channel
    slack.upload_file(channel="#general", file_path="path_to_your_file.txt", initial_comment="Here is a file.")

    # List all channels
    slack.list_channels()
