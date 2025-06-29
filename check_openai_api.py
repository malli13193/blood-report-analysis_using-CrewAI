import requests

class HuggingFaceInferenceTool:
    name = "huggingface_tool"
    description = "Tool to interact with Hugging Face hosted models"

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

    def run(self, input_text: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"inputs": input_text}
        response = requests.post(self.api_url, headers=headers, json=payload)

        if response.status_code != 200:
            return f"Error: {response.status_code} - {response.text}"

        result = response.json()
        return result[0].get('generated_text', 'No output') if result else "No output"
