import openpyxl

# Открываем файл Excel
workbook = openpyxl.load_workbook('./NinzniyNovgorod/NizniyNovgorod.xlsx')
# Выбираем лист, на котором расположены данные
worksheet = workbook.active

# Читаем значения ячеек в строке и преобразуем в массив

Type_Baths = ['финская парная','русская баня','инфракрасная сауна','турецкая парная(хамам)']

for idx,cell in enumerate(worksheet['E']):
    try:
        # values = cell.value.split(',')
        values = [x.strip() for x in cell.value.split(',')]
        print(values)
        # values = cell.value.replace(', ', ',')
        print('Что в ячейке(массив): ', values)
        print('Чистые значения: ',cell.value)
        for words in values:
            if words in Type_Baths:
                print('Match')
        idx += 1
        print(idx)
    except Exception as e:
        print(e)
        continue

