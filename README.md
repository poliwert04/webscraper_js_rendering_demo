# JavaScript Web Scraper — Python Demonstration Project

A Python script that scrapes dynamic JavaScript-rendered content from a website using Playwright and exports it to a clean CSV file. Built as a portfolio demonstration.

This project targets [quotes.toscrape.com/js](https://quotes.toscrape.com/js), a sandbox site built specifically for scraping practice
---

## Output

A CSV file containing the following fields for every quote scraped:

| Column | Description |
|--------|-------------|
| ID | Sequential quote number |
| Quote | Full quote text |
| Author | Author name |

---

## Requirements

- Python 3.8+
- Install dependencies with:

```
pip install playwright
playwright install
```

---

## Usage

**Basic usage (scrapes all 10 pages, outputs to `output.csv`):**
```
python scraper.py OUTPUT_FILE_NAME
```

**Custom number of pages and filename:**
```
python scraper.py OUTPUT_FILE_NAME --pages 5
```

**Custom delay between pages:**
```
python scraper.py OUTPUT_FILE_NAME --pages 5 --timeout 2
```

---

## Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `filename` | Name of the output CSV file (without extension) | Required |
| `-p`, `--pages` | Number of pages to scrape | 10 |
| `-t`, `--timeout` | Delay between page requests (in seconds)| 1 |

---

## Notes

- Delay between requests is configurable to avoid overloading the server.

---

*Available for custom scraping projects — feel free to reach out.*
