
## OSINT-tool konteinerio paleidimo ir naudojimo instrukcija

### 1. Įrankio paskirtis
osint-tool yra OSINT domeno analizės Flask aplikacija, veikiantis Docker konteineryje. Aplikacija leidžia vartotojui patikrinti DNS informaciją, WHOIS ir SSL sertifikatų duomenis, susijusius su pasirinktu domenu.	
### 2. Funkcionalumas
• Web sąsaja, leidžianti vartotojui įvesti domeną ir matyti analizės rezultatus naršyklėje.
• REST API (/osint?domain=example.com), kuris pateikia analizės rezultatus JSON formatu.
	
### 3. Docker konteinerio paleidimas


    docker run -p 5000:5000 atomux/osint-tool:latest
    
Paleidimui per Docker Compose su Caddy reverse proxy naudokite docker-compose.yml ir Caddyfile failus. Paleidimo komanda:

    docker compose up -d

### 4. Aplikacijos naudojimas
Aplikacija pasiekiama naršyklėje adresu: [http:/localhost:5000](http://localhost:5000)
API užklausa [http://localhost:5000/osint?domain=example.com](http://localhost:5000/osint?domain=example.com)

Docker compose atveju adresu: [http:/localhost](http://localhost)
API užklausa:  API užklausa [http://localhost/osint?domain=example.com](http://localhost:5000/osint?domain=example.com)

