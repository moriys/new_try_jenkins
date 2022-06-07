from transformers import pipeline

classifier = pipeline("sentiment-analysis", 'blanchefort/rupert-base-cased-sntiment")

classifier('Я люблю  мармелад')
