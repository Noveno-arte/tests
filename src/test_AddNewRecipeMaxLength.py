# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddNewRecipeMaxLength(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_new_recipe_max_length(self):
        driver = self.driver
        driver.get("http://localhost:3000/")
        driver.find_element("id","new-recipe-btn").click()
        time.sleep(1)
        driver.find_element("id","input-titulo").click()
        driver.find_element("id","input-titulo").clear()
        driver.find_element("id","input-titulo").send_keys("Receta de Empanadas de calabaza y queso Receta de Empanadas de calabaza y quesooo")
        driver.find_element("id","input-ingrediente").click()
        driver.find_element("id","input-ingrediente").clear()
        driver.find_element("id","input-ingrediente").send_keys("ingrediente 1")
        driver.find_element("id","cargar-ingrediente-btn").click()
        driver.find_element("id","input-ingrediente").click()
        driver.find_element("id","input-ingrediente").clear()
        driver.find_element("id","input-ingrediente").send_keys("ingrediente 2")
        driver.find_element("id","cargar-ingrediente-btn").click()
        driver.find_element("id","input-preparacion").click()
        driver.find_element("id","input-preparacion").clear()
        driver.find_element("id","input-preparacion").send_keys("paso 1")
        driver.find_element("id","cargar-preparacion-btn").click()
        driver.find_element("id","input-preparacion").click()
        driver.find_element("id","input-preparacion").clear()
        driver.find_element("id","input-preparacion").send_keys("paso 2")
        driver.find_element("id","guardar-receta").click()
        self.assertEqual(u"¡El titulo no puede exceder los 80 caracteres!", driver.find_element("id","warning-length-id").text)
        driver.find_element("id","input-titulo").click()
        driver.find_element("id","input-titulo").clear()
        driver.find_element("id","input-titulo").send_keys("Receta de Empanadas de calabaza y queso Receta de Empanadas de calabaza y quesoo")
        driver.find_element("id","guardar-receta").click()
        time.sleep(1)
        self.assertEqual("Receta de Empanadas de calabaza y queso Receta de Empanadas de calabaza y quesoo", driver.find_element("id","receta-carta-titulo-0").text)
    
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
