from selenium.webdriver.common.keys import Keys
import time
import random

from utils.common import print_time
from utils.mv_conf import ITERATOR, IS_LIVE, SLEEP_TIME_QUICK_SEG, MIN_SLEEP_TIME_MIN, MAX_SLEEP_TIME_MIN
from data.link import URL_VIDEO_IDS
from utils.connect import get_driver


class WhatchVideo:
    ITERATOR = ITERATOR
    SLEEP_TIME_QUICK_SEG = SLEEP_TIME_QUICK_SEG
    IS_LIVE = IS_LIVE

    '''Tiempo en Segundos'''
    MIN_SLEEP_TIME_SEG = MIN_SLEEP_TIME_MIN * 60
    MAX_SLEEP_TIME_SEG = MAX_SLEEP_TIME_MIN * 60

    def __init__(self, driver=False, quick_execution=False):
        if not driver:
            driver = get_driver()
        self.driver = driver
        self.quick_execution = quick_execution
        self.movie_player = False

    def watch_random_video(self):
        random_video = random.randint(0, len(URL_VIDEO_IDS) - 1)
        url_video = URL_VIDEO_IDS[random_video]
        self.driver.get(url_video)
        self.watch_video(is_play=False)

    def watch_video(self, min_sleep_time=MIN_SLEEP_TIME_SEG, max_sleep_time=MAX_SLEEP_TIME_SEG, is_play=True):
        start_time = print_time("Inicio - Viendo video: ")
        time.sleep(5)
        self.movie_player = self.driver.find_element_by_id("movie_player")

        if self.movie_player:
            if not is_play:
                self.movie_player.send_keys(Keys.SPACE)

            if not self.quick_execution:
                sleep_time = random.randint(min_sleep_time, max_sleep_time)
                sleep_time_iterator = random.randint(MIN_SLEEP_TIME_MIN, MAX_SLEEP_TIME_MIN)
                sleep_time_iterator = int(sleep_time_iterator / 4)
                self.do_actions(sleep_time, sleep_time_iterator)
            else:
                self.do_actions(self.SLEEP_TIME_QUICK_SEG, 1)

        end_time = print_time("Fin - Viendo video: ")
        print(f" -> Tiempo de visualización del video: {end_time - start_time}")

    def do_actions(self, sleep_time, sleep_time_iterator):
        sleep_time_base = int(sleep_time / sleep_time_iterator)
        print(f"Se programan {sleep_time_iterator} iteraciones de {sleep_time_base} segundos")
        for i in range(sleep_time_iterator):
            sleep_time = abs(
                random.randint(sleep_time_base - int(sleep_time_base / 6), sleep_time_base + int(sleep_time_base / 5)))
            print(f"--> Iteración {i + 1}/{sleep_time_iterator} con un tiempo de espera de {sleep_time} segundos <--")
            sleep_time -= self.do_action_arrow_right(sleep_time)
            time.sleep(abs(sleep_time))

    def do_action_arrow_right(self, max_sleep_time):
        iterator = random.randint(0, 5)
        if self.IS_LIVE or self.quick_execution:
            iterator = 1
        print(f"Se programan {iterator} acciones Siguiente")
        sleep_total = 0
        while iterator > 0:
            self.movie_player.send_keys(Keys.ARROW_RIGHT)
            sleep = random.randint(3, int((max_sleep_time/iterator) - 10))
            sleep_total += sleep
            time.sleep(sleep)
            iterator -= 1
        return sleep_total


if __name__ == "__main__":
    quick_exe = input("Enter --> para Ejecución Larga; o resto de teclas para Ejecución Corta: ")

    watch_video = False
    try:
        for i in range(ITERATOR):
            print(f"-----> Ejecución nro {i + 1}/{ITERATOR} <-----")
            watch_video = WhatchVideo(False, quick_exe)
            watch_video.watch_random_video()
            watch_video.driver.quit()

            if not quick_exe:
                sleep_time = random.randint(450, 1500)
                print(f"Ejecución pausada {int(sleep_time/60)} minutos")
                time.sleep(sleep_time)
    finally:
        if watch_video:
            watch_video.driver.quit()
