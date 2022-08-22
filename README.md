# Keep it short
<i>Text summarization project</i>
<p></p>
<p></p>

```diff
```

## Notebook ▶️ 01_Centroid_based_Text_Summarization
<b>Uses:</b> [TF-IDF] [cossim] [Word2Vec]

<b>Intro:</b>
<i>
Centroids are the most relevant tokens (tokens that contain the same meaning).
One can use them to extract sentences that cointain the most information in a given text. </i>

<b>Steps:</b>
<i>
1. Construct centroids based on tf-idf.
2. Get embedding representation of centroids. 
3. Get embedding representation of every sentence
4. Score every sentence based on how similar it is to the centroid.
5. Select sentences based on their score until a certain number of words (hyperparameter) is reached
6. Avoid redundancy - if a chosen sentence is too similar to the ones in the already produced summary, don't add it (cosine similarity + predefined threshold)
</i>