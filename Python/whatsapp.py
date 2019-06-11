import time
try:
    from selenium import webdriver
    from  selenium.webdriver.common.keys import Keys
except:
    print("Please install selenium library for this program to work and also download chromedrivers for the selenium library")
    input("Press enter to exit")
    exit()

message='%'.join(input().split())
number=input("Enter number to which of reciver with country code \t+")
driver=webdriver.Chrome()
url='https://web.whatsapp.com/send?phone='+number+'&text='+message+"&source=&data="
driver.get(url)
while True:
    time.sleep(10)
    if driver.current_url=="https://web.whatsapp.com/":
        time.sleep(10)
        send=driver.find_element_by_css_selector(".hnQHL")
        send.click()
    else:
        print('please scan qr code from your whatsapp')
