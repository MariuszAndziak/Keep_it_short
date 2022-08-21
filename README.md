# Keep it short
Text summarization project

## ▶️ 01_Centroid_based_Text_Summarization
[TF-IDF] [cossim] [Word2Vec]

Centroids are the most relevant tokens (tokens that contain the same meaning).

1. Sum up vector representation of words that are part of a centroid => get embedding representation of the centroid.
2. Every sentence is scored (cosine similarity) based on how similar they are to the centroid embedding.
3. Select sentences based on their score until a certain number of words (hyperparameter) is reached
4. Avoid redundancy - if a chosen sentence is too similar to the ones in the already produced summary, don't add it (cosine similarity + predefined threshold)
