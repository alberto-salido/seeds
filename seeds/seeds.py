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
ES_SELECT_TWEEPY_FILE_MSG = "Seleccione el directorio donde se encuentra la configuración de Tweepy.\nPara usar la configuración por defecto, pulse ENTER:"

ES_SEARCH_USER_MSG = "Nombre de la persona a buscar en LinkedIn:\n"
ES_USER_PROFILE_MSG = "Nombre el identificador de LinkedIn:\n"

# System error messages
ES_ERROR_LOGIN_MSG = "Ouch! El nombre de usuario o contraseña no es válido!"
ES_ERROR_CONFIG_FILE_MSG = "Ouch! No se encuentra el fichero de configuración de Tweepy o su formato no es el correcto.\n"

# Constants
DEFAULT_TWEEPY_CONFIG = "tweepy.conf"


def read_tweepy_config_file(filename=DEFAULT_TWEEPY_CONFIG):
	"""
	Reads the content of the information needed for Tweepy.
	For security reasons this information should be never hardcoded,
	so for the proper use create a file with the next structure:

		Private information about Twitter API.
		api_key=QwErTy...
		api_secret_key=QwErTy...
		access_token=QwErTy...
		access_token_secret=QwErTy....

	The diferent parameter can be found in your Twitter application.

    Parameters
    ----------
    filename : str, optional
        Path for the configuration file.
        Dafault: uses the configuration stored current folder
        'tweepy.conf'

    Returns
    -------
    Dictionary
    	A dictionary with the infomation in the configuration file.
    	Ex: 
	    	dic = {
				"api_key" : "QwErTy..."
				"api_secret_key" : "QwErTy..."
				"access_token" : "QwErTy..."
				"access_token_secret" : "QwErTy....	"
	    	}
    """
	try:
		f = open(filename, 'r')
	except Exception as e:
		print(bcolors.FAIL, ES_ERROR_CONFIG_FILE_MSG, bcolors.ENDC)
		exit()

	try:
		f.readline() # header line. not usefull
		tweepy_config = {
			"api_key": f.readline().split('=')[1],
			"api_secret_key": f.readline().split('=')[1],
			"access_token": f.readline().split('=')[1],
			"access_token_secret": f.readline().split('=')[1]
		}
	except Exception as e:
		f.close()
		print(bcolors.FAIL, ES_ERROR_CONFIG_FILE_MSG, bcolors.ENDC)
		exit()

	f.close()
	return tweepy_config



# Application menu
while True:
	decision = input(ES_SELECT_OPTION_MSG)
	if decision == "3":
		exit()
	elif decision == "1":
		print(ES_CONFIGURATION_MSG)
		# TODO: define a function that authenticates the user in both networks
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


		# Access to Tweepy
		# Read Tweepy OAuth tokens from configuration file.
		filename = input(ES_SELECT_TWEEPY_FILE_MSG)
		if (filename == ""):
			tweepy_config = read_tweepy_config_file()
		else:
			tweepy_config = read_tweepy_config_file(filename)

		auth = tweepy.OAuthHandler(tweepy_config["api_key"], tweepy_config["api_secret_key"])
		auth.set_access_token(tweepy_config["access_token"], tweepy_config["access_token_secret"])

		# TODO: Handle error
		twitter_api = tweepy.API(auth)
		print(twitter_api)
		break
	elif decision == "2":
		# TODO: Print help
		pass

print("continuamos por aqui mañana...")