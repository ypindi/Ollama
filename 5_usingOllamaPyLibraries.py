# pip install ollama

# This is to run ollama using python libraries.
# This also uses the REST API but we don't have to explicitly
# define the url like in 4.py

import ollama

# response = ollama.list()
# all models information
# print(response)

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> python .\5_usingOllamaPyLibraries.py
# models=[Model(model='llama3.2:latest', 
#               modified_at=datetime.datetime(2024, 12, 17, 19, 40, 26, 224893, tzinfo=TzInfo(+01:00)), 
#               digest='a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72', size=2019393189, 
#               details=ModelDetails(parent_model='', format='gguf', family='llama', families=['llama'], 
#                                    parameter_size='3.2B', quantization_level='Q4_K_M'))]
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama>











# create a Chat API
# using a Chat endpoint using the ollama library
# res = ollama.chat(
#     model="llama3.2",
#     messages=[{
#         "role": "user",
#         "content": "Why is the Sky Blue?"
#     }]
# )

# print(res)

# whole output comes out all at once on terminal.

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> python .\5_usingOllamaPyLibraries.py
# model='llama3.2' created_at='2024-12-18T20:53:16.4915917Z' done=True done_reason='stop' 
# total_duration=33986400700 load_duration=8497701600 prompt_eval_count=31 prompt_eval_duration=2903000000 
# eval_count=262 eval_duration=22499000000 
# message=Message(role='assistant', 
#                 content="The sky appears blue to us during the day due to a phenomenon called Rayleigh scattering, 
#                 named after the British physicist Lord Rayleigh. He discovered that when sunlight enters Earth's atmosphere, 
#                 it encounters tiny molecules of gases such as nitrogen (N2) and oxygen (O2).
#                 \n\nThese gas molecules are much smaller than the wavelength of light, which means they scatter shorter 
#                 (blue) wavelengths more than longer (red) wavelengths. As a result, the blue light is dispersed in all 
#                 directions and reaches our eyes from all parts of the sky.\n\nHere's what happens:\n\n1. Sunlight enters 
#                 Earth's atmosphere.\n2. The shorter blue wavelengths are scattered by the tiny gas molecules.\n3. The 
#                 scattered blue light travels in all directions.\n4. Our eyes perceive this scattered blue light as the 
#                 color of the sky.\n\nThe reason the sky isn't blue at sunrise and sunset is because the sun's rays have to 
#                 travel through more of the Earth's atmosphere, which scatters the shorter wavelengths even more, leaving mainly 
#                 longer wavelengths (reds and oranges) to reach our eyes. This is why the sky appears red or orange during these times.
#                 \n\nIn summary, the sky appears blue because of Rayleigh scattering, where tiny gas molecules in the atmosphere scatter 
#                 shorter blue wavelengths, making them visible to us from all directions.", images=None, tool_calls=None)
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> 
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> 
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama>

# print(res["message"]["content"])













# using streams of data
# res2 = ollama.chat(
#     model="llama3.2",
#     messages=[{
#         "role": "user",
#         "content": "Why is the Sky Blue?"
#     }],
#     stream=True
# )

# print(res2)
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama>
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> python .\5_usingOllamaPyLibraries.py
# <generator object Client._request.<locals>.inner at 0x000001989AA78280>
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama>


# for chunk in res2:
#     print(chunk["message"]["content"], end="", flush=True)

# this is if you want to see the data coming out on the terminal as a stream.












# res3 = ollama.generate(
#     model='llama3.2',
#     prompt='How old are dinosaurs'
# )
# print(res3)








print(ollama.show('llama3.2'))
# shows some metadata