#pip install tf-keras

from transformers import pipeline

# Load summarization pipeline with the specified model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Sample text for summarization
text = """Artificial intelligence (AI) is a rapidly evolving field of computer science focused on creating machines capable of performing tasks that typically require human intelligence. 
These tasks include learning, reasoning, problem-solving, perception, and language understanding. AI is broadly classified into narrow AI, which is designed for specific tasks, 
and general AI, which aims to replicate human cognitive abilities across various domains. Machine learning, a subset of AI, enables systems to learn from data and improve performance 
over time without being explicitly programmed. As AI continues to advance, it is being increasingly integrated into industries such as healthcare, finance, and transportation, 
revolutionizing the way we work and live."""

# Generate summary
summary = summarizer(text, max_length=100, min_length=50, do_sample=False)

# Print model used and the summarized text
print("Summarization Model Used:", summarizer.model.config.name_or_path)
print("\nSummary of the Text:")
print(summary[0]['summary_text'])
