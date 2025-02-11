import faiss
import json
import numpy as np
import openai
from config.env_config import load_api_key


load_api_key()


class FAISSKnowledgeDatabaseManager:
    def __init__(self, json_file):
        self.model = "text-embedding-3-small"  # -large
        self.dimension = 1536                  # 3072
        self.index = faiss.IndexFlat(self.dimension)
        self.issues = []  # List known issues
        self.load_json(json_file)

    def get_embedding(self, text):
        """Get text embedding with OpenAI."""
        response = openai.embeddings.create(
            input=text,
            model=self.model
        )
        embedding = np.array(response.data[0].embedding, dtype=np.float32)
        # Normalize embedding to use cosine similarity (better than euclidean distance for text)
        embedding /= np.linalg.norm(embedding)
        return embedding

    def load_json(self, json_file):
        """Load JSON knowledge database and index issues."""
        with open(json_file, "r") as f:
            data = json.load(f)
        for entry in data["troubleshooting_scenarios"]:
            issue_text = entry["issue"]
            self.issues.append({"issue": issue_text, "steps": entry["steps"]})
            embedding = self.get_embedding(issue_text)
            self.index.add(np.array([embedding]))

    def search(self, query, top_k=1, similarity_threshold=0.55):
        """Search for a related issue in FAISS."""
        query_embedding = self.get_embedding(query)
        distances, indices = self.index.search(np.array([query_embedding]), top_k)
        # Convert euclidean distance to cosine similarity
        similarities = 1 - distances[0]
        print("DEBUG FAISS")
        for i, index in enumerate(indices[0]):
            if index < len(self.issues):
                print(f"Match: issue={self.issues[index]['issue']} similarities={similarities[i]}")
        # Filter results based on similarity_threshold
        results = []
        for i, index in enumerate(indices[0]):
            if index < len(self.issues) and similarities[i] >= similarity_threshold:
                results.append(self.issues[index])

        return results if results else None
