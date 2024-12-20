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

    # Create a new page in the persistent context
    page = browser.new_page()
    #page.goto("http:///xaydungdangtuan_1674824/admin", timeout=60000)
    page.goto("http:////admin/news/add/ma-mau-quoc-te", timeout=60000)
    #sleep(1000)
    #browser.close()
    #n=input('ZZZZZZZZZZZZZZZ')
    
    i=169
    for key in keys:
      colors = dataJson.get(key)
      countColors = len(colors)
      #n=input(countColors)
      for color in colors:
        i+=1
        page.click("xpath=(//a[@class='menu-link menu-name menu-toggle'])[2]")
        page.click("xpath=(//span[@role='combobox'])[1]") 
        # Đọc dữ liệu từ tệp JSON
        if color:
          page.click(f"xpath=//li[contains(text(), '{key}')]")
          #Pastel,Red,Grey,Blue,Brown,Yellow,Green,Purple 
          page.fill('#namevi', f'{color[1]}')
          page.fill('#color', f'{color[0]}')
          page.fill('#numb', f'{i}')
        page.click("xpath=(//button[@type='submit'])[1]")
        ##f5f5f5
        #a href="news/man/ma-mau-quoc-te"i
        #(//span[@role='combobox'])[1]
        #(//ul[@class='select2-results__options'])[1]
        #(//button[@type='submit'])[1]
        while True:
          current_url = page.url
          if current_url == 'http:///xaydungdangtuan_1674824/admin/news/man/ma-mau-quoc-te?page=1':
            break
          sleep(0.7)
        page.goto("http:///xaydungdangtuan_1674824/admin/news/add/ma-mau-quoc-te", timeout=60000)

        #n=input('toine!!')

    '''
    # Fill in the input fields
    page.fill('#username', '')  # Replace with your username
    page.fill('#password', '')  # Replace with your password

    # Check the "remember me" checkbox
    page.check('input[type="checkbox"]')

    # Click the submit button
    page.click('button[type="submit"]')

    n=input('stopppp!!!')
    # Your further actions here
    content = page.content()
    print(content)
    '''
    # Close the browser after you're done
    browser.close()
except Exception as e:
  print(e)
  traceback.print_exc()
'''
import time
from playwright.sync_api import sync_playwright
import os

# Tạo thư mục profile nếu chưa tồn tại
profile_dir = ''
os.makedirs(profile_dir, exist_ok=True)

with sync_playwright() as p:
    # Khởi động trình duyệt với context trống
    browser = p.chromium.launch(
        user_data_dir=profile_dir,  # Đường dẫn đến thư mục profile
        headless=False, # Chạy ở chế độ không ẩn
        slow_mo=500
    )
    
    cookies=input('Do you want clear cookies? Y/N')
    if cookies.lower() == "y":
        # Xóa các cookie và bộ nhớ cache
        browser.clear_cookies()
        browser.clear_permissions()
        browser.set_geolocation({'longitude': 0, 'latitude': 0})  
        print('clear cookies')    
    
    # Mở một trang mới với User-Agent
    page = browser.new_page()
    page.goto('http:///xaydungdangtuan_1674824/admin')
    print(page.content())
    n=input('hihi')
    time.sleep(200)
    # Đóng trình duyệt
    browser.close()

'''
