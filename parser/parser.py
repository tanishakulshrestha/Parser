import nltk
import sys
import re

# --------------------- TERMINALS ---------------------
TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

# ------------------- NONTERMINALS -------------------
NONTERMINALS = """
S -> NP VP
S -> S Conj S

VP -> V
VP -> V NP
VP -> V PP
VP -> V NP PP
VP -> VP Conj VP

NP -> N
NP -> Det N
NP -> Det Adj N
NP -> Det Adj Adj N
NP -> NP PP
NP -> Det N PP

PP -> P NP
"""

# -------------------- PARSER ------------------------
grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)

# ------------------- MAIN FUNCTION ------------------
def main():
    # Read sentence from file or input
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()
    else:
        s = input("Sentence: ")

    # Preprocess sentence
    s = preprocess(s)

    # Attempt to parse
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return

    if not trees:
        print("Could not parse sentence.")
        return

    # Print parse trees and noun phrase chunks
    for tree in trees:
        tree.pretty_print()
        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


# ------------------ PREPROCESS ----------------------
def preprocess(sentence):
    """
    Tokenize sentence: lowercase words and remove non-alphabetic tokens.
    Avoids nltk.word_tokenize() to fix punkt_tab issue.
    """
    words = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
    return words


# ------------------ NP CHUNKS -----------------------
def np_chunk(tree):
    """
    Return all noun phrase (NP) chunks that do not contain nested NPs.
    """
    chunks = []
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            # Only keep NP chunks with no nested NPs
            if not list(subtree.subtrees(lambda t: t != subtree and t.label() == "NP")):
                chunks.append(subtree)
    return chunks


# ------------------ RUN SCRIPT ----------------------
if __name__ == "__main__":
    main()
