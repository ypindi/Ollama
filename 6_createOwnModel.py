import ollama

modelfile = """
FROM llama3.2
SYSTEM You are Nico, a very smart assistant who know everything about oceans. You answer questions succintly and informatively.
PARAMETER temperature 0.8
"""


ollama.create(model='Model2', modelfile=modelfile)

response = ollama.generate(
    model='Model2',
    prompt='How deep is the Atlantic Ocean'
)

print(response["response"])

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> python .\6_createOwnModel.py
# The Atlantic Ocean's maximum depth is approximately 8,376 meters (27,500 feet) in the Puerto Rico Trench.
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> 


# go to cmd: we can see that our Model2 is visible.
# (venv) D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama>ollama list
# NAME               ID              SIZE      MODIFIED
# Model2:latest      b4acdeb08fda    2.0 GB    57 seconds ago
# llama3.2:latest    a80c4f17acd5    2.0 GB    27 hours ago

# (venv) D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama>




ollama.delete("Model2")
# print(ollama.list)
# <bound method Client.list of <ollama._client.Client object at 0x00000228A2862600>>

# cmd
# (venv) D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama>
# (venv) D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama>ollama list
# NAME               ID              SIZE      MODIFIED
# llama3.2:latest    a80c4f17acd5    2.0 GB    27 hours ago

# (venv) D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama>