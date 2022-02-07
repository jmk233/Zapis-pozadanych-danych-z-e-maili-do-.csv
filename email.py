# Importing libraries
import imaplib, email
import csv 
import datetime
import ftplib

user = 'xxx'
password = 'xxx'
imap_url = 'xxx'
 
# tu kod pobieranie e-maili, zakończony jako msgs, pobieramy maile wysłane z adresu, który ustawiłem w programie do kopii
msgs = get_emails(search('FROM', 'xxx@xx.pl', con))


with open('kopie.csv', 'w', newline='') as file:
    data_writer = csv.writer(file, delimiter=';')
    header = ['Temat', 'Status', 'Data', 'Dzisiejsza data', 'Ile dni od ostatniej kopii'] 
    data_writer.writerow(header)   
    for msg in msgs[::-1]:
        for sent in msg:
            if type(sent) is tuple: 
                content = str(sent[1], 'utf-8')
                data = str(content)
            
                indexstart = data.find("Date:")
                indexend = data.find("+0100")
               
                data2 = str((data[indexstart: indexend]))
                weeks = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']     
                if weeks[0] in data2:
                   dataEnd = (data2.removeprefix("Date: Mon, "))
                if weeks[1] in data2:
                   dataEnd = (data2.removeprefix("Date: Tue, "))
                if weeks[2] in data2:
                   dataEnd = (data2.removeprefix("Date: Wed, "))  
                if weeks[3] in data2:
                   dataEnd = (data2.removeprefix("Date: Thu, "))                                       
                if weeks[4] in data2:
                   dataEnd = (data2.removeprefix("Date: Fri, "))   
                if weeks[5] in data2:
                   dataEnd = (data2.removeprefix("Date: Sat, "))                                          
                if weeks[6] in data2:
                   dataEnd = (data2.removeprefix("Date: Sun, "))               
                                 
                subjectstart = data.find("Subject")
                subjectend = data.find("]")
                data3 =  str((data[subjectstart: subjectend]))
                subEnd =  (data3.removeprefix("Subject: "))
                subEnd = subEnd + ']'
                
                if 'Failed' in subEnd:
                    status = 'nie ok'
                if 'Warning' in subEnd:
                    status = 'sprawdz'
                if 'Success' in subEnd:
                    status = 'ok'   
                
                howLong = datetime.datetime.now()
                howLong = (howLong.strftime("%d %b %Y %X"))
                howLong = howLong[0:11]
                dataEnd = dataEnd[0:11]
                
                if howLong > dataEnd:
                    statusDaty = int(howLong[0:2]) - int(dataEnd[0:2])
                    #s = ('Kopia nie wykonała się od')
                    #t = ("dni")
                    #statusDaty = str(statusDaty)
                    #statusDaty = (s  + statusDaty + t)

                if howLong == dataEnd:
                    statusDaty = 'Aktualna!'
                    
                data_csv = [subEnd, status, dataEnd, howLong, statusDaty]
                data_writer.writerow(data_csv)
 

session = ftplib.FTP('xxx.pl','xxxftp','xxx')
file = open('kopie.csv','rb')                  # file to send
session.storbinary('STOR web/kopie.csv', file)     # send the file
file.close()                                    # close file and FTP
session.quit()

