

import time
from plyer import notification
 if __name__ == '__main__':
 	while True:
 		notification.notify(
 			title = "**Please Drink Water Now!!",
 			message ="Please Drink Water",
 			app_icon = "path to your .ico file",
 			timeout= 12
 			)
 		#	time.sleep(6)
 			time.sleep(60*60)
