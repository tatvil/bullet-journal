from fpdf import FPDF
import calendar
from datetime import datetime
from fpdf.enums import XPos, YPos  # Importar las nuevas posiciones

class BulletJournalPDF(FPDF):
    def __init__(self, title=""):
        super().__init__()
        self.title = title

    def header(self):
        # Header con el título en cada página
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    def add_monthly_view(self, year, month, mes):
        # Vista mensual con cuadrados para cada día
        self.add_page()
        self.title = f"{mes} de {year}"
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

        # Cabecera con los nombres de los días de la semana en español
        days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        day_width, day_height = 40, 30
        self.set_font('Helvetica', 'B', 12)

        # Cabecera de los días de la semana
        for day in days_of_week:
            self.cell(day_width, day_height, day, border=1, align='C')
        self.ln(day_height)  # Salto de línea después de la cabecera

        # Obtener el calendario del mes
        cal = calendar.monthcalendar(year, month)
        self.set_font('Helvetica', '', 12)

        # Imprimir las semanas
        for week in cal:
            for day in week:
                if day != 0:
                    # Celda con espacio para escribir y número pequeño en la esquina superior derecha
                    self.cell(day_width, day_height, '', border=1, align='L')
                    # Posicionar el número del día
                    self.set_xy(self.get_x() - day_width + day_width - 10, self.get_y() - day_height + 5)
                    self.set_font('Helvetica', '', 8)
                    self.cell(10, 5, str(day), border=0, align='R')
                    self.set_font('Helvetica', '', 12)  # Volver al tamaño normal
                else:
                    # Celda vacía para días fuera del mes
                    self.cell(day_width, day_height, '', border=1, align='L')
            self.ln(day_height)  # Salto de línea después de cada semana

    def add_daily_pages(self, year, month, mes, days_of_week):
        # Añadir una página por cada día del mes
        num_days = calendar.monthrange(year, month)[1]

        for day in range(1, num_days + 1):
            self.add_page()
            dia_semana = days_of_week[calendar.weekday(year, month, day)]
            self.title = f'{dia_semana}, {day} de {mes} de {year}'  # Título por día
            self.set_font('Helvetica', 'B', 16)
            self.cell(0, 10, self.title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

            # Secciones de "Santo del día", "Tareas", "Eventos", "Notas"
            self.set_font('Helvetica', '', 12)
            self.cell(0, 10, 'Santo del día:', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.cell(0, 10, 'Tareas:', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.cell(0, 10, 'Eventos:', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
            self.cell(0, 10, 'Notas:', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')

# Crear un bullet journal para el mes actual
year = datetime.now().year
month = datetime.now().month
months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
mes = months[month-1]
days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

pdf = BulletJournalPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Añadir vista mensual
pdf.add_monthly_view(year, month, mes)

# Añadir páginas diarias
pdf.add_daily_pages(year, month, mes, days_of_week)

# Guardar el PDF en un archivo
archivo = f"bullet_journal_{year}_{month}.pdf"
pdf.output(archivo)

print(f"PDF {archivo} generado correctamente!")
