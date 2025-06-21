import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")

if openai_api_key is None:
	raise ValueError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=openai_api_key)
response = client.chat.completions.create(
	model="gpt-3.5-turbo",
	max_completion_tokens= 100,
	messages = [
		{"role": "user",
		 "content": "Why is learning the OpenAI API valuable for developers?"
		 }
	])
print(response.choices[0].message.content)
# Example output:
"""
Learning the OpenAI API is valuable for developers for several reasons:

1. Access to advanced AI capabilities: The OpenAI API provides developers with access to cutting-edge AI models and capabilities, allowing them to create more sophisticated and intelligent applications.
2. Streamlined development process: By leveraging pre-trained AI models from the OpenAI API, developers can save time and resources in building and training new models from scratch.
3. Enhanced user experience: Integrating AI into applications using the OpenAI API can significantly improve
"""