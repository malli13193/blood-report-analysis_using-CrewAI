import requests

def check_api_key(api_key):
    url = "https://google.serper.dev/search"  # ✅ Correct endpoint

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "q": "test"
    }

    try:
        # ✅ Serper.dev requires POST requests
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            print("✅ API key is valid.")
            print("Response:", response.json())
        elif response.status_code == 401:
            print("❌ API key is invalid or unauthorized.")
        else:
            print(f"⚠️ Received unexpected status code: {response.status_code}")
            print("Response message:", response.json())
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Replace with your actual API key
api_key = "10e1d41d529b6e96a24f54baf08a6214fc0fe3e7"
check_api_key(api_key)
