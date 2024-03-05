
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "write an email to the boss for resignation?"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''

Completion(id='cmpl-8sm1AfhD30khUYcMGtqId5V6qC6gj', choices=[CompletionChoice(finish_reason='length', index=0, logprobs=None, text='\n\nSubject: Resignation Letter\n\nDear [Boss’s Name],\n\nI am writing to inform you of my decision to resign from my position as [Your Position] at [Company Name]. My last day of work will be [Date].\n\nIt has been an utmost privilege to work with such a talented and supportive team like ours. I have learned a great deal during my time at [Company Name] and I am extremely grateful for all the opportunities and experiences I have had here.\n\nAfter careful consideration, I have decided to move forward in my career and explore new opportunities. I have been offered another position that aligns with my career goals and I believe it is the right move for me at this point in my professional journey.\n\nI want to thank you for your guidance, support and encouragement throughout my time here. I appreciate the trust and confidence you have always placed in me and I have enjoyed working under your leadership.\n\nI am committed to ensuring a smooth transition during my remaining time here. I have already made a plan with my team to complete all my pending projects and I will be available to assist in finding and training my replacement.\n\nPlease let me know if there are any specific tasks you would like me to complete before my last day. I will also provide you with a detailed hand')], created=1708064984, model='gpt-3.5-turbo-instruct', object='text_completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=256, prompt_tokens=9, total_tokens=265))


'''



