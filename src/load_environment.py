# mock environment settings
# for dev purposes

import os

os.environ['PERSIST_DIRECTORY'] = "../db"
os.environ['SOURCE_DIRECTORY'] = "source_documents" 
os.environ['EMBEDDINGS_MODEL_NAME'] = "all-MiniLM-L6-v2"
os.environ['MODEL_TYPE'] = "LlamaCpp"
os.environ['MODEL_PATH'] = "../models/llama_2/codellama-7b-instruct.Q6_K.gguf"
os.environ['MODEL_N_CTX'] = "1000"
os.environ['MODEL_N_BATCH'] = "8"
os.environ['TARGET_SOURCE_CHUNKS'] = "4"