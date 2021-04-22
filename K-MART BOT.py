# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:48:49 2021

@author: alejandro.gutierrez
"""

#Importar paqueterias
import os
import shutil
os.chdir('C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\ALEJANDRO RAMOS GTZ\\GIT\\BOT_KMART') # relative path: scripts dir is under Lab

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # Guardar en las paginas
#from selenium.webdriver.support import expected_conditions as EC #Guardar en las paginas import unittest
#from selenium.webdriver.chrome.options import Options
from datetime import date, timedelta
import time 
import datetime
#from calendar import monthrange
import calendar

from LOGIN_PAGE import login_page
from MAIN_PAGE import main_page

#import pandas as pd

class Download_K_Mart_Data(unittest.TestCase):
    
    def setUp(self):
        #option = Options()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        prefs = {'download.default_directory' : 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\DOWNLOADS'} #'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\ALEJANDRO RAMOS GTZ\\TEST'} #CAMBIAR ESTO PARA CADA TEST
        chrome_options.add_experimental_option('prefs', prefs)
      #  chrome_options.add_argument('--headless')
        chromedriver_path = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\ALEJANDRO RAMOS GTZ\\PYTHON\\chromedriver'
        url = 'https://myhome.svharbor.com/siteminderagent/forms/svhlogin.fcc?TYPE=33554433&REALMOID=06-000d8ea6-308c-1c8b-8ca7-651f0aaa0000&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=$SM$A2B0iCpbmbLLMgkIF4IjrjvRfda87wfgFDIDSEjuhps4ZSB%2bGCC9OELQczQ9D4b7&TARGET=$SM$https%3a%2f%2fmyhome%2esvharbor%2ecom%2fcontent%2fsvhb%2fhome%2ehtml'
        self.driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
        self.driver.get(url)
        self.WebDriverWait = WebDriverWait
        #self.driver.implicity_wait(7)
        self.PageInitial = login_page(self.driver)
        self.PageMain = main_page(self.driver)
        self.dir_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\DOWNLOADS'
        #self.driver.maximize_window()
    
    
    #@unittest.skip('Not need now') #AQUI INICIA EL TEST PARA MONTHLY DC, BAJA EL ARCHIVO DESDE EL 1RO DEL MES HASTA EL ULTIMO SABADO (A PARTIR DE LA FECHA DE EJECUCION)
    def test_Naterra(self):
        before = os.listdir(self.dir_download) 

        #Cargamos los datos del inicio de sesion
        email = 'jdamour'  
        pswd = '67xvfybp' 
        report = 'Naterra'
        
        self.PageInitial.logg_inn(email,pswd)
        self.PageMain.alex_sales_butto()
        self.PageMain.alex_corporate_reports()
        self.PageMain.my_reports(report)
        self.PageMain.folder_kmack3() #Eliminar 
        self.PageMain.report_select(report)
        self.PageMain.set_date()
        self.PageMain.run_report()
        self.PageMain.export_report()

        
        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue
                        
            time.sleep(60) #REDUCIR ESTE TIEMPO DE ESPERA
            
            #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
            Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
            Initial_path = self.dir_download 
            filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
            
            today = date.today()
            idx = (today.weekday() + 1) % 7
            sat = today - datetime.timedelta(7+idx-6) #Ultimo sabado
            d1 = sat.strftime("%m-%d-%Y")
            
            new_name = 'Naterra L52 Weeks $, Unit TY vs LY Ending %s' %d1 + str(Current_Date) + '.xlsx'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
            
            #MOVER EL ARCHIVO A LA UBICACION DESEADA
            new_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\K-MART\\NATERRA'
            shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)
            
            #Mas bien una vez que termine, volver a checar si la carpeta de downloads tiene algun archivo (volverlo a mover) o si no tiene ninguna entonces fin, Ver que solo se descargue un archivo 
            #dir_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\DOWNLOADS'
            #print(len([name for name in os.listdir(dir_download) if os.path.isfile(os.path.join(dir_download, name))]))
            time.sleep(2)
            number_of_files = len([name for name in os.listdir(self.dir_download) if os.path.isfile(os.path.join(self.dir_download, name))])
            if number_of_files==1:
                filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
                print(filename)
                shutil.move('%s'%filename, '%s'%new_download)
            else:
                pass
            
        #Listo
        print("Naterra is READY!!" ) 
        time.sleep(3)
    

    def test_Chinet(self):
        before = os.listdir(self.dir_download) 

        #Cargamos los datos del inicio de sesion
        email = 'jdamou0'  
        pswd = 'pvh4e3av' 
        report = 'Huhtamaki Chinet'
        
        self.PageInitial.logg_inn(email,pswd)
        self.PageMain.alex_sales_butto()
        self.PageMain.alex_corporate_reports()
        self.PageMain.my_reports(report)
        self.PageMain.report_select(report)
        self.PageMain.set_date()
        self.PageMain.run_report()
        self.PageMain.export_report()

        
        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue
                        
            time.sleep(60) #REDUCIR ESTE TIEMPO DE ESPERA
            
            #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
            Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
            Initial_path = self.dir_download 
            filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
            
            today = date.today()
            idx = (today.weekday() + 1) % 7
            sat = today - datetime.timedelta(7+idx-6) #Ultimo sabado
            d1 = sat.strftime("%m-%d-%Y")
            
            new_name = 'Huhtamaki $, Units TY vs LY L52 Weeks Ending %s' %d1 + str(Current_Date) + '.xlsx'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
            
            #MOVER EL ARCHIVO A LA UBICACION DESEADA
            new_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\K-MART\\CHINET'
            shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)
            
            #Mas bien una vez que termine, volver a checar si la carpeta de downloads tiene algun archivo (volverlo a mover) o si no tiene ninguna entonces fin, Ver que solo se descargue un archivo 
            #dir_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\DOWNLOADS'
            #print(len([name for name in os.listdir(dir_download) if os.path.isfile(os.path.join(dir_download, name))]))
            time.sleep(2)
            number_of_files = len([name for name in os.listdir(self.dir_download) if os.path.isfile(os.path.join(self.dir_download, name))])
            if number_of_files==1:
                filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
                print(filename)
                shutil.move('%s'%filename, '%s'%new_download)
            else:
                pass
            
        #Listo
        print("Huhtamaki Chinet is READY!!" ) 
        time.sleep(3)
        
        

    def test_Duraflame_summer_total(self):
        before = os.listdir(self.dir_download) 

        #Cargamos los datos del inicio de sesion
        email = 'pwagne3'  
        pswd = '9t47py6c' 
        report = 'Duraflame summer total'
        
        self.PageInitial.logg_inn(email,pswd)
        self.PageMain.alex_sales_butto()
        self.PageMain.alex_corporate_reports()
        self.PageMain.my_reports(report)
        self.PageMain.report_select(report)
        self.PageMain.set_date()
        self.PageMain.run_report()
        self.PageMain.export_report()

        
        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue
                        
            time.sleep(60) #REDUCIR ESTE TIEMPO DE ESPERA
            
            #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
            Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
            Initial_path = self.dir_download 
            filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
            
            today = date.today()
            idx = (today.weekday() + 1) % 7
            sat = today - datetime.timedelta(7+idx-6) #Ultimo sabado
            d1 = sat.strftime("%m-%d-%Y")
            
            new_name = 'Duraflame - Summer TOTAL %s' %d1 + str(Current_Date) + '.xlsx'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
            
            #MOVER EL ARCHIVO A LA UBICACION DESEADA
            new_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\K-MART\\DURAFLAME'
            shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)
            
            #Mas bien una vez que termine, volver a checar si la carpeta de downloads tiene algun archivo (volverlo a mover) o si no tiene ninguna entonces fin, Ver que solo se descargue un archivo 
            #dir_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\DOWNLOADS'
            #print(len([name for name in os.listdir(dir_download) if os.path.isfile(os.path.join(dir_download, name))]))
            time.sleep(2)
            number_of_files = len([name for name in os.listdir(self.dir_download) if os.path.isfile(os.path.join(self.dir_download, name))])
            if number_of_files==1:
                filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
                print(filename)
                shutil.move('%s'%filename, '%s'%new_download)
            else:
                pass
            
        #Listo
        print("Duraflame summer total is READY!!" ) 
        time.sleep(3)


    def test_Duraflame_summer_weekly(self):
        before = os.listdir(self.dir_download) 

        #Cargamos los datos del inicio de sesion
        email = 'pwagne3'  
        pswd = '9t47py6c' 
        report = 'Duraflame summer weekly'
        
        self.PageInitial.logg_inn(email,pswd)
        self.PageMain.alex_sales_butto()
        self.PageMain.alex_corporate_reports()
        self.PageMain.my_reports(report)
        self.PageMain.report_select(report)
        self.PageMain.set_date()
        self.PageMain.run_report()
        self.PageMain.export_report()

        
        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue
                        
            time.sleep(60) #REDUCIR ESTE TIEMPO DE ESPERA
            
            #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
            Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
            Initial_path = self.dir_download 
            filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
            
            today = date.today()
            idx = (today.weekday() + 1) % 7
            sat = today - datetime.timedelta(7+idx-6) #Ultimo sabado
            d1 = sat.strftime("%m-%d-%Y")
            
            new_name = 'Duraflame - Summer WEEKLY %s' %d1 + str(Current_Date) + '.xlsx'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
            
            #MOVER EL ARCHIVO A LA UBICACION DESEADA
            new_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\K-MART\\DURAFLAME'
            shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)
            
            #Mas bien una vez que termine, volver a checar si la carpeta de downloads tiene algun archivo (volverlo a mover) o si no tiene ninguna entonces fin, Ver que solo se descargue un archivo 
            #dir_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\DOWNLOADS'
            #print(len([name for name in os.listdir(dir_download) if os.path.isfile(os.path.join(dir_download, name))]))
            time.sleep(2)
            number_of_files = len([name for name in os.listdir(self.dir_download) if os.path.isfile(os.path.join(self.dir_download, name))])
            if number_of_files==1:
                filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
                print(filename)
                shutil.move('%s'%filename, '%s'%new_download)
            else:
                pass
            
        #Listo
        print("Duraflame summer weekly is READY!!" ) 
        time.sleep(3)
        


    def test_Duraflame_winter_total(self):
        before = os.listdir(self.dir_download) 

        #Cargamos los datos del inicio de sesion
        email = 'pwagne3'  
        pswd = '9t47py6c' 
        report = 'Duraflame winter total'
        
        self.PageInitial.logg_inn(email,pswd)
        self.PageMain.alex_sales_butto()
        self.PageMain.alex_corporate_reports()
        self.PageMain.my_reports(report)
        self.PageMain.report_select(report)
        self.PageMain.set_date()
        self.PageMain.run_report()
        self.PageMain.export_report()

        
        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue
                        
            time.sleep(60) #REDUCIR ESTE TIEMPO DE ESPERA
            
            #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
            Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
            Initial_path = self.dir_download 
            filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
            
            today = date.today()
            idx = (today.weekday() + 1) % 7
            sat = today - datetime.timedelta(7+idx-6) #Ultimo sabado
            d1 = sat.strftime("%m-%d-%Y")
            
            new_name = 'Duraflame - Winter TOTAL %s' %d1 + str(Current_Date) + '.xlsx'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
            
            #MOVER EL ARCHIVO A LA UBICACION DESEADA
            new_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\K-MART\\DURAFLAME'
            shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)
            
            #Mas bien una vez que termine, volver a checar si la carpeta de downloads tiene algun archivo (volverlo a mover) o si no tiene ninguna entonces fin, Ver que solo se descargue un archivo 
            #dir_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\DOWNLOADS'
            #print(len([name for name in os.listdir(dir_download) if os.path.isfile(os.path.join(dir_download, name))]))
            time.sleep(2)
            number_of_files = len([name for name in os.listdir(self.dir_download) if os.path.isfile(os.path.join(self.dir_download, name))])
            if number_of_files==1:
                filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
                print(filename)
                shutil.move('%s'%filename, '%s'%new_download)
            else:
                pass
            
        #Listo
        print("Duraflame winter total is READY!!" ) 
        time.sleep(3)




    def test_Duraflame_winter_weekly(self):
        before = os.listdir(self.dir_download) 

        #Cargamos los datos del inicio de sesion
        email = 'pwagne3'  
        pswd = '9t47py6c' 
        report = 'Duraflame winter weekly'
        
        self.PageInitial.logg_inn(email,pswd)
        self.PageMain.alex_sales_butto()
        self.PageMain.alex_corporate_reports()
        self.PageMain.my_reports(report)
        self.PageMain.report_select(report)
        self.PageMain.set_date()
        self.PageMain.run_report()
        self.PageMain.export_report()

        
        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue
                        
            time.sleep(60) #REDUCIR ESTE TIEMPO DE ESPERA
            
            #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
            Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
            Initial_path = self.dir_download 
            filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
            
            today = date.today()
            idx = (today.weekday() + 1) % 7
            sat = today - datetime.timedelta(7+idx-6) #Ultimo sabado
            d1 = sat.strftime("%m-%d-%Y")
            
            new_name = 'Duraflame - Winter WEEKLY %s' %d1 + str(Current_Date) + '.xlsx'
            shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
            
            #MOVER EL ARCHIVO A LA UBICACION DESEADA
            new_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\K-MART\\DURAFLAME'
            shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)
            
            #Mas bien una vez que termine, volver a checar si la carpeta de downloads tiene algun archivo (volverlo a mover) o si no tiene ninguna entonces fin, Ver que solo se descargue un archivo 
            #dir_download = 'C:\\Users\\alejandro.gutierrez\\OneDrive - Carlin Group - CA Fortune\\Documents\\KROGER SELENIUM\\DOWNLOADS'
            #print(len([name for name in os.listdir(dir_download) if os.path.isfile(os.path.join(dir_download, name))]))
            time.sleep(2)
            number_of_files = len([name for name in os.listdir(self.dir_download) if os.path.isfile(os.path.join(self.dir_download, name))])
            if number_of_files==1:
                filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
                print(filename)
                shutil.move('%s'%filename, '%s'%new_download)
            else:
                pass
            
        #Listo
        print("Duraflame winter weekly is READY!!" ) 
        time.sleep(3)


        

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
        
        
if __name__ == '__main__':
    unittest.main()
       