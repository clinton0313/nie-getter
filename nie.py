from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
nie = "Y8809001S"
name = "Clinton Leung"
country = "CANADA"
expiry = "16/12/2023"
tel = "658427293"
email = "clinton0313@gmail.com"
city = "Barcelona"
driver = webdriver.Firefox()

def click_button(btnid):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element_by_id(btnid).click()

def select_option(menu_id, option):
    select = Select(driver.find_element_by_id(menu_id))
    select.select_by_visible_text(option)

def fill_field(fld_id, text):
    field = driver.find_element_by_id(fld_id)
    field.send_keys(text)

def start():
    driver.get("https://sede.administracionespublicas.gob.es/icpplustieb/index/")

def city_page(city):
    select_option("form", city)
    click_button("btnAceptar")

def appointment_page():
    tramite_box = driver.find_element_by_id("tramiteGrupo[0]")
    select = Select(tramite_box)
    for n in range(12):
        tramite_box.send_keys(Keys.DOWN)
    tramite_box.send_keys(Keys.RETURN)
    click_button("btnAceptar")
#could make this better

def conditions_page():
    click_button("btnEntrar")

def info_page(nie, name, country, expiry):
    fill_field("txtIdCitado", nie)
    fill_field("txtDesCitado", name)
    select_option("txtPaisNac", country)
    fill_field("txtFecha", expiry)
    click_button("btnEnviar")

def sol_cita():
    click_button("btnEnviar")

def office_page():
    click_button("btnSiguiente")

def no_cita():
    click_button("btnSalir")

start()
city_page(city)
appointment_page()
conditions_page()
info_page(nie, name, country, expiry)