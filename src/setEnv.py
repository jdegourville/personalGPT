"""
script to set env variables. Only to dev purposes
"""

import os

os.environ['PERSIST_DIRECTORY'] = "../db"
os.environ['SOURCE_DIRECTORY'] = "source_documents" 
os.environ['EMBEDDINGS_MODEL_NAME'] = "all-MiniLM-L6-v2"
os.environ['MODEL_TYPE'] = "LlamaCpp"
os.environ['MODEL_PATH'] = ".../models/llama_2/llama-2-7b.ggmlv3.q4_0.bin"
os.environ['MODEL_N_CTX'] = "1000"
os.environ['MODEL_N_BATCH'] = "8"
os.environ['TARGET_SOURCE_CHUNKS'] = "4"
