import pandas
import  time
df = pandas.read_excel(open('Drop_Down_Menu.xlsx','rb'),
                       sheet_name='Drop_Down_Menu')

df = df.values
print(df)

print(type(df))

# while 1:
#     time.sleep(10)