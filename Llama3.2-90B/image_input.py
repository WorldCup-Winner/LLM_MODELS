import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that generates HTML and tailwind code for a given image in a single page."
        ),
        UserMessage(
            content=[
                TextContentItem(text="Generate the appropriate code for this image."),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="images/Login.png",
                        image_format="png",
                        detail=ImageDetailLevel.HIGH)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)