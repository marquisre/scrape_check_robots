import requests
from bs4 import BeautifulSoup
from urllib import robotparser

def check_robots_txt(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(url + '/robots.txt')
    rp.read()
    return rp.can_fetch("*", url)

def scrape_website(url):
    try:
        # Check robots.txt before proceeding
        if not check_robots_txt(url):
            print("Access to the website is not allowed based on robots.txt. Please check the website's terms of service.")
            return

        # Make a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Example: Extracting title
            title = soup.title.text
            print(f"Title: {title}")

            # Example: Extracting all paragraphs
            paragraphs = soup.find_all('p')
            for paragraph in paragraphs:
                print(f"Paragraph: {paragraph.text}")

            # Add more code here to extract other information based on your needs

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
url_to_scrape = 'https://example.com'

# Check robots.txt before proceeding
if check_robots_txt(url_to_scrape):
    scrape_website(url_to_scrape)
else:
    print("Access to the website is not allowed based on robots.txt. Please check the website's terms of service.")
