# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:49:28 2021

@author: alejandro.gutierrez
"""


# PAGINA DEL PROCESO
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait # Guardar en las paginas
from selenium.webdriver.support import expected_conditions as EC #Guardar en las paginas import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class login_page():
    def __init__(self,my_driver):
        
        self.log = (By.ID, 'dnn_ctr442_Login_Login_LDAP_txtUsername')
        self.pswd = (By.ID, 'dnn_ctr442_Login_Login_LDAP_txtPassword')
        self.buttonid = (By.ID, 'dnn_ctr442_Login_Login_LDAP_cmdLDAPLogin')

    def logg_inn(self, mail, pwd):
        try:
            loginn = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.log))
            loginn.send_keys(mail)
            
            pwdd = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.shipment_history))
            pwdd.send_keys(pwd)

            button = WebDriverWait(self.driver,50).until(EC.element_to_be_clickable(self.buttonid))
            button.click()
            
        except TimeoutException:
            print ("Loading -login_page- took too much time!")
