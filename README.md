Course Materials – Workshop “Introduction to Python”
====================================================

This repository bundles course materials for a Python Programming
Workshop organized by the Zeppelin University Friedrichshafen in
cooperation with the Cluster of Excellence “The Politics of
Inequality” at the University of Konstanz in summer 2021 and in a
revised version in winter 2022.

Addressed to scholars in social sciences (in a very broad definition),
the workshop focuses on using Python in practice. The provided
hands-on examples will support the participants to use Python for
their own research interests.

As a short two-day workshop, some (limited) programming skills and a
first and basic understanding of the Python syntax are expected from
the participants.


# Day One

## 1. Introduction, Warm Up, Set Up

- Python puzzles / recap
  - data types
  - control structures
  - classes and objects
  - modules

- Python runtime and development environments
  - Python interpreter
  - editors, IDEs
  - Jupyter notebooks, Anaconda
  - virtual environment, Docker
  - Google Colaboratory

- last-minute help desk setting up Python work environment

Notebook: [warmup and setup](1_warmup_and_setup.ipynb)


## 2. Working with Structured Data

- read data from local files
- CSV and JSON
- elementary data analysis: Pandas and data frames
- plotting basics

Notebook: [working with structured data – the “Tree Cadastre of the City of Konstanz”](2_structured_data_tree_cadastre_konstanz.ipynb)


## 3. The Twitter API

- what is an API?
- get access to the API
- use a client: DocNow/twarc
- tweets, user timelines, followers, trends
- text statistics, language, sentiment

Notebook: [the Twitter API](3_twitter_api.ipynb)


# Day Two

## 4. Web Scraping

- HTTP requests
- HTML, XML, DOM, CSS selectors, XPath
- browser automation
- cleanse and export extracted data

Notebook: [Web Scraping](4_web_scraping.ipynb)


## 5. Text Processing and Machine Learning

- pre-processing and tokenization (splitting text into words)
- n-grams, vectorization and word embeddings
- train and evaluate a text classifier

Notebook: [Text Processing and Machine Learning](5_nlp_ml.ipynb)


# Licenses

- [Apache 2.0](./LICENSE) for the Python code and documentation
- for data shared in this repository, see the [listing of data sources and licenses](data/README.md)
