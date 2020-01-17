import bs4
import urllib.request
import urllib.parse
'''
This program process course to course articulation information.
 
It read links from a url. Then, it extracts articulation 
information from each link and output the result into a file.
'''


def read_url(url):
    """
    Get all absolute urls referred to the articulation contracts of
    all California Colleges.
    :param url: (string) the url we start with.
    :return: (list) a list of absolute url strings
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
        # first table is an image, second table is index A-Z
        # third table has 141 links we want
        table = soup.find_all('table')[2]
        absolute_links = [urllib.parse.urljoin(url, anchor.get('href', None))
                          for anchor in table.find_all('a')]
        return absolute_links


def record_articulation_one_college(college_url, course_articulation_dict):
    """
    Find CS courses equivalent to five lower division CS courses at sjsu
    from given url, and store the information in dictionary.
    :param college_url: (string)the url of community college that
    contains course to course articulation of lower division.
    :param course_articulation_dict: (dictionary) key: (string)
    CS lower division course at SJSU. value: (list) corresponding
    equivalent CS courses at California community colleges.
    :return: None
    """
    try:
        with urllib.request.urlopen(college_url) as url_file:
            bytes_read = url_file.read()
    except urllib.error.URLError as url_err:
        print(f'Error opening url: {college_url}\n{url_err}')
    else:
        soup = bs4.BeautifulSoup(bytes_read, 'html.parser')
        state_to_college = soup('h3')[0].get_text()
        # state_to_college all starts with San Jose State University to
        # split and get from the sixth words and join
        college_name = ' '.join(state_to_college.split()[5:])
        computer_science_tr = soup.find('tr',
                                        string=r'Computer Science')
        # find_all will get ResultSet, must use loop to iterate
        done = False
        current_tr = computer_science_tr.find_next('tr')
        while not done:
            if not current_tr.get_text().startswith('CS'):
                done = True
            # td_set: all tds in a tr
            td_set = current_tr.find_all('td')
            is_first_td = True
            for td in td_set:
                if is_first_td:
                    dict_key = ' '.join(td.get_text().split()[:2])
                    is_first_td = False
                elif td.get_text():
                    # has empty td in tr
                    # separator=' ' add empty space between different
                    # html elements
                    equivalent_course = ' '.join(td.get_text(separator=' ')
                                                 .split())
                    if equivalent_course != "No Current Equivalent":
                        equivalent_course += ' at ' + college_name
                        # if the index appear for the first time,
                        # set dict value to an empty list using
                        # dict.setdefault(dict_key, []).append()
                        course_articulation_dict.setdefault(dict_key, [])\
                            .append(equivalent_course)
            current_tr = current_tr.find_next('tr')


def record_articulation_all_colleges(url_list, course_articulation_dict):
    """
    Loop through all urls in url_list and store information in
    the dictionary.
    :param url_list: (list) list of absolute urls referred to
    articulation between sjsu and California community colleges
    :param course_articulation_dict: (dictionary)
    key: (string) CS lower division course at SJSU.
    value: (list) corresponding equivalent CS courses at California
    community colleges.
    :return: None
    """
    for college_url in url_list:
        record_articulation_one_college(college_url, course_articulation_dict)


def write_result_file(course_articulation_dict):
    """
    Write information in dictionary to an output file.
    :param course_articulation_dict: (dictionary)
    key: (string) CS lower division course at SJSU.
    value: (list) corresponding equivalent CS courses at California
    community colleges.
    :return: None
    """
    # w mode: overwrite existing file
    with open('articulations.txt', 'w', encoding='UTF-8') as output_file:
        for course in course_articulation_dict:
            for equivalent_course in course_articulation_dict[course]:
                output_file.write(course + ": " + equivalent_course + '\n')


def main():
    url_list = read_url('http://info.sjsu.edu/web-dbgen/artic/'
                        'all-course-to-course.html')

    course_articulation_dict = {}
    record_articulation_all_colleges(url_list, course_articulation_dict)
    print(course_articulation_dict)
    write_result_file(course_articulation_dict)


if __name__ == "__main__":
    main()

