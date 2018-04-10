
## HW2-BooleanSearch

  - A program that can search words which satisfy "and", "or", and "not" function for news title in query, then return its id.
  - For example:
    MLB and 春訓
    iPhone or MLB
    好棒棒 and 好爛爛
    ...


# Preprocessing Query Data
By reading query data first, we can split all words without "and, or, not"-having text, leaves MLB, 春訓, iPhone, MLB, 好棒棒, 好爛爛 in above example. The intention of this is to save more time when maintain inverted-index table used to store each word mapping to its existing id number. Once we create a set that contains all the words(usually much less than title text), we can just scan source.csv line by line to check whether each word exists or not. Besides, the set can filter the word that exists in previous query so we need not to spend any time on repeated words even in different query. When checking each title, we reference the inverted-index table and append the ids if a word was found in the sentence. 

# Query with Inverted-index Table
With inverted-index table, we can compute each query very easy by Python's set. For each query, we can map "and, or, not" to "intersection, union, complement" in processing set.

# Usage
python main.py --source source.csv --query query.txt --output output.txt





