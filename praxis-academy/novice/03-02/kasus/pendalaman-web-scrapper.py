'''
When you run the code for web scraping, a request is sent to the URL that you 
have mentioned. As a response to the request, the server sends the data and
allows you to read the HTML or XML page. The code then, parses the HTML or XML
 page, finds the data and extracts it. 

To extract data using web scraping with python, you need to follow these basic 
steps:

    Find the URL that you want to scrape
    Inspecting the Page
    Find the data you want to extract
    Write the code
    Run the code and extract the data
    Store the data in the required format 

library to use
    Selenium:  It is used to automate browser activities.
    BeautifulSoup: package for parsing HTML and XML documents. 
    It creates parse trees that is helpful to extract the data easily.
    Pandas: used for data manipulation and analysis. 
    It is used to extract the data and store it in the desired format. 
'''

# installing pandas, beautifulsoup, selenium using pip install <packagename>

# task : mencari nama 100 matematikawan dari list yang ada pada
# http://www.fabpedigree.com/james/mathmen.htm
# untuk ditemukan pada target link seperti https://en.wikipedia.org/wiki/Mathematician/

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# membuat fungsi get request

def simple_get(url):
    '''
    membuat http GET request untuk mengambil konten pada url
    ketika ketemu file html/xml ambil data
    jika selain itu, data kosong 
    '''
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    
    except RequestException as e:
        log_error('Error during request to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    '''
    return true jika response seperti html, selain itu return false
    '''
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    # cetak error
    print(e)

def get_names():
    '''
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    '''
    url = 'http://www.fabpedigree.com/james/mathmen.htm'
    response = simple_get(url)    
    
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)    
    
    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))

def get_hits_on_name(name):
    """
    Accepts a `name` of a mathematician and returns the number
    of hits that mathematician's wikipedia page received in the 
    last 60 days, as an `int`
    """
    # url_root is a template string that used to buld a URL.
    url_root = 'http://www.fabpedigree.com/james/mathmen.htm/{}'
    response = simple_get(url_root.format(name))    
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')

        hit_link = [a for a in html.select('a')        
                    if a['href'].find('latest-60') > -1]        
        
        if len(hit_link) > 0:
            # Strip commas:
            link_text = hit_link[0].text.replace(',', '')
            try:
                # Convert to integer
                return int(link_text)
            except:
                log_error("couldn't parse {} as an `int`".format(link_text))    
    log_error('No pageviews found for {}'.format(name))
    return None

if __name__ == '__main__':
    print('Getting the list of names....')
    names = get_names()
    print('... done.\n')    
    
    results = []    
    
    print('Getting stats for each name....')    
    
    for name in names:
        try:
            hits = get_hits_on_name(name)
            if hits is None:
                hits = -1
            results.append((hits, name))
        except:
            results.append((-1, name))
            log_error('error encountered while processing '
                      '{}, skipping'.format(name))    
        
    print('... done.\n')    
    results.sort()
    results.reverse()    
    
    if len(results) > 5:
        top_marks = results[:5]
    else:
        top_marks = results    
    
    print('\nThe most popular mathematicians are:\n')
    for (mark, mathematician) in top_marks:
        print('{} with {} page views'.format(mathematician, mark))    
    
    no_results = len([res for res in results if res[0] == -1])
    print('\nBut we did not find results for '
          '{} mathematicians on the list'.format(no_results))