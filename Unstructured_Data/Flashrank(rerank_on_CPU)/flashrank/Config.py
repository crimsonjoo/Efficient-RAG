# Moved to HF - My cloud bucket and $ wont be abused anymore :-)
# THE HF Repo is UNDER CC-BY-SA LICENSE. USE APPROPRIATELY.
model_url = 'https://huggingface.co/prithivida/flashrank/resolve/main/{}.zip'

default_cache_dir = "/tmp"
default_model = "ms-marco-TinyBERT-L-2-v2"
model_file_map = {
    "ms-marco-TinyBERT-L-2-v2": "flashrank-TinyBERT-L-2-v2.onnx",
    "ms-marco-MiniLM-L-12-v2": "flashrank-MiniLM-L-12-v2_Q.onnx",
    "ms-marco-MultiBERT-L-12": "flashrank-MultiBERT-L12_Q.onnx",
    "rank-T5-flan": "flashrank-rankt5_Q.onnx",
    "ce-esci-MiniLM-L12-v2": "flashrank-ce-esci-MiniLM-L12-v2_Q.onnx"
}