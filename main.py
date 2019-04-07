import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

email = 'rodrigo.pitta@gmail.com'
pin = '93922604'
url = 'https://www.puregym.com'


b = webdriver.Firefox()
b.get(url + '/login')
e = b.find_element(value='email').send_keys(email)
p = b.find_element(value='pin').send_keys(pin)
sub = b.find_element(value='login-submit').click()
b.implicitly_wait(10)

mess = b.find_elements_by_class_name('text-center')
num_people = int(re.search(r'\d+', mess[1].text).group())
with open('datapoints.txt', 'a') as f:
    f.write(str(num_people) + "\n")

b.quit()

