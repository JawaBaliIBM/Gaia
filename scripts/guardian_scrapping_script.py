
"""
    Script to scrap articles from The Guardian API
    
    Maintainers:
    - fellitacandini@gmail.com
    - rmayiffah@gmail.com
"""
import os, requests, json, re, datetime, logging

QUERY_URL = "https://content.guardianapis.com/search?" \
            "section=environment&show-fields=trailText%2Cbody" \
            "&from-date={from_date}" \
            "&api-key={api_key}" \
            "&page={page}" \
            "&page-size={page_size}"
DATE_FORMAT = "%Y-%m-%d"
HTML_SUBS = [
        ('<br.*?>', '/n'),
        ('<.*?>', '')
    ]

API_KEY = os.getenv('API_KEY')
PAGE_SIZE = int(os.getenv('PAGE_SIZE'))
FROM_DATE = datetime.datetime.now().strftime(DATE_FORMAT)

def dumps(obj):
    return json.dumps(obj, sort_keys=True, indent=4)

def clean_html(raw_html):
    for pattern, replacement in HTML_SUBS:
        cleaned_html = re.sub(re.compile(pattern), replacement, raw_html)
    
    return cleaned_html


def map_data(data):
    article = clean_html(data['fields']['body'])
    snippet = clean_html(data['fields']['trailText'])
    return {
        'snippet': snippet,
        'id': data['id'],
        'date': data['webPublicationDate'],
        'title': data['webTitle'],
        'url': data['webUrl'],
        'article': article
    }

def clean_data(data_list):
    return [map_data(x) for x in data_list]

def construct_url(page):
    return QUERY_URL.format(
        from_date = FROM_DATE,
        api_key = API_KEY,
        page = page,
        page_size = PAGE_SIZE
    )

data_len = 0
data_total = PAGE_SIZE
page = 1
result = list()
try:
    while data_len < data_total:
        url = construct_url(page)
        response = requests.get(url)
        json_body = response.json()
        if 'error' in json_body:
            logging.error('The requested query resulted error. Query: %s',
                url)
            break

        cleaned_data = clean_data(json_body['response']['results'])
        result.extend(cleaned_data)
        data_len += PAGE_SIZE
        if data_total != json_body['response']['total']:
            data_total = json_body['response']['total']
        page += 1
except Exception as e:
    logging.error('Got exception while trying to crawl data. Exception: %s',
        e)

print(dumps(result))