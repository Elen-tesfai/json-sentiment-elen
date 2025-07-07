# Requests, JSON, and basic NLP with spaCy

### Introduction

This project explores how to use web APIs, JSON data, and natural language processing (NLP) tools to analyze the sentiment of song lyrics. By retrieving song lyrics from the Genius API and applying sentiment analysis with spaCy and VADER, we can determine the emotional tone of various songs. The goal is to demonstrate practical skills in API usage, file handling, and text analysis using Python.

### Note  
*This README is part of the assignment for Web Mining and Applied NLP (44-620). All tasks were completed in the Jupyter notebook and committed to this repository for grading.*

Complete the tasks in the Python Notebook in this repository.
To be submitted for credit, all changes must be committed and pushed to this repository (do not create your own repository unless instructed to on the course website).

## Rubric

* (Question 1) Lyrics printed: 1 pt
* (Question 1) File created and submitted with notebook: 1 pt
* (Question 2) Correct polarity reported: 1 pt
* (Question 2) Question answered thoughtfully: 1 pt
* (Question 3) Function defined as specified: 1 pt
* (Question 3) Song lyrics retrieved and stored in separate files (0.5 pts/song): 2 pts
* (Question 4) Polarity scores printed (with appropriate label containing song title, .25 pts/song): 1 pt
* (Question 4) Questions answered thoughtfully: 2 pts


This project uses **Requests**, **JSON**, and **spaCy** for Natural Language Processing (NLP) to analyze song lyrics. The notebook demonstrates the process of fetching song data from an API, performing sentiment analysis on the lyrics, and storing the results in JSON format.

---

### Rubric Checklist

#### **(Question 1) Lyrics Printed**
- [x] Lyrics successfully printed for each song retrieved from the API.

#### **(Question 1) File Created and Submitted with Notebook**
- [x] The Jupyter notebook, **`requests-json-nlp.ipynb`**, is created and submitted with the repository.
- [x] All tasks have been committed and pushed to the repository.

#### **(Question 2) Correct Polarity Reported**
- [x] The sentiment polarity for each song was calculated correctly using **VADER Sentiment Analysis**.
- [x] Results are printed with the appropriate label, containing the song title and its polarity score.

#### **(Question 2) Question Answered Thoughtfully**
- [x] I addressed all the questions thoughtfully, discussing the sentiment analysis process, challenges, and solutions.

#### **(Question 3) Function Defined as Specified**
- [x] A custom function, **`write_song_from_api_to_json()`**, was written to retrieve song data from the API and store it in separate JSON files.

#### **(Question 3) Song Lyrics Retrieved and Stored in Separate Files**
- [x] Song lyrics were successfully retrieved using the **Genius API**.
- [x] Lyrics were stored in separate JSON files for each song (0.5 points per song).

#### **(Question 4) Polarity Scores Printed**
- [x] Polarity scores for each song were printed with appropriate labels that include the song title.
- [x] Sentiment analysis was done using the **VADER Sentiment Analyzer**, and results were displayed for each song.

#### **(Question 4) Questions Answered Thoughtfully**
- [x] I answered the questions thoughtfully, reflecting on the sentiment analysis results and challenges faced during the project.

---

### Overview

This repository contains the code for fetching and analyzing song lyrics. We use multiple APIs, primarily the **Genius API**, and perform sentiment analysis using **spaCy** and **VADER**. Here's how the project breaks down:

---

### Installation Instructions

1. **Install Required Libraries**  
   Run the following commands to install necessary dependencies:

```bash
   pip install spacy
   pip install spacytextblob
   pip install requests
   pip install vaderSentiment
```
2.**Download spaCy Model**
```bash
  Download the en_core_web_sm model used for NLP:
  python -m spacy download en_core_web_sm
```
### Key Features

- **API Integration:**  
  Successfully integrated the **Genius API** for retrieving song data. The API requests returned JSON data, which was parsed to get song lyrics.

- **Sentiment Analysis:**  
  Implemented sentiment analysis using **VADER** and **spaCy** to quantify emotions in the lyrics. Each song's sentiment polarity was calculated and displayed with the song title.

- **Reusable Functions:**  
  Created a custom function to store song data in separate JSON files, making the code reusable for other songs.

---

### Repository Links

- **GitHub Repository:** [Elen's JSON Sentiment Analysis](https://github.com/Elen-tesfai/json-sentiment-elen)

- **Jupyter Notebook:** [requests-json-nlp.ipynb](https://github.com/Elen-tesfai/json-sentiment-elen/blob/master/requests-json-nlp.ipynb)

### Reflections

#### What is JSON?
JSON (JavaScript Object Notation) is a lightweight format for storing and transporting data. It's easy for humans to read and write and easy for machines to parse and generate. In this project, JSON was used to structure the data returned by the API.

#### What is Sentiment Analysis?
Sentiment analysis is a technique in NLP that determines the sentiment or emotion behind a piece of text. It is used to classify text as positive, negative, or neutral. For this project, we used **VADER Sentiment Analysis**, which is optimized for social media texts and short pieces of content like song lyrics.

#### How Popular are These Libraries?

- **spaCy:**  
  spaCy is one of the most widely used NLP libraries, known for its speed and accuracy in processing large datasets.

- **VADER:**  
  VADER is a popular sentiment analysis tool that is widely used for analyzing text, especially in social media and reviews.

#### Challenges in Working with APIs:
APIs can be prone to changes, and sometimes they may stop functioning altogether. Learning how to adapt to such changes is a key skill. Handling errors like timeouts, incorrect responses, and authentication issues is part of working with APIs.

---

### Conclusion
This project provided valuable experience in working with **APIs**, **JSON** data, and performing **sentiment analysis** using Python libraries like **spaCy** and **VADER**. It was an excellent opportunity to apply **NLP** techniques to real-world data, analyze emotions in song lyrics, and implement a robust solution that can be reused for future projects.