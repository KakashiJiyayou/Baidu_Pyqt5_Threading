import excel2json

thisisjson= excel2json.convert_from_file('Drop_Down_Menu.xlsx')

print('Excel Sheet to JSON:\n', thisisjson)