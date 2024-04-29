# Google Analytics to DuckDB Pipeline

## Overview

This pipeline script aims to ingest data from Google Analytics into DuckDB, facilitating dashboarding and data insights. By automating the data ingestion process, users can efficiently transfer Google Analytics data into a database, enabling further analysis and visualization.

## Run with Docker

The easiest way to run is using Docker as this has been containerized into a Docker image. 
- Pull the image: `docker pull snehangsude/blackpiano:latest`
- Execute the image: `docker run snehangsude/blackpiano`

> Note: This doesn't show an tabular format in the console. For seeing data in tabular format, jump to `Installation` steps.

## Features

- Connects to Google Analytics to retrieve data
- Utilizes DuckDB as the database for storage
- Supports customization of Google Analytics metrics and dimensions

### Prerequisites

Before using this pipeline script, ensure that you have the following prerequisites installed and configured:

- Python 3.10 or later
- Google Analytics API credentials (JSON file)
- DuckDB database setup

### Installation

1. Open a folder and run `git clone https://github.com/snehangsude/blackpiano-GA.git`
2. Create an environment
    - For Ubuntu: 
    `python3 -m venv <name_of_the_env>`
    `source <name_of_the_env>/bin/activate`

    - For Windows: 
    `python3 -m venv <name_of_the_env>`
    `source <name_of_the_env>/Scripts/activate`

3. Install the `requirements.txt` file using `pip install -r requirements.txt`
4. Set the environment credentials for the GCP env using `export GOOGLE_APPLICATION_CREDENTIALS=<path_to_credentials.json>`
5. Exceute the `async_main.py` using 
    - For Ubuntu: `python3 async_main.py`
    - For Windows: `python async_main.py` 

## Files & Code Explanation

These are the files which take care of each bit of the execution.
-  `analytics_client.py`
    <br>
    > Contains `AnalyticsClient` class. This Python class provides functionality to retrieve data from the Google Analytics Data API asynchronously. It is designed to simplify the process of fetching analytics data from Google Analytics for further processing and analysis.

    - Asynchronously connect to the Google Analytics Data API.
    - Retrieve reports based on specified property ID, date range, dimensions, and metrics.


-   `database.py`
    <br>
    > Contains the `Database` class. This Python class provides functionality to manage a DuckDB database, including connecting to the database, creating tables, inserting data, executing queries, and committing transactions. It is designed to work in conjunction with Google Analytics data ingestion pipeline scripts, allowing seamless integration with DuckDB for storing and analyzing analytics data.

    - Connect to a DuckDB database.
    - Check if a table exists in the database.
    - Create a table in the database if it does not exist.
    - Insert data into the database table.
    - Execute SQL queries on the database.
    - Commit transactions to save changes to the database.

-   `config_reader.py`
    <br>
    > Contains the `read_config` function. This Python function provides functionality to read configuration settings from a YAML file. It is designed to simplify the process of loading configuration parameters from a file for use in Python applications.

    - Read configuration settings from a YAML file.
    - Safely load YAML data to prevent code execution from untrusted sources.

-   `async_main.py`
    <br>
    > This Python file provides merges the ability from the above this files and sets the code to execute based on the criteria passed in the `config.yaml` file i.e. to extract the data from the Google Analytics, store it to a database table (duckdb) and print the output to the console.

-   `config.yaml`/ `config.sample`
    <br>
    > This is the configuration file to set configurations about the database and Google Analytics. This can be customized based on the variables passed.
    A `config.sample` is attached along that informs what kind of data should be stored. In production git, we would like to not push our `config.yaml` file but instead want that to be deployed using a private repo.

-   `Dockerfile`
    <br>
    > This is to Dockerize the entire code and make it a easy run without having to worry about environments and setup. The console output is printed in in the Logs.

-   `requirements.txt`
    <br>
    > This is all the packages and dependencies that are required to be installed for the program to be run if you are using `git clone` and executing the code.
