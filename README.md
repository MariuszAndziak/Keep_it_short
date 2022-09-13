# Keep it short
<i>Text summarization project</i>
<p></p>
<p></p>
In general, text summarization software intends to produce a shorter version of predefined text whether to use it as a news headline, a web snippet for a search result of for any other reason. People are lazy from nature and usually don't want to read big blocks of text. <br>
We want to quickly grasp the general understanding of a particular text and not dwell on every individual word or sentence individually deciding in our unconscious mind is this particular 
phrase relevant or just a filler. <br>
Text summarization can be decomposed into extractive and abstractive. The former keeps the original sentence structure unchanged and only picks the sentences that convey the most meaning. On the other hand, the latter reduces the length of the original text and produces new structures that contain the same essential information (definition, tone or intention) as the original.<br>
Both types of text summarization are shown in these notebooks.
```diff

```

## ▶️ Notebook ▶️ [01_Centroid_based_Text_Summarization] (01_Centroid_based_Text_Summarization.ipynb) ##
🔵 <b>Uses:</b> <i>[TF-IDF] [cossim] [Word2Vec]</i>

🔵 <b>Intro:</b>
<i>
Centroids are the most relevant tokens (tokens that contain the most meaning).
One can use them to extract sentences that cointain inportant imformation in a given text. </i>

🔵 <b>Steps:</b>
<i>
1. Construct centroids based on tf-idf.
2. Get embedding representation of those centroids. 
3. Get embedding representation of every sentence.
4. Score every sentence based on how similar it is to the centroid.
5. Select sentences based on their score until a certain number  (hyperparameter) is reached. This will produce a summary.
6. Avoid redundancy - if a chosen sentence is too similar to the ones in the already produced summary, don't add it (use cosine similarity + predefined threshold to avoid redundancy).
</i>

```diff

```