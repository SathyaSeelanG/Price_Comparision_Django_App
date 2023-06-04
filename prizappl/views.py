from django.shortcuts import render
from .utils import search_amazon, search_flipkart
def home(request):
    query = request.GET.get('search')
    amazon_url = f"https://www.amazon.in/s?k={query}"
    flipkart_url = f"https://www.flipkart.com/search?q={query}"
    jiomart_url = f"https://www.jiomart.com/search/{query}"
    #jiomart_url =f"https://www.jiomart.com/category/groceries/{query}?page=1"
    #jiomart_url=f"https://www.snapdeal.com/search?keyword={query}"
    snapdeal_url = f"https://www.snapdeal.com/search?keyword={query}"
    meeesho_url = f"https://www.meeesho.com/search?q={query}"
    amazon_results = []
    flipkart_results = []
    jiomart_results = []
    snapdeal_results = []
    meeesho_results = []
    
    
    meeesho_data = fetch_data(meeesho_url, 'meeesho')
    print("Meeesho data:", meeesho_data)
    if meeesho_data:
        meeesho_results = extract_data_meesho(meeesho_data, 'meeesho')


    amazon_data = fetch_data(amazon_url, 'amazon')
    print("Amazon data:", amazon_data)
    if amazon_data:
        amazon_results = extract_data(amazon_data, 'amazon')

# Fetch data from Flipkart
    flipkart_data = fetch_data_flip(flipkart_url, 'flipkart')
    print("Flipkart data:", flipkart_data)
    if flipkart_data:
        flipkart_results = extract_data_flip(flipkart_data, 'flipkart')

    jiomart_data = search_jiomart(jiomart_url)
    print("JioMart data:", jiomart_data)
    if jiomart_data:
        jiomart_results = extract_data_jiomart(jiomart_data, 'jiomart')

    # Fetch data from Snapdeal
    snapdeal_data = search_snapdeal(snapdeal_url)
    print("Snapdeal data:", snapdeal_data)
    if snapdeal_data:
        snapdeal_results = extract_data_snapdeal(snapdeal_data, 'snapdeal')
    

    # # Fetch data from Amazon
    # amazon_data = fetch_data(amazon_url, 'amazon')
    # if amazon_data:
    #     amazon_results = extract_data(amazon_data, 'amazon')

    # # Fetch data from Flipkart
    # flipkart_data = fetch_data(flipkart_url, 'flipkart')
    # if flipkart_data:
    #     flipkart_results = extract_data(flipkart_data, 'flipkart')

    # print("Amazon results:", amazon_results)
    # print("Flipkart results:", flipkart_results)
    
    #return render(request, 'product1.html', { 'flipkart_results': flipkart_results})
    return render(request, 'product5.html', {'amazon_results': amazon_results, 
                                             'flipkart_results': flipkart_results,
                                             'snapdeal_results':snapdeal_results,
                                             'jiomart_results':jiomart_results,
                                             'meeesho_results':meeesho_results})
#snapdeal_results
     # Combine the results from both websites
    # results = amazon_results + flipkart_results
    # return render(request, 'product1.html', {'results': results})


    # print("Amazon results:", amazon_results)
    # print("Flipkart results:", flipkart_results)

    # return render(request, 'product1.html', {'amazon_results': amazon_results, 'flipkart_results': flipkart_results})



import requests
from bs4 import BeautifulSoup

def fetch_data(url, website):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        print(f"Failed to get data from {website}: {str(e)}")
        return None
    

def fetch_data_flip(url, website):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        print(f"Failed to get data from {website}: {str(e)}")
        return None
    


