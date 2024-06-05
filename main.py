import PySimpleGUI as sg

sg.theme("LightBlue1")

layout = [[sg.Text("Enter Expense")], [sg.Input(do_not_clear=False)], [sg.Button('Enter'), sg.Button('DONE')]]

window = sg.Window("Expense Tracker", layout)
list = []
sum = 0
numbers = sg.Input()
while True:
  event, values = window.read()

  if event == 'Enter':
    list.append(values[0])
    

  
  if event == 'DONE':
    for i in list:
      i = float(i)
      sum += i
    print(sum)
      
    sg.popup("your final cost is", sum)

window.close()