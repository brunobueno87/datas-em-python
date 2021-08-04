from datetime import date, timedelta, datetime

date_menos_um = date.today() - timedelta(days=1)
dia = date_menos_um.strftime('%d')
mes = date_menos_um.strftime('%m')
ano = date_menos_um.strftime('%Y')

print(date_menos_um.strftime('%d-%m-%Y'))
