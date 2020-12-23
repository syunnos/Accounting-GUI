import openpyxl


def draw_graph():
    wb = openpyxl.load_workbook('kaikei.xlsx', data_only=True)
    sheet = wb['dairy']
    row_num = sheet.max_row

    price = []
    res = 0
    day = 12
    for i in range(2, row_num):
        if sheet['B' + str(i)].value != day and not sheet['B' + str(i)].value is None:
            price.append(res)
            res = sheet['D' + str(i)].value
            day = sheet['B' + str(i)].value
        else:
            res += sheet['D' + str(i)].value

    print(price)

    from matplotlib import pyplot as plt
    import pandas as pd
    import matplotlib.dates as mdates

    fig = plt.figure()  # グラフの画面領域を確保
    ax = fig.add_subplot(1, 1, 1)  # 描画領域の確保

    x = pd.date_range('2020-09-12', freq='d', periods=len(price))

    ax.bar(x, price)

    # daysFmt = mdates.DateFormatter('')
    # ax.xaxis.set_major_formatter(daysFmt)
    days = mdates.DayLocator()
    ax.xaxis.set_major_locator(days)
    plt.show()

#----------------------------------------
import datetime
def today():
    return datetime.date.today()




#----------------------------------------
# GUI部分の開発
import tkinter as tk

win = tk.Tk()
win.title("Graph of Accouting")
win.geometry("150x100")

label1 = tk.Label(win, text='集計開始日')
label1.pack(anchor='center')

text1 = tk.Entry(win)
text1.pack(anchor='center')
text1.insert(tk.END, '2020-09-12')
text1.focus_set()

label2 = tk.Label(win, text='集計終了日')
label2.pack(anchor='center')

text2 = tk.Entry(win)
text2.pack(anchor='center')
text2.insert(tk.END, today())

win.mainloop()
