# Xakep parser
HackerParser is a tool which allows you to download all magazines from [xakep.ru](https://xakep.ru/issues). It's experimental branch, which in future will merged with main.

# Prerequisites

1. [Python](https://python.org/) version 3.8 or later
2. pip or pip3
3. Subscription for [xaker.ru](https://xakep.ru)

# Instructions

## Installing requirements

1. Clone this repo
        
    ```shell
    git clone https://github.com/kill-your-soul/HackerParser
    ```
2. Create virtual environment 
    
    - For Windows:

        ```shell
        python -m venv .venv
        ```

    - For Linux, MacOS:
    
        ```shell
        python3 -m venv .venv
        ```

3. Activate virtual environment

    - For Windows:
    
        ```shell
        .\.venv\Scripts\activate
        ```

    - For Linux, MacOS:

        ```shell
        source ./.venv/bin/activate
        ```

4. Install requirements

    - For Windows:

        ```shell
        pip install -r requirements.txt
        ```

    - For Linux, MacOS:
    
        ```shell
        pip3 install -r requirements.txt
        ```

## Running the script

1. Setting environment variables

    - For Windows:

        + Powershell:

            ```shell
            $env:LOGIN = "YOUR_LOGIN_TO_XAKEP";
            $env:PASSWORD = "YOUR_PASSWORD_TO_XAKEP";
            ```
        
        + cmd:

            ```shell
            set LOGIN=YOUR_LOGIN_TO_XAKEP
            set PASSWORD=YOUR_PASSWORD_TO_XAKEP
            ```

    - For Linux, MacOS:

        + Bash:

            ```shell
            export LOGIN="YOUR_LOGIN_TO_XAKEP"
            export PASSWORD="YOUR_PASSWORD_TO_XAKEP"
            ```


2. Run script

    - For Windows:

        ```shell
        python .\src\main.py
        ```

    - For Linux, MacOS
        
        ```shell
        python3 ./src/main.py
        ```