

# Krypt0n luv colors
# Krypt0n luvs making sexy scripts
# Be like Krypt0n ;-)

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERL = '\033[4m'
	ENDC = '\033[0m'
	backBlack = '\033[40m'
	backRed = '\033[41m'
	backGreen = '\033[42m'
	backYellow = '\033[43m'
	backBlue = '\033[44m'
	backMagenta = '\033[45m'
	backCyan = '\033[46m'
	backWhite = '\033[47m'

class status:
	OK = color.BLUE + '[*]' + color.ENDC
	FAIL = color.YELLOW + '[!]' + color.ENDC
	ERROR = color.RED + '[-]' + color.ENDC
	SUCCESS = color.GREEN + '[+]' + color.ENDC

def list(number, text):
	print color.GREEN + str(number) + ". " + color.ENDC + text 