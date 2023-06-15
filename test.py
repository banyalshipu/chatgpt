#main.py
import os
import tempfile
from dotenv import load_dotenv
#dotenv used for creating environment variable
from langchain import PromptTemplate, LLMChain
#langchain used for interface
from langchain.llms import OpenAI
from config import WHITE, GREEN, RESET_COLOR, model_name
from utils import format_user_question
from file_processing import clone_github_repo, load_and_index_files
from questions import ask_question, QuestionContext


