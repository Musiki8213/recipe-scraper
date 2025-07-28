import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

#opening the webpage

response = requests.get("https://test-scrape-site.onrender.com/recipes.html")

#Reading the HTML
soup = BeautifulSoup(response.text, "html.parser")
recipes = soup.find_all("div", class_="recipe")


# Creating an Excel workbook
wb = Workbook()
ws = wb.active
ws.title = "Recipes"

#Header row
ws.append(["Name", "Ingredients", "Instructions"])


#Extract and write recipe data

for r in recipes:
    name = r.find("h2").text
    ingredients = [li.text for li in r.find("ul").find_all("li")]
    instructions = r.find("p").text.replace("Instructions:","")

    # Join ingredients into a single string
    ingredients_text = ", ".join(ingredients)

    # Add row to Excel
    ws.append([name, ingredients_text, instructions])

    # Save Excel file
    wb.save("scrape_recipes.xlsx")