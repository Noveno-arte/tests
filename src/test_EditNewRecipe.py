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

class EditNewRecipe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_edit_new_recipe(self):
        driver = self.driver
        driver.get("http://localhost:3000/")
        driver.find_element("id","new-recipe-btn").click()
        time.sleep(1)
        driver.find_element("id","input-titulo").click()
        driver.find_element("id","input-titulo").clear()
        driver.find_element("id","input-titulo").send_keys("Receta de Empanadas de calabaza y queso")
        driver.find_element("name","file").clear()
        driver.find_element("name","file").send_keys(file_path+"\\imagenTest.jpg")
        driver.find_element("id","input-ingrediente").click()
        driver.find_element("id","input-ingrediente").clear()
        driver.find_element("id","input-ingrediente").send_keys("400 gramos de calabaza")
        driver.find_element("id","cargar-ingrediente-btn").click()
        driver.find_element("id","input-ingrediente").click()
        driver.find_element("id","input-ingrediente").clear()
        driver.find_element("id","input-ingrediente").send_keys("60 gramos de queso fresco")
        driver.find_element("id","cargar-ingrediente-btn").click()
        driver.find_element("id","input-preparacion").click()
        driver.find_element("id","input-preparacion").clear()
        driver.find_element("id","input-preparacion").send_keys(u"Para empezar con la receta de las empanadas de calabaza y queso, primero deberás cocinar la calabaza. Para hacerlo, tienes diferentes opciones. Una de las opciones consiste en pelarla, cortarla en cubos y hervirla durante 20 minutos hasta que al pincharla se caiga del tenedor. Al final de la receta puedes encontrar otras formas de cocinar la calabaza.")
        driver.find_element("id","cargar-preparacion-btn").click()
        driver.find_element("id","input-preparacion").click()
        driver.find_element("id","input-preparacion").clear()
        driver.find_element("id","input-preparacion").send_keys(u"Cuando esté cocida, llévala a un colador con un recipiente debajo para colarla y que libere el agua que haya podido absorber. Tanto este líquido como el que has utilizado para hervir la calabaza, tiene numerosos nutrientes, así que querrás guardarlo para un fondo de cocción o caldo.")
        driver.find_element("id","cargar-preparacion-btn").click()
        driver.find_element("id","guardar-receta").click()
        time.sleep(1)
        driver.find_element("id","link-to-0-btn-id").click()
        time.sleep(1)
        driver.find_element("id","accion-editar-btn-id").click()
        time.sleep(1)
        driver.find_element("id","input-titulo").click()
        driver.find_element("id","input-titulo").clear()
        driver.find_element("id","input-titulo").send_keys("Receta de Empanadas de calabaza y queso editado")
        driver.find_element("id","eliminar-ingrediente-btn-1").click()
        driver.find_element("id","input-ingrediente").click()
        driver.find_element("id","input-ingrediente").clear()
        driver.find_element("id","input-ingrediente").send_keys("1 kilo de queso fresco")
        driver.find_element("id","cargar-ingrediente-btn").click()
        driver.find_element("id","input-preparacion").click()
        driver.find_element("id","input-preparacion").clear()
        driver.find_element("id","input-preparacion").send_keys("disfrutar")
        driver.find_element("id","cargar-preparacion-btn").click()
        driver.find_element("id","guardar-receta").click()
        time.sleep(1)
        self.assertEqual("Receta de Empanadas de calabaza y queso editado", driver.find_element("id","id-titulo-receta").text)
        self.assertEqual("400 gramos de calabaza", driver.find_element("id","ing-0").text)
        self.assertEqual("1 kilo de queso fresco", driver.find_element("id","ing-1").text)
        self.assertEqual(u"Para empezar con la receta de las empanadas de calabaza y queso, primero deberás cocinar la calabaza. Para hacerlo, tienes diferentes opciones. Una de las opciones consiste en pelarla, cortarla en cubos y hervirla durante 20 minutos hasta que al pincharla se caiga del tenedor. Al final de la receta puedes encontrar otras formas de cocinar la calabaza.", driver.find_element("id","prep-0").text)
        self.assertEqual(u"Cuando esté cocida, llévala a un colador con un recipiente debajo para colarla y que libere el agua que haya podido absorber. Tanto este líquido como el que has utilizado para hervir la calabaza, tiene numerosos nutrientes, así que querrás guardarlo para un fondo de cocción o caldo.", driver.find_element("id","prep-1").text)
        self.assertEqual("disfrutar", driver.find_element("id","prep-2").text)
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
