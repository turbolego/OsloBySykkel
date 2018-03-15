# OsloBySykkel
Oversikt over Oslo Bysykkel sine sykkler som liste med sorteringsmulighet!
Man kan trykke på tabbene "Lokasjon", "Identifiksjon", "Sykkellåser" og "Sykkler" for å sortere dataene.
F.eks. kan man sortere etter "Sykkler" for å sortere etter hvilken holdeplass som har flest sykkler akkurat nå.

# Du må ha:
1. [Python 2.7](https://www.python.org/)
2. Bibliotek: [Requests](http://docs.python-requests.org/en/master/)
3. Bibliotek: [wxPython](https://www.wxpython.org)

# Hvordan kjøre:

1. Gå til https://developer.oslobysykkel.no og skaff deg en ID hvis du ikke har fra før:

![Skjermskudd DeveloperSiden](https://raw.githubusercontent.com/turbolego/OsloBySykkel/master/DeveloperSiden.png)

2. Stapp inn din ID i headers_stations og headers_availability hvor det står "Your ID Goes Here":

![Skjermskudd DeveloperSiden](https://raw.githubusercontent.com/turbolego/OsloBySykkel/master/OsloBySykkelID.png)

3. Kjør OsloBySykkel.py fra cmd.exe (Windows) eller fra terminal ved å navigere til mappen hvor OsloBySykkel.py ligger og kjøre "python OsloBySykkel.py":

![Skjermskudd DeveloperSiden](https://raw.githubusercontent.com/turbolego/OsloBySykkel/master/HvordanKjøre.png)

4. Du vil nå få et vindu som viser en oversikt over Oslo sine Bysykkler!

# Sortering av holdeplassene alfabetisk:
![Skjermskudd alfabetisk](https://raw.githubusercontent.com/turbolego/OsloBySykkel/master/alfabetisk.png)

# Sortering ut ifra holdeplass-ID:
![Skjermskudd ID](https://raw.githubusercontent.com/turbolego/OsloBySykkel/master/Identifikasjon.png)

# Sortering ut ifra antall låser:
![Skjermskudd låser](https://raw.githubusercontent.com/turbolego/OsloBySykkel/master/låser.png)

# Sortering ut ifra antall sykkler:
![Skjermskudd låser](https://raw.githubusercontent.com/turbolego/OsloBySykkel/master/sykkler.png)

# Ting som må fikses i denne versjonen:
1. Finne en bedre metode for å filtre ut holdeplassene fra availability json som har "-1" låser og "-1" sykkler, og som ikke finnes i json-data fra stations json.
2. Forbedre sorteringsmetode for listene.
3. Legge til tab for gps-lokasjon med link til google maps for lokasjon.
4. Pakke koden til en kjørbar .exe for bedre brukervennlighet.
5. Bytte fra wxPython til Kivy og kompilere android/ios app for mobil.

# Mulig bug i json-dataene:
Disse stasjonene finnes bare i json dataene fra "GET /stations/availability" men ikke i dataene fra "GET /stations".
Muligens en bug?

![Skjermskudd bug](https://raw.githubusercontent.com/turbolego/OsloBySykkel/master/bug.png)
