from fpdf import FPDF
import calendar
from datetime import datetime
from fpdf.enums import XPos, YPos  # Importar las nuevas posiciones

class BulletJournalPDF(FPDF):
    def __init__(self, title=""):
        super().__init__()
        self.title = title  # Inicializamos el título

    def header(self):
        # Header con el título en cada página
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    def add_monthly_view(self, year, month, mes):
        # Agregar la página con el calendario mensual
        self.add_page()
        self.title = f"{mes} de {year}"
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        # Nombres de los días de la semana en español
        days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        day_width, day_height = 40, 30
        self.set_font('Helvetica', 'B', 12)

        # Cabecera con los días de la semana
        for day in days_of_week:
            self.cell(day_width, day_height, day, border=1, align='C')
        self.ln(day_height)  # Salto de línea después de la cabecera

        # Obtener el calendario del mes
        cal = calendar.monthcalendar(year, month)
        self.set_font('Helvetica', '', 12)

        # Imprimir las semanas del calendario
        for week in cal:
            for day in week:
                if day != 0:
                    # Celda con el número del día
                    self.set_font('Helvetica', '', 8)
                     # Crear una celda para el día
                    self.cell(day_width, day_height, '', border=1, align='C')
                    # Ajustar la posición para colocar el número del día en la parte superior derecha
                    self.cell(10, 5, str(day), border=0, align='R')  # Número del día alineado a la derecha
                else:
                    # Celda vacía para días fuera del mes
                    self.cell(day_width, day_height, '', border=1, align='R')
            self.ln(day_height)  # Salto de línea después de cada semana

# Crear el bullet journal para el mes actual
year = datetime.now().year
month = datetime.now().month
months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
mes = months[month-1]

# Generar el PDF
pdf = BulletJournalPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Añadir vista mensual
pdf.add_monthly_view(year, month, mes)

# Guardar el PDF en un archivo
archivo = f"bullet_journal_mes_{year}_{month}.pdf"
pdf.output(archivo)

print(f"PDF {archivo} generado correctamente!")
