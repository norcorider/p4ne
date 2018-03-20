from openpyxl import load_workbook
from matplotlib import pyplot

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']


def getvalue(x): return x.value


year = (map(getvalue, sheet['A'][1:]))

listYear = (list(year))

print(listYear)

temp = (map(getvalue, sheet['C'][1:]))

listTemp = (list(temp))

print(listTemp)

sun = (map(getvalue, sheet['D'][1:]))

listSun = (list(sun))

print(listSun)


pyplot.plot(listYear, listSun, label="Sun")
pyplot.plot(listYear, listTemp, label="Temp")

pyplot.show()
