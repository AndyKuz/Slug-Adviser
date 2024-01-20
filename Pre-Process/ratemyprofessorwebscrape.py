import requests
from bs4 import BeautifulSoup
from googlesearch import search

    
def find_professor_url(professorName, site):
    query = f"{professorName} site:{site}"

    # Perform a Google search
    searchResults = search(query, num=5, stop=5, pause=2)

    # Iterate through the search results
    for result in searchResults:
        if site in result:
            return result

    return None

# professorName = 'Linsey Kuper'
# site_to_search = 'ratemyprofessors.com'

def rmp_exec(professorName):

    PROFESSOR_URL = find_professor_url(professorName, 'ratemyprofessors.com')

    if PROFESSOR_URL:
        print(f"The URL for {professorName} on {'ratemyprofessors.com'} is: {PROFESSOR_URL}")
    else: #error handling
        print(f"No URL found for {professorName} on {'ratemyprofessors.com'}.")


    RMP_URL = PROFESSOR_URL
    response = requests.get(RMP_URL)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        nameElement = soup.find('div', {'class': 'NameTitle__Name-dowf0z-0'})
        feedbackElements = soup.find_all('div', {'class': 'FeedbackItem__StyledFeedbackItem-uof32n-0'})
        ratingElement = soup.find('div', {'class': 'RatingValue__AvgRatingWrapper-qw8sqy-3'})

        if nameElement:
            firstName = nameElement.find('span').text.strip()
            lastName = nameElement.find('span', {'class': 'NameTitle__LastNameWrapper-dowf0z-2'}).text.strip()

            fullName = f"{firstName} {lastName}"

            print("Professor's Full Name:", fullName)
        else: #Error Handling
            print("Name element not found.")

        if len(feedbackElements) >= 2:
            difficultyElement = feedbackElements[1].find('div', {'class': 'FeedbackItem__FeedbackDescription-uof32n-2', 'class': 'kkESWs'})
            if difficultyElement:
                difficultyLevel = difficultyElement.text.strip()
                print("Level of Difficulty:", difficultyLevel)
            else: #Error Handling
                print("Difficulty element not found.")
        else: #Error Handling
            print("Insufficient feedback elements found.")

        if ratingElement:
            professorRating = ratingElement.find('div', {'class': 'RatingValue__Numerator-qw8sqy-2'}).text.strip()
            print("Professor Rating:", professorRating)
        else: #Error Handling
            print("Rating element not found.")

    else: #Error Handling
        print("Failed to retrieve the webpage. Status code:", response.status_code)
