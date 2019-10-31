import logging

#Create and configure logger 
logging.basicConfig(filename="newfile.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 

#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG
#NOTSET     0
#DEBUG      10
#INFO       20
#WARNING    30
#ERROR      40
#CRITICAL   50
logger.setLevel(logging.DEBUG)
  
#Test messages 
logger.debug("This is a DEBUG message") 
logger.info("This is an INFO message") 
logger.warning("This is a WARNING mesage") 
logger.error("This is an ERROR message") 
logger.critical("This is a CRITICAL message") 
