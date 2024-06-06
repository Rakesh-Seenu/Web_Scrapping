import scrapy
from ..items import ImbdItem
import re
from scrapy.http import FormRequest
from scrapy.http import Response

class ImdbSpider(scrapy.Spider):
    name = "imdb"
    # allowed_domains = ["www.imdb.com"]
    start_urls = [
        "https://www.imdb.com/chart/top/"
        ]

    def parse(self, response):

        items = ImbdItem()
        movie_titles = response.css('h3.ipc-title__text::text').getall()
        movie_titles = [title for title in movie_titles if title not in ["Recently viewed", "IMDb Charts"]]
        movie_year = response.css('span.sc-b189961a-8.kLaxqf.cli-title-metadata-item::text').re(r'\d{4}')
        movie_ratings = response.css('span.ipc-rating-star--imdb.ratingGroup--imdb-rating::text').getall()
        movie_durations = response.css('span.sc-b189961a-8.kLaxqf.cli-title-metadata-item::text').getall()
        durations = []
        for duration in movie_durations:
                hours_match = re.search(r'(\d+)h', duration)
                minutes_match = re.search(r'(\d+)m', duration)
                if hours_match and minutes_match:
                    hours = int(hours_match.group(1))
                    minutes = int(minutes_match.group(1))
                    total_minutes = hours * 60 + minutes
                    durations.append(f"{hours}:{minutes:02}")
                elif hours_match:
                    hours = int(hours_match.group(1))
                    durations.append(f"{hours}:00")
                elif minutes_match:
                    minutes = int(minutes_match.group(1))
                    durations.append(f"0:{minutes:02}")
                else:
                    continue  # Skip entries with duration "0:00"
            # Print the extracted durations for debugging
        items['durations']=durations
        items['movie_ratings']=movie_ratings
        items['movie_titles']=movie_titles
        items['movie_year']=movie_year
        # print(movie_year)
        # print(movietitles)
        # print(durations)
        # print(movie_ratings)
        # print(hours)
        # pass
        yield items
