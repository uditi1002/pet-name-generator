# Pet Name Generator

This project uses LangChain and GROQ to generate cute pet names based on user input. It prompts the user to enter the type of animal they have and then suggests five cute names for that pet.

## Installation

To run this project, you need Python 3.6 or higher installed. Follow these steps to set up the project:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/uditi1002/pet-name-generator.git
   cd pet-name-generator
   
2. **Create and activate a virtual environment:**
   
   ```bash
   python -m venv .venv
   source .venv/bin/activate

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   
4. **Set up environment variables:**
   
   Create a .env file in the root directory and add your GROQ API key:

   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   
5. **Run the application:**
    
   ```bash
   python main.py
   
## Usage 
1. When prompted, enter the type of animal you want to name.
2. The program will generate and display five cute names for your pet.
