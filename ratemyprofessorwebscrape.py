import requests
from bs4 import BeautifulSoup
from googlesearch import search
from professor import Professor
import course
import studentpreferences
import certifi
import urllib3
http = urllib3.PoolManager()


    
def find_professor_url(professor_name, site):
    query = f'{professor_name} site:{site}'

    # Perform a Google search
    search_results = search(query, num=1, stop=1, pause=2)

    # Iterate through the search results
    for result in search_results:
        if site in result:
            return result

    # except Exception as e:
    #     print(f"An error occurred: {e}")

    return None



def rmp_exec(professorName):
    # print("R U N N I N G RMP EXEC()")
    # professorName = 'Linsey Kuper'
    # site_to_search = 'ratemyprofessors.com'

    PROFESSOR_URL = find_professor_url(professorName, 'ratemyprofessors.com')
    flag = False
    if PROFESSOR_URL:
        flag = True
        # print(f"The URL for {professorName} on {'ratemyprofessors.com'} is: {PROFESSOR_URL}")
    else: #error handling
        flag = False
        # print(f"No URL found for {professorName} on {'ratemyprofessors.com'}.")


    RMP_URL = PROFESSOR_URL
    # response = requests.get(RMP_URL, verify=False)
    response = http.request('GET', RMP_URL, retries=False, verify=False)


    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        nameElement = soup.find('div', {'class': 'NameTitle__Name-dowf0z-0'})
        feedbackElements = soup.find_all('div', {'class': 'FeedbackItem__StyledFeedbackItem-uof32n-0'})
        ratingElement = soup.find('div', {'class': 'RatingValue__AvgRatingWrapper-qw8sqy-3'})

        if nameElement:
            firstName = nameElement.find('span').text.strip()
            lastName = nameElement.find('span', {'class': 'NameTitle__LastNameWrapper-dowf0z-2'}).text.strip()

            fullName = f"{firstName} {lastName}"

            # print("TEST - Professor's Full Name:", fullName)
        else: #Error Handling
            print("Name element not found.")

        if len(feedbackElements) >= 2:
            difficultyElement = feedbackElements[1].find('div', {'class': 'FeedbackItem__FeedbackDescription-uof32n-2', 'class': 'kkESWs'})
            if difficultyElement:
                professorDifficulty = difficultyElement.text.strip()
                # print("TEST - Level of Difficulty:", professorDifficulty)
            else: #Error Handling
                print("Difficulty element not found.")
        else: #Error Handling
            print("Insufficient feedback elements found.")

        if ratingElement:
            professorRating = ratingElement.find('div', {'class': 'RatingValue__Numerator-qw8sqy-2'}).text.strip()
            # print("TEST - Professor Rating:", professorRating)
        else: #Error Handling
            print("Rating element not found.")

        ratingDifficulty = [professorRating, professorDifficulty]
        return ratingDifficulty
    else: #Error Handling
        print("Failed to retrieve the webpage. Status code:", response.status_code)


# def main():
#     professorKuper = Professor('1','2', '3')
#     professorKuper.professorName = 'Lindsey Kuper'
#     ratingDifficulty = rmp_exec(professorKuper.professorName)
#     professorKuper.professorRating = ratingDifficulty[0]
#     professorKuper.professorDifficulty = ratingDifficulty[1]

#     # print("TESTING MAIN KUPER RATING: ", professorKuper.professorRating)
#     # print("TESTING MAIN KUPER DIFFICULTY: ", professorKuper.professorDifficulty)
#     # print("TESTING THIS IS KUPER: ", professorKuper.professorName)

# if __name__ == '__main__':
#     main()