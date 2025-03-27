# healthAIHack - DNA Sequence Analysis Toolkit

This repository contains tools for analyzing DNA sequences, including machine learning models and sequence generation utilities.

## Table of Contents

* [Files Included](#files-included)
* [ETSeq Variations](#etseq-variations)
    * [PWM/SVM Model](#pwmsvm-model)
* [Machine Learning Models](#machine-learning-models)
    * [Random Forest Classifier](#random-forest-classifier)
* [Combined Models](#combined-models)
    * [PWM, SVM, and Naive Bayes](#pwm-svm-and-naive-bayes)
* [Sequence Generation](#sequence-generation)
    * [Gemini API Sequence Generation](#gemini-api-sequence-generation)
* [Front-End Application](#front-end-application)
* [High-Performance Computing (HPC)](#high-performance-computing-hpc)
* [Installation](#installation)

## Files Included

* `data/384_sequences.csv`: Contains the DNA sequence data used for training and testing the models.

## ETSeq Variations

### PWM/SVM Model

* `test_etseq.py`: Implements a model using Position Weight Matrices (PWMs) and Support Vector Machines (SVM) based on values from [ETSeq](https://github.com/expartools/ETSeq/blob/master/Source_code_0.5.2.zip).

    **Dependencies:**

    ```bash
    pip install Bio.SeqUtils Bio.Seq scikit-learn
    ```

## Machine Learning Models

### Random Forest Classifier

* `train_own_model.py`: Trains a Random Forest Classifier to predict DNA sequence classes (CI, CII, CIII) using sequence composition and numerical features (P90, N10, Diff).

    **Dependencies:**

    ```bash
    pip install numpy pandas scikit-learn
    ```

## Combined Models

### PWM, SVM, and Naive Bayes

* `SeqDep_backup.py`: Combines PWM, SVM, and Naive Bayes models for sequence classification, utilizing feature values from [ETSeq](https://github.com/expartools/ETSeq/blob/master/Source_code_0.5.2.zip).

    **Dependencies:**

    ```bash
    pip install Bio os subprocess pandas scikit-learn
    ```

## Sequence Generation

### Gemini API Sequence Generation

* `generate_seq.py`: Uses the Gemini API to generate synthetic DNA sequences.

    **Dependencies:**

    ```bash
    pip install google-generativeai
    ```

## Front-End Application

* `frontend/`: Contains the React application for user interaction and visualization of analysis results.

## High-Performance Computing (HPC)

* For users with access to High-Performance Computing (HPC) environments, the machine learning and Large Language Model (LLM) models can be executed there for improved performance and scalability.

## Installation

1.  Clone the repository:

    ```bash
    git clone [repository URL]
    cd healthAIHack
    ```

2.  Install the required dependencies for each script as listed above. You can create virtual environments to manage dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS and Linux
    venv\Scripts\activate  # On Windows
    ```

3.  Run the desired scripts using Python:

    ```bash
    python [script_name].py
    ```

4.  For the React frontend, navigate to the `frontend` directory and install dependencies:

    ```bash
    cd frontend
    npm install
    npm start
    ```