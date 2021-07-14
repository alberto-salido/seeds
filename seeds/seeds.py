from linkedin_api import Linkedin
import tweepy
import json

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
ES_SELECT_OPTION_MSG = "Seleccione una opción:\n 0) Salir.\n 1) Configuración.\n 2) Ayuda.\n"
ES_CONFIGURATION_MSG = "Para configurar la herramienta siga los pasos.\n"
ES_LOGIN_NAME_LINKEDIN_MSG = "Indique su nombre de usuario de LinkedIn:"
ES_LOGIN_PASSWORD_LINKEDIN_MSG = "Indique su contraseña de LinkedIn:"
ES_SELECT_TWEEPY_FILE_MSG = "Seleccione el directorio donde se encuentra la configuración de Tweepy.\nPara usar la configuración por defecto, pulse ENTER:"
ES_SELECT_LINKEDIN_OPTION_MSG = "Seleccione una opción:\n 0) Salir.\n 1) Buscar en LinkedIn.\n 2) Obtener información de una persona en LinkedIn.\n 3) Buscar en Twitter.\n 4) Obtener información de una persona en Twitter.\n 5) Ayuda.\n"
ES_SEARCH_LINKEDIN_USER_MSG = "Nombre de la persona a buscar en LinkedIn:"
ES_LINKEDIN_USER_PROFILE_MSG = "Nombre o identificador(URN) de LinkedIn:"
ES_SEARCH_TWITTER_USER_MSG = "Nombre de la persona a buscar en Twitter:"
ES_SEARCH_TWITTER_PROFILE_MSG = "Identificador de la persona en Twitter:"
ES_CLOSE_MSG = "\nLimpiando la casa...\n Hasta la proxima!"

# System error messages
ES_ERROR_LOGIN_MSG = "Ouch! El nombre de usuario o contraseña no es válido!"
ES_ERROR_CONFIG_FILE_MSG = "Ouch! No se encuentra el fichero de configuración de Tweepy o su formato no es el correcto.\nSaliendo...\n"
ES_ERROR_CONFIG_FILE_FORMAT_MSG = "Ouch! Formato del fichero de configuración de Twitter no es el correcto.\nSaliendo...\n"

# Constants
DEFAULT_TWEEPY_CONFIG = "tweepy.conf"

def login_to_linkedin(username, password):
	"""
	Registers an user with the linkedin-api.
	In case of error shows a message and exit.

	Parameters
	----------
	username: str
		Valid username registered in LinkedIn.
	password: str
		User password.

	Returns
	-------
	Linkedin
		A Linkedin object authenticated to perform request to the API. 
	"""
	try:
		linkedin_api = Linkedin(username, password)
	except Exception:
		print(bcolors.FAIL, ES_ERROR_LOGIN_MSG, bcolors.ENDC)
		exit()

	return linkedin_api

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
		# important! last line should be empty.
		tweepy_config = {
			"api_key": f.readline().split('=')[1][:-1],
			"api_secret_key": f.readline().split('=')[1][:-1],
			"access_token": f.readline().split('=')[1][:-1],
			"access_token_secret": f.readline().split('=')[1][:-1]
		}
	except Exception as e:
		f.close()
		print(bcolors.FAIL, ES_ERROR_CONFIG_FILE_FORMAT_MSG, bcolors.ENDC)
		exit()

	f.close()
	return tweepy_config

def login_to_twitter(tweepy_config):
	"""
	TODO: Comment
	"""
	auth = tweepy.OAuthHandler(tweepy_config["api_key"], tweepy_config["api_secret_key"])
	auth.set_access_token(tweepy_config["access_token"], tweepy_config["access_token_secret"])
	twitter_api = tweepy.API(auth)
	return twitter_api

# Asks for an user. Returns all the coincidences.
def search_linkedin_user(search_string):
	"""
	TODO: Comment
	"""
	people = linkedin_api.search_people(search_string)
	print_json(people, 2)

# Based on one of the previous results shows the information of an user.
def get_linkedin_user(user):
	"""
	TODO: Comment
	"""
	user = linkedin_api.get_profile(user)
	print_json(user, 2)     
            
# Prints JSON data formating it using the <tabs> numbers of spaces.
def print_json(data, tabs):
	"""
	TODO: Comment
	"""
	print(json.dumps(data, indent=tabs))


# Application menu
"""
TODO: Comment
"""
while True:
	decision = input(ES_SELECT_OPTION_MSG)
	if decision == "0":
		exit(ES_CLOSE_MSG)
	elif decision == "1":
		print(ES_CONFIGURATION_MSG)
		# Prompts for username and password to login into LinkedIn
		username = input(ES_LOGIN_NAME_LINKEDIN_MSG)
		password = input(ES_LOGIN_PASSWORD_LINKEDIN_MSG)

		# Access to the LinkedIn-Api. In case of error exits.
		linkedin_api = login_to_linkedin(username, password)

		# Read Tweepy OAuth tokens from configuration file.
		filename = input(ES_SELECT_TWEEPY_FILE_MSG)
		if (filename == ""):
			tweepy_config = read_tweepy_config_file()
		else:
			tweepy_config = read_tweepy_config_file(filename)

		# Access to Tweepy
		twitter_api = login_to_twitter(tweepy_config)
		break
	elif decision == "2":
		# TODO: Print help
		pass


# User search...
"""
TODO: Comment
"""
while True:
	decision = input(ES_SELECT_LINKEDIN_OPTION_MSG)
	if decision == "0":
		exit(ES_CLOSE_MSG)
	elif decision == "1":
		linkedin_search_string = input(ES_SEARCH_LINKEDIN_USER_MSG)    
		search_linkedin_user(linkedin_search_string)
	elif decision == "2":
		linkedin_user = input(ES_LINKEDIN_USER_PROFILE_MSG)
		get_linkedin_user(linkedin_user)
	elif decision == "3":
		twitter_search_string = input(ES_SEARCH_TWITTER_USER_MSG)
		users = twitter_api.search_users(twitter_search_string)
		for user in users:
			print(user.screen_name)
	elif decision == "4":
		twitter_name = input(ES_SEARCH_TWITTER_PROFILE_MSG)
		print_json(twitter_api.get_user(twitter_name)._json, 2)
	#elif decision == "5":
	#	print("Próximamente...\n")
	# 	# TODO
	# 	linkedin_search_string = input(ES_SEARCH_LINKEDIN_USER_MSG)
	# 	twitter_search_string = input(ES_SEARCH_TWITTER_USER_MSG)
	# 	users = linkedin_api.search_people(linkedin_search_string, network_depth='10')
	# 	userdata = {}
	# 	animation = "|/-\\"
	# 	idx = 0
	# 	for user in users:
	# 		userdata.update(linkedin_api.get_profile(user["urn_id"]))
	# 		print("Por favor espere: " + animation[idx % len(animation)], end="\r")
	# 		idx += 1
	# 		#time.sleep(0.1)

	# 	print_json(userdata, 2)
	# 	df = pd.DataFrame(userdata)
	# 	df.to_excel('./DATAFILE.xlsx')

	elif decision == "5":
		# TODO: Print help
		pass


