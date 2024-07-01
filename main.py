from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

chat = ChatGroq(
  temperature=0,
  model="llama3-70b-8192",
)

system = "You are a helpful assistant."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat

def generate_pet_name(animal_type):
  input_text = {"text": f"I have a pet {animal_type} and I want to name it. Suggest me five cute names for my pet. Only names."}

  try:
    response = chain.invoke(input_text)
    return response.content
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  animal_type = input("Enter the type of animal you want to name: ")
  pet_names = generate_pet_name(animal_type)
  pet_names.split("\n")
  print("\n",  pet_names)