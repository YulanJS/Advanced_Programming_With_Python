import urllib.request
import urllib.parse
import urllib.robotparser
import urllib.error
import bs4


def read_url(url):
    try:
        with urllib.request.urlopen('http://www.sjsu.edu') as url_file:
            # print(type(url_file))
            bytes_read = url_file.read()
    except urllib.error.URLERROR as url_error:
        print(f'Error opening url: {url}\n{url_error}')
    else:
        # print(type(page))
        # print(page)
        # decoded_page = bytes_read.decode('UTF-8')
        # print(decoded_page)
        soup = bs4.BeautifulSoup(bytes_read, 'html.parser')
        for each_style_tag in soup('style'):
            each_style_tag.decompose()
        for each_script_tag in soup('script'):
            each_script_tag.decompose()
        text = soup.get_text()
        return text


'''
    except UnicodeDecodeError as decode_error:
        # if url is a pdf form, decoding error
        print(f'Error decoding url: {url}\n{decode_error}')
'''

'''
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


url = 'http://blogs.sjsu.edu/newsroom/?s=football'
parsed_url = urllib.parse.urlparse(url)
print(parsed_url.scheme)
print(parsed_url.hostname)
print(parsed_url.path)
print(parsed_url.params)
print(parsed_url.query)
print(parsed_url.fragment)

url = '/Students/Quickfacts/default.cfm#Col'
base = 'http://iea.sjsu.edu/Reports/'
abs_url = urllib.parse.urljoin(base, url)
print(abs_url)
'''


def main():
    print(read_url('http://www.sjsu.edu'))


if __name__ == "__main__":
    main()
