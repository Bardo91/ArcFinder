#
#   WebScraper
#
# I wrote this code for fun, do whatever you want with it.
# 
#

from sys import dont_write_bytecode
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from geopy.geocoders import *
import time

from ArcFinder import House


class DriverAltamira:
    def __init__(self):
        pass


    def scrap(self):
        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

        driver.get("https://www.altamirainmuebles.com/")
        buscador = driver.find_element_by_id("cajaLocalizacion").find_element_by_id("buscadorLocalizacion")
        buscador.send_keys("Sevilla")
        buscador.send_keys(Keys.RETURN)

        time.sleep(5)
        for i in range(100):
            boton_mas = driver.find_elements_by_class_name("vermas")
            if len(boton_mas) == 0:
                break
            else:
                boton_mas[0].find_element_by_id("verMasSubmit").send_keys(Keys.RETURN)

        results = driver.find_element_by_id("resultList").find_elements_by_class_name("minificha   ")

        subastasDB = []

        for res in results:
            info = House()

            webInfo = res.find_element_by_class_name("info")
            webFoto = res.find_element_by_class_name("foto").find_element_by_tag_name("img").get_attribute("src")

            info.direccion = webInfo.find_element_by_tag_name("a").text
            info.enlace = webInfo.find_element_by_tag_name("a").get_attribute("href")
            info.photo_url = webFoto
            subastasDB.append(info)

        return subastasDB

