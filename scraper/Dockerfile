FROM python:3
WORKDIR /scraper
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./spiders/post_scraper.py" ]