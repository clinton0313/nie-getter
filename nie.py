from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver = webdriver.Firefox()

#Enter Personal info here
nie = ""
name = "Test Name"
country = "CANADA" #Country in all caps - needs to match the site
expiry = ""
tel = ""
email = "test@gmail.com"
city = "Barcelona" 
nie_option = "POLICIA-TOMA DE HUELLAS (EXPEDICIÓN DE TARJETA) Y RENOVACIÓN DE TARJETA DE LARGA DURACIÓN"    #Use exact text of the option you would like

def scroll():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
def click_button(btnid):
    scroll()
    driver.find_element_by_id(btnid).click()
def select_option(menu_id, option):
    select = Select(driver.find_element_by_id(menu_id))
    select.select_by_visible_text(option)
def fill_field(fld_id, text):
    field = driver.find_element_by_id(fld_id)
    field.send_keys(text)

#ask for an appointment
def sol_cita(city, nie_option, nie, name, country, expiry):
    select_option("form", city) #Select city on the city page
    click_button("btnAceptar") 
    scroll()
    select_option("tramiteGrupo[0]", nie_option) #Select apppointment type
    click_button("btnAceptar")
    click_button("btnEntrar") #Pass the page asking to accept conditions
    fill_field("txtIdCitado", nie)
    fill_field("txtDesCitado", name)
    select_option("txtPaisNac", country)
    #fill_field("txtFecha", expiry)
    click_button("btnEnviar") #Fills your info in the info page and submits
    click_button("btnEnviar") #Solicitar Cita

#Select second office because it could return a single preselcted office or multiple where you have to make a choice
def office_page():
    try:
        driver.find_element_by_id("idSede").send_keys(Keys.DOWN)
    except:
        pass
    click_button("btnSiguiente")

#if there are no offices to choose from, exit
def no_cita():
    click_button("btnSalir")

#info to be inputted after office selection - last step
def info_compl(tel, email):
    fill_field("txtTelefonoCitado", tel)
    fill_field("emailUNO", email)
    fill_field("emailDOS", email)
    click_button("btnSiguiente")

def run():
    driver.get("https://sede.administracionespublicas.gob.es/icpplustieb/index/")
    try:
        while True:
            sol_cita(city, nie_option, nie, name, country, expiry)
            try:
                office_page()
                info_compl(tel, email)
                if not driver.getPageSource().contains("no hay citas disponibles"):
                    os.system('play -nq -t alsa synth 1 sine 440') #This sound is not very loud, can probably change to something else
                    print("found cita!")
                    os.system('notify-send "Found Cita!!!!"')
                    break
                else:
                    click_button("btnSubmit")
            except:
                try:
                    click_button("btnSubmit")
                except:
                    no_cita()
    except KeyboardInterrupt:
        WebDriverWait(driver, 60)

run()