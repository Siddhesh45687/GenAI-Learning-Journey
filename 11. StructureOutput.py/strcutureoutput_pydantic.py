from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Literal,Optional
from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI

load_dotenv()

class Review(BaseModel):
    themes: list[str] = Field(description="themes of the review")
    summary: str = Field(description="Summary of the themes")
    sentiment: Literal['Positive','Negative','Neutral'] = Field(description="All the Sentiment")
    cons : Optional[list[str]] = None
    pros : Optional[list[str]] = None
    name : Optional[str] = None

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.5).with_structured_output(Review,method="json_schema")

review_text = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse!

The Snapdragon 8 Gen 3 processor makes everything lightning fast.

The 5000mAh battery easily lasts a full day.

The S-Pen integration is a great touch.

The 200MP camera is stunning.

However, the weight and size make it uncomfortable.

Samsung's One UI still comes with bloatware.

The $1,300 price tag is also a hard pill to swallow.

Pros:

- Insanely powerful processor
- Stunning 200MP camera
- Long battery life with fast charging
- S-Pen support

Cons:

- Bulky and heavy
- Bloatware
- Expensive compared to competitors

Review by Akshay Kumar
"""
review = model.invoke(f"Analyze the text {review_text}")

print(review)

print("Themes",review.themes)
print("Summary",review.summary)
print("Sentiment",review.sentiment)
print("Cons",review.cons)
print("Pros",review.pros)
print("Name",review.name)