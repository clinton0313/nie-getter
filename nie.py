from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

driver = webdriver.Firefox()

# Enter Personal info here
nie = os.getenv("NIE", "")
passport = os.getenv("PASSPORT", "")
name = os.getenv("FULL_NAME", "")
country = os.getenv("COUNTRY", "")  # Country in all caps - needs to match the site
expiry = os.getenv("EXPIRY", "")
tel = os.getenv("PHONE", "")
email = os.getenv("EMAIL", "")
city = os.getenv("CITY", "Barcelona")
sleep_time_page = int(os.getenv("SLEEP_TIME_PAGE", "5"))
sleep_time_try = int(os.getenv("SLEEP_TIME_TRY", "60"))
mode = os.getenv("MODE", "nie")  # { nie, dni, passport} TODO dni?
nie_option = os.getenv(
    "APPT_TYPE", "POLICIA-CERTIFICADOS Y ASIGNACION NIE (NO COMUNITARIOS)"
)
alert_cli_1 = os.getenv("ALERT_CLI_1", "")
alert_cli_2 = os.getenv("ALERT_CLI_2", "")
alert_cli_3 = os.getenv("ALERT_CLI_3", "")
alert_mode = int(os.getenv("ALERT_MODE", "0"))  # set to 1 to enable
test_mode = int(os.getenv("TEST_MODE", "0"))  # set to 1 to force "found" to test

# scroll to bottom of page
def wait(time):
    WebDriverWait(driver, time)


def scroll():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# click button after scrolling to bottom of page
def click_button(btnid):
    scroll()
    driver.find_element_by_id(btnid).click()


# select option from a drop down menu
def select_option(menu_id, option):
    select = Select(driver.find_element_by_id(menu_id))
    select.select_by_visible_text(option)


# fill a text field
def fill_field(fld_id, text):
    field = driver.find_element_by_id(fld_id)
    field.send_keys(text)


# open the nie website
def start():
    driver.get("https://sede.administracionespublicas.gob.es/icpplustieb/index/")


# fill in and continue on the select city page
def city_page(city):
    select_option("form", city)
    click_button("btnAceptar")


# choose the correct type of appointment for NIE page
def appointment_page():
    scroll()
    select_option("tramiteGrupo[0]", nie_option) #Select apppointment type
    click_button("btnAceptar")


# could make this better

# conditions page after appointment page
def conditions_page():
    click_button("btnEntrar")


# inpiut basic info to ask for appointment
def info_page(nie, name, country, expiry):
    fill_field("txtIdCitado", nie)
    fill_field("txtDesCitado", name)
    select_option("txtPaisNac", country)
    # fill_field("txtFecha", expiry)
    click_button("btnEnviar")


def info_page_passport(passport, name):
    click_button("rdbTipoDocPas")
    fill_field("txtDesCitado", name)
    fill_field("txtIdCitado", passport)
    click_button("btnEnviar")


# ask for an appointment
def sol_cita():
    click_button("btnEnviar")


# Select second office because it could return a single preselcted office or multiple where you have to make a choice
def office_page():
    try:
        driver.find_element_by_id("idSede").send_keys(Keys.DOWN)
    except:
        pass
    click_button("btnSiguiente")


# if there are no offices to choose from, exit
def no_cita():
    click_button("btnSalir")


# info to be inputted after office selection - last step
def info_compl(tel, email):
    fill_field("txtTelefonoCitado", tel)
    fill_field("emailUNO", email)
    fill_field("emailDOS", email)
    click_button("btnSiguiente")


# def run():
#     start()
#     city_page(city)
#     appointment_page()
#     conditions_page()
#     # info_page(nie, name, country, expiry)
#     info_page_passport(passport, name)
#     sol_cita()
def office():
    office_page()
    info_compl(tel, email)


start()
tries = 0
try:
    while True:
        tries = tries + 1
        print("---- start [", tries, "] ----")
        city_page(city)
        time.sleep(sleep_time_page)
        print("appt")

        appointment_page()
        time.sleep(sleep_time_page)
        print("cond")

        conditions_page()
        time.sleep(sleep_time_page)
        print("info")

        if mode == "nie":
            info_page(nie, name, country, expiry)
        elif mode == "passport":
            info_page_passport(passport, name)
        else:
            print("Need to set Mode to nie, passport, etc")
            break

        time.sleep(sleep_time_page)
        print("sol cita")

        sol_cita()
        try:
            # office_page()
            # info_compl(tel, email)
            if test_mode or not ("no hay citas disponibles") in driver.page_source:
                # os.system('play -nq -t alsa synth 1 sine 440')
                print("found cita!")
                if alert_mode:
                    if len(alert_cli_1):
                        os.system(alert_cli_1)
                    if len(alert_cli_2):
                        os.system(alert_cli_2)
                    if len(alert_cli_3):
                        os.system(alert_cli_3)
                break
            # else:
            #     print("click submit [a]")
            #     click_button("btnSalir")
        except AssertionError as error:
            print(error)
            try:
                print("click submit [b]")
                click_button("btnSalir")
            except:
                print("no cita?")
                no_cita()
        print("sleeping...")
        time.sleep(sleep_time_try)
        print("click submit [a]")
        click_button("btnSalir")
        print("again..!")

except KeyboardInterrupt:
    wait(60)

# error page URL https://sede.administracionespublicas.gob.es/icpplustieb/acOfertarCita

# office selection page URL is https://sede.administracionespublicas.gob.es/icpplustieb/acCitar

# for the info_compl page URL is https://sede.administracionespublicas.gob.es/icpplustieb/acVerFormulario

# could get generic back page: https://sede.administracionespublicas.gob.es/icpplustieb/infogenerica
# use click_button("btnSubmit") if so
