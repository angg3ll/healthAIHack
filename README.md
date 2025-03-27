# healthAIHack

# files included 

# data
384_sequences.csv

## ETSeq variations
# PWM/SVM only with ETSeq pwm values (pwm values obtained from https://github.com/expartools/ETSeq/blob/master/Source_code_0.5.2.zip)
test_etseq.py 

# packages needed to run
pip install Bio.SeqUtils, Bio.Seq, sklearn

# evaluate a Random Forest Classifier to predict the class labels (CI, CII, CIII) of DNA sequences based on their sequence composition and some numerical features (P90, N10, Diff)
train_own_model.py

# packages needed to run
pip install numpy, pandas

# PWM and SVM plus Naive Bayes (pwm and features values obtained from https://github.com/expartools/ETSeq/blob/master/Source_code_0.5.2.zip)
SeqDep_backup.py

# packages needed to run
pip install Bio, os, subprocess, time, pandas, sklearn

# Additional functions
# Use gemini API to generate sequences 
generate_seq.py

# packages needed to run
pip install google.generativeai

## front end folder
# contains react app


