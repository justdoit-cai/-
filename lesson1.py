import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

'''
四史刷课
'''
d = {
    1: '一',
    2: '二',
    3: '三',
    4: '四',
    5: '五',
    6: '六',
    7: '七',
    8: '八',
    9: '九',
    10: '十',
}
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

        btn = self.driver.find_element(By.LINK_TEXT, "四史")
        btn.click()
        time.sleep(2)
        for i in range(1, 11):
            print("=================================================")
            print(f"第{d.get(i)}讲")
            section = self.driver.find_element(By.LINK_TEXT, f"第{d.get(i)}讲")
            section.click()
            videos = self.driver.find_elements(By.CLASS_NAME, "activityinstance")
            num = len(videos)
            for j in range(0, num):
                # 切换页面后需要重新加载页面元素
                videos = self.driver.find_elements(By.CLASS_NAME, "activityinstance")
                video = videos[j]
                if '【视频】' in video.text:
                    print(video.text)
                    video.click()
                    time.sleep(2)
                    # 这里有嵌套两个iframe
                    iframe1 = self.driver.find_element(By.TAG_NAME, 'iframe')
                    self.driver.switch_to.frame(iframe1)
                    iframe2 = self.driver.find_element(By.TAG_NAME, 'iframe')
                    self.driver.switch_to.frame(iframe2)
                    btn = self.driver.find_element(By.CLASS_NAME, 'h5p-splash-play-icon')
                    btn.click()
                    js = "return document.getElementsByTagName('video')[0].duration"
                    duration = self.driver.execute_script(js)
                    print(f"该视频持续:{str(duration)}秒")
                    print("开始观看视频ing...")
                    time.sleep(duration)
                    print("观看视频结束!")
                    # 这里直接切换到根页面，不然需要切换两次parent_frame
                    self.driver.switch_to.default_content()
                    time.sleep(2)
                    self.driver.back()


if __name__ == '__main__':
    lesson = Lesson()
    lesson.start('<学号>', '<密码>')
