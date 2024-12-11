# Load model directly
# from transformers import AutoTokenizer, AutoModelForTableQuestionAnswering

# tokenizer = AutoTokenizer.from_pretrained("google/tapas-base-finetuned-wtq")
# model = AutoModelForTableQuestionAnswering.from_pretrained("google/tapas-base-finetuned-wtq")

# from transformers import AutoTokenizer, AutoModelForSequenceClassification

# # Carregar modelo pré-treinado
# tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
# model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=7)

# # Classificar cabeçalhos
# headers = ["DATA_MOV", "VALOR_TOTAL", "RAZAO_SOCIAL"]

# inputs = tokenizer(headers, padding=True, truncation=True, return_tensors="pt")
# outputs = model(**inputs)
# predictions = outputs.logits.argmax(dim=1)
# print(predictions)  # Retorna o mapeamento das colunas


from sentence_transformers import SentenceTransformer
sentences = ["I like the sun", "The sun is good"]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(sentences)
print(embeddings)
