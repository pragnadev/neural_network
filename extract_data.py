import openai
import json
import time

time.sleep(5)
openai.api_key ="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"
def extract_data(text):
    prompt = f"""
    Extract structured data from the following text:
    "{text}"
    Provide the output as JSON with fields : title , release_year , platform and genre.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role":"user","content":prompt}],
        temperature =0
    )
    structured_data = response["choice"][0]["message"]["content"]
    return json.loads(structured_data)
    
input_text = "Stranger Things is a 2016 Netflix show with a horror/sci-fi theme."
extracted_info = extract_data(input_text)
print(json.dumps(extracted_info,indent=2))