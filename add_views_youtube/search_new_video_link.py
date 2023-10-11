import time

from utils.common import FILE_NAME_NEW_LINK, URL_SEARCH_QUERY, FILE_NAME_CANAL_LINK_TO_EXPLORE
from utils.connect import get_driver, connect

SEARCH_QUERY_TEXT = 'musica para relajar'
URL_SEARCH_BASE = 'https://www.youtube.com/channel/UCwA01HsEJpPA1oZv8n3w43w/videos'


def search_new_link_iterator(canal_links=False):
    print("Inicio Ejecución")
    driver = get_driver()
    if not canal_links:
        canal_links = read_canal_link()
    try:
        for canal in canal_links:
            search_new_link(canal, driver)
            time.sleep(3)
    finally:
        driver.quit()
    print("Fin Ejecución")


def search_new_link(url_base, driver):
    connect(driver, with_sing_in=False, url_base=url_base)
    time.sleep(7)

    # last_height = driver.execute_script("return document.body.scrollTop")
    # print(last_height)

    driver.execute_script("window.scrollTo(0, 2000);")
    time.sleep(4)

    # Seleccionar lista de videos (link)
    new_link = []
    elems = driver.find_elements_by_id("video-title")
    elems = elems[:10]
    for elem in elems:
        link = elem.get_attribute('href')
        if link:
            new_link.append(link)

    new_link.append('')
    write_file(new_link)


def write_file(new_link):
    comment_video_txt = open(FILE_NAME_NEW_LINK, 'a')
    for link in new_link:
        link += '\n'
        comment_video_txt.write(link)
    comment_video_txt.close()


def read_canal_link():
    file_links = open(FILE_NAME_CANAL_LINK_TO_EXPLORE, "r", encoding="utf-8")
    canal_links = list(file_links)
    file_links.close()
    return canal_links


if __name__ == "__main__":
    url_base = False
    # query_type = input("Escriba el tipo de búsqueda (1 - Por texto); o (2 - Por link): ")
    query_type = '2'

    if query_type == str(1):
        search_query = input("Escriba el nombre de la búsqueda que desea: ")
        if not search_query:
            search_query = SEARCH_QUERY_TEXT
        url_base = (URL_SEARCH_QUERY + search_query)
    elif query_type == str(2):
        url_base = input("Escriba link: ")
        if not url_base:
            url_base = URL_SEARCH_BASE

    if url_base:
        search_new_link_iterator([url_base])

    if query_type == str(3):
        search_new_link_iterator()
