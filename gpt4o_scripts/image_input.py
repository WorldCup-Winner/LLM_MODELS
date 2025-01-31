import os 
import base64
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

def get_image_data_url(image_file: str, image_format: str) -> str:
    """
    Helper function to convert an image file to a data URL string. 
    Args:
        image_file (str): The path to the image file.
        image_format (str): The format of the image file.
    Returns:
        str: The data URL string of the image file.
    """
    try:
        with open(image_file, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
    except FileNotFoundError:
        print(f"Could not read {image_file}.")
        exit()
    return f"data:image/{image_format};base64,{image_data}"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that generates HTML and tailwind code for a given image in a single page.",
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url" : {
                    "url" : get_image_data_url("images/Login.png", "png"),
                    "detail" : "high"
                    }
                },
                {
                    "type": "text",
                    "content": "Generate the appropriate code for this image."
                },
            ]
        }
    ],
    model=model_name,
)

print(response.choices[0].message.content)