from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import random

from utils.connect import get_driver, connect
from utils.common import FILE_NAME_COMMENT_TEXT, FILE_NAME_LINK_TO_COMMENT


class WriteComment:

    def __init__(self, driver=False, comment_description=False, video_links=False):
        if not driver:
            driver = get_driver()
        self.driver = driver
        self.comment_description = comment_description
        self.video_links = video_links

    def read_comment_file(self):
        file_comment = open(FILE_NAME_COMMENT_TEXT, "r", encoding="utf-8")
        self.comment_description = file_comment.readlines()
        file_comment.close()

    def read_video_link(self):
        file_links = open(FILE_NAME_LINK_TO_COMMENT, "r", encoding="utf-8")
        self.video_links = list(file_links)
        file_links.close()

    def do_arrow_down(self, body, iterator):
        while iterator > 0:
            body.send_keys(Keys.ARROW_DOWN)
            iterator -= 1
            if iterator % 2 == 0:
                time.sleep(1)

    def find_placeholder(self):
        try:
            placeholder = self.driver.find_element_by_id("simplebox-placeholder")
            return placeholder
        except Exception:
            pass
        return False

    def write_comment_on_video(self, video_link):
        connect(self.driver, with_sing_in=False, url_base=video_link)
        time.sleep(3)

        # self.driver.execute_script("window.scrollTo(0, 800);")
        body = self.driver.find_element_by_xpath("/html")
        self.do_arrow_down(body, 13)
        placeholder = self.find_placeholder()
        if not placeholder:
            self.do_arrow_down(body, 7)
            placeholder = self.find_placeholder()

        if placeholder:
            print("Escribiendo comentario ...")
            placeholder.click()

            # Seleccionar el input ok
            comment_input = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, "contenteditable-root")))
            comment_input.send_keys(self.comment_description)

            # Click en el boton Aceptar
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "submit-button")))
            self.driver.find_element_by_id("submit-button").click()
            print(f"Comentario escrito OK en {video_link}")
            time.sleep(3)
        else:
            print(f"No se encontro sección Comentarios en --> {video_link}")

    def write_comment(self, user_name, user_password):
        try:
            print("Abriendo video ...")
            connect(self.driver, with_sing_in=True, user_name=user_name, user_password=user_password)
            time.sleep(1)

            for video_link in self.video_links:
                self.write_comment_on_video(video_link)

                sleep_time_to_comment = random.randint(10, 20)
                print(f"Esperando {sleep_time_to_comment} segundos")
                time.sleep(sleep_time_to_comment)

        finally:
            self.driver.quit()


if __name__ == "__main__":
    # user_name = input("Usuario para conexión; o Enter --> para continuar: ")
    user_password = input("Contraseña para conexión; o Enter --> para continuar: ")
    user_name = 'micanal1119'

    writer = WriteComment()
    writer.read_comment_file()
    writer.read_video_link()
    writer.write_comment(user_name, user_password)
