'''
    ---------- RETO 13 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que sea capaz de encontrar la diferencia completa entre dos fechas, mostrando días, horas, minutos y segundos.
'''

from datetime import datetime

def date_diff_in_seconds(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds

def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)


def reto13Avanzado():
  date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

  date2 = datetime.now()

  print("\n%d días, %d horas, %d minutos, %d segundos" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))