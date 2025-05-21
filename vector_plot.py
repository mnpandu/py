import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def plot_similarity_results(docs_and_scores, embedding_model):
    # Extract texts and scores
    texts = [doc.page_content for doc, _ in docs_and_scores]
    scores = [score for _, score in docs_and_scores]

    # Get embeddings
    embeddings = embedding_model.embed_documents(texts)
    reduced = PCA(n_components=2).fit_transform(embeddings)

    # Plot
    plt.figure(figsize=(10, 7))
    for i, (x, y) in enumerate(reduced):
        plt.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, width=0.005, color='blue')
        label = f"Doc {i+1}\nScore: {1 - scores[i]:.2f}"  # cosine similarity = 1 - score
        plt.text(x + 0.01, y + 0.01, label, fontsize=9)

    plt.title("Vector Plot: Retrieved Documents (Cosine Similarity)")
    plt.xlabel("PCA Dimension 1")
    plt.ylabel("PCA Dimension 2")
    plt.grid(True)
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

    return list(zip(texts, reduced.tolist(), scores))
