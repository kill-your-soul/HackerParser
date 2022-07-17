# Xakep parser
XakerParser is a tool which allows you to download all magazines from [xakep.ru](https://xakep.ru/issues)

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
            $env:login = "YOUR_LOGIN_TO_XAKEP";
            $env:password = "YOUR_PASSWORD_TO_XAKEP";
            ```
        
        + cmd:

            ```shell
            set login=YOUR_LOGIN_TO_XAKEP
            set password=YOUR_PASSWORD_TO_XAKEP
            ```

    - For Linux, MacOS:

        + Bash:

            ```shell
            export login="YOUR_LOGIN_TO_XAKEP"
            export password="YOUR_PASSWORD_TO_XAKEP"
            ```


2. Run script

    - For Windows:

        ```shell
        python main.py
        ```

    - For Linux, MacOS
        
        ```shell
        python3 main.py
        ```