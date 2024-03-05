from openai import OpenAI
from config import OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url