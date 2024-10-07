'''
Crea un Bullet Journal en PDF con la vista mensual y una página por cada día del mes actual.
La idea es que puedas imprimirlo y usarlo como agenda personalizada.
'''
from fpdf import FPDF
import calendar
from datetime import datetime
from fpdf.enums import XPos, YPos  # Importar las nuevas posiciones

class BulletJournalPDF(FPDF):
    def __init__(self, title=""):
        super().__init__()
        self.title = title  # Atributo 'title' inicializado

    def header(self):
        # Header con el título en cada página
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    def add_monthly_view(self, year, month, mes):
        # Vista mensual (primera página) con cuadrados para cada día
        self.add_page()
        self.title = f"{mes} de {year}"
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        # Agregar los nombres de los días de la semana en español
        days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        day_width, day_height = 40, 30
        self.set_font('Helvetica', 'B', 12)

        for day in days_of_week:
            self.cell(day_width, day_height, day, border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
        self.ln(day_height)  # Salto de línea después de la cabecera de los días

        # Obtener el calendario del mes
        cal = calendar.monthcalendar(year, month)
        self.set_font('Helvetica', '', 12)

        for week in cal:
            for day in week:
                if day != 0:
                    # Celda vacía con número pequeño en la esquina superior derecha
                    self.set_font('Helvetica', '', 8)  # Número del día pequeño
                    self.cell(day_width, day_height, str(day), border=0, align='R')
                    self.cell(10, 5, str(day), border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='R')
                    self.set_font('Helvetica', '', 12)  # Volver al tamaño normal
                else:
                    self.cell(day_width, day_height, '', border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
            self.ln(day_height)  # Salto de línea después de cada semana

    def add_daily_pages(self, year, month):
        # Añadir una página por cada día del mes
        num_days = calendar.monthrange(year, month)[1]

        for day in range(1, num_days + 1):
            self.add_page()
            diaSemana = days_of_week[calendar.weekday(year, month, day)]
            self.title = f'{diaSemana}, {day} de {mes} de {year}'  # Título por día
            self.set_font('Helvetica', 'B', 16)
            # Santo del día
            self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
            self.set_font('Helvetica', '', 12)
            self.cell(0, 10, 'Santo del día', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
            self.cell(0, 20, 'Tareas:', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.cell(0, 20, 'Eventos:', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.cell(0, 20, 'Notas:', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            
 #           self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

# Crear un bullet journal para el mes actual
year = datetime.now().year
month = datetime.now().month
months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
mes = months[month-1]
days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

pdf = BulletJournalPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Añadir vista mensual
pdf.add_monthly_view(year, month, mes)  # Pasar 'mes' como argumento

# Añadir páginas diarias
pdf.add_daily_pages(year, month)

# Guardar el PDF en un archivo
archivo = f"bullet_journal{year}{month}.pdf"
pdf.output(archivo)

print(f"PDF {archivo} generado correctamente!")
