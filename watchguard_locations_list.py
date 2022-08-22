import requests
import bs4
import csv

class LocationList:
    
    def __init__(self) :
        locations_list = []
        response = requests.get('https://www.watchguard.com/wgrd-about/contact')
        soup = bs4.BeautifulSoup(response.text,"html.parser")
        location_links = soup.select('.location img')
        for i in  location_links:
            row = []
            row.append(i['alt'])
            locations_list.append(row)
        self.store_to_csv(locations_list)

    def store_to_csv(self,locations_list):
        with open('watchguard_locations.csv','w+',newline='') as file:
            write = csv.writer(file)
            for location in locations_list:
                write.writerow(location)


if __name__ == "__main__":
    
    location_obj = LocationList()
        