from selenium.webdriver.common.keys import Keys
import time
import random

from utils.common import CANAL_NAME, CANAL_LINK, EMAIL_DAYANA1989
from utils.connect import get_driver, connect
from utils.mv_conf import ITERATOR
from data.link_search import SEARCH_URLS, CANAL_URLS
from watch_video import WhatchVideo


class SearchCanal:

    # def _sing_on_youtube(self):
    #     if self.user_password:
    #         if not self.user_name:
    #             self.user_name = EMAIL_DAYANA1989
    #         connect(self.driver, True, False, self.user_name, self.user_password)
    #
    def __init__(self, driver=False, search_type=False, quick_execution=False, user=False, password=False):
        if not driver:
            driver = get_driver()
        self.driver = driver
        self.search_type = search_type
        self.quick_execution = quick_execution
        self.user_name = user
        self.user_password = password
        # self._sing_on_youtube()

    def connect(self, right_canal=False, with_sing_in=False):
        if right_canal:
            url_base = CANAL_LINK
        else:
            url_id = random.randint(0, len(SEARCH_URLS) - 1)
            url_base = SEARCH_URLS[url_id]

        connect(self.driver, with_sing_in=with_sing_in, url_base=url_base)
        time.sleep(4)
        return url_base

    def _check_search_data(self, canal_name, video):
        found = False
        if canal_name in CANAL_NAME:
            video.click()
            found = True

            print("Canal encontrado OK.")
            sleep_load = random.randint(2, 5)
            time.sleep(sleep_load)
        return found

    def search_canal_or_video(self, is_my_canal):
        iterator = 1
        found_canal = False
        found_video = False
        body = self.driver.find_element_by_xpath("/html/body")
        while iterator <= 20 and (not found_canal and not found_video):
            iterator += 1
            is_video = True
            row_ids = self.driver.find_elements_by_id("dismissible")
            if not row_ids:
                is_video = False
                row_ids = self.driver.find_elements_by_id("text-container")

            for row_id in row_ids:
                if is_video:
                    video = row_id.find_element_by_id('thumbnail')
                    canal_names = row_id.find_elements_by_id('text-container')
                    for canal in canal_names:
                        canal_name = CANAL_NAME[0] if is_my_canal else ''
                        if not canal_name and canal.text:
                            canal_name = canal.text
                        found_video = self._check_search_data(canal_name, video)
                        if found_video:
                            break
                else:
                    link = row_id
                    canal_name = row_id.text
                    found_canal = self._check_search_data(canal_name, link)

                if found_canal or found_video:
                    break

            if not found_canal and not found_video:
                for i in range(15):
                    body.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)
        return found_canal, found_video

    def open_random_video(self):
        video_ids = self.driver.find_elements_by_id("details")
        if video_ids:
            open_id = random.randint(0, len(video_ids) - 1)
            video_ids[open_id].click()
    #
    # def connect_direct_to_canal(self, with_sing_in=False):
    #     self.connect(True, with_sing_in)
    #
    # def connect_direct_to_canal_and_open_video(self, with_sing_in=False):
    #     self.connect_direct_to_canal(with_sing_in)
    #     self.open_random_video()
    #     watch_video = WhatchVideo(self.driver, self.quick_execution)
    #     watch_video.watch_video(True)

    def is_my_canal(self, url_base):
        is_my_canal = True if url_base in CANAL_URLS else False
        return is_my_canal

    def connect_by_search_and_open_video(self, with_sing_in=False):
        url_base = self.connect(False, with_sing_in)
        found_canal = self.is_my_canal(url_base)
        found_video = False
        if not found_canal:
            found_canal, found_video = self.search_canal_or_video(found_canal)

        if found_canal and not found_video:
            self.open_random_video()
        if found_canal or found_video:
            watch_video = WhatchVideo(self.driver, self.quick_execution)
            watch_video.watch_video()


if __name__ == "__main__":
    # user_name = input("Usuario para conexión; o Enter --> para continuar: ")
    # user_password = input("Contraseña para conexión; o Enter --> para continuar: ")
    user_name = False
    user_password = False

    # exe_type = input("Enter --> para Ejecución individual; o Resto de teclas para Multihilos: ")
    quick_exe = input("Enter --> para Ejecución Larga; o resto de teclas para Ejecución Corta: ")
    # search_type = input("Enter -> Busqueda; o Resto de teclas para Abrir Canal directamente: ")
    search_canal = False
    try:

        for i in range(ITERATOR):
            print(f"---> Ejecución  {i + 1}/{ITERATOR} <---")
            search_canal = SearchCanal(quick_execution=quick_exe, user=user_name, password=user_password)
            search_canal.connect_by_search_and_open_video()
            search_canal.driver.quit()

            # if self.search_type:
            #     self.connect_direct_to_canal_and_open_video()
            # else:
            if not quick_exe:
                sleep_time = random.randint(300, 2000)
                print(f"Ejecución pausada {int(sleep_time / 60)} minutos")
                time.sleep(sleep_time)
    finally:
        if search_canal:
            search_canal.driver.quit()

