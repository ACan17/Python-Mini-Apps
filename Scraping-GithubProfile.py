import requests
from bs4 import BeautifulSoup

url="https://github.com/"
githubUser = input("Enter the Github Username: ")
request = requests.get(url+githubUser)
soup = BeautifulSoup(request.content, 'html.parser')

#Get the avatar image of the user
profileImage = soup.find('img', {'alt' : 'Avatar'})['src']
print(profileImage)