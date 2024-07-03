import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("Locutusque/gpt2-large-medical")
model = AutoModelForCausalLM.from_pretrained("Locutusque/gpt2-large-medical").to(device)

def inference(prompt):


    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)

    # Generate
    generate_ids = model.generate(
        input_ids,
        max_length=512,  # Increase max_length to allow longer responses
        min_length=50,  # Ensure minimum length
        num_beams=5,  # Use beam search for better quality
        temperature=0.5,  # Adjust temperature for creativity
        top_k=50,  # Top-k sampling for diversity
        top_p=0.95,  # Nucleus sampling for diversity
        no_repeat_ngram_size=2,
        # do_sample=True,
        pad_token_id=tokenizer.eos_token_id  # Set pad_token_id to eos_token_id
    )


    output_text = tokenizer.decode(generate_ids[0], skip_special_tokens=True)

    return output_text

