from qdrant_client import QdrantClient
import torch
from transformers import BertTokenizer, BertModel

client = QdrantClient(
    url="https://f92f74ee-f795-441b-a5b9-2783cb082d6e.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="FWFmcohveoQQQltuEQyCsiaAgCEP4K4ZaDWCb6IcMWSzFWWgCO9lJw",
)

def generate_embeddings(text, model_name='bert-base-uncased'):
    # Load tokenizer and model
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name)
    model.eval()  # Put the model in evaluation mode
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    all_embeddings = []

    for i in range(0, len(text)):
        # Tokenize and encode the batch of texts
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)

        with torch.no_grad():
            outputs = model(**inputs)

        # Extract the embeddings for the [CLS] token (first token)
        cls_embeddings = outputs.last_hidden_state[:, 0, :]

        # Convert each embedding in the batch to a list of floats and append to the result
        for embedding in cls_embeddings:
            all_embeddings.append(embedding.cpu().tolist())

    return all_embeddings

def query(text):
    result = client.search(collection_name="Big_Basket", 
                           query_vector=generate_embeddings("soap")[0],
                           limit=1)
    string = ""
    for item in result:
        details = item.payload
        for key, value in details.items():
            string += (key + " : " + str(value) + " \n")
        string += '\n'
    return string