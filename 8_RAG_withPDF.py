## 1. Ingest PDF Files
# 2. Extract Text from PDF Files and split into small chunks
# 3. Send the chunks to the embedding model
# 4. Save the embeddings to a vector database
# 5. Perform similarity search on the vector database to find similar documents
# 6. retrieve the similar documents and present them to the user
## run pip install -r requirements.txt to install the required packages

from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

doc_path = "ollama-fundamentals-main\ollama-fundamentals-main\data\BOI.pdf"
model = 'llama3.2'


# loading the PDF file
if doc_path:
    loader = UnstructuredPDFLoader(file_path=doc_path)
    data = loader.load()
    print(f'Done Loading the {doc_path}')
else:
    print(f'Upload a PDF file.')


# check 1st page to see if its working
content = data[0].page_content
# print(content[:100])

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> python .\8_RAG_withPDF.py
# D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama\8_RAG_withPDF.py:12: SyntaxWarning: invalid escape sequence '\o'
#   doc_path = "ollama-fundamentals-main\ollama-fundamentals-main\data\BOI.pdf"
# Done Loading the ollama-fundamentals-main\ollama-fundamentals-main\data\BOI.pdf
# Beneficial Ownership Information Report

# Filing Instructions

# Financial Crimes Enforcement Network


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> 



# extract the PDF and get chunks
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Also we use LANGCHAIN because it has so many wrapper
# classes for every single LLM work. It also gives us a lot of metadata.

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap = 300)
chunks = text_splitter.split_documents(data)
print(f'Done Splitting.')

# print(f'Number of chunks: {len(chunks)}')
# print(f'Example Chunk: {chunks[0]}')

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> python .\8_RAG_withPDF.py
# D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama\8_RAG_withPDF.py:12: SyntaxWarning: invalid escape sequence '\o'
#   doc_path = "ollama-fundamentals-main\ollama-fundamentals-main\data\BOI.pdf"
# Done Loading the ollama-fundamentals-main\ollama-fundamentals-main\data\BOI.pdf
# Done Splitting.
# Number of chunks: 42
# Example Chunk: page_content=





# Adding to the vector database.
# Using the nomic embed text library.
# https://ollama.com/library/nomic-embed-text

# ollama pull nomic-embed-text
import ollama
ollama.pull("nomic-embed-text")
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name="simple-rag"
    # any collection_name of our choice.
)
print(f'Done adding to the vector database.')





# Retreival
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_ollama import ChatOllama

from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever
# to get many queries out and the LLM chooses the best answer.


# setting up model
llm = ChatOllama(model=model)

# a simple technique to generate multiple questions from a single question and then retrieve documents
# based on those questions, getting the best of both worlds.
QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI language model assistant. Your task is to generate five
    different versions of the given user question to retrieve relevant documents from
    a vector database. By generating multiple perspectives on the user question, your
    goal is to help the user overcome some of the limitations of the distance-based
    similarity search. Provide these alternative questions separated by newlines.
    Original question: {question}""",
)
# pass this query prompt to the retreiver and it will deal with this.


retreiver = MultiQueryRetriever.from_llm(
    vector_db.as_retriever(), llm, prompt=QUERY_PROMPT
)
# to get information from the database.
# Based on the query and vector database, llm will process.



# RAG prompt
template = """Answer the question based ONLY on the following context:
{context}
Question: {question}
"""


prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retreiver, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
# from context goes to prompt which goes to llm
# which goes to StrOutputParser which makes it neat.


res = chain.invoke(
    input=("Summarize BOI in 500 characters.",)
)

print(res)


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> 
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> python .\8_RAG_withPDF.py
# D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama\8_RAG_withPDF.py:12: SyntaxWarning: invalid escape sequence '\o'
#   doc_path = "ollama-fundamentals-main\ollama-fundamentals-main\data\BOI.pdf"
# Done Loading the ollama-fundamentals-main\ollama-fundamentals-main\data\BOI.pdf
# Done Splitting.
# Done adding to the vector database.
# The Bank Secrecy Act (BSA) requires certain financial institutions to report beneficial ownership information. The Beneficial Ownership Information (BOI) form is used for this purpose. It must be completed by a reporting company and submitted electronically to FinCEN through the BOI E-Filing portal. The form requires all fields marked with an asterisk (*) to be filled, including middle names, if applicable.
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Ollama> 