import requests
import json

class TeamsIntegration:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_message(self, message, title=None):
        """
        Sends a message to a Microsoft Teams channel using a webhook.
        """
        payload = {
            "text": message
        }

        if title:
            payload["title"] = title

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(self.webhook_url, data=json.dumps(payload), headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error sending message: {response.status_code}, {response.text}")
        return response.status_code

    def send_card(self, title, text, buttons=[]):
        """
        Sends a rich card message with buttons to a Microsoft Teams channel.
        """
        card = {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "themeColor": "0072C6",
            "summary": title,
            "sections": [{
                "activityTitle": title,
                "text": text
            }],
            "potentialAction": buttons
        }

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(self.webhook_url, data=json.dumps(card), headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error sending card: {response.status_code}, {response.text}")
        return response.status_code

if __name__ == "__main__":
    # Example usage
    webhook_url = "https://outlook.office.com/webhook/your_webhook_url"
    teams = TeamsIntegration(webhook_url)

    # Send a simple message
    teams.send_message("This is a test message from Python.")

    # Send a card with buttons
    buttons = [
        {
            "@type": "OpenUri",
            "name": "View Documentation",
            "targets": [
                {"os": "default", "uri": "https://docs.microsoft.com"}
            ]
        },
        {
            "@type": "OpenUri",
            "name": "Visit GitHub",
            "targets": [
                {"os": "default", "uri": "https://github.com"}
            ]
        }
    ]
    teams.send_card("Important Update", "Please review the latest changes.", buttons)
