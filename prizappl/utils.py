
import requests
from bs4 import BeautifulSoup

def search_amazon(product_name):
    url = f'https://www.amazon.in/s?k={product_name}'
    print(f"Amazon search URL: https://www.amazon.in/s?k={product_name}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    if not products:
        return None
    
    product = products[0]
    name = product.find('h2').text.strip()
    description = product.find('div', {'class': 'a-section'}).text.strip()
    image_url = product.find('img')['src']
    product_url = f"https://www.amazon.in{product.find('a')['href']}"
    price_element = product.find('span', {'class': 'a-price-whole'})
    if price_element is not None:
        price = float(price_element.text.replace(',', ''))
    else:
        price = None
    return {
        'name': name,
        'description': description,
        'image_url': image_url,
        'product_url': product_url,
        'price': price
    }

def search_flipkart(product_name):
    url = f'https://www.flipkart.com/search?q={product_name}'
    print(f"Flipkart search URL: https://www.flipkart.com/search?q={product_name}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', {'class': '_2kHMtA'})
    if not products:
        return None
    product = products[0]
    name = product.find('a', {'class': '_2mylT6'}).text.strip()
    description = product.find('ul', {'class': '_1xgFaf'}).text.strip()
    image_url = product.find('img')['src']
    product_url = f"https://www.flipkart.com{product.find('a')['href']}"
    price_element = product.find('div', {'class': '_30jeq3 _1_WHN1'})
    if price_element is not None:
        price = float(price_element.text.replace('₹', '').replace(',', ''))
    else:
        price = None
    return {
        'name': name,
        'description': description,
        'image_url': image_url,
        'product_url': product_url,
        'price': price
    }



import requests
from bs4 import BeautifulSoup

def search_snapdeal(product_name):
    url = f'https://www.snapdeal.com/search?keyword={product_name}'
    print(f"Snapdeal search URL: https://www.snapdeal.com/search?keyword={product_name}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', {'class': 'product-tuple-listing'})
    if not products:
        return None
    product = products[0]
    name = product.find('p', {'class': 'product-title'}).text.strip()
    description = product.find('p', {'class': 'product-desc'}).text.strip()
    image_url = product.find('img')['src']
    product_url = product.find('a')['href']
    price_element = product.find('span', {'class': 'product-price'})
    if price_element is not None:
        price = float(price_element.text.replace('Rs.', '').replace(',', ''))
    else:
        price = None
    return {
        'name': name,
        'description': description,
        'image_url': image_url,
        'product_url': product_url,
        'price': price
    }
import requests
from bs4 import BeautifulSoup

def search_jiomart(product_name):
    url = f'https://www.jiomart.com/search/{product_name}'
    print(f"Jiomart search URL: https://www.jiomart.com/search/{product_name}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', {'class': 'col-6 col-md-3 pdp-card'})
    if not products:
        return None
    product = products[0]
    name = product.find('div', {'class': 'name'}).text.strip()
    description = product.find('div', {'class': 'description'}).text.strip()
    image_url = product.find('img')['src']
    product_url = product.find('a')['href']
    price_element = product.find('div', {'class': 'final-price'})
    if price_element is not None:
        price = float(price_element.text.replace('Rs.', '').replace(',', ''))
    else:
        price = None
    return {
        'name': name,
        'description': description,
        'image_url': image_url,
        'product_url': product_url,
        'price': price
    }





# import requests
# from bs4 import BeautifulSoup

# def search_amazon(product_name):
#     url = f'https://www.amazon.in/s?k={product_name}'
#     print(f"Amazon search URL: https://www.amazon.in/s?k={product_name}")
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
#     if not products:
        
#         return None
#     element = soup.find('div', {'class': 'example-class'})
    

#     product = products[0]
#     name = product.find('h2').text.strip()
#     description = product.find('div', {'class': 'a-section'}).text.strip()
#     image_url = product.find('img')['src']
#     product_url = f"https://www.amazon.in{product.find('a')['href']}"
#     price = float(product.find('span', {'class': 'a-price-whole'}).text.replace(',', ''))
#     return {
#         'name': name,
#         'description': description,
#         'image_url': image_url,
#         'product_url': product_url,
#         'price': price
#     }





# def search_flipkart(product_name):
#     url = f'https://www.flipkart.com/search?q={product_name}'
#     print(f"Flipkart search URL: https://www.flipkart.com/search?q={product_name}")
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     products = soup.find_all('div', {'class': '_2kHMtA'})
#     if not products:
#             return None
#     product = products[0]
#     name = product.find('a', {'class': '_2mylT6'}).text.strip()
#     description = product.find('ul', {'class': '_1xgFaf'}).text.strip()
#     image_url = product.find('img')['src']
#     product_url = f"https://www.flipkart.com{product.find('a')['href']}"
#     price = float(product.find('div', {'class': '_30jeq3 _1_WHN1'}).text.replace('₹', '').replace(',', ''))
#     return {
#         'name': name,
#         'description': description,
#         'image_url': image_url,
#         'product_url': product_url,
#         'price': price
#     }







# def search_amazon(product_name):
#     url = f'https://www.amazon.in/s?k={product_name}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     products = soup.find_all('div', {'data-component-type': 's-search-result'})
#     product = products[0]
#     name = product.find('h2').text.strip()
#     description = product.find('div', {'class': 'a-section'}).text.strip()
#     image_url = product.find('img')['src']
#     product_url = f"https://www.amazon.in{product.find('a')['href']}"
#     price = float(product.find('span', {'class': 'a-price-whole'}).text.replace(',', ''))
#     return {
#         'name': name,
#         'description': description,
#         'image_url': image_url,
#         'product_url': product_url,
#         'price': price
#     }

# def search_flipkart(product_name):
#     url = f'https://www.flipkart.com/search?q={product_name}'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     products = soup.find_all('div', {'class': '_2kHMtA'})
#     product = products[0]
#     name = product.find('a', {'class': '_2mylT6'}).text.strip()
#     description = product.find('ul', {'class': '_1xgFaf'}).text.strip()
#     image_url = product.find('img')['src']
#     product_url = f"https://www.flipkart.com{product.find('a')['href']}"
#     price = float(product.find('div', {'class': '_30jeq3 _1_WHN1'}).text.replace('₹', '').replace(',', ''))
#     return {
#         'name': name,
#         'description': description,
#         'image_url': image_url,
#         'product_url': product_url,
#         'price': price
#     }
