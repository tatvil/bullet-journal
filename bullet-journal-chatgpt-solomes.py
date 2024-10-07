from fpdf import FPDF
import calendar
from datetime import datetime

class BulletJournalPDF(FPDF):
    def __init__(self, title=""):
        super().__init__()
        self.title = title  # Inicializamos el título

    def header(self):
        # Header con el título en cada página
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, self.title, 0, 1, 'C')

    def add_monthly_view(self, year, month, mes):
        # Agregar la página con el calendario mensual
        self.add_page()
        self.title = f"{mes} de {year}"
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, self.title, 0, 1, 'C')

        # Nombres de los días de la semana en español
        days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        day_width = 40  # Ancho de cada día
        self.set_font('Helvetica', 'B', 12)

        # Cabecera con los días de la semana
        for day in days_of_week:
            self.cell(day_width, 10, day, 0, 0, 'C')  # Sin bordes y centrado
        self.ln(10)  # Salto de línea después de la cabecera

        # Obtener el calendario del mes
        cal = calendar.monthcalendar(year, month)
        self.set_font('Helvetica', '', 12)

        # Imprimir las semanas del calendario
        for week in cal:
            for day in week:
                if day != 0:
                    # Mostrar el número del día sin bordes y alineado a la izquierda
                    self.cell(day_width, 20, str(day), 0, 0, 'L')
                else:
                    # Celda vacía para días fuera del mes
                    self.cell(day_width, 20, '', 0, 0, 'L')
            self.ln(20)  # Salto de línea después de cada semana

# Crear el bullet journal para el mes actual
year = 2024
month = 10  # Octubre
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
