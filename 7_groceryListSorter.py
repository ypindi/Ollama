import ollama
import os

model = "llama3.2"
# can just change this to any other model and do what you want.
# This is the beauty of Ollama.
# Can swap the Embedding LLM and the Query LLM with what we want
# after setting up the system in Ollama.

input_file = "ollama-fundamentals-main\ollama-fundamentals-main\data\grocery_list.txt"
output_file = "7_groceryListSorted.txt"

if not os.path.exists(input_file):
    print(f'Input File {input_file} not found.')
    exit(1)

else:
    print(f'Found!!')

# read the grocery list.
with open(input_file, "r") as f:
    items = f.read().strip()

# print(items)

# prepare the prompt for the model
prompt = f"""
    You are an intelligent assistant that categorizes and sorts grocery items.
    Here is the list of grocery items:
    {items}.
    Please:
    1. Categorize the items into appropriate categories.
    2. Display the items alphabetically in each list.
    3. Present the list in a bulleted fashion.
"""


# send prompt
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print(f'Generated Text:')
    print(generated_text)

    with open(output_file, "w") as f:
        f.write(generated_text.strip())
        print(f"Categorized list has been saved to {output_file} ")
except Exception as e:
    print("An error occurred", str(e))




# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> python .\7_groceryListSorter.py
# D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama\7_groceryListSorter.py:6: SyntaxWarning: invalid escape sequence '\o'
#   input_file = "ollama-fundamentals-main\ollama-fundamentals-main\data\grocery_list.txt"Found!!
# Categorized list has been saved to 7_groceryListSorted.txt
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama>