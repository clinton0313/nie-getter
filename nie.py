from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

driver = webdriver.Firefox()

#Enter Personal info here
nie = ""
name = ""
country = "CANADA" #Country in all caps - needs to match the site
expiry = ""
tel = ""
email = ""
city = "Barcelona" 

#scroll to bottom of page
def wait(time):
    WebDriverWait(driver, time)
def scroll():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#click button after scrolling to bottom of page
def click_button(btnid):
    scroll()
    driver.find_element_by_id(btnid).click()

#select option from a drop down menu
def select_option(menu_id, option):
    select = Select(driver.find_element_by_id(menu_id))
    select.select_by_visible_text(option)

#fill a text field
def fill_field(fld_id, text):
    field = driver.find_element_by_id(fld_id)
    field.send_keys(text)

#open the nie website
def start():
    driver.get("https://sede.administracionespublicas.gob.es/icpplustieb/index/")

#fill in and continue on the select city page
def city_page(city):
    select_option("form", city)
    click_button("btnAceptar")

#choose the correct type of appointment for NIE page
def appointment_page():
    scroll()
    select_option("tramiteGrupo[0]", "POLICIA-TOMA DE HUELLAS (EXPEDICIÓN DE TARJETA) Y RENOVACIÓN DE TARJETA DE LARGA DURACIÓN")
    click_button("btnAceptar")
#could make this better

#conditions page after appointment page
def conditions_page():
    click_button("btnEntrar")

#inpiut basic info to ask for appointment
def info_page(nie, name, country, expiry):
    fill_field("txtIdCitado", nie)
    fill_field("txtDesCitado", name)
    select_option("txtPaisNac", country)
    #fill_field("txtFecha", expiry)
    click_button("btnEnviar")

#ask for an appointment
def sol_cita():
    click_button("btnEnviar")

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
    start()
    city_page(city)
    appointment_page()
    conditions_page()
    info_page(nie, name, country, expiry)
    sol_cita()
def office():
    office_page()
    info_compl(tel, email)

start()
try:
    while True:
        city_page(city)
        appointment_page()
        conditions_page()
        info_page(nie, name, country, expiry)
        sol_cita()
        try:
            office_page()
            info_compl(tel, email)
            if not driver.getPageSource().contains("no hay citas disponibles"):
                os.system('play -nq -t alsa synth 1 sine 440')
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
    wait(60)

#error page URL https://sede.administracionespublicas.gob.es/icpplustieb/acOfertarCita

#office selection page URL is https://sede.administracionespublicas.gob.es/icpplustieb/acCitar

#for the info_compl page URL is https://sede.administracionespublicas.gob.es/icpplustieb/acVerFormulario

#could get generic back page: https://sede.administracionespublicas.gob.es/icpplustieb/infogenerica
#use click_button("btnSubmit") if so