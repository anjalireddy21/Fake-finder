from transformers import pipeline

# ✅ Force use of PyTorch framework
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", framework="pt")

def detect_fake_text(text):
    labels = ["real", "fake", "satire"]
    result = classifier(text, candidate_labels=labels)
    best_label = result["labels"][0]
    score = result["scores"][0]
    return best_label.upper(), score
