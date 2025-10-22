from transformers import pipeline

def generate_answer(prompt):
    model = pipeline("text-generation", model="gpt2")
    output = model(prompt, max_length=200, num_return_sequences=1)
    return output[0]['generated_text']
