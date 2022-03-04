import pyautogui
from tkinter import *
import pyperclip3 as pc
import keyboard

janela = Tk()
janela.title("Collor Micker")
janela.geometry('250x58')
janela.configure(bg='#FFFFFF')
janela.iconbitmap("icon.ico")

global pixelColorHEX


def atualizar_cor():
    x, y = pyautogui.position()
    print(f"x:{x} y:{y}")
    pixelColor = pyautogui.screenshot().getpixel((x, y))
    r, g, b = pixelColor
    print("RGB: {}".format(pixelColor))
    # converte RGB para HEX

    pixelColorHEX = '#%02x%02x%02x' % (pixelColor)
    print("HEX: {}".format(pixelColorHEX))
    print("________________________")
    txtt = f"x: {x} y: {y}\nRGB: {pixelColor}\nHEX: {pixelColorHEX}"

    txt.set(txtt)
    label.grid(row=0, column=0, sticky=W)
    label.after(100, atualizar_cor)
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        pc.copy(pixelColorHEX)


txt = StringVar()
frame = Frame(janela, bg="#FFFFFF", borderwidth=1, relief="solid").place(x=0, y=0)
label = Label(frame,
                textvariable=txt,
                bg="#FFFFFF",
                fg="#000000",
                font="Arial 12",
                width="26",
                bd=1,
                #relief="solid",
                #height=6,
                anchor=W,
                padx=6,
                pady=0,
                justify=LEFT
                )

label.after(100, atualizar_cor)

janela.mainloop()

