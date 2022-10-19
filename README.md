# rwthonline_crawler


# Getting Started

## 1. Installing the virtual environment

Use anaconda for a virtual environment, in this case 'rwth_crawler' from our 'environment.yml' file:

    $ conda env create -f environment.yml

Or alternatively create the venv from scratch with:

    $ conda create -n rwth_crawler notebook pandas pip
    $ conda activate rwth_crawler

## 2. Web Crawler with Selenium/Chrome

Using ChromeDriver for Chrome version 95: ChromeDriver 95.0.4638.17

from: https://chromedriver.chromium.org/downloads


Code based in tutorial from: https://medium.com/swlh/introduction-to-selenium-create-a-web-bot-with-python-cd59a741fdae

https://selenium-python.readthedocs.io/locating-elements.html

## 3. Execture our Script

- Start the chromedriver.exe
- run the main.ipynb