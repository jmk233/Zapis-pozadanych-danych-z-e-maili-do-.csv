# Save email data to csv with python

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
