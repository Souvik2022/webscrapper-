


import requests
from bs4 import BeautifulSoup
url = "https://www.1mg.com/diseases/acne-261"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

#link section
title = soup.title
anchors = soup.find_all('a')
container = soup.find_all('div' , class_='col-6 marginTop-16' )
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'): 
        linkText = "https://www.1mg.com" +link.get('href')
        all_links.add(link)
        print("References - " + linkText) 


#Disease name  section
divvar = soup.find('h1' , class_='l1SemiBold' )

print("Topic name is - " + divvar.get_text())


#overview section
overview = soup.find('p')
print("overview is - " + overview.get_text())


#Treatment section

treatments = soup.find(id = "treatment")

var = treatments.find_all("p")
var2 = treatments.find_all("ul")

for key,key2 in var , var2:
    print("key: " + key.text )
    print("value: " + key2.text)

#prevention portion
print(soup.find_all("p" , id="prevention"))

results = soup.find(id="prevention")
elements = results.find_all("p")
for element in elements:
    print(element.get_text())

#causes section

causes = soup.find(id="causes")
for cause in causes:

    var = cause.find("h3")
    var2 = cause.find("p")
    print(var)
    print(var2)

#Some points -

#the img website have all the relevent sections but
#   the class name is not very weirdy wrapped some sections have proper class name 
#  some sections which are intrecate doesnt even have class names or improperly wrapped them
# the code is commented in a proper manned but due to the immense amout of class name 
# wrapping there are some issues feel like i should mention it 
