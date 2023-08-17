import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class CodeGenerator:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def generate_code(self, input_text):
        inputs = self.tokenizer.encode(input_text, return_tensors='pt')
        outputs = self.model.generate(inputs, max_length=100, temperature=0.7, num_return_sequences=1)
        return self.tokenizer.decode(outputs[0])