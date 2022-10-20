from gravel_ import gravel
from log_ import log
import time

from selectors import SELECTORS


class App:
    def __init__(self) -> None:
        self.gravel = gravel()
        self.authFile = './assets/auth-list.txt'
        self.urlsList = './assets/data.txt'
        self.currentAuth = 0
        self.currentListIndex = 0

    def goOnGo(self):
        linkList = self.getDataLinksList()
        for url in linkList[self.currentListIndex::]:
            if url == 'waqas':
                continue
            log('goOnGo => ', url)
            self.currentListIndex += 1
            self.gravel.driver.get(self.__filter__(url))
            try:
                self.gravel.wait4element(SELECTORS.get('a_83929'))
            except:
                log('Download Option Not Available Yet!')
                continue
            try:
                action = self.gravel.chain()
                action.move_to_element(
                    self.gravel.getElement('a_93823')).perform()
                action.move_to_element(
                    self.gravel.getElement('a_83929')).click().perform()
                self.gravel.wait4element(SELECTORS.get('a_19384'))
                final_ = str(self.gravel.getElement(
                    'a_92382').get_attribute('href'))
                log(self.currentListIndex + ' - find => ', final_)
            except Exception as e:
                log('error: ', e)
                log("error on => " + url)
                return self.currentListIndex

    def login(self):
        log('login.... in progresss')
        self.gravel.driver.get('https://samfw.com/login')
        try:
            self.gravel.getElement('a_18392').click()
        except Exception as e:
            log(e)
        auth_list = self.authList()
        if self.currentAuth >= len(auth_list):
            self.currentAuth = 0
        email, password = auth_list[self.currentAuth].replace(
            '\n', '').split(',')
        self.currentAuth += 1
        self.gravel.getElement('a_43232').send_keys(email)
        pswd = self.gravel.getElement('a_68443')
        pswd.send_keys(password)
        pswd.send_keys(self.gravel.keys.RETURN)
        log('login.... in progresss complete')
        time.sleep(2)

    def __filter__(self, str_):
        return str_.replace('\n', '').replace('\r', '')

    def getDataLinksList(self):
        with open(self.urlsList, 'r', encoding='utf-8') as file:
            return file.readlines()

    def authList(self):
        with open(self.authFile, 'r', encoding='utf-8') as file:
            return file.readlines()

    def close(self):
        self.gravel.close()


if __name__ == '__main__':
    app = App()
    app.login()
    app.goOnGo()
    app.close()
