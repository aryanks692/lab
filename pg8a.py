import os
import getpass
from langchain_google_community import GoogleDriveLoader
from langchain.prompts import PromptTemplate
from langchain_cohere import ChatCohere
from langchain_core.output_parsers import JsonOutputParser

# Secure API key input
if "COHERE_API_KEY" not in os.environ:
    os.environ["COHERE_API_KEY"] = getpass.getpass("Enter Cohere API key:")

# Load from Google Drive
loader = GoogleDriveLoader(
    file_ids=["YOUR_FILE_ID_HERE"],
    token_path="token.json"
)
docs = loader.load()

text = docs[0].page_content

# JSON parser
parser = JsonOutputParser()

# Proper prompt
prompt = PromptTemplate(
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    template="""
    Analyze the following text and return structured JSON.

    {format_instructions}

    Text:
    {text}
    """
)

# LLM
llm = ChatCohere(model="command-r")

# Chain
chain = prompt | llm | parser

# Run
output = chain.invoke({"text": text})

print(output)