from playwright.sync_api import sync_playwright

import argparse
import csv

URL = "https://quotes.toscrape.com/js"
def format_url(page_number):
    return URL+f'/page/{page_number}/'
def check_status_code(response):
    if response is None:
        print("Response object is None, cannot check status code")
        return
    if response.status != 200:
        print(f"Failed to navigate to initial URL. Status code: {response.status}")
        exit(1)

def scrape(browser_ref, num_of_pages, timeout):
    page = browser_ref.new_page()
    try:
        print("Checking initial URL navigation")
        check_status_code(page.goto(URL, timeout=5000))
    except TimeoutError:
        print(f"Navigation to initial URL timed out")
        exit(1)
    except Exception as e:
        print(f"Error navigating to initial URL: {e}")
        exit(1)

    print("Initial URL navigation successful\n")
    scrape_data = []


    for page_num in range(1, num_of_pages+1):
        try:
            check_status_code(page.goto(format_url(page_num), timeout=10000))
            page.wait_for_timeout(timeout)
            print(f"Scraping page {page_num} of {num_of_pages}")

            quote_scrape = page.locator('span.text').all_text_contents()
            author_scrape = page.locator('small.author').all_text_contents()

            if not quote_scrape:
                print("The page has no quotes")
                continue

            for quote, author in zip(quote_scrape, author_scrape):
                scrape_data.append((quote, author))

        except TimeoutError as e:
            print(f"Page {page_num} scraping timed out: {e}")
            continue
        except Exception as e:
            print(f"Error scraping page {page_num}: {e}")
            continue

    print('Scraping finished')
    return scrape_data

def output(filename, scrape_data_output):
    print(f"\nOutputting to : {filename}.csv")
    try:
        with open(filename+'.csv', 'w', newline='', encoding='utf-8') as file:
            quote_number = 1
            writer = csv.writer(file)
            writer.writerow(['ID', 'Quote', 'Author'])
            for data in scrape_data_output:
                writer.writerow([quote_number, data[0], data[1]])
                quote_number += 1
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='Output file name for scraped data')
    parser.add_argument('-t', '--timeout', type=int, default=1, help='Timeout for page loading in seconds')
    parser.add_argument('-p', '--pages', type=int, default=10, help='Number of pages to scrape')
    args = parser.parse_args()

    with sync_playwright() as p:
        browser = p.chromium.launch()

        scrape_data_final = scrape(browser, args.pages, args.timeout*1000)
        output(args.filename, scrape_data_final)

if __name__ == "__main__":
    main()