def search_jiomart(url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.content
        except Exception as e:
            print(f"Failed to get data from JioMart: {str(e)}")


def search_snapdeal(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        print(f"Failed to get data from snapdeal: {str(e)}")


def search_meesho(search_term):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = f'https://meesho.com/search/catalog?query={search_term}'
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
    except Exception as e:
        print(f"Failed to get data from Meesho: {str(e)}")

from bs4 import BeautifulSoup

def extract_data(html_content, website):
    if website == 'amazon':
        soup = BeautifulSoup(html_content, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})
        products = []
        #for result in results:
        for result in results:

            try:
                name = result.find('span', {'class': 'a-size-base-plus'}).text.strip()
            except AttributeError:
                name = None

            try:
                price = result.find('span', {'class': 'a-price-whole'}).text.strip()
            except AttributeError:
                price = None

            try:
                image_url = result.find('img', {'class': 's-image'}).get('src')
            except AttributeError:
                image_url = None

            try:
                product_url = 'https://www.amazon.in' + result.find('a', {'class': 'a-link-normal'}).get('href')
            except AttributeError:
                product_url = None

            products.append({
                'name': name,
                'price': price,
                'image_url': image_url,
                'product_url': product_url,
                'website': 'Amazon'
            })

        return products
    
   


def extract_data_flip(html_content, website):
    if website == 'flipkart':

        soup = BeautifulSoup(html_content, 'html.parser')
        results = soup.find_all('div', {'class': '_2kHMtA'})
        products = []
        for result in results:
            try:
                name = result.find('a', {'class': '_2mylT6'}).text.strip()
            except AttributeError:
                name = None

            try:
                price = result.find('div', {'class': '_30jeq3 _1_WHN1'}).text.strip()
            except AttributeError:
                price = None

            try:
                image_url = result.find('img', {'class': '_396cs4 _3exPp9'}).get('src')
            except AttributeError:
                image_url = None

            try:
                product_url = 'https://www.flipkart.com' + result.find('a', {'class': '_2mylT6'}).get('href')
            except AttributeError:
                product_url = None

            products.append({
                'name': name,
                'price': price,
                'image_url': image_url,
                'product_url': product_url,
                'website': 'Flipkart'
        })

        return products
    

def extract_data_jiomart(html_content, website):
    if website == 'jiomart':

        soup = BeautifulSoup(html_content, 'html.parser')
        results = soup.find_all('div', {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
        products = []
        for result in results:
            try:
                name = result.find('div', {'class': 'name'}).text.strip()
            except AttributeError:
                name = None

            try:
                price = result.find('div', {'class': 'price'}).text.strip()
            except AttributeError:
                price = None

            try:
                image_url = result.find('img', {'class': 'lazy'}).get('data-original')
            except AttributeError:
                image_url = None

            try:
                product_url = result.find('a', {'class': 'category-name'}).get('href')
            except AttributeError:
                product_url = None

            products.append({
                'name': name,
                'price': price,
                'image_url': image_url,
                'product_url': product_url,
                'website': 'JioMart'
            })

        return products
def extract_data_snapdeal(html_content, website):
    if website == 'snapdeal':
        soup = BeautifulSoup(html_content, 'html.parser')
        results = soup.find_all('div', {'class': 'product-tuple-listing'})
        products = []
        for result in results:
            try:
                name = result.find('p', {'class': 'product-title'}).text.strip()
            except AttributeError:
                name = None

            try:
                price = result.find('span', {'class': 'product-price'}).text.strip()
            except AttributeError:
                price = None

            try:
                image_url = result.find('img', {'class': 'product-image'}).get('src')
            except AttributeError:
                image_url = None

            try:
                product_url = result.find('a', {'class': 'dp-widget-link'}).get('href')
            except AttributeError:
                product_url = None

            products.append({
                'name': name,
                'price': price,
                'image_url': image_url,
                'product_url': product_url,
                'website': 'Snapdeal'
            })

        return products
    

def extract_data_meesho(html_content, website):
    if website == 'Meesho':
        soup = BeautifulSoup(html_content, 'html.parser')
        results = soup.find_all('div', {'class': 'styles_productCard__1e0vB'})
        products = []
        for result in results:
            try:
                name = result.find('div', {'class': 'styles_productTitle__2Pz5E'}).text.strip()
            except AttributeError:
                name = None

            try:
                price = result.find('div', {'class': 'styles_cardPrice__HgIuh'}).text.strip()
            except AttributeError:
                price = None

            try:
                image_url = result.find('img', {'class': 'styles_productImg__2Qx7J'}).get('src')
            except AttributeError:
                image_url = None

            try:
                product_url = 'https://meesho.com' + result.find('a', {'class': 'styles_productCardLink__3sD97'}).get('href')
            except AttributeError:
                product_url = None

            products.append({
                'name': name,
                'price': price,
                'image_url': image_url,
                'product_url': product_url,
                'website': 'Meesho'
            })

        return products



        # Implementation for Flipkart
        

    elif website == 'mart':
        # Implementation for Flipkart
        pass



# from django.shortcuts import render
# from .utils import search_amazon, search_flipkart

# def home(request):
#     if request.method == 'GET':
#         product_name = request.GET.get('search', None)
#         if product_name:
#             amazon_results = search_amazon(product_name)
#             flipkart_results = search_flipkart(product_name)
#             # print(amazon_results) 
#             # print(flipkart_results)
#             context = {
#                 'amazon_results': amazon_results,
#                 'flipkart_results': flipkart_results,
#                 # 'product_name': product_name
#             }
#             return render(request, 'product2.html', context)
#     return render(request, 'home1.html')


# from django.shortcuts import render
# from .utils import search_amazon, search_flipkart

# def home(request):
#     if request.method == 'GET':
#         product_name = request.GET.get('search', None)
#         if product_name:
#             amazon_results = search_amazon(product_name)
#             flipkart_results = search_flipkart(product_name)
#             context = {
#                 'amazon_results': amazon_results,
#                 'flipkart_results': flipkart_results,
#             }
#             return render(request, 'product2.html', context)
#     return render(request, 'home1.html')


# Create your views here.


# from django.shortcuts import render
# from .utils import search_amazon, search_flipkart


# from django.shortcuts import render
# from .utils import search_amazon, search_flipkart

# def home(request):
#     if request.method == 'POST':
#         product_name = request.POST['product_name']
#         amazon_products = search_amazon(product_name)
#         flipkart_products = search_flipkart(product_name)
#         return render(request, 'product.html', {'amazon_products': amazon_products, 'flipkart_products': flipkart_products})
#     return render(request, 'home11.html')

# from django.shortcuts import render
# from .utils import search_amazon, search_flipkart

# def home(request):
#     if request.method == 'GET':
#         product_name = request.GET.get('search', None)
#         if product_name:
#             amazon_results = search_amazon(product_name)
#             flipkart_results = search_flipkart(product_name)
#             print(amazon_results)
#             print(flipkart_results)
#             context = {
#                 'amazon_results': amazon_results,
#                 'flipkart_results': flipkart_results,
#             }
#             return render(request, 'product1.html', context)
#     return render(request, 'home1.html')


# def home(request):
#     if request.method == 'GET':
#         product_name = request.GET.get('search', None)
#         if product_name:
#             amazon_results = search_amazon(product_name)
#             flipkart_results = search_flipkart(product_name)
#             context = {
#                 'amazon_results': amazon_results,
#                 'flipkart_results': flipkart_results,
#             }
#             return render(request, 'product.html', context)
#     return render(request, 'home11.html')



#main code
# def home(request):
#     if request.method == 'POST':
#         product_name = request.POST['product_name']
#         amazon_product = search_amazon(product_name)
#         flipkart_product = search_flipkart(product_name)
        
#         if amazon_product or flipkart_product:
#             if amazon_product and flipkart_product:
#                 product = amazon_product if amazon_product['price'] < flipkart_product['price'] else flipkart_product
#             else:
#                 product = amazon_product or flipkart_product
#             return render(request, 'product.html', {'product': product})
    
#     return render(request, 'home11.html')

