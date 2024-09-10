import sqlite3
import os
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
import json
import random




def criar_clientes(tela):

    frame_corretores = ctk.CTkFrame(tela, fg_color="transparent")
    frame_corretores.pack(padx=10, pady=10, fill='both', expand=True)
    frame_tipo = ctk.CTkFrame(tela, fg_color="transparent",width=200,height=460)
    frame_tipo.place(x=10,y=40)

    label_id = ctk.CTkLabel(tela, text='ID do Imóvel', font=('Arial Bold', 15))
    label_id.place(x=230,y=20)
    id = ctk.CTkEntry(tela)
    id.place(x=230,y=50)

    label_nome_locador = ctk.CTkLabel(tela, text='Nome do Locador', font=('Arial Bold', 15))
    label_nome_locador.place(x=230,y=80)
    nome_locador = ctk.CTkEntry(tela)
    nome_locador.place(x=230,y=110)

    label_nome_locatario = ctk.CTkLabel(tela, text='Nome do Locatario', font=('Arial Bold', 15))
    label_nome_locatario.place(x=230,y=140)
    nome_locatario = ctk.CTkEntry(tela)
    nome_locatario.place(x=230,y=170)

    label_data = ctk.CTkLabel(tela, text='Data', font=('Arial Bold', 15))
    label_data.place(x=260,y=200)
    dia = ctk.CTkEntry(tela, width=50, placeholder_text='Dia', placeholder_text_color='gray')
    dia.place(x=200,y=230)
    mes = ctk.CTkEntry(tela, width=50, placeholder_text='Mes', placeholder_text_color='gray')
    mes.place(x=260,y=230)
    ano = ctk.CTkEntry(tela, width=50, placeholder_text='Ano', placeholder_text_color='gray')
    ano.place(x=320,y=230)



    label_corretores = ctk.CTkLabel(tela, text='Quantidade de corretores', font=('Poppins', 15))
    label_corretores.place(x=230,y=270)
    corretores_options = ["1 Corretor", "2 Corretores", "3 Corretores", "4 Corretores"]  
    corretores_menu = ctk.CTkOptionMenu(
        master=tela, 
        values=corretores_options, 
        command=on_option_change_corretores,
        dropdown_font=("Poppins", 12),  
        button_color="lightblue",  
        dropdown_fg_color="#3c8cd4",
        dropdown_text_color="white"
    )
    corretores_menu.place(x=230, y=300)



    label_tipo = ctk.CTkLabel(tela,text="Serviço requisitado", font=('Arial Bold', 15))
    label_tipo.place(x=30, y=20)
    tipo_options = ["Venda", "Aluguel"]
    tipo_menu = ctk.CTkOptionMenu(
        master=tela, 
        values=tipo_options, 
        command=on_option_change_tipo,
        dropdown_font=("Arial", 12),  
        button_color="lightblue",  
        dropdown_fg_color="#3c8cd4",
        dropdown_text_color="white"
    )
    tipo_menu.place(x=30,y=50)

    def corretor_entries(selected_value):

        for widget in frame_corretores.winfo_children():
            widget.destroy()

            global corretor1 
            global corretor2
            global corretor3
            global corretor4

            global comissao1 
            global comissao2
            global comissao3
            global comissao4

        if selected_value == '1 Corretor':

            corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor', placeholder_text_color='gray')
            corretor1.place(x=220, y=340)
            comissao1 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=365,y=340)
            corretor2 = "Vazio"
            corretor3 = "Vazio"
            corretor4 = "Vazio"

        if selected_value == '2 Corretores':
            corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 1', placeholder_text_color='gray')
            corretor1.place(x=220, y=340)
            comissao1 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=365,y=340)
            
            corretor2 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 2', placeholder_text_color='gray')
            corretor2.place(x=220, y=370)
            comissao2 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=365,y=370)
            
            corretor3 = "Vazio"
            corretor4 = "Vazio"

        
        if selected_value == '3 Corretores':
            corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 1', placeholder_text_color='gray')
            corretor1.place(x=220, y=340)
            comissao1 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=365,y=340)
        
            corretor2 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 2', placeholder_text_color='gray')
            corretor2.place(x=220, y=370)
            comissao2 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=365,y=370)
            
            corretor3 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 3', placeholder_text_color='gray')
            corretor3.place(x=220, y=400)
            comissao3 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao3.place(x=365,y=400)

            corretor4 = "Vazio"

        if selected_value == '4 Corretores':
            corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 1', placeholder_text_color='gray')
            corretor1.place(x=220, y=340)
            comissao1 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=365,y=340)
        
            corretor2 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 2', placeholder_text_color='gray')
            corretor2.place(x=220, y=370)
            comissao2 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=365,y=370)
            
            corretor3 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 3', placeholder_text_color='gray')
            corretor3.place(x=220, y=400)
            comissao3 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao3.place(x=365,y=400)

            corretor4 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 4', placeholder_text_color='gray')
            corretor4.place(x=220, y=430)
            comissao4 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao4.place(x=365,y=430)


            
    def on_option_change_corretores(choice):
        corretor_entries(choice)



    def tipo_eventos(selected_value):
        for widget in frame_tipo.winfo_children():
            widget.destroy()

        global valor_venda
        global entry_comissao
        global entry_royal
        global valor_calcao
        global tipo_selec

        if selected_value == "Venda":
            tipo_selec = "Venda"
            valor_venda = ctk.CTkEntry(frame_tipo, placeholder_text='R$ Valor venda', placeholder_text_color='gray')
            valor_venda.place(x=20, y=50)

            label_royal = ctk.CTkLabel(frame_tipo,text="Valor Royalties", font=('Arial Bold', 15))
            label_royal.place(x=20,y=140)
            entry_royal = ctk.CTkEntry(frame_tipo,placeholder_text="Em porcentagem(%)",placeholder_text_color="gray")
            entry_royal.place(x=20,y=170)

        if selected_value == "Aluguel":
            tipo_selec ="Aluguel"
            label_calcao = ctk.CTkLabel(frame_tipo,text="Valor Calção", font=('Arial Bold', 15))
            label_calcao.place(x=20,y=50)
            valor_calcao = ctk.CTkEntry(frame_tipo, placeholder_text='R$ Valor', placeholder_text_color='gray')
            valor_calcao.place(x=20, y=80)

            label_royal = ctk.CTkLabel(frame_tipo,text="Valor Royalties", font=('Arial Bold', 15))
            label_royal.place(x=20,y=170)
            entry_royal = ctk.CTkEntry(frame_tipo,placeholder_text="Em porcentagem(%)",placeholder_text_color="gray")
            entry_royal.place(x=20,y=200)


    def on_option_change_tipo(choice):
        tipo_eventos(choice)
        

    def salvar_dados_clientes():

        db_path = 'Banco_de_Dados.db'

        conex = sqlite3.connect(db_path)
        cursor = conex.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes (
                    id TEXT PRIMARY KEY NOT NULL,
                    tipo TEXT NOT NULL,
                    valor FLOAT,
                    royalties FLOAT,
                    calcao FLOAT,
                    nome_locador TEXT NOT NULL,
                    nome_locatario TEXT NOT NULL,
                    data TEXT NOT NULL,
                    corretor1 TEXT NOT NULL,
                    comissao1 FLOAT,
                    corretor2 TEXT,
                    comissao2 FLOAT,
                    corretor3 TEXT,
                    comissao3 FLOAT,
                    corretor4 TEXT,
                    comissao4 FLOAT
                    );           
            
        ''')


        Id = id.get()
        tipo = tipo_selec

        if tipo == "Venda":
            valor = valor_venda.get()
        else:
            valor = 0
        
        royalties = entry_royal.get()


        if tipo == "Aluguel":
            calcao = valor_calcao.get()
        else:
            calcao = 0
        
        Nome_locador = nome_locador.get()
        Nome_locatario = nome_locatario.get()
        Data = get_combined_date(dia.get(), mes.get(), ano.get())

        try:
            Corretor1 = corretor1.get() if isinstance(corretor1, ctk.CTkEntry) else corretor1
            Corretor2 = corretor2.get() if isinstance(corretor2, ctk.CTkEntry) else corretor2
            Corretor3 = corretor3.get() if isinstance(corretor3, ctk.CTkEntry) else corretor3
            Corretor4 = corretor4.get() if isinstance(corretor4, ctk.CTkEntry) else corretor4

            Comissao1 = comissao1.get() if isinstance(comissao1, ctk.CTkEntry) else comissao1
            Comissao2 = comissao2.get() if isinstance(comissao2, ctk.CTkEntry) else comissao2
            Comissao3 = comissao3.get() if isinstance(comissao3, ctk.CTkEntry) else comissao3
            Comissao4 = comissao4.get() if isinstance(comissao4, ctk.CTkEntry) else comissao4
            calcao=0

            cursor.execute('''
            INSERT INTO Clientes (  id,tipo,valor,royalties,
                                    calcao,nome_locador,nome_locatario,data, 
                                    corretor1,comissao1, corretor2,comissao2,
                                    corretor3,comissao3, corretor4,comissao4
                                    )
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''',(Id,tipo,valor,royalties,calcao,Nome_locador,Nome_locatario,Data, 
                Corretor1,Comissao1, Corretor2,Comissao2, Corretor3,Comissao3,
                Corretor4,Comissao4))

            conex.commit()
            messagebox.showinfo("Sucesso!", "Dados enviados ao banco de dados com sucesso!")

        except NameError as erro:

            messagebox.showinfo("Erro!", "É necessário definir ao menos 1 corretor por ID!")
            
        finally:
            conex.close()
        


    botao_salvar = ctk.CTkButton(tela, text='Salvar', command=salvar_dados_clientes)
    botao_salvar.place(x=230, y=550)