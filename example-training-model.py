from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

# 1. Carregue o dataset
dataset = load_dataset('path_to_your_dataset.csv', split='train')

# 2. Tokenizer do modelo pré-treinado
model_name = 'sentence-transformers/all-MiniLM-L6-v2'
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 3. Tokenização
def preprocess_data(examples):
    return tokenizer(examples['Input'], truncation=True, padding=True)

tokenized_dataset = dataset.map(preprocess_data, batched=True)

# 4. Modelo
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(categories))

# 5. Configurações de treinamento
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    num_train_epochs=5,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir='./logs',
)

# 6. Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

# 7. Treine o modelo
trainer.train()

# 8. Salve o modelo
model.save_pretrained('./fine_tuned_model')
tokenizer.save_pretrained('./fine_tuned_model')
