# IMDb Scrapy Web Scraping Project
## Overview
Welcome to the IMDb Scrapy Web Scraping Project. This project leverages Scrapy, an advanced web scraping framework for Python, to meticulously extract data from IMDb's Top 250 movies chart. The extracted data encompasses movie titles, release years, ratings, and durations, and is subsequently stored in an SQLite database for comprehensive analysis.

## Project Structure
This project is structured to ensure clarity and maintainability:

imdb_spider.py: The core spider file containing the scraping logic.
items.py: Defines the data structure for the scraped items.
pipelines.py: Contains the pipeline for processing and storing the scraped data into an SQLite database.
requirements.txt: Lists the necessary Python packages for the project.
README.md: Provides an extensive overview and detailed instructions for the project.

## Scrapy Spider (imdb_spider.py)
The ImdbSpider is designed to navigate the IMDb Top 250 movies chart and extract critical data points:

Movie Titles: Extracted using CSS selectors.
Release Years: Extracted using CSS selectors and regular expressions.
Ratings: Extracted using CSS selectors.
Durations: Extracted and formatted using CSS selectors and regular expressions.

## Key Components
Selectors: Utilizes CSS selectors to accurately target and extract the required elements from the webpage.
Regex: Employs regular expressions to precisely format movie durations.
Items: Scrapy item objects are used to store the extracted data in a structured manner.

## Data Pipeline (pipelines.py)
The PracticePipeline is responsible for processing the scraped data and inserting it into an SQLite database. The pipeline performs the following functions:

Create Connection: Establishes a connection to the SQLite database.
Create Table: Creates a table within the database if it does not already exist.
Store Data: Inserts the scraped data into the database, ensuring data integrity and consistency.

## Data Stored In SQLite as follows:
![WhatsApp Image 2024-06-06 at 05 13 26_40444cbe](https://github.com/Rakesh-Seenu/Web_Scrapping/assets/126412041/bb1f0bd9-9845-4136-8cb1-b4c76cb387ec)

