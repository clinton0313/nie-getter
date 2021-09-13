from selenium import webdriver as wd
from selenium import Select
from selenium.webdriver.common.keys import Keys

driver = wd.Firefox
driver.get("https://sede.administracionespublicas.gob.es/icpplustieb/citar?p=8&locale=es")

nie = "Y8809001S"
name = "Clinton Leung"
country = "CANADA"
expiry = "16/12/2023"
tel = "658427293"
email = "clinton0313@gmail.com"

#function for the page to select appointment type and continue
def sel_apt_type():
    select = Select(driver.find_element_by_id("tramiteGrupo[0]"))
    select.select_by_visible_text("POLICIA-TOMA DE HUELLAS (EXPEDICIÓN DE TARJETA) Y RENOVACIÓN DE TARJETA DE LARGA DURACIÓN")
    accept = driver.find_element_by_id("btnAceptar")
    accept.click()

#click the entrar button on the info page
def info_page():
    entrar = Select(driver.find_element_by_id("btnEntrar"))
    entrar.click()

def fill_info(nie, name, country, expiry):
    nie_field = driver.find_element_by_id("txtIdCitadto")
    name_field = driver.find_element_by_id("txtDesCitado")
    country_select = Select(driver.find_element_by_id("txtPaisNac")
    expiry_field = driver.find_element_id("txtFecha")

#fill fields

    country_select.select_by_visible_text(country)
    accept = Select(driver.find_element_by_id("btnEnviar"))
    accept.click()

def cita_info(tel, email):
    tel_field = driver.find_element_by_id("txtTelefonoCitado")
    email_field = driver.find_element_by_id("emailUNO")
    emailconfirm_field = driver.find_element_by_id("emailDOS")
    siguiente = Select(driver.find_element_by_id("btnSiguiente"))
    siguiente.click()
    #check this is how to click
    #fill fields

def select_office():
    office = Select(driver.find_element_by_id("idSede")
    siguiente = Select(driver.find_element_by_id("btnSiguiente"))
    siguiente.click()

