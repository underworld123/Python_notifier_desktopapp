import time
import notify2

# path to notification window icon 
ICON_PATH = "put full path to icon image here"

# initialise the d-bus connection 
# D-Bus is a message bus system, a simple way for applications to talk to one another.
notify2.init("Python notifier")

# create Notification object 
# The general syntax:
# notify2.Notification(summary, message='', icon='')
n = notify2.Notification(None)

# set urgency level 
n.set_urgency(notify2.URGENCY_NORMAL) 
  
# set timeout for a notification 
n.set_timeout(10000)

# for newsitem in newsitems: 
  
#     # update notification data for Notification object 
#     n.update(newsitem['title'], newsitem['description']) 
  
#     # show notification on screen 
#     n.show() 
  
#     # short delay between notifications 
#     time.sleep(15) 

n.update("The Python notifier", "hello world description") 
n.show()
