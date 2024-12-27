'''
from  time import sleep
from playwright.sync_api import sync_playwright
import os
import traceback
import json

# Create profile directory if it doesn't exist
profile_dir = ''
#os.makedirs(profile_dir, exist_ok=True)

# Đọc dữ liệu từ tệp JSON
with open('colors_data.json', 'r', encoding='utf-8') as json_file:
    dataJson = json.load(json_file)

keys = ['Red','Grey','Blue','Brown','Yellow','Green','Purple']
try:
  with sync_playwright() as p:
    # Launch the browser with a persistent context
    browser = p.chromium.launch_persistent_context(
        user_data_dir=profile_dir,  # Path to the profile directory
        headless=True,  # Run in headless mode
        slow_mo=500  # Slow down actions by 500ms
    )
'''
from lxml import html
from unidecode import unidecode
import time
from playwright.sync_api import sync_playwright
import os
import json 
# Tạo thư mục profile nếu chưa tồn tại
profile_dir = 'Profile'
#os.makedirs(profile_dir, exist_ok=True)
linkweb = 'https://shopsuatramanh.com/'
with open ('file1.json', 'r', encoding='utf-8') as file:
  data = json.load(file)
#for category in data:
#    for key, value in category.items():
#       print(str(key) + ' \n\n')#+ str(value)
        #n=input('zz')
with sync_playwright() as p:
    # Khởi động trình duyệt với context trống
    browser = p.chromium.launch_persistent_context(
        user_data_dir=profile_dir,  # Đường dẫn đến thư mục profile
        headless=False, # Chạy ở chế độ không ẩn
        slow_mo=700
    )
    '''
    cookies=input('Do you want clear cookies? Y/N')
    if cookies.lower() == "y":
        # Xóa các cookie và bộ nhớ cache
        browser.clear_cookies()
        browser.clear_permissions()
        browser.set_geolocation({'longitude': 0, 'latitude': 0})  
        print('clear cookies')    
    '''
    # Mở một trang mới với User-Agent
    page = browser.new_page()
    #page.goto('http://apfoodvn.com/admin')
    #http://apfoodvn.com/admin/product-list/add/san-pham
    page.goto('http://apfoodvn.com/admin/product-cat/add/san-pham')
    #print(page.content())
    
    #sp
    linkSP = []
    pagingFlag = False
    for category in data:
        for key, value in category.items():
            #print(str(key).strip() + '\n ')
            for subcategory in value:
                for key2, value2 in subcategory.items():
                    #print( str(key2).strip() + '\n  ')
                    if value2:
                        for subcategory_ in value2:
                          print(subcategory_[1])
                          page.goto(subcategory_[1], timeout=60000)
                          while True:
                            htmlContent = page.content()
                            tree = html.fromstring(htmlContent)
                            
                            checkBox = tree.xpath("//div[@class='box-product']")
                            if not checkBox:
                                break
                            else: 
                                print('product')
                                item_products = tree.xpath("//div[@class='item-product']")
                                if item_products:
                                    num_item_products = len(item_products)
                                    arrProductlink = []
                                    for num_item_product in range(1, num_item_products + 1):
                                        productLink = tree.xpath(f"(//div[@class='item-product']/div[contains(@class, 'image')]/a)[{num_item_product}]")[0]
                                        priceProduct = tree.xpath(f"(//div[@class='item-product']/div[@class='content-product']/div[@class=' price-product']/span)[{num_item_product}]")[0].text_content()
                                        if  productLink is not None and priceProduct is not None:
                                            print(productLink.get('href') + '\n' + priceProduct)
                                            linkEachProduct = linkweb + productLink.get('href')
                                            arrProductlink.append(linkEachProduct)
                                        else:
                                            print('Problem')
                                    
                                    for Productlink in arrProductlink:
                                        page.goto(Productlink, timeout=60000)
                                        htmlne = page.content()
                                        tree2 = html.fromstring(htmlne)
                                        imagep = tree2.xpath('//figure/img')
                                        imageLink = linkweb + imagep[0].get('src') 
                                        print(imageLink)
                                        titleProduct = tree2.xpath("//h2[@class='pro-detail-desc-title']")
                                        
                                        
                                        n=input('Linkne')
                            checkPaging = tree.xpath("//div[@class='pagination-home']")
                            if  checkPaging:
                                print('Paging')
                                nextPage = tree.xpath(f"//a[text()='Next']")
                                if nextPage:
                                    next_page_link = nextPage[0].get('href')
                                    page.goto(next_page_link, timeout=60000)
                                    
                                    n=input('next')
                                else:
                                    break
                            else:
                                print('not Paging')
                                break
                            
                    
    
    '''
    #ds2
    for category in data:
        for key, value in category.items():
            
            for subcategory in value:
                for key2, value2 in subcategory.items():
                    
                    page.fill("//input[@id='namevi']", str(key2).strip())
                    print(unidecode(str(key2).strip()).replace(' ', '-').lower())
                    linkey = unidecode(str(key2).strip()).replace(' ', '-').lower()
                    page.fill("//input[@id='slugvi']", linkey)
                    
                    
                    page.wait_for_selector("//span[@class='selection']")
                    page.click("//span[@class='selection']")
                    
                    xpath_selector = "//ul[@class='select2-results__options']/li"
                    
                    
                    #//span[@class='selection']
                    #//ul[@class='select2-results__options']/li
                    
                    page.wait_for_selector(xpath_selector)

                    # Lấy tất cả các phần tử phù hợp với XPath
                    options = page.query_selector_all(xpath_selector)

                    # Click vào từng phần tử
                    for option in options:
                        if option.inner_text() == str(key).strip():
                            
                          option.click()  # Click vào phần tử
                          print(option.inner_text())
                    page.click("//button[@class='btn btn-primary submit-check waves-effect']")
                    
                    while True:
                          current_url = page.url
                          if current_url == 'http://apfoodvn.com/admin/product-cat/man/san-pham?page=1':
                            break
                          time.sleep(0.7)
                    page.goto("http://apfoodvn.com/admin/product-cat/add/san-pham", timeout=60000)
    #ds1
    for category in data:
        for key, value in category.items():
            page.fill("//input[@id='namevi']", str(key).strip())
            print(unidecode(str(key).strip()).replace(' ', '-').lower())
            linkey = unidecode(str(key).strip()).replace(' ', '-').lower()
            page.fill("//input[@id='slugvi']", linkey)
            
            page.click("//button[@class='btn btn-primary submit-check waves-effect']")
            while True:
                  current_url = page.url
                  if current_url == 'http://apfoodvn.com/admin/product-list/man/san-pham?page=1':
                    break
                  time.sleep(0.7)
            page.goto("http://apfoodvn.com/admin/product-list/add/san-pham", timeout=60000)
    '''
    #time.sleep(200)
    # Đóng trình duyệt
    browser.close()

#'http://apfoodvn.com/admin/product-list/man/san-pham?page=1'
#http://apfoodvn.com/admin/product-cat/man/san-pham?page=1

