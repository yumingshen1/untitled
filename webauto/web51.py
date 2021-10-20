from selenium import webdriver
import time

driver = webdriver.Chrome(r"/Users/shenyuming/Downloads/webdriver/chromedriver")
driver.get("https://www.51job.com/")
driver.find_element_by_id("kwdselectid").clear()
driver.find_element_by_id("kwdselectid").send_keys("python")
driver.find_element_by_id("work_position_click").click()
#清空已选择的地点
eles = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em[class=on]')
for i in eles:
    i.click()
time.sleep(2)
#重新选择地点
driver.find_element_by_xpath('//*[@id="work_position_click_center_right_list_category_000000_040000"]').click()
time.sleep(2)

driver.find_element_by_id("work_position_click_bottom_save").click()

time.sleep(3)

driver.quit()