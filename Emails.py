import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
Purpose: Sends the email to the recipient
Parameters: Message - the message that was gotten from the read file
'''
def send(body):
    msg = MIMEMultipart()
    msg['From'] = 'xaveayk@gmail.com'
    msg['To'] = 'xaveayk@gmail.com'
    password = "(Raiders753)"
    msg['Subject'] = "It works!!!"
    msg.attach(MIMEText(body, 'html'))
    print(msg)
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

'''
Purpose: To create the email from the text file as its a lot easier to craft it 
         in a text file
Parameters: filename - the name of the file to be opened and read from
'''
def create_string(filename):
    if not isinstance(filename, str): raise TypeError
    if filename[-4:] != '.txt':
        if '.txt' in filename: filename = filename.replace('.txt', '')
        if '.txt' not in filename: filename += '.txt' #ensures .txt    
        
    try: file = open(filename) #Tries to open the filename
    except: raise Exception("File name does not exist as inputted.") #if the file can't be opened, exception    
    
    files = file.read() #Reads the info in the file
    file.close() #Closes the file so it can't be changed or read from again  
    
    main(files)