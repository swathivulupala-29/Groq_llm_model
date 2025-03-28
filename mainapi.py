import os
from dotenv import load_dotenv
from groqapi import llama_70b_versatile_api_call,deepseek_r1_api_call,gemma2_9b_it_api_call


load_dotenv()
api = os.getenv("api_key")

condition = True
while condition:
    gemma2_9b_it_api_call(api, input("Ask your question!!"))
    print('''
    
    _________________________________task completed_____________________________________
    
    ''')



