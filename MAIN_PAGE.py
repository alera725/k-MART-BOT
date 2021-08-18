# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:50:00 2021

@author: alejandro.gutierrez
"""

# PAGINA DEL PROCESO
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait # Guardar en las paginas
from selenium.webdriver.support import expected_conditions as EC #Guardar en las paginas import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
from datetime import date
import datetime

class main_page():
    
    def __init__(self,my_driver):
        
        self.driver = my_driver
        self.popup = (By.XPATH, '//*[@id="Form"]/div[4]/div[1]/button')
        self.home = (By.XPATH, '//*[@id="dnn_wrapper"]/div[2]/div[3]/div/div/div/div[1]/a')
        self.Alex_sales_button = (By.ID, 'dnn_ctr424_Links_lstLinks_linkHyp_0')
        self.Alex_corporate = (By.XPATH, '//*[@id="projects_ProjectsStyle"]/table/tbody/tr/td[2]/div/table/tbody/tr/td[2]/a')
        self.myreports = (By.ID, 'main')
        self.myreports_all = (By.LINK_TEXT, 'My Reports')
        self.kmack = (By.LINK_TEXT, 'Reports from kmack3')
        self.naterra_report = (By.XPATH, '//*[@id="FolderIcons"]/tbody/tr/td/div/table/tbody/tr/td[2]')
        self.chinet_report = (By.XPATH, '//*[@id="FolderIcons"]/tbody/tr/td/div/table/tbody/tr/td[2]')
        self.duraflame_summer_total_report = (By.XPATH, '//*[@id="FolderIcons"]/tbody/tr[1]/td[1]/div/table/tbody/tr/td[2]')
        self.duraflame_summer_week_report = (By.XPATH, '//*[@id="FolderIcons"]/tbody/tr[1]/td[2]/div/table/tbody/tr/td[2]')
        self.duraflame_winter_total_report = (By.XPATH, '//*[@id="FolderIcons"]/tbody/tr[2]/td[1]/div/table/tbody/tr/td[2]')
        self.duraflame_winter_week_report = (By.XPATH, '//*[@id="FolderIcons"]/tbody/tr[2]/td[2]/div/table/tbody/tr/td[2]')
        self.date_box = (By.ID, 'id_mstr285_txt')
        self.run_reportt = (By.ID, 'id_mstr286')
        self.exp_report = (By.ID, 'tbExport')
        self.ad_hoc_metricss = (By.XPATH, '//*[@id="id_mstr86"]/table/tbody/tr[9]/td[2]')
        self.invty = (By.XPATH, '//*[@id="id_mstr316ListContainer"]/div[2]/div/a')
        self.metric = (By.ID, 'id_mstr316ListContainer') 
        self.find_metric = (By.ID, 'id_mstr315_txt')
        self.store_end_inv_units = (By.XPATH, '//*[@id="id_mstr316ListContainer"]/div[1]/div')
        self.arrow = (By.ID, 'id_mstr318')
        
        #Esto es en el ultimo paso en export paso en summer total
        #//*[@id="ribbonToolbarTabsListContainer"]/div[1]/table/tbody/tr/td[2]/div
        #Report Home 

    def POPs_up(self):
        try:
            
            popup_window = WebDriverWait(self.driver,60).until(EC.visibility_of_element_located(self.popup))
            popup_window.click()
            
            home_button = WebDriverWait(self.driver,60).until(EC.visibility_of_element_located(self.home))
            home_button.click()
            
        except TimeoutException:
            
            print ("Loading -POPs_up- took too much time!")
            pass        
        
    def alex_sales_butto(self):
        try:
            
            Alex_sales = WebDriverWait(self.driver,50).until(EC.element_to_be_clickable(self.Alex_sales_button))
            Alex_sales.click()

        except TimeoutException:
            print ("Loading -Alex_sales- took too much time!")
          
            
    def alex_corporate_reports(self):
        try:
            a_c_r = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.Alex_corporate)) 
            a_c_r.click()
            #time.sleep(2)
            
        except TimeoutException:
            print ("Loading -alex_corporate_reports- took too much time!")
            
            
    def my_reports(self, report):
        try:
            if report == 'Naterra':
                my_rep = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.myreports)) 
                my_rep.click()
                #time.sleep(2)
            else:
                my_rep = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.myreports_all)) 
                my_rep.click()
                #time.sleep(2)
            
        except TimeoutException:
            print ("Loading -my_reports- took too much time!")


    def folder_kmack3(self):
        try:
            
            kmack_click = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.kmack)) 
            kmack_click.click()
            #time.sleep(2)
            
        except TimeoutException:
            print ("Loading -folder_kmack3- took too much time!")      
    
    
    def report_select(self, report):
        try:
            if report == 'Naterra':
                
                #CLick en el reporte
                naterra = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.naterra_report)) 
                naterra.click()
                #time.sleep(7)

            elif report == 'Huhtamaki Chinet':

                #CLick en el reporte
                chinet = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.chinet_report)) 
                chinet.click()
                #time.sleep(7)

            elif report == 'Duraflame summer total':
                
                #CLick en el reporte
                duraflame = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.duraflame_summer_total_report)) 
                duraflame.click()
                #time.sleep(7)
                
            elif report == 'Duraflame summer weekly':
                
                #CLick en el reporte
                duraflame = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.duraflame_summer_week_report)) 
                duraflame.click()
                #time.sleep(7)
                
            elif report == 'Duraflame winter total':
                
                #CLick en el reporte
                duraflame = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.duraflame_winter_total_report)) 
                duraflame.click()
                #time.sleep(7)

            elif report == 'Duraflame winter weekly':
                
                #CLick en el reporte
                duraflame = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.duraflame_winter_week_report)) 
                duraflame.click()
                #time.sleep(7)  
                
            else:
                print('Error, please select a valid Report name (naterra,  or duraflame summer-winter ...')
            
        except TimeoutException:
            print ("Loading -report_select- took too much time!")  
            
  
    def ad_hoc_metrics(self):
        try:
            
            ad_hoc_click = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.ad_hoc_metricss)) 
            ad_hoc_click.click()
            #time.sleep(2)
            inventory_click = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.invty)) 
            inventory_click.click()
            time.sleep(5)  
            
            
            #Buscar la metrica en el containerlist
            #div title = Store (+/-) End Inv Units
            #mettt = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.metric)) 
            #mettt.click()
            #time.sleep(5)  
            
            #Find Store (+/-) End Inv Units
            id_search = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.find_metric)) 
            id_search.send_keys('Store (+/-) End inv units')
            id_search.send_keys(Keys.RETURN)
            
            #Click on Store (+/-) End Inv Units
            metric_store_end_inv_units = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.store_end_inv_units)) #Store (+/-) End Inv Units
            metric_store_end_inv_units.click()
            #time.sleep(2)

            #click en la flecha
            ARRW = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.arrow)) 
            ARRW.click()
            #time.sleep(10)
            
        except TimeoutException:
            print ("Loading -ad_hoc_metrics- took too much time!")   

  
    def set_date(self):
        try:
            
            today = date.today()
            idx = (today.weekday() + 1) % 7
            sat = today - datetime.timedelta(7+idx-6) #Ultimo sabado
            d1 = sat.strftime("%m-%d-%Y")
            
            #Poner la fecha de hoy en el reporte
            date_boxx = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.date_box))
            date_boxx.send_keys(' %s'%d1)
            
        except TimeoutException:
            print ("Loading -set_date- took too much time!")      
    
    
    def run_report(self):
        try:
            
            #Run report    
            rreport = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.run_reportt)) 
            rreport.click()
            #time.sleep(2)
            
        except TimeoutException:
            print ("Loading -run_report- took too much time!")  
            
            
    def export_report(self):
        try:
            
            #Run report    
            expor_report = WebDriverWait(self.driver,200).until(EC.visibility_of_element_located(self.exp_report)) 
            expor_report.click()
            #time.sleep(2)
            
        except TimeoutException:
            print ("Loading -export_report- took too much time!")           
            