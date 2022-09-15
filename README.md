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

## ▶️ Notebook ▶️ [01_Centroid_based_Text_Summarization](01_Centroid_based_Text_Summarization.ipynb) ##
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

## ▶️ Notebook ▶️ [02_TextRank_and_KeyPhrase_Text_Summarization](02_TextRank_and_KeyPhrase_Text_Summarization.ipynb) ##
🔵 <b>Uses:</b> <i>[keras] [cossim] [networkx] [KeyPhraseTransformer]</i>

🔵 <b>Intro:</b>
<i>
Another approach to address text summary, using cosine similarity is to use pagerank algorithm to transform the content into a pseudo-graph and produce a ranking of nodes (sentences) based on the connections (cos_sim). The highest ranking sentences should be considered when construction the summary. </i>
<i>
Additionally, a Keyphrase is introduced to show individual phrases that are meaningful to the text content. </i>

🔵 <b>Steps:</b>
<i>
1. Make text representation using keras text tokenizer.
2. Construct similarity matrix between sentences using cosine similarity.
3. Rank the sentences using the structure of other sentences representations that particular sentence is connected to.
4. Specify percent of sentences to be used as final prediction.
5. Use KeyPhraseTransformer to highlight meaningful phrases. 
</i>


```diff
