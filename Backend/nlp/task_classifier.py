from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="valhalla/distilbart-mnli-12-1"
)

TASKS = [
    "job search",
    "product price search",
    "general question"
]

def classify_task(text):
    result = classifier(text, TASKS)
    return result["labels"][0]
