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

5. For the `NT(LLM)-XGBOOST.ipynb` notebook demonstrates how to utilize a Large Language Model (LLM) combined with XGBoost for enhanced sequence analysis. This approach leverages the power of LLMs to extract meaningful features from DNA sequences, which are then used to train a high-performance XGBoost model.

    **Dependencies:**

    To run the `NT(LLM)-XGBOOST.ipynb` notebook, ensure you have the following packages installed. You can install them using `pip`:

    ```bash
pip install \
    absl-py==2.2.0 \
    accelerate==1.5.2 \
    aiohttp==3.11.14 \
    aiosignal==1.3.2 \
    anyio==4.9.0 \
    asttokens==2.2.1 \
    attrs==23.1.0 \
    Babel==2.12.1 \
    backcall==0.2.0 \
    bio==1.7.1 \
    biopython==1.85 \
    biothings_client==0.4.1 \
    bleach==6.2.0 \
    bokeh==3.6.3 \
    CacheControl==0.12.14 \
    certifi==2023.5.7 \
    cffi==1.15.1 \
    chardet==5.1.0 \
    charset-normalizer==3.1.0 \
    chex==0.1.89 \
    click==8.1.3 \
    cloudpickle==2.2.1 \
    colorama==0.4.6 \
    colorcet==3.1.0 \
    comm==0.1.4 \
    commonmark==0.9.1 \
    contourpy==1.3.1 \
    cryptography==41.0.1 \
    cycler==0.12.1 \
    Cython==0.29.35 \
    datasets==3.4.1 \
    datashader==0.17.0 \
    debugpy==1.6.7.post1 \
    decorator==5.1.1 \
    dill==0.3.8 \
    distlib==0.3.6 \
    distro==1.8.0 \
    dm-haiku==0.0.13 \
    docopt==0.6.2 \
    docutils==0.20.1 \
    doit==0.36.0 \
    dulwich==0.21.5 \
    ecdsa==0.18.0 \
    et_xmlfile==2.0.0 \
    etils==1.12.2 \
    exceptiongroup==1.1.1 \
    execnet==1.9.0 \
    executing==1.2.0 \
    filelock==3.12.2 \
    fonttools==4.56.0 \
    frozenlist==1.5.0 \
    fsspec==2023.6.0 \
    future==0.18.3 \
    glob2==0.7 \
    gprofiler-official==1.0.0 \
    h11==0.14.0 \
    holoviews==1.20.2 \
    html5lib==1.1 \
    httpcore==1.0.7 \
    httpx==0.28.1 \
    huggingface-hub==0.29.3 \
    idna==3.4 \
    imageio==2.37.0 \
    imagesize==1.4.1 \
    importlib-metadata==6.7.0 \
    importlib-resources==5.12.0 \
    iniconfig==2.0.0 \
    intervaltree==3.1.0 \
    intreehooks==1.0 \
    ipaddress==1.0.23 \
    ipykernel==6.25.1 \
    ipython==8.14.0 \
    jax==0.5.3 \
    jaxlib==0.5.3 \
    jedi==0.19.0 \
    jeepney==0.8.0 \
    Jinja2==3.1.2 \
    jmp==0.0.4 \
    joblib==1.2.0 \
    jsonschema==4.17.3 \
    jupyter_client==8.3.0 \
    jupyter_core==5.3.1 \
    keyring==23.13.1 \
    keyrings.alt==4.2.0 \
    kiwisolver==1.4.8 \
    lazy_loader==0.4 \
    liac-arff==2.5.0 \
    linkify-it-py==2.0.3 \
    llvmlite==0.44.0 \
    lockfile==0.12.2 \
    lxml==4.9.2 \
    Markdown==3.7 \
    markdown-it-py==3.0.0 \
    MarkupSafe==2.1.3 \
    matplotlib==3.10.1 \
    matplotlib-inline==0.1.6 \
    mdit-py-plugins==0.4.2 \
    mdurl==0.1.2 \
    ml_dtypes==0.5.1 \
    mock==5.0.2 \
    more-itertools==9.1.0 \
    mpmath==1.3.0 \
    msgpack==1.0.5 \
    multidict==6.2.0 \
    multipledispatch==1.0.0 \
    multiprocess==0.70.16 \
    mygene==3.2.2 \
    nest-asyncio==1.5.7 \
    netaddr==0.8.0 \
    netifaces==0.11.0 \
    networkx==3.4.2 \
    nucleotide-transformer@git+[https://github.com/instadeepai/nucleotide-transformer@98af0a12f2c00fb5d1b35915e554611be4578a16](https://github.com/instadeepai/nucleotide-transformer@98af0a12f2c00fb5d1b35915e554611be4578a16) \
    numba==0.61.0 \
    numpy==2.1.3 \
    openpyxl==3.1.5 \
    opt_einsum==3.4.0 \
    optax==0.2.4 \
    packaging==23.1 \
    pandas==2.2.3 \
    panel==1.6.1 \
    param==2.2.0 \
    parso==0.8.3 \
    pastel==0.2.1 \
    pathlib2==2.3.7.post1 \
    pathspec==0.11.1 \
    pbr==5.11.1 \
    peft==0.15.0 \
    pexpect==4.8.0 \
    pickleshare==0.7.5 \
    pillow==11.1.0 \
    pkginfo==1.9.6 \
    platformdirs==3.8.0 \
    pluggy==1.2.0 \
    pooch==1.7.0 \
    prompt-toolkit==3.0.39 \
    propcache==0.3.0 \
    psutil==5.9.5 \
    ptyprocess==0.7.0 \
    pure-eval==0.2.2 \
    py==1.11.0 \
    py-expression-eval==0.3.14 \
    pyarrow==19.0.1 \
    pyasn1==0.5.0 \
    pycparser==2.21 \
    pycryptodome==3.18.0 \
    pyct==0.5.0 \
    pydevtool==0.3.0 \
    Pygments==2.15.1 \
    pylev==1.4.0 \
    PyNaCl==1.5.0 \
    pynndescent==0.5.13 \
    pyparsing==3.1.0 \
    pyrsistent==0.19.3 \
    pytest==7.4.0 \