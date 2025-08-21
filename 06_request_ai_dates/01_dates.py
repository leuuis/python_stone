# Trabajando con fechas y horas en Python

from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")  # Configurar el locale a español

now = datetime.now()
print(f"Fecha y hora actual: {now}")

# 2. Crear una fecha específica y hora
specific_date = datetime(2025, 10, 1, 12, 15, 30, 0)
print(f"Fecha específica: {specific_date}")

# 3. Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato especificado
# formato: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
formatted_date = now.strftime("%A, %d de %B de %Y %H:%M:%S %%porque quiero y puedo")
print(f"Fecha formateada: {formatted_date}")

# 4. Operaciones con fechas
# sumar o restar días, horas, minutos, etc.
# usar timedelta para realizar operaciones con fechas
tomorrow = now + timedelta(days=0.5, horas=2) # 2 hours later
print(f"Mañana será: {tomorrow}")
next_week = now + timedelta(weeks=1)
print(f"La próxima semana será: {next_week}")
yesterday = now - timedelta(days=1)
print(f"Ayer fue: {yesterday}")

# 5. Obtener componentes individuales de una fecha
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print(f"Año: {year}, Mes: {month}, Día: {day}, Hora: {hour}, Minuto: {minute}, Segundo: {second}")

# 6. Calcular la diferencia entre dos fechas
my_last_birthday = datetime(2025, 1, 16)
now = datetime.now()
difference = my_last_birthday - now
print(f"Diferencia entre mi último cumpleaños y ahora: {difference.days} \n{difference.days} días, {difference.seconds // 3600} horas, {(difference.seconds // 60) % 60} minutos")