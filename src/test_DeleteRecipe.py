# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

import pathlib
file_path= str(pathlib.Path(__file__).parent.absolute())

class DeleteRecipe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_delete_recipe(self):
        driver = self.driver
        driver.get("http://localhost:3000/")
        driver.find_element("id","new-recipe-btn").click()
        time.sleep(1)
        driver.find_element("id","input-titulo").click()
        driver.find_element("id","input-titulo").clear()
        driver.find_element("id","input-titulo").send_keys("Receta de Puding de arroz con leche Thermomix")
        driver.find_element("name","file").clear()
        driver.find_element("name","file").send_keys(file_path+"\\imagenTest.jpg")
        driver.find_element("id","input-ingrediente").click()
        driver.find_element("id","input-ingrediente").clear()
        driver.find_element("id","input-ingrediente").send_keys("100 gramos de Arroz")
        driver.find_element("id","cargar-ingrediente-btn").click()
        driver.find_element("id","input-ingrediente").click()
        driver.find_element("id","input-ingrediente").clear()
        driver.find_element("id","input-ingrediente").send_keys(u"200 gramos de Azúcar (1 taza)")
        driver.find_element("id","cargar-ingrediente-btn").click()
        driver.find_element("id","input-preparacion").click()
        driver.find_element("id","input-preparacion").clear()
        driver.find_element("id","input-preparacion").send_keys(u"El primer paso para preparar el pudin con thermomix será triturar el arroz. Para ello, programa con velocidad 5-7-9, ve aumentando de forma progresiva hasta que el arroz quede completamente pulverizado. Reserva.")
        driver.find_element("id","cargar-preparacion-btn").click()
        driver.find_element("id","input-preparacion").click()
        driver.find_element("id","input-preparacion").clear()
        driver.find_element("id","input-preparacion").send_keys(u"Aparte, pulveriza también el azúcar junto con la cáscara de limón. Primero el azúcar programando la thermomix con velocidad 5-7-9, aumentando progresivamente hasta moler por completo y luego añade la cáscara de limón y repite el proceso.")
        driver.find_element("id","cargar-preparacion-btn").click()
        driver.find_element("id","guardar-receta").click()
        time.sleep(1)
        self.assertEqual("Receta de Puding de arroz con leche Thermomix", driver.find_element("id","receta-carta-titulo-0").text)
        driver.find_element("id","link-to-0-btn-id").click()
        time.sleep(1)
        self.assertEqual("Receta de Puding de arroz con leche Thermomix", driver.find_element("id","id-titulo-receta").text)
        self.assertTrue(self.is_element_present(By.ID, "img-src-loaded"))
        self.assertEqual("100 gramos de Arroz", driver.find_element("id","ing-0").text)
        self.assertEqual(u"200 gramos de Azúcar (1 taza)", driver.find_element("id","ing-1").text)
        self.assertEqual(u"El primer paso para preparar el pudin con thermomix será triturar el arroz. Para ello, programa con velocidad 5-7-9, ve aumentando de forma progresiva hasta que el arroz quede completamente pulverizado. Reserva.", driver.find_element("id","prep-0").text)
        self.assertEqual(u"Aparte, pulveriza también el azúcar junto con la cáscara de limón. Primero el azúcar programando la thermomix con velocidad 5-7-9, aumentando progresivamente hasta moler por completo y luego añade la cáscara de limón y repite el proceso.", driver.find_element("id","prep-1").text)
        driver.find_element("id","return-btn").click()
        time.sleep(1)
        driver.find_element("id","link-to-0-btn-id").click()
        time.sleep(1)
        driver.find_element("id","accion-eliminar-btn-id").click()
        time.sleep(1)
        #Warning: assertTextNotPresent may require manual changes
        self.assertNotRegex(driver.find_element("css selector","BODY").text, r"^[\s\S]*id=receta-carta-titulo[\s\S]*$")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
