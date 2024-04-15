import requests
from bs4 import BeautifulSoup

def scrape_weather_data(location):
    url = f"https://openweathermap.org/city/{location}"
    html = '<span data-v-3e6e9f12="" class="heading">9°C</span>'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    temperature_element = soup.find("span", class_="heading")
    if temperature_element:
        temperature = temperature_element.get_text().strip()
        return temperature
    else:
        return "Temperature data not found"

# Example usage
location = "2643743"  # London city ID
temperature = scrape_weather_data(location)
print(f"Temperature in London: {temperature}")
