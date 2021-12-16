import xlwings as xw
import openpyxl
from datetime import date
import os
from pathlib import Path

filepath = r"\\Apckranefa01pv\apckr001\CKR\APCKRMFLPT001P\G_Drive\Groups\QA\SQT by QE\MODULES\TeleBot\QC Molding System for Telebot.xlsm"

parentDir = "//Apckranefa01pv/apckr001/CKR/APCKRMFLPT001P/G_Drive/Groups/QA/SQT by QE/MODULES/TeleBot/"
dateDir = str(date.today())
link = os.path.join(parentDir, dateDir)
p = Path(link)

if p.exists() == True:
    dirExist = True
    print("Exist")
else:
    os.mkdir(link)
    print(link)


def runSave(path):
    app = xw.App(visible=True, add_book=False)
    wb = app.books.open(filepath)
    run = wb.app.macro("SQL_Server.runs")
    run()

    wb.save()
    if len(wb.app.books) == 1:
        wb.app.quit()
    else:
        wb.close()

    wb = openpyxl.load_workbook(filepath)

    sheets = wb.sheetnames

    for s in sheets:
        print(s)
        if s != 'MAIN':
            sheet_name = wb.get_sheet_by_name(s)
            wb.remove_sheet(sheet_name)

    if p.exists() == True:
        savedXl = fr'{link}/ScheduleToday.xlsx'
        wb.save(savedXl)
        return savedXl
    else:
        print("No Such Directory")
        return None


# runSave(filepath)

class Movie():
    def __init__(self, movie_title, movie_stroyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_stroyline
        self.poster_image_url = poster_image
        self.trailer_yourube_url = trailer_youtube

toy_story = Movie("Marvel", "A story", "www.google.com", "www.youtube.com")
print(Movie("Marvel", "A story", "www.google.com", "www.youtube.com").storyline)