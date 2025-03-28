from dotenv import load_dotenv
import os
from groq import Groq

#load_dotenv()
api = os.getenv("api_key")

def groq_api(API_KEY):
    client = Groq(api_key = API_KEY)
    

    completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=[
        {
            "role": "user",
            "content": "who was the first president of USA?"
        }

    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
    )

    for chunk in completion:
        print(chunk.choices[0].delta.content or "", end="")
 


def deepseek_r1_api_call(API_KEY,question):
    client = Groq(api_key=API_KEY)
    try:

        completion = client.chat.completions.create(
            model="deepseek-r1-distill-llama-70b",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        for chunk in completion:
            print(chunk.choices[0].delta.content or "", end="")
    except Exception as e:
        print(e, "some error happened during the chat")

def llama_70b_versatile_api_call(API_KEY,question):
    try:

        client = Groq(api_key=API_KEY)
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=1,
            max_completion_tokens=50,
            top_p=1,
            stream=True,
            stop=None,
        )
        for chunk in completion:
            print(chunk.choices[0].delta.content or "", end="")
    except Exception as e:
        print(e,"error happened during the chat")

#stream=True → The model sends tokens as they are generated.
#stream=False → The model sends the full response at once.
#top_p (Float between 0 and 1)
#Purpose: Controls the diversity of the output using nucleus sampling.
# More creative and random responses.about temparature: 0.7 is a good starting point for most tasks.

def gemma2_9b_it_api_call(API_KEY,question):
    try:

        client = Groq(api_key=API_KEY)
        completion = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=1,
            max_completion_tokens=50,
            top_p=1,
            stream=True,
            stop=None,
        )
        for chunk in completion:
            print(chunk.choices[0].delta.content or "", end="")
    except Exception as e:
        print(e,"error happened during the chat")
