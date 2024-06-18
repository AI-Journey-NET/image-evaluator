import base64
import sys
import requests

LLM_GENERATE_API="http://localhost:11434/api/generate"
LLM_GENERATE_MODEL="llava:34b"

LLM_HEADERS = {
    'Content-Type': 'application/json'
}

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def generate_response(user_input, image_list=[]):
    response = requests.post(
        LLM_GENERATE_API,
        headers=LLM_HEADERS,
        json={
            'model': LLM_GENERATE_MODEL,
            'stream': False,
            'prompt': user_input,
            'images' : image_list
        }
    )
    response.raise_for_status()
    return response.json()['response']

def main():
    if len(sys.argv) == 3:
        path = sys.argv[1]
        print("Parsing image")
        b64_content = image_to_base64(path)
        print("Waiting for AI response...")
        print("AI Response:", generate_response(sys.argv[2], [b64_content]))
    else:
        print(f"Please call this script with two arguments: python {sys.argv[0]} \"file.jpg\" \"describe the image\"")
if __name__ == "__main__":
    main()