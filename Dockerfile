# Pasirenkame Image
FROM python:3.11-slim
#Nustatome darbo kataloga
WORKDIR /osint
#Instaliuojame git
RUN apt-get update && apt-get install -y git && apt-get clean
#Klonuojame git repositorija
RUN git clone https://github.com/4tomux/osint-tool.git .
#Kopijuojame failus
COPY app /osint-tool/app
#Keiciame darbini kataloga
WORKDIR /osint-tool/app
#Intaliuojame reikalingas python bibliotekas
RUN pip install --no-cache-dir -r requirements.txt
#Atidarome prievada
EXPOSE 5000
#Paleidziame aplikacija
CMD ["python", "main.py"]
