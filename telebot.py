import json
import datetime
import requests
import telegram_send

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=2)
date_time = yesterday.strftime("%d.%m.%Y")
with open('file.json', "r") as f:
        data = json.load(f)
        pobor = data['sum']
        pobor_zaokr = round(pobor, 1)
        produkcja = data['OZEValue']
        produkcja_zaokr = round(produkcja, 1)
        roznica = produkcja - pobor


if roznica < 0:
    wynik_produkcji = "Produkcja energii NIE pokryła całkowitego zapotrzebowania na prąd."
else:
    wynik_produkcji = "Produkcja energii POKRYŁA całkowite zapotrzebowania na prąd."


telegram_send.send(messages=["*Informacja o saldzie prądu pobrana z serwerów Tauron z dnia: {}".format(date_time) +"*" "\n" "\n" "Pobór pradu z sieci: {}".format(pobor_zaokr) + "kWh" "\n" "Zwrot pradu do sieci: {}".format(produkcja_zaokr) + "kwh" "\n \n{}".format(wynik_produkcji)], parse_mode= "Markdown")

