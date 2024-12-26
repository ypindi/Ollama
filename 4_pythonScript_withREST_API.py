# pip install requests

# All this using the REST API of Ollama.
# But can also do using Ollama Python library (without using url.)

import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "Tell me a short story and make it funny."
}

response = requests.post(url, json=data, stream=True)

if response.status_code == 200:
    print("Generated Text: ", end=" ", flush=True)
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode("utf-8")
            result = json.loads(decoded_line)
            # decode the line and parse to JSON.

            generated_text = result.get("response","")
            print(generated_text, end="", flush=True)
            # getting text from the response
else:
    print("Error: ", response.status_code, response.text)




# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> python .\4_pythonScript.py 
# Generated Text:  Once upon a time, there was a chicken named Cluck Norris (yes, that's his real name). Cluck was a master of the ancient art of Chicken-Fu, which he claimed allowed him to lay the most epic eggs in all the land.

# One sunny afternoon, Cluck decided to enter the annual "Farm Fest" talent show. He strutted onto the stage, puffed out his chest, and proclaimed, "I shall kick some serious fowl butt... I mean, butt!"

# The judges were amused by Cluck's bravado, but things took a turn for the absurd when he began doing his Chicken-Fu moves – flapping his wings like a helicopter, squawking loudly, and executing an impressive head-spinning move.

# However, just as Cluck was about to deliver the final blow (a.k.a. his signature "Egg-cellent Kick"), he tripped on his own feet and face-planted into a nearby puddle of mud.

# The audience erupted in laughter, and even the judges couldn't help but crack up. Cluck emerged from the mud, covered in squelching brown goo, with a triumphant grin plastered on his beak.

# To everyone's surprise, the crowd roared its approval, and Cluck was declared the winner of Farm Fest! As he accepted his prize – a year's supply of oats and a trophy shaped like a giant egg – he quipped, "I guess you could say I 'cracked' under pressure... Ha! Chicken joke!"

# From that day on, Cluck Norris was known as the greatest chicken comedian in the land. And whenever someone asked him about his legendary Chicken-Fu moves, he'd respond with a sassy shrug and a wink: "Hey, when you're egg-cellent, even your fowl-ups are awesome!"
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> 
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama>