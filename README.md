# my-first-app-inclass-summer-2024

## Setup

Create virtual environment:

```sh
conda create -n ump-env python=3.11
```

Activate the environment:

```sh
conda activate ump-env
```

Install packages:

```sh
#pip install requests
#pip install plotly
#pip install python-dotenv

# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt
```


Obtain an [API Key](https://www.alphavantage.co/support/#api-key) from Alphavantage. Then create a ".env" file in the root directory of the repo, and paste some contents in like this, but using your own api key:

```sh
# this is the ".env" file:

ALPHAVANTAGE_API_KEY="__________"
```

## Usage

Run the script:

```sh
python app/unemployment.py

# equivalent (we'll need this once we start importing code from one file to another):
python -m app.unemployment
```














