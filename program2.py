import requests as rq;
from time import sleep;

def fetch_url(url, retries=3, delay=1):
    atmpt = 1;
    while (atmpt <=retries):
        try:
            response = rq.get(url, timeout=5);
            response.raise_for_status();
            return response.text;
        except rq.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}");
        except rq.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}");
        except rq.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}");
        except rq.exceptions.RequestException as req_err:
            print(f"General error occurred: {req_err}");
        atmpt+=1;
        print(f"Retrying... ({atmpt}/{retries})");
        sleep(delay)
    return None;

def fetch_urls(urls):
    contents = [];
    for url in urls:
        print(f"Fetching: {url}");
        cntnt = fetch_url(url);
        if cntnt is not None:
            contents.append(cntnt);
        else:
            print(f"Failed to fetch: {url} after {3} retries");
    return contents;

urls = ["https://en.wikipedia.org/wiki/%22Hello%2C_World!%22_program",
    "https://www.nonexistentwebsite.xyz",
    "https://httpbin.org/status/500"];
fetched_contents = fetch_urls(urls);
for i, content in enumerate(fetched_contents):
    print(f"Content {i + 1}:\n{content[:100]}...");