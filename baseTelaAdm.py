import customtkinter as ctk
import tkinter as tk
from tkinter import *

janela = ctk.CTk()

class telaAMD():

#Padrão temas da tela
   def __format__(self, __format_spec: str):
      pass   
   ctk.set_appearance_mode("dark")
   ctk.set_default_color_theme("blue")

#padrão da tela
   janela = ctk.CTk()
   janela.geometry("1080x540") 
   janela.title("Tela Administrador")
   janela.iconbitmap("logo_insight.ico")
   janela.resizable(False, False)

#imagem logo 360
   img = PhotoImage(file = "logo_insight.png").subsample(2)
   label_img = ctk.CTkLabel(master=janela, image=img, text="")
   label_img.place(x=15, y=20)
#titulo ADM
   label_tt = ctk.CTkLabel(master=janela, text='Administrador', font=('Roboto',32, 'bold'), text_color="white").place(x=400, y=80)

#Imagem do botão logout
   logout = PhotoImage(file = "logout.png").subsample(2)
   Button = ctk.CTkButton(master=janela, image=logout, text="", fg_color="#242424")
   Button.place(x=950, y=40)

#logout_button = ctk.CTkButton("logout.JPG", text="", width=300, text_color='blue', fg_color="#00FFFF", font = ('Roboto', 14), cursor="hand2", hover_color='#2FCDCD', command="s").place(x=45, y=250)

#frame esquerda
   frame1 = ctk.CTkFrame(master=janela, width=250, height=350, fg_color="#242424")
   frame1.place(x=15, y=180)

#lado direito
   frame2 = ctk.CTkFrame(master=janela, width=100, height=60)
   frame2.place(x=300, y=190)
   frame3 = ctk.CTkFrame(master=janela, width=100, height=60)
   frame3.place(x=420, y=190)
   frame4 = ctk.CTkFrame(master=janela, width=100, height=100)
   frame4.place(x=300, y=260)
   frame5 = ctk.CTkFrame(master=janela, width=100, height=100)
   frame5.place(x=420, y=260)
   frame6 = ctk.CTkFrame(master=janela, width=245, height=150)
   frame6.place(x=290, y=375)
   frame7 = ctk.CTkFrame(master=janela, width=245, height=150)
   frame7.place(x=550, y=200)
   frame8 = ctk.CTkFrame(master=janela, width=245, height=150)
   frame8.place(x=810, y=200)
   frame9 = ctk.CTkFrame(master=janela, width=245, height=150)
   frame9.place(x=550, y=360)
   frame10 = ctk.CTkFrame(master=janela, width=245, height=150)
   frame10.place(x=810, y=360)

#botoes widgets
   Button = ctk.CTkButton(master=frame1,width=180, fg_color="#5CE1E6", text="CADASTROS", font = ('Roboto', 18, 'bold'), text_color= ('black'))
   Button.place(x=35, y=20)
   Button = ctk.CTkButton(master=frame1, width=180, fg_color="#5CE1E6", text="USUÁRIO", font = ('Roboto', 18, 'bold'), text_color= ('black'))
   Button.place(x=35, y=65)
   Button = ctk.CTkButton(master=frame1, width=180, fg_color="#5CE1E6", text="TURMAS", font = ('Roboto', 18, 'bold'), text_color= ('black'))
   Button.place(x=35, y=155)
   Button = ctk.CTkButton(master=frame1, width=180, text="TIMES", fg_color="#5CE1E6", font = ('Roboto', 18, 'bold'), text_color= ('black'))
   Button.place(x=35, y=200)
   Button = ctk.CTkButton(master=frame1, width=180, text="SPRINTS", fg_color="#5CE1E6", font = ('Roboto', 18, 'bold'), text_color= ('black'))
   Button.place(x=35, y=245)
   Button = ctk.CTkButton(master=frame1, width=180, text="INTEGRANTES", fg_color="#5CE1E6", font = ('Roboto', 18, 'bold'), text_color= ('black'))
   Button.place(x=35, y=295)

janela.mainloop()