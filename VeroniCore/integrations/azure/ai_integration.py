import requests
import json
import os


class AIIntegration:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url
        self.cache = {}

    def call_api(self, endpoint, data):
        if endpoint in self.cache:
            return self.cache[endpoint]

        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(
            f"{self.api_url}/{endpoint}", headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            result = response.json()
            self.cache[endpoint] = result  # Cache the result
            return result
        else:
            raise Exception(
                f"API call failed: {response.status_code}, {response.text}")

    def support_multi_language(self, text, target_language):
        data = {'text': text, 'target_language': target_language}
        return self.call_api('translate', data)

    def adaptive_learning(self, user_feedback):
        data = {'feedback': user_feedback}
        return self.call_api('adaptive_learning', data)


if __name__ == "__main__":
    ai_integration = AIIntegration(
        api_key="your_api_key_here", api_url="https://api.yourservice.com")

    # Example API call for multi-language support
    translated_text = ai_integration.support_multi_language(
        "Hello, world!", "es")
    print(f"Translated text: {translated_text}")

    # Example API call for adaptive learning
    feedback_result = ai_integration.adaptive_learning(
        {"user": "test_user", "feedback": "positive"})
    print(f"Adaptive learning result: {feedback_result}")
