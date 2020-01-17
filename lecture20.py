# ----------------------------------------------------------------------
# Name:        lecture20
# Purpose:     Demonstrate using Beautiful Soup to parse html files
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Skeleton module to be used in lecture 20.

Demonstrate using Beautiful Soup to parse html files.
"""
import bs4
import re


def make_soup(filename):
    """
    Parse the html file specified.
    :param filename: string - name of the html file to be parsed
    :return: BeautifulSoup object
    """
    with open(filename, 'r', encoding='utf-8') as html_file:
        soup = bs4.BeautifulSoup(html_file, "html.parser")
    return soup


def taste(soup):
    """
    Explore the given Beautiful soup object.
    :param soup: BeautifulSoup object
    :return: None
    """
    # Your code here
    # print(soup)  # html
    # print(soup.get_text())  # a visible document in html

    # result = soup.find_all('p')  # extract all paragraphs
    # print(result)
    # print(type(result))

    # print(len(soup.find_all('a')))  # find all <a> anchor tags
    # print(soup('a'))  # short way of find all <a>
    # extract href links
    '''
    for each_anchor in soup('a'):
        print(each_anchor.get('href', None))  # set default if not found
    '''
    # print(soup('h3')[0].get_text())  # get the first header of h3 tag

    # get href links in table only
    '''
    tables = soup.find_all('table')
    table = tables[0]
    for each_anchor in table.find_all('a'):
        print(each_anchor.get('href', None))
    '''

    # get the text in the second column in the table that is associated
    # with site(s)
    tables = soup.find_all('table')
    table = tables[0]
    regex = re.compile(r"site", re.IGNORECASE)
    all_sites = table.find_all('td', string=regex)
    for each_site in all_sites:
        next_column = each_site.find_next_sibling('td')
        # adds a space between 'and' and 'Section 3'
        description = next_column.get_text(separator=' ')
        # add separator between different html elements
        # get rid of extra spaces and new line characters
        description = ' '.join(description.split())
        print(description)


'''
def read_url(url):
    # remove tag style and all its contents, related to JS style
    for each_style_tag in soup('style'):
        each_style_tag.decompose()
'''


def main():
    soup = make_soup("demosoup.html")
    taste(soup)


if __name__ == "__main__":
    main()
