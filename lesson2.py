import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

'''
心理健康刷课
'''
class Lesson:
    def __init__(self):
        self.url = "https://moodle.scnu.edu.cn/"
        self.service = Service("./chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.driver.maximize_window()

    def start(self, username, password):
        btn1 = self.driver.find_element(By.XPATH, "/html/body/div[4]/header[1]/div/div/div[2]/div/form/div[2]/a")
        btn1.click()

        btn2 = self.driver.find_element(By.LINK_TEXT, "统一身份认证")
        btn2.click()

        input1 = self.driver.find_element(By.ID, "account")
        input2 = self.driver.find_element(By.ID, "password")
        input1.send_keys(username)
        input2.send_keys(password)

        btn = self.driver.find_element(By.TAG_NAME, "button")
        btn.click()

        btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[3]/span[2]/a")
        btn.click()

        btn = self.driver.find_element(By.LINK_TEXT, "我的课程")
        btn.click()

        btn = self.driver.find_element(By.LINK_TEXT, "大学生心理健康Ⅰ")
        btn.click()

        for i in range(1, 4):
            section = self.driver.find_element(By.ID, "section-" + str(i))
            print("=================================================")
            print("section" + str(i))
            print("=================================================")
            videos = section.find_elements(By.CLASS_NAME, 'activityinstance')
            for video in videos:
                print("=======================")
                print(video.text + "开始播放")
                video.click()
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(4)

                js = "return document.getElementsByTagName('video')[0].duration"
                duration = self.driver.execute_script(js)
                print("该视频持续:" + str(duration))
                time.sleep(2)
                # time.sleep(duration)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])
                print(video.text + "已播放完毕")

if __name__ == '__main__':
    lesson = Lesson()
    lesson.start('<学号>', '<密码>')