from pydantic import BaseModel
from openai import OpenAI
"enter the key"

client = OpenAI(api_key=api_key)

class sentiment(BaseModel):
    res: str
    score: float
def analyze(text):

    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Classify the sentiment of the following text as Positive, Negative, or Neutral with sentiment score from -1 to 1."},
            {"role": "user", "content": text},
        ],
        response_format=sentiment,
    )

    event = completion.choices[0].message.parsed
    
    return str(event)

with open('review.txt') as f:
    lines = f.readlines()

    for line in lines:
        if len(line) > 1:
            print(line.strip())
            print(analyze(line.strip()))
