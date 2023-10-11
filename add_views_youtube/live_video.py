from selenium.webdriver.common.keys import Keys
import time
import random

from utils.common import print_time
from utils.mv_conf import LIVE_ITERATOR, LIVE_URL_VIDEO, LIVE_MIN_SLEEP_TIME_MIN, LIVE_MAX_SLEEP_TIME_MIN
from utils.connect import get_driver


class LiveVideo:
    LIVE_URL_VIDEO = LIVE_URL_VIDEO

    '''Tiempo en Minutos'''
    MIN_SLEEP_TIME_MIN = LIVE_MIN_SLEEP_TIME_MIN
    MAX_SLEEP_TIME_MIN = LIVE_MAX_SLEEP_TIME_MIN

    MIN_SLEEP_TIME_SEG = MIN_SLEEP_TIME_MIN * 60
    MAX_SLEEP_TIME_SEG = MAX_SLEEP_TIME_MIN * 60

    def __init__(self, driver=False):
        if not driver:
            driver = get_driver()
        self.driver = driver

    def do_actions(self, sleep_time, sleep_time_iterator, movie_player):
        sleep_time_base = int(sleep_time / sleep_time_iterator)
        for i in range(sleep_time_iterator):
            sleep_time = abs(random.randint(sleep_time_base - 45, sleep_time_base + 45))
            print(f"--> Iteración {i + 1}/{sleep_time_iterator} con un tiempo de espera de {sleep_time} segundos <--")
            movie_player.send_keys(Keys.ARROW_RIGHT)
            time.sleep(sleep_time)

    def watch_video(self, min_sleep_time=MIN_SLEEP_TIME_SEG, max_sleep_time=MAX_SLEEP_TIME_SEG, is_play=True):
        start_time = print_time("Inicio - Viendo video: ")

        time.sleep(5)
        movie_player = self.driver.find_element_by_id("movie_player")

        if movie_player:
            movie_player.send_keys(Keys.SPACE)

            sleep_time = random.randint(min_sleep_time, max_sleep_time)
            sleep_time_iterator = random.randint(self.MIN_SLEEP_TIME_MIN, self.MAX_SLEEP_TIME_MIN)
            self.do_actions(sleep_time, sleep_time_iterator, movie_player)

        end_time = print_time("Fin - Viendo video: ")
        print(f" -> Tiempo de visualización del video: {end_time - start_time}")

    def watch_video_iterator(self):
        url_video = LIVE_URL_VIDEO
        self.driver.get(url_video)
        self.watch_video(False)


if __name__ == "__main__":

    try:
        for i in range(LIVE_ITERATOR):
            print(f"-----> Ejecución nro {i + 1}/{LIVE_ITERATOR} <-----")
            watch_video = LiveVideo(False)
            watch_video.watch_video_iterator()
            watch_video.driver.quit()
    finally:
        if watch_video:
            watch_video.driver.quit()
