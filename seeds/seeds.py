from linkedin_api import Linkedin
import tweepy
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
print("                                         Alberto Salido")
print("                                  alberto.026@gmail.com")
print("                                              July 2021")
print("-------------------------------------------------------")

# Text colors
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

# System messages
ES_SELECT_OPTION_MSG = "Seleccione una opción:\n 1) Configuración.\n 2) Ayuda.\n 3) Salir.\n"
ES_CONFIGURATION_MSG = "Para configurar la herramienta siga los pasos.\n"
ES_LOGIN_NAME_LINKEDIN_MSG = "Indique su nombre de usuario de LinkedIn:"
ES_LOGIN_PASSWORD_LINKEDIN_MSG = "Indique su contraseña de LinkedIn:"

ES_SEARCH_USER_MSG = "Nombre de la persona a buscar en LinkedIn:\n"
ES_USER_PROFILE_MSG = "Nombre el identificador de LinkedIn:\n"

# System error messages
ES_ERROR_LOGIN_MSG = "Ouch! El nombre de usuario o contraseña no es válido!"


# Application menu
while True:
	decision = input(ES_SELECT_OPTION_MSG)
	if decision == "3":
		exit()
	elif decision == "1":
		print(ES_CONFIGURATION_MSG)
		# TODO define a function that authenticates the user in both networks
		# Access to the LinkedIn-Api
		# Prompts for username and password to login into LinkedIn
		# WARNING! Remove user/pass
		username = input(ES_LOGIN_NAME_LINKEDIN_MSG)
		password = input(ES_LOGIN_PASSWORD_LINKEDIN_MSG)

		try:
			linkedin_api = Linkedin(username, password)
		except Exception:
			print(bcolors.FAIL, ES_ERROR_LOGIN_MSG, bcolors.ENDC)
			exit()

		# User logged succesfuly
		print(linkedin_api)


		#Access to Tweepy

		# Tweepy OAuth tokens 
		# TODO: Read from configuration file.
		api_key = ''
		api_secret_key = ''
		access_token = ''
		access_token_secret = ''

		auth = tweepy.OAuthHandler(api_key, api_secret_key)
		auth.set_access_token(access_token, access_token_secret)

		# TODO: Handle error
		twitter_api = tweepy.API(auth)
		print(twitter_api)
		break
	elif decision == "2":
		# TODO Print help
		pass

print("continuamos por aqui mañana...")