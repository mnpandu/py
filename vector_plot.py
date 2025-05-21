import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

def plot_similarity_results(docs_and_scores, embedding_model):
    # Extract content and scores
    texts = [doc.page_content for doc, _ in docs_and_scores]
    scores = [score for _, score in docs_and_scores]  # cosine distances

    # Embed and reduce to 2D
    embeddings = embedding_model.embed_documents(texts)
    reduced = PCA(n_components=2).fit_transform(embeddings)

    # Normalize vector lengths to improve layout
    vectors = np.array(reduced)
    max_length = np.linalg.norm(vectors, axis=1).max()
    scaled_vectors = vectors / max_length * 0.8  # scale to fit nicely

    # Plot setup
    plt.figure(figsize=(10, 6))
    for i, (x, y) in enumerate(scaled_vectors):
        plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, width=0.005, color='blue')
        label = f"D{i+1} (sim={1 - scores[i]:.2f})"
        plt.text(x + 0.02, y + 0.02, label, fontsize=8)

    plt.title("2D Vector Plot of Retrieved Documents")
    plt.xlabel("PCA Dimension 1")
    plt.ylabel("PCA Dimension 2")
    plt.grid(True)
    plt.axhline(0, color='gray', lw=0.5)
    plt.axvline(0, color='gray', lw=0.5)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

    return list(zip(texts, scaled_vectors.tolist(), scores))
