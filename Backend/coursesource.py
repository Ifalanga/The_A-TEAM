from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the GPT-J model and tokenizer
model_name = "EleutherAI/gpt-j-6B"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


def get_answer(question):
    inputs = tokenizer(question, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=100)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer


# Example usage
question = "What is the capital of France?"
answer = get_answer(question)
print(f"Question: {question}")
print(f"Answer: {answer}")
