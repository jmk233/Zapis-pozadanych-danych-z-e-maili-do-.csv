# Save email data to csv with python
This is my first program that I made in Python.

A program that downloads e-mails from the mailbox, then I select the part of each e-mail that interests me and save it in a selected format to a .csv file

A simple program for the automation and transparent visualization of the status of computer backups.
I used Veeam Backup to make the backup:
https://www.veeam.com/pl
After proper configuration - giving the appropriate name for the copy task, in my case it was the name of the client, setting the sending of e-mails after making a copy with the information:
[SUCCESS], [WARNING], [FAILED]. I configured myself so that the subject of the e-mail is: Client XXX - [FAILED].
I also needed to extract the date of each e-mail.

The first step is to use a ready-made script to download e-mails, there are many of them, I will not paste / show it. Perhaps they are better / easier. However, the one I used downloaded all e-mails with all the data, my program was to extract what I needed from this e-mail:
- customer name
- date of the copy

I wanted to shorten the entry, so I used a condition that put three options 'ok', 'not ok' or 'check' in the 'status' table in case of finding 'success', 'failed' or 'warning' in the e-mail subject.

Then I needed the current date and the difference of dates, because sometimes the copy was not done at all, i.e. the computer was turned off. I needed some simple informer that the copy is not made, for example, for more than 3 days (because, for example, it was not made after the weekend).

The last problem was filtering the content so that one client has only one row in the sheet - I am not interested in whether the client's copy was made a week ago or what status it had at that time, I am interested in its last status or when the last time it was done.

I placed the data arranged in this way in the .csv file, separated by a comma, arranged in the appropriate columns:

Subject; Status; Date; Today's Date; How many days since the last copy

Each new e-mail is written on the next line. For my own, I uploaded a convenient .csv file to the ftp server, where I formatted it with the php language into an html table and used it as a template in Wordpress. Using javascript, I colored the 'status' fields (ok green, not red) and the number over 3 days from the last copy (also red).

I now have an up-to-date inspection of copies with my customers on hand. 


---
Polish version:

To mój pierwszy program, który zrobiłem w Pythonie.

Program, który pobiera maile ze skrzynki, potem wybieram interesującą mnie cześć każdego maila i zapisuję w wybranej formi do pliku .csv

Prosty program do automatyzacji i przejrzystej wizualizacji statusów wykonywanych kopii zapasowych komputerów.
Do wykonywania kopii używałem programu Veeam Backup:
https://www.veeam.com/pl
Po odpowiednim skonfigurowaniu - nadaniu odpowiedniej nazwy dla zadania kopii, w moim przypadku była to nazwa klienta, ustawieniu wysyłki maili po wykonaniu kopii z informacją:
[SUCCESS], [WARNING], [FAILED]. Skonfigurowałem sobie tak, że temat maila to: Klient XXX - [FAILED]. 
Potrzebowałem także z każdego maila wyjąć jego datę. 

Pierwszy krok to użycie gotowego skryptu do pobierania maili, jest ich wiele, nie będęgo wklejał/pokazywał. Być może są lepsze/łatwiejsze. Natomiast ten, który użyłem pobierał mi wszystkie maile z wszystkimi danymi, mój program miał za zadanie wyjąć z tego maila to co potrzebowałem:
- nazwę klienta
- datę kopii

Chciałem skrócić zapis, więc zastosowałem warunek wpisujący do tabeli 'status' trzy możliwości 'ok', 'nie ok' lub 'sprawdź' w przypadku znalezienia w temacie maila odpowiednio 'success' , 'failed' lub 'warning'.

Następnie potrzebowałem aktualnej daty oraz różnicy dat, bo czasami kopia się np. w ogóle nie wykonała tj. komputer był wyłączony. Potrzebowałem jakiegoś prostego informatora, że kopia nie wykonuje się np. powyżej 3 dni (bo np. nie zrobiła się po weekendzie). 

Ostatnim problemem było odfiltrowanie zawartości tak, by jeden klient miał tylko jeden wiersz w arkuszu - nie interesuje mnie czy kopia u danego kllienta wykonała się tydzień temu albo jaki miała wtedy status, interesuje mnie jej ostatni status albo kiedy ostatni raz się wykonała. 

Tak ułożone dane umieszczałem w pliku .csv oddzielone przecinkiem, uporządkowane w odpowiednich kolumnach:

Temat;Status;Data;Dzisiejsza data;Ile dni od ostatniej kopii

Każdy nowy mail zapisuje się w kolejnym wierszu. Dla właśnej wygodny plik .csv wrzucałem jeszcze na serwer ftp, gdzie formatowałem go za pomocą języka php do tabeli w html i użyłem jako szablon podstorny w Wordpressie. Za pomocą javascript pokolorowałem sobie pola 'status' (ok zielone, nieok czerwone) oraz liczbę powyżej 3 dni od ostantniej kopii (też czerwono). 

Mam teraz pod ręką zawsze dostępny aktualny przegląd kopii u klientów.
