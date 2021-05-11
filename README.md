# cs224n-project
Natural Language Processing (NLP) project
Analysing football and basketball news articles.

## Sources
Football news:
- [talkSPORT](https://talksport.com/)

Basketball news:
- [nba.com](https://www.nba.com/news)

## Pre-Fetching datasets:
1. [Download zip file](https://drive.google.com/file/d/1_kU9HLdk1v7RA1MtTs6_eSgFcHhw7mi7/view?usp=sharing) 
2. Extract it under `src/data/` directory

Project repository structure should be like:
```
cs224n-project/
├─ src/
│  ├─ crawler/
│  ├─ data/
│  │  ├─ raw/
│  │  ├─ clean/
│  │  ├─ corpus/
│  │  ├─ clean-text.ipynb
│  │  ├─ analytics.ipynb
├─ README.md
```


## Data Gathering
Datas are gathered via scrapy web crawler, for each news source theres a `<site>_spider.py` under `src/crawler/spiders/` directory.

In order to re-crawl data, follow the instruction

1. Initialize a new python3 virtual environment
```bash
cd src
python3 -m venv venv
source venv/bin/activate
```
2. Install project requirements
```bash
pip3 install -r requirements.txt
```
3. run crawlers
```bash
scrapy runspider crawler/spiders/nba_basketball_news_spider.py -o data/raw/basketball-nba.jl
scrapy runspider crawler/spiders/talksports_football_news_spider.py -o data/raw/football-talksports.jl
```
`.jl` file format is used which is abbreviation of JSON lines, it doesn't contain brackets `[,]` so it's data can be appendable.

**You can Also download both files as it mentioned [here](#pre-fetching-datasets)**

## Data Cleaning
In order to make crawled data ready for analysing and processing these steps are taken.
- Fix unicode characters

unicode escaped characters like `\u00A0` should be converted into ascii form

- Transliterate to cl`ó`sest ASCII representation
- Lowercase words
- Remove URLs and digits
- Remove stopwords
- Stemming & Lemmatization

You can see observe the process by taking a look at `clean-text.ipynb` jupyter notebook

**Note that it needs raw datas under `src/data/raw` so first download them and place them there**
```bash
jupyter notebook `src/data/clean-text.ipynb`
```

## Analytics
There are some cool statistics in `analytics.ipynb` which you can either run them by yourself:

```bash
jupyter notebook src/data/analytics.ipynb
```
or see the exported notebook `.html` file `src/data/analytics.html`
