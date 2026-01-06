# Parser
A natural language parser that uses context-free grammar to analyze sentence structure and extract noun phrase chunks
# Sentence Parser and Noun Phrase Extraction

Understanding the structure of natural language is a fundamental challenge in artificial intelligence. One important task in natural language processing (NLP) is **parsing**, which involves determining the grammatical structure of a sentence. Parsing allows a computer to better understand meaning and extract useful information from text.

In this project, a sentence parser is implemented using **context-free grammar (CFG)** to analyze English sentences and extract **noun phrase chunks**. The project is part of **CS50’s Introduction to Artificial Intelligence with Python**.

---

##  Project Overview

The parser takes an English sentence as input, tokenizes and preprocesses it, and then constructs a **parse tree** based on defined grammar rules. From this parse tree, the program identifies and extracts noun phrase chunks—noun phrases that do not contain other noun phrases within them.

For example:
Sentence: Holmes sat.
Produces a parse tree and extracts:

---

## 📐 Grammar & Parsing Approach

The project uses **context-free grammar rules** to describe how sentences are structured.  
Key grammatical components include:

- **Noun Phrases (NP)** – subjects or objects of sentences
- **Verb Phrases (VP)** – actions or states
- **Prepositional Phrases (PP)** – relationships between objects
- Determiners, adjectives, adverbs, conjunctions, and verbs

By expanding the grammar rules beyond simple sentence structures, the parser is capable of handling more complex English sentences found in the provided dataset.

---

## 🔍 Noun Phrase Chunking

A **noun phrase chunk** is defined as a noun phrase that does not contain any other noun phrases within it. This allows the parser to extract the most meaningful atomic noun phrases from a sentence without redundancy.

The parser traverses the syntax tree and selects only those noun phrases that meet this definition.

---

## 🛠️ Technologies Used

- **Python 3.12**
- **NLTK (Natural Language Toolkit)**
- Context-Free Grammar (CFG)
- Parse Trees

---

## 🎯 Learning Outcomes

Through this project, I learned how to:
- Design and extend context-free grammar rules
- Parse English sentences into syntax trees
- Tokenize and preprocess natural language input
- Extract meaningful grammatical structures from parsed text

This project highlights how symbolic approaches like grammars still play an important role in NLP alongside modern machine learning techniques.

---

