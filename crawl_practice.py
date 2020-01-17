import bs4
import urllib.robotparser
import urllib.request
import re


def visit_url(url):
    """
    Open the given url and return its visible content and the
    referenced links.
    :param url:(string) - the address of the web page to be read
    :return: (tuple) (text, links)
        text: a text string containing the visible content
            of the corresponding web page.
        links: a set of strings containing the referenced links.
        None if there is an error opening the url.
    """
    try:
        with urllib.request.urlopen(url) as url_file:
            bytes_read = url_file.read()
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {url}\n{url_err}')
    else:
        soup = bs4.BeautifulSoup(bytes_read, 'html.parser')
        for each_style_tag in soup("style"):
            each_style_tag.decompose()
        for each_script_tag in soup("script"):
            each_script_tag.decompose()
        text = soup.get_text()
        absolute_links = {urllib.parse.urljoin(url, anchor.get('href', None))
                          for anchor in soup('a')}
    return text, absolute_links


def ok_to_crawl(url):
    parsed_url = urllib.parse.urlparse(url)
    if not parsed_url.scheme or not parsed_url.hostname:
        print('Not a valid absolute url:', url)
        return False
    robot = urllib.parse.urljoin(f'{parsed_url.scheme}://{parsed_url.netloc}',
                                 'robots.txt')
    user_agent = urllib.request.URLopener.version
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robot)
    try:
        rp.read()
    except urllib.error.URLError as url_error:
        print(url, robot, url_error)
        return False
    else:
        return rp.can_fetch(user_agent, url)


def crawl(seed, search_term):
    """
    Crawl the web starting at the seed url specified and counting the
    occurrences of the search term specified in each of them.
    :param seed: (string) absolute url
    :param search_term: (string) the term we are looking in the urls
    :return: a dictionary where the keys are the urls crawled and
    the values are counts of the search term in each url.
    """
    to_crawl = {seed}
    visited = set()
    search_counts = {}
    url_count = 0
    while to_crawl and url_count <= 20:  # limit crawling to 20 urls.
        url = to_crawl.pop()
        if url[-3:] not in ('pdf', 'jpg'):  # skip pdf and jpg
            if url not in visited:
                visited.add(url)
                if ok_to_crawl(url):
                    result = visit_url(url)
                if result is not None:
                    text, new_urls = result
                    to_crawl = to_crawl | new_urls  # set union
                    # \b means backspace
                    occurrences = re.findall(fr'(\b{search_term}s?\b)', text,
                                             re.IGNORECASE)
                    search_counts[url] = len(occurrences)
                    url_count += 1
                    return search_counts


def main():
    seed = 'http://www.sjsu.edu/'
    search_term = 'spartan'
    result = crawl(seed, search_term)
    top3 = sorted(result, key=lambda url: result[url], reverse=True)[0:3]
    all_counts = sum(result.values())
    print(f'Total occurrences of "{search_term}" in all urls crawled:',
          all_counts)
    for each_url in top3:
        print(f'In {each_url}, {result[each_url]} occurrences of '
              f'"{search_term}" were found')
