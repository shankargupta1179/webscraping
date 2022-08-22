import requests
import bs4
import csv

class Scrape:

    def __init__(self) :
        product_list =[]
        response = requests.get('https://www.watchguard.com/wgrd-products/all-products-list')
        soup = bs4.BeautifulSoup(response.text,"html.parser")
        product_links = soup.select('.prod-list a')
        for i in product_links:
            row = []
            row.append(i.text)
            product_list.append(row)
        self.store_to_csv(product_list)
    
    def store_to_csv(self,product_list):
        with open('watchguard_product_list.csv','w+',newline='') as file:
            write = csv.writer(file)
            for product in product_list:
                write.writerow(product)
                
if __name__ == "__main__":

    scrape_obj = Scrape()
