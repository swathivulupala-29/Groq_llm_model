import os
from dotenv import load_dotenv
from groqapi import llama_70b_versatile_api_call,deepseek_r1_api_call

load_dotenv()
api = os.getenv("api_key")


from langchain_groq import ChatGroq
import os
from langchain.memory.summary import ConversationSummaryMemory
from langchain.schema import AIMessage, HumanMessage, SystemMessage

llm = ChatGroq(
    groq_api_key = os.getenv("api_key"),
    model_name="llama-3.3-70b-versatile",
)
memory =   ConversationSummaryMemory(llm=llm)

while True:
    user_input = input("You: ask your question here-")
    chat_history = memory.load_memory_variables({})['history']
    #conversation_history = memory.load_memory_variable({})[user_input]
    print(chat_history,"history of chat-----------------------------")
    messages = [
        ("human",f"Ask your question: \n{user_input}\n\nChat History:\n{chat_history}"),
    ]

    response=llm.invoke(messages)
    print(response.content)
    
    memory.save_context({"input":user_input},{"output": (response.content)})

    with open("chat_history.txt", "a") as f:
        f.write(f"User: {user_input}\nAI: {response.content}\n\n")
    # Print the chat history to the console
    print(f"Chat History:\n{chat_history}\n")
    # Print the AI's response to the console
    print(f"AI: {response.content}\n")
    # Save the chat history to a file   

