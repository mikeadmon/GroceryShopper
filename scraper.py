import requests
import bs4

def shufersal_products():

    url = 'https://www.shufersal.co.il/online/he/A04'
    response = requests.get(url)
    html_soup = bs4.BeautifulSoup(response.text, 'html.parser')
    products = html_soup.find_all('div', class_ = "corporateProduct")
    i = 0
    for each in products:

        each = products[i]
        productName = (each.find('span',class_='productName').text.strip())
        productPrice = (each.find('div',class_='number').text.strip())
        print(productName)
        print(productPrice)
        i = i + 1


shufersal_products()

