import json

# Đọc dữ liệu từ tệp JSON
with open('colors_data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Lấy danh sách màu cho "Grey"
grey_colors = data.get("Grey")

if grey_colors:
    # Lấy màu đầu tiên
    first_grey_color = grey_colors[0]
    color_code = first_grey_color[0]
    color_name = first_grey_color[1]

    print(f"Mã màu đầu tiên của 'Grey': {color_code}, Tên màu: {color_name}")
else:
    print("Không tìm thấy màu 'Grey'.")
'''
import json
import requests
from lxml import html
response = requests.get('https://nhadepcuaban.com/cay-mau-pro/')
n=input(response.status_code)


tree = html.fromstring(response.content)

data = {}

for i in range(1,9):
  subject = tree.xpath(f'//li[@id="tab-color{i}"]')
  subject_text = subject[0].xpath('.//text()')
  cleaned_text1 = [text.strip() for text in subject_text if text.strip()]
  print(cleaned_text1[0])
  tab_color = tree.xpath(f'//div[@id="tab_color{i}"]')
  colors = tab_color[0].xpath('.//div[@class="col-4 col-md-auto color-item"]/div')
  color_arr =[]
  for color in colors:
    color_code = color.get('color_value')
    print(color_code)
    all_text = color.xpath('.//text()')
    cleaned_text2 = [text.strip() for text in all_text if text.strip()]
    print(cleaned_text2[0])
    color_arr.append([color_code, cleaned_text2[0]])
  data[cleaned_text1[0]] = color_arr

with open('colors_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)





import requests
from lxml import html
import json

# Gửi yêu cầu GET đến URL
response = requests.get('https://nhadepcuaban.com/cay-mau-pro/')

# Kiểm tra mã trạng thái
print("Mã trạng thái:", response.status_code)

# Phân tích cú pháp HTML
tree = html.fromstring(response.content)

# Tạo một từ điển để lưu trữ dữ liệu
data = {}

# Lặp qua các tab màu
for i in range(1, 9):
    subject = tree.xpath(f'//li[@id="tab-color{i}"]')
    if subject:
        subject_text = subject[0].xpath('.//text()')
        cleaned_text1 = [text.strip() for text in subject_text if text.strip()]
        
        if cleaned_text1:  # Kiểm tra nếu cleaned_text1 không rỗng
            print(cleaned_text1[0])
            tab_color = tree.xpath(f'//div[@id="tab_color{i}"]')
            if tab_color:
                colors = tab_color[0].xpath('.//div[@class="col-4 col-md-auto color-item"]/div')
                
                # Khởi tạo danh sách để lưu trữ các màu
                color_list = []
                
                for color in colors:
                    color_code = color.get('color_value')
                    if color_code:  # Kiểm tra nếu color_code không rỗng
                        print(color_code)
                        all_text = color.xpath('.//text()')
                        cleaned_text2 = [text.strip() for text in all_text if text.strip()]
                        
                        # Lưu vào danh sách
                        for text in cleaned_text2:
                            color_list.append([color_code, text])

                # Lưu vào từ điển với cleaned_text1[0] là khóa
                data[cleaned_text1[0]] = color_list

# Lưu dữ liệu vào tệp JSON
with open('colors_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print("Dữ liệu đã được lưu vào tệp colors_data.json")

import requests
from lxml import html
import json

# Gửi yêu cầu GET đến URL
response = requests.get('https://nhadepcuaban.com/cay-mau-pro/')

# Kiểm tra mã trạng thái
print("Mã trạng thái:", response.status_code)

# Phân tích cú pháp HTML
tree = html.fromstring(response.content)

# Tạo một từ điển để lưu trữ dữ liệu
data = {}

# Lặp qua các tab màu
for i in range(1, 9):
    subject = tree.xpath(f'//li[@id="tab-color{i}"]')
    if subject:
        subject_text = subject[0].xpath('.//text()')
        cleaned_text1 = [text.strip() for text in subject_text if text.strip()]
        
        if cleaned_text1:  # Kiểm tra nếu cleaned_text1 không rỗng
            print(cleaned_text1[0])
            tab_color = tree.xpath(f'//div[@id="tab_color{i}"]')
            if tab_color:
                colors = tab_color[0].xpath('.//div[@class="col-4 col-md-auto color-item"]/div')
                
                # Khởi tạo danh sách để lưu trữ các màu
                color_list = []
                
                for color in colors:
                    color_code = color.get('color_value')
                    if color_code:  # Kiểm tra nếu color_code không rỗng
                        print(color_code)
                        all_text = color.xpath('.//text()')
                        cleaned_text2 = [text.strip() for text in all_text if text.strip()]
                        
                        # Lưu vào danh sách
                        for text in cleaned_text2:
                            color_list.append([color_code, text])

                # Lưu vào từ điển với cleaned_text1[0] là khóa
                data[cleaned_text1[0]] = color_list

# In ra dữ liệu dưới dạng JSON
json_data = json.dumps(data, ensure_ascii=False, indent=4)
print(json_data)


import requests
from lxml import html
response = requests.get('https://nhadepcuaban.com/cay-mau-pro/')
n=input(response.status_code)


tree = html.fromstring(response.content)

tcolor = 'tab_color'

for i in range(1,9):
  subject = tree.xpath(f'//li[@id="tab-color{i}"]')
  subject_text = subject[0].xpath('.//text()')
  cleaned_text = [text.strip() for text in subject_text if text.strip()]
  print(cleaned_text[0])
  tab_color = tree.xpath(f'//div[@id="tab_color{i}"]')
  colors = tab_color[0].xpath('.//div[@class="col-4 col-md-auto color-item"]/div')
  for color in colors:
    color_code = color.get('color_value')
    print(color_code)
    all_text = color.xpath('.//text()')
    cleaned_text = [text.strip() for text in all_text if text.strip()]
    print(cleaned_text[0])
    
    
'''
#with open ('filex.html', 'w', encoding='utf8') as file:
#  file.write(str(response.content))