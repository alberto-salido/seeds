from linkedin_api import Linkedin

import json
import sys

print("         #o#")
print("       ####o#")
print("      #o# \#|_#,#")
print("     ###\ |/   #o#      ___  ___  ___  __   ___  ")
print("      # {}{      #     / __|| __|| __||  \ / __| ")
print("         }{{           \__ \| __|| __|| D |\__ \ ")
print("        ,'  `          |___/|___||___||__/ |___/ ")
print("-------------------------------------------------------")
print("Social engEEring and Data extraction in Social networks")
print("-------------------------------------------------------")
print("Alberto Salido")
print("     July 2021\n\n")

ES_LOGIN_NAME = "Indique su nombre de usuario de LinkedIn:"
ES_LOGIN_PASSWORD = "Indique su contraseña de LinkedIn:"

ES_SEARCH_USER_MSG = "Nombre de la persona a buscar en LinkedIn:\n"
ES_USER_PROFILE_MSG = "Nombre el identificador de LinkedIn:\n"
ES_SELECT_OPTION_MSG = "Selecciona una opción:\n 1) Buscar usuarios en Linkedin.\n 2) Obtener información de un usuario.\n 0) Salir.\n"

class bcolors:
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ES_ERROR_LOGIN = "Ouch! El nombre de usuario o contraseña no es válido!"

# Prompts for username and password to login into LinkedIn
username = input(ES_LOGIN_NAME)
password = input(ES_LOGIN_PASSWORD)

# Access to the LinkedIn-Api
try:
	api = Linkedin(username, password)
except Exception:
	print(bcolors.FAIL, ES_ERROR_LOGIN, bcolors.ENDC)
	exit()

# User logged succesfuly
print(api)



  


