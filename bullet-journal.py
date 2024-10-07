from fpdf import FPDF
import calendar
from datetime import datetime
from fpdf.enums import XPos, YPos  # Importar las nuevas posiciones para evitar advertencias

class BulletJournalPDF(FPDF):
    def __init__(self, title=""):
        super().__init__()
        self.title = title  # Inicializamos el título

    def header(self):
        # Header con el título en cada página
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    def add_monthly_view(self, year, month, mes):
        # Agregar la página con el calendario mensual
        self.add_page()
        self.title = f"{mes} de {year}"
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        # Nombres de los días de la semana en español
        days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        day_width = 27  # Ancho de cada día
        self.set_font('Helvetica', 'B', 12)

        # Cabecera con los días de la semana
        for day in days_of_week:
            self.cell(day_width, 10, day, border=0, new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
        self.ln(10)  # Salto de línea después de la cabecera

        # Obtener el calendario del mes
        cal = calendar.monthcalendar(year, month)
        self.set_font('Helvetica', '', 12)

        # Imprimir las semanas del calendario
        for week in cal:
            for day in week:
                if day != 0:
                    # Mostrar el número del día con bordes y centrado y arriba
                    self.cell(day_width, 20, str(day), border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='L')
                    #self.cell(day_width, 20, str(day), border=1, new_x=XPos.RIGHT, new_y=YPos.TOP, align='T')

                else:
                    # Celda vacía para días fuera del mes
                    self.cell(day_width, 20, '', border=0, new_x=XPos.RIGHT, new_y=YPos.TOP, align='L')
            self.ln(20)  # Salto de línea después de cada semana

    def add_daily_pages(self, year, month):
        # Añadir una página por cada día del mes
        num_days = calendar.monthrange(year, month)[1]
        days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

        for day in range(1, num_days + 1):
            if day != 0:
                self.add_page()
                self.title = f"{mes} de {year}"
                self.set_font('Helvetica', 'B', 16)
                self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
            """
            self.add_page()
            diaSemana = days_of_week[calendar.weekday(year, month, day)]
            self.title = f'{diaSemana}, {day} de {mes} de {year}'  # Título por día
            self.set_font('Helvetica', 'B', 16)
            # Santo del día
            self.set_font('Helvetica', '', 12)
            self.cell(0, 10, 'Santo del día', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
            self.cell(0, 20, 'Tareas:', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.cell(0, 20, 'Eventos:', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.cell(0, 20, 'Notas:', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            """

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

# Añadir páginas diarias
pdf.add_daily_pages(year, month)

# Guardar el PDF en un archivo
archivo = f"bullet_journal{year}{month}.pdf"
pdf.output(archivo)

print(f"PDF {archivo} generado correctamente!")
