# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddNewRecipeWithoutImage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_new_recipe_without_image(self):
        driver = self.driver
        driver.get("http://localhost:3000/")
        driver.find_element("id","new-recipe-btn").click()
        driver.find_element("id","input-titulo").click()
        time.sleep(1)
        driver.find_element("id","input-titulo").clear()
        driver.find_element("id","input-titulo").send_keys(u"Receta de Huesillos extremeños")
        driver.find_element("id","input-ingrediente").click()
        driver.find_element("id","input-ingrediente").clear()
        driver.find_element("id","input-ingrediente").send_keys(u"500 gramos de harina de repostería")
        driver.find_element("id","cargar-ingrediente-btn").click()
        driver.find_element("id","input-ingrediente").click()
        driver.find_element("id","input-ingrediente").clear()
        driver.find_element("id","input-ingrediente").send_keys("100 mililitros de aceite de oliva")
        driver.find_element("id","cargar-ingrediente-btn").click()
        driver.find_element("id","input-preparacion").click()
        driver.find_element("id","input-preparacion").clear()
        driver.find_element("id","input-preparacion").send_keys(u"Para empezar con la receta de huesillos extremeños, primero debes poner los 100 ml. de aceite de oliva en un cazo a calentar 2-3 minutos con la cucharada de anís en grano o molido y 2-3 tiras de piel de limón. Cuando esté caliente, retira del fuego y deja enfriar para que el aceite adquiera los sabores del limón y del anís. Cuando esté frío, retira los trozos de limón y, si lo deseas, puedes quitar el anís o dejarlo.")
        driver.find_element("id","cargar-preparacion-btn").click()
        driver.find_element("id","input-preparacion").click()
        driver.find_element("id","input-preparacion").clear()
        driver.find_element("id","input-preparacion").send_keys(u"En un bol bate los huevos, añade el aceite ya frío y mezcla.")
        driver.find_element("id","cargar-preparacion-btn").click()
        driver.find_element("id","guardar-receta").click()
        time.sleep(1)
        self.assertEqual(u"Receta de Huesillos extremeños", driver.find_element("id","receta-carta-titulo-0").text)
        driver.find_element("id","link-to-0-btn-id").click()
        time.sleep(1)
        self.assertEqual(u"Receta de Huesillos extremeños", driver.find_element("id","id-titulo-receta").text)
        self.assertTrue(self.is_element_present(By.ID, "img-src-default"))
        self.assertEqual(u"500 gramos de harina de repostería", driver.find_element("id","ing-0").text)
        self.assertEqual("100 mililitros de aceite de oliva", driver.find_element("id","ing-1").text)
        self.assertEqual(u"Para empezar con la receta de huesillos extremeños, primero debes poner los 100 ml. de aceite de oliva en un cazo a calentar 2-3 minutos con la cucharada de anís en grano o molido y 2-3 tiras de piel de limón. Cuando esté caliente, retira del fuego y deja enfriar para que el aceite adquiera los sabores del limón y del anís. Cuando esté frío, retira los trozos de limón y, si lo deseas, puedes quitar el anís o dejarlo.", driver.find_element("id","prep-0").text)
        self.assertEqual(u"En un bol bate los huevos, añade el aceite ya frío y mezcla.", driver.find_element("id","prep-1").text)
        driver.find_element("id","return-btn").click()
    
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
