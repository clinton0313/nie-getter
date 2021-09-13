from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = WebDriver


nie = "Y8809001S"
name = "Clinton Leung"
country = "CANADA"
expiry = "16/12/2023"
tel = "658427293"
email = "clinton0313@gmail.com"

#function for the page to select appointment type and continue (skips choosing city)
def sel_apt_type():
    driver.get("https://sede.administracionespublicas.gob.es/icpplustieb/citar?p=8&locale=es")
    select = Select(driver.find_element_by_id("tramiteGrupo[0]"))
    select.select_by_visible_text("POLICIA-TOMA DE HUELLAS (EXPEDICIÓN DE TARJETA) Y RENOVACIÓN DE TARJETA DE LARGA DURACIÓN")
    accept = driver.find_element_by_id("btnAceptar")
    accept.click()

#click the entrar button on the info page
def info_page():
    entrar = Select(driver.find_element_by_id("btnEntrar"))
    entrar.click()

def fill_info(nie, name, country, expiry):
    nie_field = driver.find_element_by_id("txtIdCitado")
    name_field = driver.find_element_by_id("txtDesCitado")
    country_select = Select(driver.find_element_by_id("txtPaisNac"))
    expiry_field = driver.find_element_id("txtFecha")

#fill fields
    nie_field.send_keys(nie)
    name_field.send_keys(name)
    expiry_field.send_keys(expiry)
    country_select.select_by_visible_text(country)

#hit accept
    accept = Select(driver.find_element_by_id("btnEnviar"))
    accept.click()

def cita_info(tel, email):
    tel_field = driver.find_element_by_id("txtTelefonoCitado")
    email_field = driver.find_element_by_id("emailUNO")
    emailconfirm_field = driver.find_element_by_id("emailDOS")
    
    tel_field.send_keys(tel)
    email_field.send_keys(email)
    emailconfirm_field.send_keys(email)
    
    siguiente = Select(driver.find_element_by_id("btnSiguiente"))
    siguiente.click()
    #check this is how to click

def select_office():
    office = Select(driver.find_element_by_id("idSede"))
    siguiente = Select(driver.find_element_by_id("btnSiguiente"))
    siguiente.click()

sel_apt_type
info_page
fill_info(nie, name, country, expiry)
#if statement
#cita_info(tel, email)
#select_office
#alert or restart