import datetime



class Base():
    def __init__(self, driver):
        self.driver = driver

    #Method get_current_url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    #Method assert words
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word" + " " + value_word)

    # Method assert elements
    def assert_elements(self, word, result):
        value_word = word.text
        result_word = result.text
        assert value_word == result_word
        print("Good value word")

    # Method screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\Dench\\Desktop\\Stepik\\homework_itog\\screen\\' + name_screenshot)

    # Method assert url
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Correct url opened")
