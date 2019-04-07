import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import sched, time
from datetime import datetime


s = sched.scheduler(time.time, time.sleep)
def run():
    print("Executing...")
    email = 'rodrigo.pitta@gmail.com'
    pin = '93922604'
    url = 'https://www.puregym.com'


    
    options = Options()
    options.add_argument("--headless")
    b = webdriver.Firefox(options=options)
    b.get(url + '/login')
    e = b.find_element(value='email').send_keys(email)
    p = b.find_element(value='pin').send_keys(pin)
    sub = b.find_element(value='login-submit').click()
    b.implicitly_wait(10)

    mess = b.find_elements_by_class_name('text-center')
    num_people = int(re.search(r'\d+', mess[1].text).group())
    with open('datapoints.txt', 'a') as f:
        f.write(str(datetime.now()) + ", " + str(num_people) + "\n")

    b.quit()
    print("Done.")
    s.enter(60 * 5, 1, run)

s.enter(1, 1, run)
s.run()



