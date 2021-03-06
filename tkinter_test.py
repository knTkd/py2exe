import sys
import tkinter

height, width = 300, 400

root = tkinter.Tk()
root.title('Titleeeee')
root.geometry(f'{height}x{width}')


# ラベル
static1 = tkinter.Label(text='static1 label text', foreground='#ff0000', background='#ffaacc')
static1.pack()


# エントリー（一行入力ボックス）
editbox = tkinter.Entry(width=30)
editbox.insert(tkinter.END, "初期文字列")
editbox.pack()


def ref_label(e):
    # エントリーボックスのテキストをラベルのテキストに反映させ、エントリーを削除
    static1['text'] = editbox.get()
    editbox.delete(0, tkinter.END)


button = tkinter.Button(text='反映ぼたん', width=20)
button.bind('<Button-1>', ref_label)
button.pack()



root.mainloop()
