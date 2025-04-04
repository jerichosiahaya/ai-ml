import os
from dotenv import load_dotenv
from config.log import log

load_dotenv()

DATA_PATH = os.environ.get('DATA_PATH', 'data\data-id.jsonl')

OPENAI_API_TYPE = os.environ.get('OPENAI_API_TYPE')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_API_BASE = os.environ.get('OPENAI_API_BASE')
OPENAI_API_VERSION = os.environ.get('OPENAI_API_VERSION')
OPENAI_API_DEPLOYMENT_NAME = os.environ.get('OPENAI_API_DEPLOYMENT_NAME')

EMBEDDING_OPENAI_API_TYPE = os.environ.get('EMBEDDING_OPENAI_API_TYPE')
EMBEDDING_OPENAI_API_KEY = os.environ.get('EMBEDDING_OPENAI_API_KEY')
EMBEDDING_OPENAI_API_BASE = os.environ.get('EMBEDDING_OPENAI_API_BASE')
EMBEDDING_OPENAI_API_VERSION = os.environ.get('EMBEDDING_OPENAI_API_VERSION')
EMBEDDING_OPENAI_API_DEPLOYMENT_NAME = os.environ.get('EMBEDDING_OPENAI_API_DEPLOYMENT_NAME')

VECTOR_PATH = os.environ.get('VECTOR_PATH')

EMBEDDING = os.environ.get('EMBEDDING')

MODEL_PATH = os.environ.get('MODEL_PATH')

TOKENIZER_PATH = os.environ.get('TOKENIZER_PATH')