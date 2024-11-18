import sqlite3
import os
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
import json
import random
from functools import partial
from PIL import Image, ImageTk
import io
from tkinter import filedialog




def ir_para_proximo_entry(event, proximo_entry):
    proximo_entry.focus_set()

def solicitar_saldo(arquivo='saldo.json'):

    if not os.path.exists(arquivo):
        global label_inicial
        global entry_saldo
        global botao_salvar_saldo
        label_inicial = ctk.CTkLabel(left_frame, text='Valor inicial do saldo',font=('Poppins',15))
        label_inicial.grid(row=1,column=0,padx=20,sticky="w")
        entry_saldo = ctk.CTkEntry(left_frame)
        entry_saldo.grid(row=2,column=0)

        botao_salvar_saldo = ctk.CTkButton(left_frame, text='Salvar saldo inicial',font=('Poppins',15),corner_radius=15,
                                                command=lambda: ((salvar_saldo(entry_saldo.get(), arquivo)),solicitar_saldo(arquivo='saldo.json')))
        botao_salvar_saldo.grid(row=3,column=0,padx=20,pady=10,sticky="w")

    else:
        global label_saldo
        global label_alterar
        global entry_alterar
        global botao_alterar

        
         # Se o arquivo já existe, carrega o saldo existente
        with open(arquivo, 'r') as f:
            dados = json.load(f)
            saldo_existente = dados.get('saldo', None)
            
            if saldo_existente is not None:
                
                label_saldo = ctk.CTkLabel(left_frame, text=f"Saldo: R${saldo_existente}", font=('Poppins',15),image=money_image, anchor="w",
                                             width=180,compound="left",fg_color="#3c8cd4",text_color="white",corner_radius=15)
                
                label_saldo.grid(row=4,column=0,padx=0,pady=15,ipady=5)

                label_alterar = ctk.CTkLabel(left_frame, text="Alterar o Saldo?",font=('Poppins',15))
                label_alterar.grid(row=6,column=0,padx=15,sticky="w")

                entry_alterar = ctk.CTkEntry(left_frame,placeholder_text="Novo Saldo",placeholder_text_color='gray',font=('Poppins Bold',15))
                entry_alterar.grid(row=7,column=0,padx=15,sticky="w")

                botao_alterar = ctk.CTkButton(left_frame, text="Alterar saldo",font=('Poppins',15),width=170,
                                              command=lambda:(alterar_saldo(entry_alterar.get(),arquivo='saldo.json'),
                                                             solicitar_saldo(arquivo='saldo.json')) )
                botao_alterar.grid(row=8,column=0,pady=10,padx=0)

                botao_atualizar = ctk.CTkButton(left_frame, text="Atualizar",font=('Poppins',15),
                                              width=170,command=lambda:(atualizar_saldo(arquivo='saldo.json'),
                                                             solicitar_saldo(arquivo='saldo.json')) )
                botao_atualizar.grid(row=5,column=0,pady=5,padx=0)

            else:
                messagebox.showerror("Erro", "Arquivo de saldo encontrado, mas sem valor válido. Por favor, verifique o arquivo.")







def alterar_saldo(valor_alterar, arquivo='saldo.json'):
    label_saldo.destroy()
   
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            dados = json.load(f)
            chave = 'saldo'
            if valor_alterar == "":
                valor_alterar = dados.get('saldo', None)
        valor_diferente = float(valor_alterar)
        dados[chave] = valor_diferente
        
        with open(arquivo, 'w') as f:
            json.dump(dados, f,)

def atualizar_saldo(arquivo="saldo.json"):
    label_saldo.destroy()
   
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            dados = json.load(f)
            chave = 'saldo'
        dados[chave] = dados[chave]
        



def salvar_saldo(valor_inicial, arquivo='saldo.json'):
    label_inicial.destroy()
    entry_saldo.destroy()
    botao_salvar_saldo.destroy()

    try:
        valor = float(valor_inicial)
        chave = 'saldo'
        
        # Cria o arquivo com o valor inicial
        with open(arquivo, 'w') as f:
            json.dump({chave: valor}, f)
        
        messagebox.showinfo("Sucesso", "Saldo inicial salvo com sucesso!")
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")




def criar_clientes(tela):

    destruir_widgets(tela)
    frame_corretores = ctk.CTkFrame(tela, fg_color="transparent",width=350,height=400)
    frame_corretores.place(x=695,y=110)
    frame_tipo = ctk.CTkFrame(tela, fg_color="transparent",width=250,height=400)
    frame_tipo.place(x=400,y=130)

    label_id = ctk.CTkLabel(tela, text='ID do Imóvel', font=('Poppins Bold', 16))
    label_id.place(x=400, y=30)
    id = ctk.CTkEntry(tela,width=180,font=("Poppins", 15))
    id.place(x=398,y=70)

    label_nome_locador = ctk.CTkLabel(tela, text='Nome do Locador', font=('Poppins', 16))
    label_nome_locador.place(x=50,y=130)
    nome_locador = ctk.CTkEntry(tela,width=300,font=("Poppins", 15))
    nome_locador.place(x=50,y=170)

    label_nome_locatario = ctk.CTkLabel(tela, text='Nome do Locatario',  font=('Poppins', 16))
    label_nome_locatario.place(x=50,y=230)
    nome_locatario = ctk.CTkEntry(tela,width=300,font=("Poppins", 15))
    nome_locatario.place(x=50,y=270)

    label_data = ctk.CTkLabel(tela, text='Data Contrato',  font=('Poppins', 16))
    label_data.place(x=50,y=330)
    data_completa = ctk.CTkEntry(tela,width=300,font=("Poppins", 15))
    data_completa.place(x=50,y=370)

    data_completa.bind("<KeyRelease>", lambda event: formatar_data_entry(data_completa,event))

    
    nome_locador.bind("<Return>", lambda event: ir_para_proximo_entry(event, nome_locatario))
    nome_locatario.bind("<Return>", lambda event: ir_para_proximo_entry(event, data_completa))
    data_completa.bind("<Return>", lambda event: ir_para_proximo_entry(event, id))


    def corretor_entries(selected_value):

        
        for widget in frame_corretores.winfo_children():
            widget.destroy()

        global corretor1, corretor2, corretor3, corretor4
        global comissao1, comissao2, comissao3, comissao4

        def buscar_corretores():
            try:
                conn = sqlite3.connect('Banco_de_Dados.db')
                cursor = conn.cursor()
                cursor.execute("SELECT nome FROM corretores")
                corretores = [row[0] for row in cursor.fetchall()]
                return corretores

            except sqlite3.OperationalError:
                messagebox.showerror("Erro!", "Nenhum corretor cadastrado!")

            finally:
                conn.close()
           

        lista_corretores = buscar_corretores()
        

        def criar_option_menu(x, y):

            if lista_corretores != None:
                var = ctk.StringVar(value="Selecione um corretor")

                option_menu = ctk.CTkOptionMenu(frame_corretores,
                                                values=lista_corretores, 
                                                width=290,
                                                variable=var, 
                                                font=("Poppins", 15),
                                                dropdown_font=("Poppins", 15),
                                                text_color="black",
                                                fg_color= "white",
                                                button_color="#C0C0C0",
                                                button_hover_color= "gray",
                                                dropdown_text_color="black")
                option_menu.place(x=x, y=y)
                return option_menu
            else:
                pass

        if selected_value == '1 Corretor':
            corretor1 = criar_option_menu(5, 0)
            comissao1 = ctk.CTkEntry(frame_corretores, width=50, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=300, y=0)

            corretor2 = corretor3 = corretor4 = None
            comissao2 = comissao3 = comissao4 = None

        elif selected_value == '2 Corretores':
            corretor1 = criar_option_menu(5, 0)
            comissao1 = ctk.CTkEntry(frame_corretores, width=50, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=300, y=0)

            corretor2 = criar_option_menu(5, 40)
            comissao2 = ctk.CTkEntry(frame_corretores, width=50, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=300, y=40)

            corretor3 = corretor4 = None
            comissao3 = comissao4 = None

        elif selected_value == '3 Corretores':
            corretor1 = criar_option_menu(5, 0)
            comissao1 = ctk.CTkEntry(frame_corretores, width=50, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=300, y=0)

            corretor2 = criar_option_menu(5, 40)
            comissao2 = ctk.CTkEntry(frame_corretores, width=50, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=300, y=40)

            corretor3 = criar_option_menu(5, 80)
            comissao3 = ctk.CTkEntry(frame_corretores, width=50, placeholder_text='(%)', placeholder_text_color='gray')
            comissao3.place(x=300, y=80)

            corretor4 = None
            comissao4 = None

        elif selected_value == '4 Corretores':
            corretor1 = criar_option_menu(5, 0)
            comissao1 = ctk.CTkEntry(frame_corretores, width=50, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=300, y=0)

            corretor2 = criar_option_menu(5, 40)
            comissao2 = ctk.CTkEntry(frame_corretores, width=50, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=300, y=40)

            corretor3 = criar_option_menu(5, 80)
            comissao3 = ctk.CTkEntry(frame_corretores, width=50, placeholder_text='(%)', placeholder_text_color='gray')
            comissao3.place(x=300, y=80)

            corretor4 = criar_option_menu(5, 120)
            comissao4 = ctk.CTkEntry(frame_corretores, width=50, placeholder_text='(%)', placeholder_text_color='gray')
            comissao4.place(x=300, y=120)

            corretor1.bind("<Return>", lambda event: ir_para_proximo_entry(event,comissao1))
            comissao1.bind("<Return>", lambda event: ir_para_proximo_entry(event,corretor2))
            corretor2.bind("<Return>", lambda event: ir_para_proximo_entry(event,comissao2))
            comissao2.bind("<Return>", lambda event: ir_para_proximo_entry(event,corretor3))
            corretor3.bind("<Return>", lambda event: ir_para_proximo_entry(event,comissao3))
            comissao3.bind("<Return>", lambda event: ir_para_proximo_entry(event,corretor4))
            corretor4.bind("<Return>", lambda event: ir_para_proximo_entry(event,comissao4))


            
    def on_option_change_corretores(choice):
        corretor_entries(choice)



    def tipo_eventos(selected_value):
        for widget in frame_tipo.winfo_children():
            widget.destroy()

        global valor_venda
        global valor_aluguel
        global valor_pri_aluguel
        global valor_caucao
        global entry_parcelas
        global entry_valor_parcelas
        global entry_entrada
        global tipo_selec

        if selected_value == "Venda":
            tipo_selec = "Venda"

            label_nome_locador.configure(text="Vendedor")
            label_nome_locatario.configure(text="Comprador")

            label_valor = ctk.CTkLabel(frame_tipo,text="Valor", font=('Poppins', 16))
            label_valor.place(x=0,y=0)
            valor_venda = ctk.CTkEntry(frame_tipo, placeholder_text='R$ Valor', placeholder_text_color='gray',width=120,font=("Poppins", 15))
            valor_venda.place(x=0, y=40)

            entry_entrada = ctk.CTkEntry(frame_tipo,width=50, font=("Poppins", 15))
            entry_entrada.place(x=130,y=40)
            ctk.CTkLabel(frame_tipo,text="%",font=("Poppins", 15)).place(x=180,y=40)

            ctk.CTkLabel(frame_tipo,text="OBS: Colocar o Valor Total, e a",
                         font=("Poppins Bold", 13)).place(x=0,y=80)
            ctk.CTkLabel(frame_tipo,text="porcentagem desse valor que",
                         font=("Poppins Bold", 13)).place(x=0,y=100)
            ctk.CTkLabel(frame_tipo,text="será retirada",
                         font=("Poppins Bold", 13)).place(x=0,y=120)
            

            id.bind("<Return>", lambda event: ir_para_proximo_entry(event, valor_venda))
            valor_venda.bind("<Return>", lambda event: ir_para_proximo_entry(event,entry_entrada))
            



        if selected_value == "Aluguel":
            tipo_selec ="Aluguel"

            label_nome_locador.configure(text="Locador")
            label_nome_locatario.configure(text="Locatário")

            label_aluguel = ctk.CTkLabel(frame_tipo,text="Valor Aluguel", font=('Poppins', 16))
            label_aluguel.place(x=0,y=0)
            valor_aluguel = ctk.CTkEntry(frame_tipo,width=180,font=("Poppins", 15))
            valor_aluguel.place(x=0, y=40)
            label_pri_aluguel = ctk.CTkLabel(frame_tipo,text="Valor 1° Aluguel", font=('Poppins', 16))
            label_pri_aluguel.place(x=0,y=100)
            valor_pri_aluguel = ctk.CTkEntry(frame_tipo,width=180,font=("Poppins", 15))
            valor_pri_aluguel.place(x=0, y=140)
            label_caucao = ctk.CTkLabel(frame_tipo,text="Valor Caução", font=('Poppins', 16))
            label_caucao.place(x=0,y=200)
            valor_caucao = ctk.CTkEntry(frame_tipo,width=180,font=("Poppins", 15))
            valor_caucao.place(x=0, y=240)

            id.bind("<Return>", lambda event: ir_para_proximo_entry(event, valor_aluguel))
            valor_aluguel.bind("<Return>", lambda event: ir_para_proximo_entry(event,valor_pri_aluguel))
            valor_pri_aluguel.bind("<Return>", lambda event: ir_para_proximo_entry(event,valor_caucao))


    def on_option_change_tipo(choice):
        tipo_eventos(choice)
        

    label_corretores = ctk.CTkLabel(tela, text='Corretores', font=('Poppins Bold', 16))
    label_corretores.place(x=700,y=30)
    corretores_options = ["1 Corretor", "2 Corretores", "3 Corretores", "4 Corretores"]  
    corretores_menu = ctk.CTkOptionMenu(
        master=tela,
        values=corretores_options, 
        command=on_option_change_corretores,
        font=("Poppins", 15),
        dropdown_font=("Poppins", 15),  
        button_color="lightblue",  
        dropdown_fg_color="#3c8cd4",
        dropdown_text_color="white"
    )
    corretores_menu.place(x=700, y=70)



    label_tipo = ctk.CTkLabel(tela,text="Serviço requisitado", font=('Poppins Bold', 16))
    label_tipo.place(x=50,y=30)
    tipo_options = ["Venda", "Aluguel"]
    tipo_menu = ctk.CTkOptionMenu(
        master=tela,
        width=165, 
        values=tipo_options, 
        command=on_option_change_tipo,
        font=("Poppins", 15),
        dropdown_font=("Poppins", 15),  
        button_color="lightblue",  
        dropdown_fg_color="#3c8cd4",
        dropdown_text_color="white"
    )
    tipo_menu.place(x=50,y=70)




    def salvar_dados_clientes():

        db_path = 'Banco_de_Dados.db'

        conex = sqlite3.connect(db_path)
        cursor = conex.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes (
                    id TEXT PRIMARY KEY NOT NULL,
                    tipo TEXT NOT NULL,
                    valor FLOAT NULL,
                    valor_aluguel FLOAT NULL,
                    entrada FLOAT NULL,
                    primeiro_aluguel FLOAT NULL,
                    caucao FLOAT NULL,
                    nome_locador TEXT NOT NULL,
                    nome_locatario TEXT NOT NULL,
                    data TEXT NOT NULL,
                    corretor1 TEXT NOT NULL,
                    comissao1 FLOAT NOT NULL,
                    corretor2 TEXT,
                    comissao2 FLOAT,
                    corretor3 TEXT,
                    comissao3 FLOAT,
                    corretor4 TEXT,
                    comissao4 FLOAT,
                    royalties FLOAT NOT NULL
                );           
            
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Entradas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente TEXT,
                    nome TEXT,
                    data TEXT NOT NULL,
                    valor FLOAT NOT NULL,
                    valor_entrada FLOAT NOT NULL,
                    status TEXT NULL,
                    FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
                );             
            ''')
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentacao (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT,
            tipo1 TEXT,
            descricao TEXT,
            valor FLOAT,
            data TEXT
        )
        """)


        Id = id.get()
        tipo = tipo_selec

        #VENDA
        if tipo_selec == "Venda":
            valor = valor_venda.get()
            entrada = entry_entrada.get()
            valor_al = None
            primeiro_aluguel = None
            caucao = None
            royalties = 0.09 * (float(valor)*(float(entrada)/100))

        #ALUGUEL
        else:
            valor_al = valor_aluguel.get()
            primeiro_aluguel = valor_pri_aluguel.get()
            caucao = valor_caucao.get()
            valor = None
            entrada = None
            royalties = 0.09 * float(primeiro_aluguel)

        
        Nome_locador = nome_locador.get()
        Nome_locatario = nome_locatario.get()
        data_inicio = data_completa.get()  
        

        try:

            
            Corretor1 = corretor1.cget("variable").get() if isinstance(corretor1, ctk.CTkOptionMenu) else corretor1.get()
            Corretor2 = corretor2.cget("variable").get() if isinstance(corretor2, ctk.CTkOptionMenu) else corretor2.get() if corretor2 else None
            Corretor3 = corretor3.cget("variable").get() if isinstance(corretor3, ctk.CTkOptionMenu) else corretor3.get() if corretor3 else None
            Corretor4 = corretor4.cget("variable").get() if isinstance(corretor4, ctk.CTkOptionMenu) else corretor4.get() if corretor4 else None

          
            Comissao1 = comissao1.get() if comissao1 else None
            Comissao2 = comissao2.get() if comissao2 else None
            Comissao3 = comissao3.get() if comissao3 else None
            Comissao4 = comissao4.get() if comissao4 else None


            if Comissao1 == "45" or Comissao1 == "30" or Comissao1 == "15":
                Comissao1 = float(Comissao1)
                Comissao1 = Comissao1 / 2

            if Comissao2 == "45" or Comissao2 == "30" or Comissao2 == "15":
                Comissao2 = float(Comissao2)
                Comissao2 = Comissao2 / 2

            if Comissao3 == "45" or Comissao3 == "30" or Comissao3 == "15":
                Comissao3 = float(Comissao3)
                Comissao3 = Comissao3 / 2

            if Comissao4 == "45" or Comissao4 == "30" or Comissao4 == "15":
                Comissao4 = float(Comissao4)
                Comissao4 = Comissao4 / 2

           
            cursor.execute('''
                INSERT INTO Clientes (
                id, tipo, valor, valor_aluguel, entrada,
                primeiro_aluguel, caucao, nome_locador, nome_locatario, data,
                corretor1, comissao1, corretor2, comissao2, corretor3, comissao3,
                corretor4, comissao4, royalties
                )
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''', (
                Id, tipo, valor, valor_al, entrada,
                primeiro_aluguel, caucao, Nome_locador, Nome_locatario, data_inicio,
                Corretor1, Comissao1, Corretor2, Comissao2, Corretor3, Comissao3,
                Corretor4, Comissao4, royalties
                ))
            
            

            conex.commit()
            messagebox.showinfo("Sucesso!", "Dados enviados ao banco de dados com sucesso!")

        except NameError as erro:

            messagebox.showinfo("Erro!", f"Erro ao inserir dados: {erro}")
        
        except sqlite3.IntegrityError:
            
            messagebox.showerror("Erro!", "Não é possível criar dois clientes com o mesmo ID")
            
        finally:
            conex.close()


    botao_salvar = ctk.CTkButton(tela, text='Salvar',font=("Poppins",17),width=170,height=40,corner_radius=15, command=salvar_dados_clientes)
    botao_salvar.place(x=400, y=600)




## FUNÇOES USADAS NA CRIAÇAO DE CONTAS

def mostrar_contas(nome_tabela, filtro, valor_filtro, frame, janela):

    try:
        for widget in frame.winfo_children():
            widget.destroy()


        conex = sqlite3.connect('Banco_de_Dados.db')
        cursor = conex.cursor()

        if nome_tabela == "Todas":

            cursor.execute(f'''
            SELECT * FROM Contas WHERE {filtro} = ?
            UNION
            SELECT * FROM ContasPagas WHERE {filtro} = ?
            ''', (valor_filtro, valor_filtro))

            if filtro == "data_pg":

                cursor.execute(f'''
                SELECT * FROM Contas WHERE substr(data_pg, 4, 2) = ?
                UNION
                SELECT * FROM ContasPagas WHERE substr(data_pg, 4, 2) = ?
                ''', (valor_filtro, valor_filtro))


        elif filtro == None or valor_filtro == None:
            cursor.execute(f"SELECT * FROM {nome_tabela}")

        elif filtro == "data_pg":

            cursor.execute(f'''
            SELECT * FROM {nome_tabela}
            WHERE substr(data_pg, 4, 2) = ? 
            ''', (valor_filtro,))

        else:
            cursor.execute(f"SELECT * FROM {nome_tabela} WHERE {filtro} = ?", (valor_filtro,))

        contas = cursor.fetchall()
        conex.close()
        checkboxes = []
        headers = ["  Pago "," ID ", " Tipo ", " Fornecedor ", " Valor ", " Data "]


        for col, header in enumerate(headers):
            ctk.CTkLabel(frame, text=header, font=('Poppins Bold', 15)).grid(row=0, column=col, padx=15,pady=10)

        for i, conta in enumerate(contas, start=1):

            check = ctk.IntVar()
            checkbox = ctk.CTkCheckBox(frame,text="",width=25,variable=check)
            checkbox.grid(row=i,column=0)
            checkboxes.append((check, conta))

            for j, valor in enumerate(conta, start=1):
                ctk.CTkLabel(frame, text=str(valor),font=('Poppins', 14) ).grid(row=i, column=j)
                
        def novo_valor():

            global valor_inserido
            valor_inserido = None

            def retornar_novo_valor():
                global valor_inserido
                valor_inserido = novo_valor_entry.get()
                tela.destroy()

            tela = ctk.CTkToplevel(janela)
            tela.attributes('-topmost', True)
            janela.attributes("-topmost", False)
            tela.geometry("+400+400")

            ctk.CTkLabel(tela, text="Novo Valor",font=("Poppins Bold",15)).place(x=10,y=5)
            novo_valor_entry = ctk.CTkEntry(tela)
            novo_valor_entry.place(x=10, y=35)

            botao_mudar = ctk.CTkButton(tela, text="Alterar", command=retornar_novo_valor)
            botao_mudar.place(x=10, y=80)

            tela.wait_window()  # Aguarda até que a janela seja fechada
            
            

        def marcar_pagamento():
            conex = sqlite3.connect('Banco_de_Dados.db')
            cursor = conex.cursor()

            for check, conta in checkboxes:
                if check.get() == 1: 

                    id, tipo, fornecedor, valor, data_pg = conta    
                    ask_valor = messagebox.askyesno("Confirmaçao",f"Voce deseja mudar o valor da conta {tipo} Data:{data_pg}? Valor atual:{valor}",parent=frame)

                    if ask_valor:
                        novo_valor()
                        valor = float(valor_inserido)
                    else:
                        valor = valor

                    arquivo = "saldo.json"
                    with open(arquivo, 'r') as f:
                        dados = json.load(f)
                        saldo = dados.get('saldo', 0)
                    
                    saida = valor
                    novo_saldo = saldo - saida

                    cursor.execute('''
                    INSERT INTO ContasPagas(tipo,fornecedor,valor,data_pg)
                    VALUES (?,?,?,?)
                    ''',(tipo, fornecedor, valor, data_pg))
        

                    cursor.execute("DELETE FROM Contas WHERE id=?", (id,))
                    with open(arquivo, 'w') as f:
                        json.dump({'saldo': novo_saldo}, f)
                    

                    cursor.execute('''
                    INSERT INTO movimentacao(tipo,tipo1,descricao,valor,data)
                    VALUES (?,?,?,?,?)
                    ''',("Saída","Contas",tipo, valor, data_pg))
            
            conex.commit()
            conex.close()
            messagebox.showinfo("Sucesso", "Contas pagas com sucesso!", parent=janela)

            atualizar_saldo(arquivo='saldo.json')
            solicitar_saldo(arquivo='saldo.json')


        def deletar_contas():
            conex = sqlite3.connect('Banco_de_Dados.db')
            cursor = conex.cursor()
            for check, conta in checkboxes:
                if check.get() == 1: 
                    id, tipo, fornecedor, valor, data_pg = conta 

                    cursor.execute("DELETE FROM ContasPagas WHERE id=?", (id,))

            conex.commit()
            conex.close()
            messagebox.showinfo("Sucesso", "Contas removidas com sucesso!", parent=janela)
            



        if nome_tabela == "Contas":
            botao_pagar_contas = ctk.CTkButton(frame, text="Pagar Contas", command=marcar_pagamento)
            botao_pagar_contas.grid(row=i+1,column=2)

        if nome_tabela == "ContasPagas":
            botao_deletar = ctk.CTkButton(frame, text="Deletar Contas", command=deletar_contas)
            botao_deletar.grid(row=i+1,column=2)

    except UnboundLocalError:
    
        messagebox.showinfo("Erro!", "Não há contas nessa sessão!",parent=janela)

    finally:
    
        conex.close()



def destruir_widgets(frame):
    
    for widget in frame.winfo_children():
        widget.destroy()



def formatar_data_entry(entry_widget, event):

    texto = entry_widget.get()

    # Remove qualquer caractere que não seja numérico
    texto = ''.join([char for char in texto if char.isdigit()])

    # Insere as barras conforme o tamanho do texto
    if len(texto) > 2 and len(texto) <= 4:
        texto = texto[:2] + '/' + texto[2:]
    elif len(texto) > 4:
        texto = texto[:2] + '/' + texto[2:4] + '/' + texto[4:6]

    # Atualiza o texto no entry
    entry_widget.delete(0, 'end')
    entry_widget.insert(0, texto)
    


def criar_contas(tela):

    destruir_widgets(tela)
    
    label_tipoc = ctk.CTkLabel(tela, text="Tipo de conta", font=('Poppins Bold', 16))
    label_tipoc.place(x=50, y=30)

    frame_tipo = ctk.CTkFrame(tela,width=300,height=60,fg_color="transparent")
    frame_tipo.place(x=50,y=80)

    opcoes = ["Energia", "Aluguel", "Advogado", "Sistema", "Internet", "Serasa", 
          "Contabilidade", "Vigilância", "Imposto", "Digital", "Royalties", "Outros"]
    
    conta_entry = ctk.CTkEntry(frame_tipo, placeholder_text="Digite o tipo da conta...",width=300,font=("Poppins", 15))
    conta_entry.place_forget()  

    def option_selected(choice):
        if choice == "Outros":
            conta_entry.place(x=0, y=20)  
        else:
            conta_entry.delete(0, ctk.END)
            conta_entry.insert(0,choice)


    conta_option_menu = ctk.CTkOptionMenu(tela, values=opcoes, 
    command=option_selected,
    font=("Poppins", 15),
    dropdown_font=("Poppins", 15),  
    button_color="lightblue",  
    dropdown_fg_color="#3c8cd4",
    dropdown_text_color="white")

    conta_option_menu.place(x=50, y=60)

    label_fornecedorc = ctk.CTkLabel(tela, text="Fornecedor", font=('Poppins', 16))
    label_fornecedorc.place(x=50, y=140)
    fornecedor_entry = ctk.CTkEntry(tela, width=300, font=('Poppins', 15))
    fornecedor_entry.place(x=50,y=180)

    label_valorc = ctk.CTkLabel(tela, text="Valor Conta", font=('Poppins', 16))
    label_valorc.place(x=50, y=240)
    valor_entry = ctk.CTkEntry(tela, width=300, font=('Poppins', 15))
    valor_entry.place(x=50,y=280)

    label_datac = ctk.CTkLabel(tela, text="Data de Vencimento", font=('Poppins', 16))
    label_datac.place(x=50, y=340)
    data_completa = ctk.CTkEntry(tela,font=("Poppins",15),width=300)
    data_completa.place(x=50,y=380)

    data_completa.bind("<KeyRelease>", lambda event: formatar_data_entry(data_completa,event))

    ctk.CTkLabel(tela,text="Repetir essa Conta para proximos meses?",font=("Poppins", 16)).place(x=50,y=440)

    conta_entry.bind("<Return>", lambda event: ir_para_proximo_entry(event, fornecedor_entry))
    fornecedor_entry.bind("<Return>", lambda event: ir_para_proximo_entry(event, valor_entry))
    valor_entry.bind("<Return>", lambda event: ir_para_proximo_entry(event, data_completa))

    

    frame_ask= ctk.CTkFrame(tela,fg_color="transparent",width=300,height=100)
    frame_ask.place(x=50,y=520)

    def ask_eventos(selected_value):
        
        destruir_widgets(frame_ask)

        global entry_quantidade_mes
        
        if selected_value == "Sim":

            ctk.CTkLabel(frame_ask, text="Quantos meses a frente?",font=('Poppins', 16)).place(x=0, y=0)
            entry_quantidade_mes = ctk.CTkEntry(frame_ask,width=60, placeholder_text="1,2,3...", placeholder_text_color="gray",font=("Poppins",15))
            entry_quantidade_mes.place(x=210, y=0)



        if selected_value == "Não":
            global meses_a_frente
            meses_a_frente = 0
    


    botao_salvar_contas = ctk.CTkButton(tela,text="Salvar",font=('Poppins', 17), width=170,height=40,corner_radius=15,command=lambda:salvar_contas(
        conta_entry.get(), fornecedor_entry.get(),
        valor_entry.get(), data_completa.get()))
    
    botao_salvar_contas.place(x=400, y=600)


    def on_option_change_ask(choice):
        global selected_value
        selected_value = choice
        ask_eventos(selected_value)

    yes_no_options = ["Sim", "Não"]
    yes_no_menu = ctk.CTkOptionMenu(    
    master=tela, 
    values=yes_no_options, 
    command=on_option_change_ask,
    dropdown_font=("Poppins", 15), 
    font=("Poppins", 15),
    button_color="lightblue",  
    dropdown_fg_color="#3c8cd4",
    dropdown_text_color="white"
    )
    yes_no_menu.place(x=50,y=480)



def salvar_contas(tipo,fornecedor,valor,data):

    if selected_value == "Sim":
        meses_a_frente = int(entry_quantidade_mes.get())
        
    else:
        meses_a_frente = 0

    if meses_a_frente > 12:

        messagebox.showinfo("Erro!", "Não é possível adicionar a mesma conta para mais de 12 meses!")
        conex.close()

    else:      
        i=0

        dia, mes, ano = data.split("/")

        mes = int(mes)

        while meses_a_frente >= 0:
            db_path = 'Banco_de_Dados.db'
            conex = sqlite3.connect(db_path)
            cursor = conex.cursor()
    

            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Contas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tipo TEXT NOT NULL,
                        fornecedor TEXT NOT NULL,
                        valor FLOAT NOT NULL,
                        data_pg TEXT NOT NULL
                        );           
            ''')

            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS ContasPagas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            tipo TEXT NOT NULL,
                            fornecedor TEXT NOT NULL,
                            valor FLOAT NOT NULL,
                            data_pg TEXT NOT NULL
                            );           
                            ''')


            conex = sqlite3.connect(db_path)
            cursor = conex.cursor()

            try:

                if mes > 12:
                    mes = 1
                    ano = int(ano) + 1

                    data = f"{int(dia):02}/{int(mes):02}/{int(ano):02}"

                else:
                    mes = int(mes)
                    data = f"{int(dia):02}/{int(mes):02}/{int(ano):02}"
                
                cursor.execute('''
                    INSERT INTO Contas (tipo,fornecedor,valor,data_pg)
                    VALUES (?,?,?,?)
                    ''',(tipo,fornecedor,valor,data))
                
                conex.commit()
                i+=1
                meses_a_frente -= 1
                mes += 1

            except NameError as erro:

                messagebox.showinfo("Erro!", "Erro dados colocados de forma incorreta!")
                
            finally:
                conex.close()

        messagebox.showinfo("Sucesso!", "Dados enviados ao banco de dados com sucesso!")
        





def exibir_informacoes_contas():
    
    destruir_widgets(criar_frame)

    main_frame = ctk.CTkFrame(criar_frame,fg_color="transparent")
    main_frame.pack(fill="both", expand=True)

    left_frame = ctk.CTkFrame(main_frame,fg_color="transparent",border_width=5,border_color="#C0C0C0")
    left_frame.pack(side="left", fill="y",ipadx=20)
    
    frame_contas = ctk.CTkScrollableFrame(main_frame)
    frame_contas.pack(side="right", fill="both", expand=True, padx=(0, 20))

    ctk.CTkLabel(left_frame, text="Exibir Todas:",font=('Poppins Bold', 16)).place(x=40, y=20)

    botao_todas_contas = ctk.CTkButton(left_frame, text="Contas a Pagar",font=('Poppins', 15), command=lambda:mostrar_contas("Contas", None, None, frame_contas, tela))
    botao_todas_contas.place(x=40,y=60)

    botao_exibir_pagas = ctk.CTkButton(left_frame, text="Contas pagas",font=('Poppins', 15), command=lambda:mostrar_contas("ContasPagas", None, None, frame_contas, tela))
    botao_exibir_pagas.place(x=40,y=120)

    label_filtro = ctk.CTkLabel(left_frame, text="Filtrar",font=('Poppins Bold', 15))
    label_filtro.place(x=40,y=170)

    frame_filtro = ctk.CTkFrame(left_frame,fg_color="transparent",width=150,height=300)
    frame_filtro.place(x=40,y=250)

    filter_var = ctk.StringVar(value="outro")

    def on_radio_change(filtro1, valor_filtro1):

        selected_option = filter_var.get()
        
        if selected_option == "Todas Contas":
            mostrar_contas("Todas",filtro1, valor_filtro1, frame_contas, tela)
            
        elif selected_option == "Pagas":
            mostrar_contas("ContasPagas",filtro1, valor_filtro1, frame_contas, tela)

        elif selected_option == "Não Pagas":
            mostrar_contas("Contas",filtro1, valor_filtro1, frame_contas, tela)


    def filtros(selected_value):

        destruir_widgets(frame_filtro)

        if selected_value == "Data":

            ctk.CTkLabel(frame_filtro, text="Mês",font=('Poppins Bold', 15), text_color= "#484E55").place(x=0, y=0)

            entry_data_filtro = ctk.CTkEntry(frame_filtro, placeholder_text="01,02,03...", placeholder_text_color="gray")
            entry_data_filtro.place(x=0,y=30)

            radio1 = ctk.CTkRadioButton(frame_filtro, text="Todas Contas",font=('Poppins', 13), variable=filter_var, value="Todas Contas")
            radio1.place(x=0,y=70)

            radio2 = ctk.CTkRadioButton(frame_filtro, text="Pagas",font=('Poppins', 13), variable=filter_var, value="Pagas")
            radio2.place(x=0,y=100)

            radio3 = ctk.CTkRadioButton(frame_filtro, text="Não Pagas",font=('Poppins', 13), variable=filter_var, value="Não Pagas")
            radio3.place(x=0,y=130)

            botao_selecionar_radio = ctk.CTkButton(frame_filtro, text="Selecionar",font=('Poppins', 15), command=lambda:on_radio_change("data_pg", entry_data_filtro.get()))
            botao_selecionar_radio.place(x=0,y=160)

        if selected_value == "Tipo":

            ctk.CTkLabel(frame_filtro, text="Tipo Conta",font=('Poppins Bold', 15), text_color= "#484E55").place(x=0, y=0)

            opcoes = ["Energia", "Aluguel", "Advogado", "Sistema", "Internet", "Serasa", 
            "Contabilidade", "Vigilância", "Imposto", "Digital", "Royalties", "Outros"]
    
            entry_data_filtro = ctk.CTkEntry(frame_filtro, placeholder_text="Digite o tipo da conta...")
            entry_data_filtro.place_forget()  

            def option_selected(choice):
                if choice == "Outros":
                    entry_data_filtro.place(x=0, y=60)  
                else:
                    entry_data_filtro.delete(0, ctk.END)
                    entry_data_filtro.insert(0,choice)


            conta_option_menu = ctk.CTkOptionMenu(frame_filtro, values=opcoes, 
            command=option_selected,
            font=("Poppins", 13),
            dropdown_font=("Poppins", 13),  
            button_color="lightblue",  
            dropdown_fg_color="#3c8cd4",
            dropdown_text_color="white")

            conta_option_menu.place(x=0, y=30)

            # entry_data_filtro = ctk.CTkEntry(frame_filtro, placeholder_text="Energia,Agua...", placeholder_text_color="gray")
            # entry_data_filtro.place(x=0,y=30)

            radio1 = ctk.CTkRadioButton(frame_filtro, text="Todas Contas",font=('Poppins', 13), variable=filter_var, value="Todas Contas")
            radio1.place(x=0,y=100)

            radio2 = ctk.CTkRadioButton(frame_filtro, text="Pagas",font=('Poppins', 13), variable=filter_var, value="Pagas")
            radio2.place(x=0,y=130)

            radio3 = ctk.CTkRadioButton(frame_filtro, text="Não Pagas",font=('Poppins', 13), variable=filter_var, value="Não Pagas")
            radio3.place(x=0,y=160)

            botao_selecionar_radio = ctk.CTkButton(frame_filtro, text="Selecionar",font=('Poppins', 15), command=lambda:on_radio_change("tipo", entry_data_filtro.get()))
            botao_selecionar_radio.place(x=0,y=190)
        
        if selected_value == "Valor":

            ctk.CTkLabel(frame_filtro, text="Valor",font=('Poppins Bold', 15), text_color= "#484E55").place(x=0, y=0)

            entry_data_filtro = ctk.CTkEntry(frame_filtro, placeholder_text="200,300,500...", placeholder_text_color="gray")
            entry_data_filtro.place(x=0,y=30)

            radio1 = ctk.CTkRadioButton(frame_filtro, text="Todas Contas",font=('Poppins', 13), variable=filter_var, value="Todas Contas")
            radio1.place(x=0,y=70)

            radio2 = ctk.CTkRadioButton(frame_filtro, text="Pagas",font=('Poppins', 13), variable=filter_var, value="Pagas")
            radio2.place(x=0,y=100)

            radio3 = ctk.CTkRadioButton(frame_filtro, text="Não Pagas",font=('Poppins', 13), variable=filter_var, value="Não Pagas")
            radio3.place(x=0,y=130)

            botao_selecionar_radio = ctk.CTkButton(frame_filtro, text="Selecionar",font=('Poppins', 15), command=lambda:on_radio_change("valor", entry_data_filtro.get()))
            botao_selecionar_radio.place(x=0,y=160)


    def on_option_change_filtros(choice):
        filtros(choice)
    
    filtros_options = ["Data", "Tipo", "Valor"] 
    filtros_menu = ctk.CTkOptionMenu(    
    master=left_frame, 
    values=filtros_options, 
    font=('Poppins', 15),
    command=on_option_change_filtros,
    dropdown_font=("Poppins", 12),  
    button_color="lightblue",  
    dropdown_fg_color="#3c8cd4",
    dropdown_text_color="white"
    )
    filtros_menu.place(x=40,y=210)
    




def mostrar_clientes(tabela,frame,frame2,filtro,valor_filtro):

    destruir_widgets(frame)

    conex = sqlite3.connect('Banco_de_Dados.db')
    cursor = conex.cursor()

    if filtro == None and valor_filtro == None:
        cursor.execute(f"SELECT * FROM {tabela}")
    else:
        cursor.execute(f"SELECT * FROM {tabela} WHERE {filtro}=?", (valor_filtro,))

    clientes = cursor.fetchall()
    conex.close() 
    i=0
    for cliente in clientes:
        id_cliente = cliente[0]  
        nome_cliente = cliente[7]
        text_nome = f"{nome_cliente}"
        text_id= f"{id_cliente}"

        label_id = ctk.CTkLabel(frame,text=text_nome,image=add_image,font=('Poppins', 13),compound="left",anchor="w")
        label_id.grid(row=i,column=0, sticky='w')

        label_nome = ctk.CTkLabel(frame,text=f"ID:{text_id}",font=('Poppins', 13),image=key_image,compound="left",anchor="w")
        label_nome.grid(row=i+1,column=0, sticky='w')

        button = ctk.CTkButton(frame,text="Ver Mais>>", font=('Poppins', 13),width=200,
                                command=partial(mostrar_info_clientes,tabela,id_cliente,frame2,))
        
        button.grid(row=i+2,column=0,sticky='w')

        ctk.CTkLabel(frame,text="").grid(row=i+3,column=0,pady=5,sticky='w')

        i+=4
    



def verificar_situacao(id,nome_filtro,filtro):
    
    def novo_valor():

            global valor_inserido1
            global data_inserida
            valor_inserido1 = None
            data_inserida = None

            def retornar_novo_valor():
                global valor_inserido1
                global data_inserida
                valor_inserido1 = novo_valor_entry.get()
                data_inserida = nova_data_entry.get()
                tela.destroy()

            tela = ctk.CTkToplevel(janela_dados)
            tela.attributes('-topmost', True)
            janela_dados.attributes("-topmost", False)
            tela.geometry("+400+400")

            ctk.CTkLabel(tela, text="Novo Valor",font=("Poppins Bold",15)).place(x=10,y=5)
            novo_valor_entry = ctk.CTkEntry(tela)
            novo_valor_entry.place(x=10, y=35)
            ctk.CTkLabel(tela, text="Nova Data",font=("Poppins Bold",15)).place(x=10,y=65)
            nova_data_entry = ctk.CTkEntry(tela,font=("Poppins",13))
            nova_data_entry.place(x=10, y=95)

            nova_data_entry.bind("<KeyRelease>", lambda event: formatar_data_entry(nova_data_entry, event))


            botao_mudar = ctk.CTkButton(tela, text="Alterar", command=retornar_novo_valor)
            botao_mudar.place(x=10, y=130)

            tela.wait_window()  # Aguarda até que a janela seja fechada
        
    janela_dados = ctk.CTkToplevel(tela)
    janela_dados.title("Situaçao Cliente")
    janela_dados.geometry("1000x500")
    janela_dados.attributes('-topmost', True)
    

    principal_frame = ctk.CTkScrollableFrame(janela_dados)
    principal_frame.pack(fill="both", expand=True)
    

    db_path = 'Banco_de_Dados.db'

    conex = sqlite3.connect(db_path)
    cursor = conex.cursor()


    if id == None:
        
        if filtro == None and nome_filtro ==None:
            cursor.execute(f"SELECT * FROM Entradas")
            dados = cursor.fetchall()
            
        elif nome_filtro == "Data":
            cursor.execute(f"SELECT * FROM Entradas WHERE substr(data, 4, 2) = ? ",(filtro,))
            dados = cursor.fetchall()

        elif nome_filtro == "Dia":
            cursor.execute(f"SELECT * FROM Entradas WHERE data = ? ",(filtro,))
            dados = cursor.fetchall()

        elif nome_filtro == "Status":
            cursor.execute(f"SELECT * FROM Entradas WHERE status = ? ",(filtro,))
            dados = cursor.fetchall()

        else:
            cursor.execute(f"SELECT * FROM Entradas WHERE {nome_filtro} = ?",(filtro,))
            dados = cursor.fetchall()

    else:
        cursor.execute(f"SELECT * FROM Entradas WHERE id_cliente = ?",(id,))
        dados = cursor.fetchall()
        conex.close()

    checkboxes = []
    headers = [" Pagar "," ID ", " ID_Cliente ", "Nome", " Data ", " Valor ", " Valor Entrada ", " Status "]

    for col, header in enumerate(headers):
        ctk.CTkLabel(principal_frame, text=header, font=('Poppins Bold', 14)).grid(row=0, column=col,pady=10)

    for i, dado in enumerate(dados, start=1):

        check = ctk.IntVar()
        checkbox = ctk.CTkCheckBox(principal_frame,text="",width=10,variable=check)
        checkbox.grid(row=i,column=0)
        checkboxes.append((check, dado))

        for j, valor in enumerate(dado, start=1):
            ctk.CTkLabel(principal_frame, text=str(valor),font=('Poppins', 15)).grid(row=i, column=j,padx=10)


        
    def marcar_pagamento():

        conex = sqlite3.connect('Banco_de_Dados.db')
        cursor = conex.cursor()

        for check, dado in checkboxes:
            if check.get() == 1: 

                id, id_cliente, nome, data, valor, valor_entrada, status = dado   
                
                valor = valor * 0.1

                arquivo = "saldo.json"
                with open(arquivo, 'r') as f:
                    dados = json.load(f)
                    saldo = dados.get('saldo', 0)
                
                status_new = "Pago!"
                entrada = valor
                novo_saldo = saldo + entrada

                cursor.execute('''
                UPDATE Entradas
                SET status = ?
                WHERE id = ? AND status = ?
                ''',(status_new, id, status))

                ask_valor = messagebox.askyesno("Confirmaçao",f"Voce deseja mudar o valor do Aluguel ID: {id_cliente}, Data:{data}? Valor atual:{valor}",parent=janela_dados)
                
                if ask_valor:
                    novo_valor()
                    valor_novo = float(valor_inserido1)
                    data = data_inserida

                    cursor.execute('''
                    UPDATE Entradas
                    SET status = ?, data = ?, valor = ?
                    WHERE id = ?
                    ''',(status_new,data,valor_novo,id))

                with open(arquivo, 'w') as f:
                    json.dump({'saldo': novo_saldo}, f)

                cursor.execute('''
                INSERT INTO movimentacao (tipo,tipo1,descricao,valor,data)
                VALUES (?,?,?,?,?)

                ''', ("Entrada", "Entrada Aluguel", "Pag. Aluguel" + f" ID: {id_cliente}", entrada, data))

    
        
        conex.commit()
        conex.close()
        messagebox.showinfo("Sucesso", "Entradas Recebidas com sucesso!", parent=janela_dados)
        janela_dados.destroy()
        verificar_situacao(id_cliente, None, None)
    
    botao_receber = ctk.CTkButton(principal_frame, text="Receber Entrada",font=("Poppins",15), command=marcar_pagamento)
    botao_receber.grid(row=i+1,column=1,pady=30)
        


def mostrar_info_clientes(tabela,id_cliente,frame,):


    def atualizar_cliente():

        def confirmar():

            def salvar_dados(entries):

                conn = sqlite3.connect('banco_de_dados.db')
                cursor = conn.cursor()

                # Verifique se o campo foi preenchido antes de tentar atualizar no banco de dados
                if "id" in entries and entries["id"].get():
                    novo_id = entries["id"].get()
                    cursor.execute("UPDATE clientes SET id = ? WHERE id = ?", (novo_id, id_cliente))

                if "nome_locador" in entries and entries["nome_locador"].get():
                    novo_nome_locador = entries["nome_locador"].get()
                    cursor.execute("UPDATE clientes SET nome_locador = ? WHERE id = ?", (novo_nome_locador, id_cliente))

                if "nome_locatario" in entries and entries["nome_locatario"].get():
                    novo_nome_locatario = entries["nome_locatario"].get()
                    cursor.execute("UPDATE clientes SET nome_locatario = ? WHERE id = ?", (novo_nome_locatario, id_cliente))

                if "data" in entries and entries["data"].get():
                    nova_data = entries["data"].get()
                    cursor.execute("UPDATE clientes SET data = ? WHERE id = ?", (nova_data, id_cliente))

                if "valor_aluguel" in entries and entries["valor_aluguel"].get():
                    novo_valor_aluguel = entries["valor_aluguel"].get()
                    cursor.execute("UPDATE clientes SET valor_aluguel = ? WHERE id = ?", (novo_valor_aluguel, id_cliente))

                if "primeiro_aluguel" in entries and entries["primeiro_aluguel"].get():
                    novo_primeiro_aluguel = entries["primeiro_aluguel"].get()
                    cursor.execute("UPDATE clientes SET primeiro_aluguel = ? WHERE id = ?", (novo_primeiro_aluguel, id_cliente))

                if "caucao" in entries and entries["caucao"].get():
                    novo_caucao = entries["caucao"].get()
                    cursor.execute("UPDATE clientes SET caucao = ? WHERE id = ?", (novo_caucao, id_cliente))

                if "corretor1" in entries and entries["corretor1"].get():
                    novas_info_corretor1 = entries["corretor1"].get()
                    cursor.execute("UPDATE clientes SET corretor1 = ? WHERE id = ?", (novas_info_corretor1, id_cliente))

                if "comissao1" in entries and entries["comissao1"].get():
                    nova_comissao1 = entries["comissao1"].get()
                    cursor.execute("UPDATE clientes SET comissao1 = ? WHERE id = ?", (nova_comissao1, id_cliente))

                if "corretor2" in entries and entries["corretor2"].get():
                    novas_info_corretor2 = entries["corretor2"].get()
                    cursor.execute("UPDATE clientes SET corretor2 = ? WHERE id = ?", (novas_info_corretor2, id_cliente))

                if "comissao2" in entries and entries["comissao2"].get():
                    nova_comissao2 = entries["comissao2"].get()
                    cursor.execute("UPDATE clientes SET comissao2 = ? WHERE id = ?", (nova_comissao2, id_cliente))

                if "corretor3" in entries and entries["corretor3"].get():
                    novas_info_corretor3 = entries["corretor3"].get()
                    cursor.execute("UPDATE clientes SET corretor3 = ? WHERE id = ?", (novas_info_corretor3, id_cliente))

                if "comissao3" in entries and entries["comissao3"].get():
                    nova_comissao3 = entries["comissao3"].get()
                    cursor.execute("UPDATE clientes SET comissao3 = ? WHERE id = ?", (nova_comissao3, id_cliente))

                if "corretor4" in entries and entries["corretor4"].get():
                    novas_info_corretor4 = entries["corretor4"].get()
                    cursor.execute("UPDATE clientes SET corretor4 = ? WHERE id = ?", (novas_info_corretor4, id_cliente))

                if "comissao4" in entries and entries["comissao4"].get():
                    nova_comissao4 = entries["comissao4"].get()
                    cursor.execute("UPDATE clientes SET comissao4 = ? WHERE id = ?", (nova_comissao4, id_cliente))
                                # Salva as alterações e fecha a conexão com o banco de dados

                conn.commit()
                conn.close()

                messagebox.showinfo("Sucesso!", "Dados do Cliente atualizados com Sucesso!",parent=janela_atualizar)
                janela_atualizar.destroy()

                mostrar_info_clientes(tabela,id_cliente,frame)


            destruir_widgets(frame_main)
            ctk.CTkLabel(frame_main, text="Alterações", font=("Poppins Bold", 15)).grid(row=0, column=0, padx=20,pady=20, sticky="w")

            entries = {}

            # Criação dos Entry dinamicamente, com base nas CheckBox marcadas
            row_counter = 1
            
            if var_id.get():
                ctk.CTkLabel(frame_main, text="Novo ID do Cliente:",font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                entries["id"] = ctk.CTkEntry(frame_main,placeholder_text=f"{cliente[0]}")
                entries["id"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                row_counter += 1

            if var_nome_locador.get():
                if tipo == "Venda":
                    ctk.CTkLabel(frame_main, text="Novo Nome do Vendedor:",font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                    entries["nome_locador"] = ctk.CTkEntry(frame_main,placeholder_text=f"{cliente[7]}")
                    entries["nome_locador"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                    row_counter += 1
                else:
                    ctk.CTkLabel(frame_main, text="Novo Nome do Locador:",font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                    entries["nome_locador"] = ctk.CTkEntry(frame_main,placeholder_text=f"{cliente[7]}")
                    entries["nome_locador"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                    row_counter += 1

            if var_nome_locatario.get():
                if tipo == "Venda":
                    ctk.CTkLabel(frame_main, text="Novo Nome do Comprador:",font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                    entries["nome_locatario"] = ctk.CTkEntry(frame_main,placeholder_text=f"{cliente[8]}")
                    entries["nome_locatario"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                    row_counter += 1
                else:
                    ctk.CTkLabel(frame_main, text="Novo Nome do Locatário:",font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                    entries["nome_locatario"] = ctk.CTkEntry(frame_main,placeholder_text=f"{cliente[8]}")
                    entries["nome_locatario"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                    row_counter += 1

            if var_valor.get():
                ctk.CTkLabel(frame_main, text="Novo Valor de Venda:", font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                entries["valor"] = ctk.CTkEntry(frame_main, placeholder_text=f"{cliente[2]}")  # Substitua pelo índice correto
                entries["valor"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                row_counter += 1

            if var_entrada.get():
                ctk.CTkLabel(frame_main, text="Nova Porcentagem Trabalhada:", font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                entries["entrada"] = ctk.CTkEntry(frame_main, placeholder_text=f"{cliente[4]}")  # Substitua pelo índice correto
                entries["entrada"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                row_counter += 1

            if var_data.get():
                ctk.CTkLabel(frame_main, text="Nova Data:",font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                entries["data"] = ctk.CTkEntry(frame_main,placeholder_text=f"{cliente[9]}")
                entries["data"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                entries["data"].bind("<KeyRelease>", lambda event: formatar_data_entry(entries["data"],event))

                row_counter += 1

            if var_valor_aluguel.get():
                ctk.CTkLabel(frame_main, text="Novo Valor do Aluguel:",font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                entries["valor_aluguel"] = ctk.CTkEntry(frame_main,placeholder_text=f"{cliente[3]}")
                entries["valor_aluguel"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                row_counter += 1

            if var_primeiro_aluguel.get():
                ctk.CTkLabel(frame_main, text="Novo Valor do Primeiro Aluguel:",font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                entries["primeiro_aluguel"] = ctk.CTkEntry(frame_main,placeholder_text=f"{cliente[5]}")
                entries["primeiro_aluguel"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                row_counter += 1


            if var_caucao.get():
                ctk.CTkLabel(frame_main, text="Novo Valor de Caução:",font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                entries["caucao"] = ctk.CTkEntry(frame_main,placeholder_text=f"{cliente[6]}")
                entries["caucao"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                row_counter += 1

            if var_corretor1.get():
                ctk.CTkLabel(frame_main, text="Novas Informações Corretor 1:", font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                entries["corretor1"] = ctk.CTkEntry(frame_main, placeholder_text=f"{cliente[10]}")
                entries["corretor1"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                entries["comissao1"] = ctk.CTkEntry(frame_main, width=60, placeholder_text=f"{2 * float(comissao_1)}")
                entries["comissao1"].grid(row=row_counter, column=2, pady=10, padx=5, sticky="w")
                row_counter += 1

            if var_corretor2.get():
                ctk.CTkLabel(frame_main, text="Novas Informações Corretor 2:", font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                entries["corretor2"] = ctk.CTkEntry(frame_main, placeholder_text=f"{cliente[12]}")  # Supondo que cliente[12] seja o nome do corretor 2
                entries["corretor2"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                entries["comissao2"] = ctk.CTkEntry(frame_main, width=60, placeholder_text=f"{2 * float(comissao_2)}")  # Supondo que cliente[13] seja a comissão do corretor 2
                entries["comissao2"].grid(row=row_counter, column=2, pady=10, padx=5, sticky="w")
                row_counter += 1

            if var_corretor3.get():
                ctk.CTkLabel(frame_main, text="Novas Informações Corretor 3:", font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                entries["corretor3"] = ctk.CTkEntry(frame_main, placeholder_text=f"{cliente[14]}")  # Supondo que cliente[14] seja o nome do corretor 3
                entries["corretor3"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                entries["comissao3"] = ctk.CTkEntry(frame_main, width=60, placeholder_text=f"{2 * float(comissao_3)}")  # Supondo que cliente[15] seja a comissão do corretor 3
                entries["comissao3"].grid(row=row_counter, column=2, pady=10, padx=5, sticky="w")
                row_counter += 1

            if var_corretor4.get():
                ctk.CTkLabel(frame_main, text="Novas Informações Corretor 4:", font=("Poppins", 14)).grid(row=row_counter, column=0, padx=20, pady=10, sticky="w")
                entries["corretor4"] = ctk.CTkEntry(frame_main, placeholder_text=f"{cliente[16]}")  # Supondo que cliente[16] seja o nome do corretor 4
                entries["corretor4"].grid(row=row_counter, column=1, padx=10, pady=10, sticky="w")
                entries["comissao4"] = ctk.CTkEntry(frame_main, width=60, placeholder_text=f"{2 * float(comissao_4)}")  # Supondo que cliente[17] seja a comissão do corretor 4
                entries["comissao4"].grid(row=row_counter, column=2, pady=10, padx=5, sticky="w")
                row_counter += 1

            # Botão para salvar as alterações
            salvar_btn = ctk.CTkButton(frame_main, text="Salvar Alterações",font=("Poppins", 14),command=lambda: salvar_dados(entries))
            salvar_btn.grid(row=row_counter, column=0, columnspan=2, padx=20, pady=20)




        janela_atualizar = ctk.CTkToplevel(tela)
        janela_atualizar.title("Atualizar Dados")
        #janela_atualizar.geometry("800x600")
        janela_atualizar.attributes('-topmost', True)

        frame_main= ctk.CTkFrame(janela_atualizar)
        frame_main.pack(fill="both", expand=True)
        
        ctk.CTkLabel(frame_main, text="O que deseja alterar?", font=("Poppins Bold", 15)).grid(row=0, column=0, padx=20,pady=20, sticky="w")

        var_id = ctk.BooleanVar()
        var_nome_locador = ctk.BooleanVar()
        var_nome_locatario = ctk.BooleanVar()
        var_data = ctk.BooleanVar()
        
        var_valor = ctk.BooleanVar()
        var_entrada = ctk.BooleanVar()
        var_valor_aluguel = ctk.BooleanVar()
        var_primeiro_aluguel = ctk.BooleanVar()
        var_caucao = ctk.BooleanVar()

        var_corretor1 = ctk.BooleanVar()
        var_corretor2 = ctk.BooleanVar()
        var_corretor3 = ctk.BooleanVar()
        var_corretor4 = ctk.BooleanVar()

        if tipo == "Venda":
            
            # CheckBox para ID
            check_id = ctk.CTkCheckBox(frame_main, text="ID do Cliente",font=("Poppins", 14), variable=var_id)
            check_id.grid(row=1, column=0, padx=20, pady=10, sticky="w")

            # CheckBox para Nome do Locador
            check_nome_locador = ctk.CTkCheckBox(frame_main, text="Nome do Vendedor",font=("Poppins", 14), variable=var_nome_locador)
            check_nome_locador.grid(row=2, column=0, padx=20, pady=10, sticky="w")

            # CheckBox para Nome do Locatário
            check_nome_locatario = ctk.CTkCheckBox(frame_main, text="Nome do Comprador",font=("Poppins", 14), variable=var_nome_locatario)
            check_nome_locatario.grid(row=3, column=0, padx=20, pady=10, sticky="w")

            # CheckBox para Data
            check_data = ctk.CTkCheckBox(frame_main, text="Data",font=("Poppins", 14), variable=var_data)
            check_data.grid(row=5, column=0, padx=20, pady=10, sticky="w")

            # CheckBox para Valor (Venda)
            check_valor = ctk.CTkCheckBox(frame_main, text="Valor da Venda",font=("Poppins", 14), variable=var_valor)
            check_valor.grid(row=6, column=0, padx=20, pady=10, sticky="w")

            # CheckBox para Entrada (Venda)
            check_entrada = ctk.CTkCheckBox(frame_main, text="Entrada",font=("Poppins", 14), variable=var_entrada)
            check_entrada.grid(row=7, column=0, padx=20, pady=10, sticky="w")

            check_corretor1 = ctk.CTkCheckBox(frame_main, text="Informaçoes Corretor 1",font=("Poppins", 14), variable=var_corretor1)
            check_corretor1.grid(row=8, column=0, padx=20, pady=10, sticky="w")

            check_corretor2 = ctk.CTkCheckBox(frame_main, text="Informaçoes Corretor 2",font=("Poppins", 14), variable=var_corretor2)
            check_corretor2.grid(row=9, column=0, padx=20, pady=10, sticky="w")

            check_corretor3 = ctk.CTkCheckBox(frame_main, text="Informaçoes Corretor 3",font=("Poppins", 14), variable=var_corretor3)
            check_corretor3.grid(row=10, column=0, padx=20, pady=10, sticky="w")

            check_corretor4 = ctk.CTkCheckBox(frame_main, text="Informaçoes Corretor 4",font=("Poppins", 14), variable=var_corretor4)
            check_corretor4.grid(row=11, column=0, padx=20, pady=10, sticky="w")
        
        elif tipo == "Aluguel":

            check_id = ctk.CTkCheckBox(frame_main, text="ID do Cliente",font=("Poppins", 14), variable=var_id)
            check_id.grid(row=1, column=0, padx=20, pady=10, sticky="w")

            # CheckBox para Nome do Locador
            check_nome_locador = ctk.CTkCheckBox(frame_main, text="Nome do Locador",font=("Poppins", 14), variable=var_nome_locador)
            check_nome_locador.grid(row=2, column=0, padx=20, pady=10, sticky="w")

            # CheckBox para Nome do Locatário
            check_nome_locatario = ctk.CTkCheckBox(frame_main, text="Nome do Locatario",font=("Poppins", 14), variable=var_nome_locatario)
            check_nome_locatario.grid(row=3, column=0, padx=20, pady=10, sticky="w")

            # CheckBox para Data
            check_data = ctk.CTkCheckBox(frame_main, text="Data",font=("Poppins", 14), variable=var_data)
            check_data.grid(row=5, column=0, padx=20, pady=10, sticky="w")

            check_valor_aluguel = ctk.CTkCheckBox(frame_main, text="Valor do Aluguel",font=("Poppins", 14), variable=var_valor_aluguel)
            check_valor_aluguel.grid(row=6, column=0, padx=20, pady=10, sticky="w")

            check_primeiro_aluguel = ctk.CTkCheckBox(frame_main, text="Entrada",font=("Poppins", 14), variable=var_primeiro_aluguel)
            check_primeiro_aluguel.grid(row=7, column=0, padx=20, pady=10, sticky="w")

            check_caucao = ctk.CTkCheckBox(frame_main, text="Entrada",font=("Poppins", 14), variable=var_caucao)
            check_caucao.grid(row=8, column=0, padx=20, pady=10, sticky="w")

            check_corretor1 = ctk.CTkCheckBox(frame_main, text="Informaçoes Corretor 1",font=("Poppins", 14), variable=var_corretor1)
            check_corretor1.grid(row=8, column=0, padx=20, pady=10, sticky="w")

            check_corretor2 = ctk.CTkCheckBox(frame_main, text="Informaçoes Corretor 2",font=("Poppins", 14), variable=var_corretor2)
            check_corretor2.grid(row=9, column=0, padx=20, pady=10, sticky="w")

            check_corretor3 = ctk.CTkCheckBox(frame_main, text="Informaçoes Corretor 3",font=("Poppins", 14), variable=var_corretor3)
            check_corretor3.grid(row=10, column=0, padx=20, pady=10, sticky="w")

            check_corretor4 = ctk.CTkCheckBox(frame_main, text="Informaçoes Corretor 4",font=("Poppins", 14), variable=var_corretor4)
            check_corretor4.grid(row=11, column=0, padx=20, pady=10, sticky="w")

        botao_salvar_altera = ctk.CTkButton(frame_main, text="Alterar", font=("Poppins", 14), command=confirmar)
        botao_salvar_altera.grid(row=12,column=0, padx=20,pady=10)
        
            
    def deletar_cliente():

        conn = sqlite3.connect("Banco_de_Dados.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))
        
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso!", "Cliente removido com sucesso!", parent=tela)

        exibir_informacoes_clientes()



    def meses_pagamento(data,id,valor,primeiro,com1,com2,com3,com4,tipo_cliente): 

        db_path = 'Banco_de_Dados.db'

        conex = sqlite3.connect(db_path)
        cursor = conex.cursor()

        cursor.execute(''' CREATE TABLE IF NOT EXISTS comissoes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            cpf_corretor TEXT,
                            tipo_operacao TEXT,
                            valor_comissao FLOAT,
                            data_comissao TEXT,
                            id_cliente INTEGER,
                            nome_cliente TEXT,
                            descricao TEXT,
                            FOREIGN KEY (cpf_corretor) REFERENCES corretores(cpf)
                        );''')

        dia, mes, ano = data.split("/")

        if tipo_cliente == "Aluguel":

            quantidade = 12
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)

            com1 = float(com1)
            com2 = float(com2)
            com3 = float(com3)
            com4 = float(com4)
            
            com_total = com1 + com2 + com3 + com4   

            comissa_corretor = primeiro * (com_total/100)
            franquia = primeiro * 0.09

            entrada = primeiro - comissa_corretor

            entrada_1 = valor * 0.10

            status = "Aguardando Pg."  
            status_1 = "Pago!"

            data_inicial = f"{int(dia):02}/{int(mes):02}/{int(ano):02}"

            tipo_operacao = "Aluguel"
            descricao = "Comissão 1° Aluguel"
            data_comissao = data_inic.get()


            if corretor_1 is not None:
                cursor.execute("SELECT * FROM corretores WHERE nome = ?", (corretor_1,))
                corr_1 = cursor.fetchone()
                if corr_1 is not None:
                    cpf_corretor1 = corr_1[0]
                    cursor.execute('''
                        INSERT INTO comissoes (cpf_corretor, tipo_operacao, valor_comissao, data_comissao, id_cliente, nome_cliente, descricao)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (cpf_corretor1, tipo_operacao, (com1/100) * primeiro, data_comissao, id_cliente, nome_locador, descricao))

            if corretor_2 is not None:
                cursor.execute("SELECT * FROM corretores WHERE nome = ?", (corretor_2,))
                corr_2 = cursor.fetchone()
                if corr_2 is not None:
                    cpf_corretor2 = corr_2[0]
                    cursor.execute('''
                        INSERT INTO comissoes (cpf_corretor, tipo_operacao, valor_comissao, data_comissao, id_cliente, nome_cliente, descricao)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (cpf_corretor2, tipo_operacao, (com2/100) * primeiro, data_comissao, id_cliente,nome_locador, descricao))

            if corretor_3 is not None:
                cursor.execute("SELECT * FROM corretores WHERE nome = ?", (corretor_3,))
                corr_3 = cursor.fetchone()
                if corr_3 is not None:
                    cpf_corretor3 = corr_3[0]
                    cursor.execute('''
                        INSERT INTO comissoes (cpf_corretor, tipo_operacao, valor_comissao, data_comissao, id_cliente, nome_cliente, descricao)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (cpf_corretor3, tipo_operacao, (com3/100) * primeiro, data_comissao, id_cliente,nome_locador, descricao))

            if corretor_4 is not None:
                cursor.execute("SELECT * FROM corretores WHERE nome = ?", (corretor_4,))
                corr_4 = cursor.fetchone()
                if corr_4 is not None:
                    cpf_corretor4 = corr_4[0]
                    cursor.execute('''
                        INSERT INTO comissoes (cpf_corretor, tipo_operacao, valor_comissao, data_comissao, id_cliente, nome_cliente, descricao)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (cpf_corretor4, tipo_operacao, (com4/100) * primeiro, data_comissao, id_cliente,nome_locador, descricao))


            def atualizar_corretor(corretor_nome, comissao):
                cursor.execute('''
                    UPDATE corretores
                    SET comissao_total = comissao_total + ?,
                        qtd_aluguel = qtd_aluguel + 1
                        WHERE nome = ?
                ''', (comissao, corretor_nome))

            if com1 != 0:
                atualizar_corretor(cliente[10], (com1 / 100) * primeiro)
            if com2 != 0:
                atualizar_corretor(cliente[12], (com2 / 100) * primeiro)
            if com3 != 0:
                atualizar_corretor(cliente[14], (com3 / 100) * primeiro)
            if com4 != 0:
                atualizar_corretor(cliente[16], (com4 / 100) * primeiro)



            cursor.execute('''
                INSERT INTO Entradas (id_cliente,nome,data,valor,valor_entrada,status)
                VALUES (?,?,?,?,?,?)

                ''', (id,nome_locador, data_inicial, valor, entrada, status_1))
            

            cursor.execute('''
                INSERT INTO movimentacao (tipo,tipo1,descricao,valor,data)
                VALUES (?,?,?,?,?)

                ''', ("Entrada", "Entrada do 1° Aluguel", "Pag. 1° Aluguel" + f" ID: {id}", entrada, data_inicial))


            cursor.execute('''
                INSERT INTO movimentacao (tipo,tipo1,descricao,valor,data)
                VALUES (?,?,?,?,?)

                ''', ("Saída", f"Comissão de {2*com1}% /" + f"Corretor: {cliente[10]}", f" ID: {id}", (com1/100)*primeiro, data_inicial))
            
            if com2 != 0:
                cursor.execute('''
                INSERT INTO movimentacao (tipo,tipo1,descricao,valor,data)
                VALUES (?,?,?,?,?)

                ''', ("Saída", f"Comissão de {2*com2}% /" + f"Corretor: {cliente[12]}", f" ID: {id}", (com2/100)*primeiro, data_inicial))

            if com3 != 0:
                cursor.execute('''
                INSERT INTO movimentacao (tipo,tipo1,descricao,valor,data)
                VALUES (?,?,?,?,?)

                ''', ("Saída", f"Comissão de {2*com3}% /" + f"Corretor: {cliente[14]}", f" ID: {id}", (com3/100)*primeiro, data_inicial))
            
            if com4 != 0:
                cursor.execute('''
                INSERT INTO movimentacao (tipo,tipo1,descricao,valor,data)
                VALUES (?,?,?,?,?)

                ''', ("Saída", f"Comissão de {2*com4}% /" + f"Corretor: {cliente[16]}", f" ID: {id}", (com4/100)*primeiro, data_inicial))

            


            i=0
            quantidade = quantidade - 1
            for i in range(quantidade):

                mes += 1

                if mes > 12:
                    mes=1
                    ano += 1

                data_inicial = f"{int(dia):02}/{int(mes):02}/{int(ano):02}"

                cursor.execute('''
                    INSERT INTO Entradas (id_cliente,nome,data,valor,valor_entrada,status)
                    VALUES (?,?,?,?,?,?)

                    ''', (id, nome_locador, data_inicial, valor, entrada_1, status))
                
                

            arquivo = "saldo.json"
            with open(arquivo, 'r') as f:
                dados = json.load(f)
                saldo = dados.get('saldo', 0)
            
            novo_saldo = saldo + entrada

            with open(arquivo, 'w') as f:
                json.dump({'saldo': novo_saldo}, f)
            

            conex.commit()
            conex.close()
            messagebox.showinfo("Sucesso!", "Dados enviados ao banco de dados com sucesso!", parent=frame)
        
        elif tipo == "Venda":

            dia = int(dia)
            mes = int(mes)
            ano = int(ano)

            com1 = float(com1)
            com2 = float(com2)
            com3 = float(com3)
            com4 = float(com4)
            
            com_total = (com1 + com2 + com3 + com4)/100
            franquia = 9/100
            valor_trabalhar = valor * (primeiro/100)

            saida_total = com_total * valor_trabalhar
            entrada_total = valor_trabalhar - saida_total

            status = "Aguardando Pg."  
            status_1 = "Pago!"

            data_inicial = f"{int(dia):02}/{int(mes):02}/{int(ano):02}"

            tipo_operacao = "Venda"
            descricao = "Comissão Venda"
            data_comissao = data_inic.get()

            if corretor_1 is not None:
                cursor.execute("SELECT * FROM corretores WHERE nome = ?", (corretor_1,))
                corr_1 = cursor.fetchone()
                if corr_1 is not None:
                    cpf_corretor1 = corr_1[0]
                    cursor.execute('''
                        INSERT INTO comissoes (cpf_corretor, tipo_operacao, valor_comissao, data_comissao, id_cliente, nome_cliente, descricao)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (cpf_corretor1, tipo_operacao, (com1/100) * valor_trabalhar, data_comissao, id_cliente,nome_locador, descricao))

            if corretor_2 is not None:
                cursor.execute("SELECT * FROM corretores WHERE nome = ?", (corretor_2,))
                corr_2 = cursor.fetchone()
                if corr_2 is not None:
                    cpf_corretor2 = corr_2[0]
                    cursor.execute('''
                        INSERT INTO comissoes (cpf_corretor, tipo_operacao, valor_comissao, data_comissao, id_cliente, nome_cliente, descricao)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (cpf_corretor2, tipo_operacao, (com2/100) *  valor_trabalhar, data_comissao, id_cliente,nome_locador, descricao))

            if corretor_3 is not None:
                cursor.execute("SELECT * FROM corretores WHERE nome = ?", (corretor_3,))
                corr_3 = cursor.fetchone()
                if corr_3 is not None:
                    cpf_corretor3 = corr_3[0]
                    cursor.execute('''
                        INSERT INTO comissoes (cpf_corretor, tipo_operacao, valor_comissao, data_comissao, id_cliente, nome_cliente, descricao)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (cpf_corretor3, tipo_operacao, (com3/100) *  valor_trabalhar, data_comissao, id_cliente,nome_locador, descricao))

            if corretor_4 is not None:
                cursor.execute("SELECT * FROM corretores WHERE nome = ?", (corretor_4,))
                corr_4 = cursor.fetchone()
                if corr_4 is not None:
                    cpf_corretor4 = corr_4[0]
                    cursor.execute('''
                        INSERT INTO comissoes (cpf_corretor, tipo_operacao, valor_comissao, data_comissao, id_cliente, nome_cliente, descricao)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    ''', (cpf_corretor4, tipo_operacao, (com4/100) *  valor_trabalhar, data_comissao, id_cliente,nome_locador, descricao))


            def atualizar_corretor_venda(corretor_nome, comissao):
                cursor.execute('''
                    UPDATE corretores
                    SET comissao_total = comissao_total + ?,
                        qtd_vendas = qtd_vendas + 1
                        WHERE nome = ?
                ''', (comissao, corretor_nome))

            if com1 != 0:
                atualizar_corretor_venda(cliente[10], (com1 / 100) * valor_trabalhar)
            if com2 != 0:
                atualizar_corretor_venda(cliente[12], (com2 / 100) * valor_trabalhar)
            if com3 != 0:
                atualizar_corretor_venda(cliente[14], (com3 / 100) * valor_trabalhar)
            if com4 != 0:
                atualizar_corretor_venda(cliente[16], (com4 / 100) * valor_trabalhar)


            cursor.execute('''
                INSERT INTO Entradas (id_cliente,nome,data,valor,valor_entrada,status)
                VALUES (?,?,?,?,?,?)

                ''', (id,nome_locador, data_inicial, valor, entrada_total, status_1))
            
            cursor.execute('''
                INSERT INTO movimentacao (tipo,tipo1,descricao,valor,data)
                VALUES (?,?,?,?,?)

                ''', ("Entrada", "Entrada Pag. da Venda", "Pag. Venda" + f" ID: {id}", entrada_total, data_inicial))


            cursor.execute('''
                INSERT INTO movimentacao (tipo,tipo1,descricao,valor,data)
                VALUES (?,?,?,?,?)

                ''', ("Saída", f"Comissão de {2*com1}% /" + f"Corretor: {cliente[10]}", f" ID: {id}", (com1/100)*valor_trabalhar, data_inicial))
            
            if com2 != 0:
                cursor.execute('''
                INSERT INTO movimentacao (tipo,tipo1,descricao,valor,data)
                VALUES (?,?,?,?,?)

                ''', ("Saída", f"Comissão de {2*com2}% /" + f"Corretor: {cliente[12]}", f" ID: {id}", (com2/100)*valor_trabalhar, data_inicial))

            if com3 != 0:
                cursor.execute('''
                INSERT INTO movimentacao (tipo,tipo1,descricao,valor,data)
                VALUES (?,?,?,?,?)

                ''', ("Saída", f"Comissão de {2*com3}% /" + f"Corretor: {cliente[14]}", f" ID: {id}", (com3/100)*valor_trabalhar, data_inicial))
            
            if com4 != 0:
                cursor.execute('''
                INSERT INTO movimentacao (tipo,tipo1,descricao,valor,data)
                VALUES (?,?,?,?,?)

                ''', ("Saída", f"Comissão de {2*com4}% /" + f"Corretor: {cliente[16]}", f" ID: {id}", (com4/100)*valor_trabalhar, data_inicial))


            
            arquivo = "saldo.json"
            with open(arquivo, 'r') as f:
                dados = json.load(f)
                saldo = dados.get('saldo', 0)
            
            novo_saldo = saldo + entrada_total

            with open(arquivo, 'w') as f:
                json.dump({'saldo': novo_saldo}, f)
            

            conex.commit()
            conex.close()

            messagebox.showinfo("Sucesso!", "Dados enviados ao banco de dados com sucesso!", parent=frame)


        mostrar_info_clientes(tabela,id_cliente,frame)
        


    destruir_widgets(frame)

    conex = sqlite3.connect('Banco_de_Dados.db')
    cursor = conex.cursor()
    cursor.execute(f"SELECT * FROM {tabela} WHERE id=?",(id_cliente,))
    cliente = cursor.fetchone()
    conex.close()

    if cliente:

        id_cliente = cliente[0]               # id
        tipo = cliente[1]                     # tipo
        valor = cliente[2]                    # valor (venda ou aluguel)
        valor_aluguel = cliente[3]            # valor_aluguel
        entrada = cliente[4]                  # entrada
        primeiro_aluguel = cliente[5]         # primeiro_aluguel
        calcao = cliente[6]                   # caucao
        nome_locador = cliente[7]             # nome_locador
        nome_locatario = cliente[8]          # nome_locatario
        data = cliente[9]                    # data
        corretor_1 = cliente[10]              # corretor1
        comissao_1 = cliente[11]              # comissao1
        corretor_2 = cliente[12]              # corretor2
        comissao_2 = cliente[13]              # comissao2
        corretor_3 = cliente[14]              # corretor3
        comissao_3 = cliente[15]              # comissao3
        corretor_4 = cliente[16]              # corretor4
        comissao_4 = cliente[17]  
        royalties = cliente[18]


    if comissao_1 == None:
        comissao_1=0
    
    if comissao_2 == None:
        comissao_2=0

    if comissao_3 == None:
        comissao_3=0

    if comissao_4 == None:
        comissao_4=0


    ctk.CTkLabel(frame, text="Informações do Cliente", image=add_image, 
             font=('Poppins', 14), fg_color="#3c8cd4",
             corner_radius=15, text_color="white", anchor="w", compound="left").grid(row=0, column=0, pady=10, sticky="w")

    ctk.CTkLabel(frame, text=f"ID: {id_cliente}", font=("Poppins", 14),
                fg_color="#3c8cd4", image=key_image, corner_radius=10,
                text_color="white", anchor="w", compound="left").grid(row=1, column=0, pady=10, sticky="w")
        
    ctk.CTkLabel(frame, text=f"Tipo: {tipo}", font=("Poppins", 14)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Locador: {nome_locador}", font=("Poppins", 14)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Locatário: {nome_locatario}", font=("Poppins", 14)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Data: {data}", font=("Poppins", 14)).grid(row=5, column=0, padx=10, pady=10, sticky="w")

    botao_atualizar_dados = ctk.CTkButton(frame,text="Alterar Dados", font=("Poppins", 14),
                                        command= atualizar_cliente)
    botao_atualizar_dados.grid(row=12,column=1,padx=10,pady=10,sticky="w")

    botao_deletar =  ctk.CTkButton(frame,text="Deletar Cliente", font=("Poppins", 14), fg_color="#b95557", hover_color="#bd3038",
                                        command= deletar_cliente)
    botao_deletar.grid(row=11,column=1,padx=10,pady=10,sticky="w")

    conex = sqlite3.connect('Banco_de_Dados.db')
    cursor = conex.cursor()
    cursor.execute('SELECT id FROM Entradas WHERE id_cliente = ?', (id_cliente,))
    resultado = cursor.fetchone()

    cursor.execute('SELECT data,valor_entrada FROM Entradas WHERE id_cliente = ?', (id_cliente,))
    valores_al = cursor.fetchone()

    
    conex.close

    if resultado == None:
        ctk.CTkLabel(frame, text="< Data do 1° Pagamento (Aluguel/Venda) >", font=("Poppins Bold", 14)).grid(row=8, column=0, padx=10, pady=10, sticky="w")
        data_inic = ctk.CTkEntry(frame, font=("Poppins", 13))
        data_inic.grid(row=9, column=0, padx=10, sticky="w")
        data_inic.bind("<KeyRelease>", lambda event: formatar_data_entry(data_inic,event))
        

    else:

        botao_verificar = ctk.CTkButton(frame,text="Verificar Situação", font=("Poppins", 14),
                                        command=lambda:verificar_situacao(id_cliente, None, None))
        botao_verificar.grid(row=11,column=0,padx=10,pady=10,sticky="w")
        ctk.CTkLabel(frame,text=f"< Primeiro pagamento ja realizado >",font=("Poppins Bold", 14)).grid(row=8, column=0, padx=10, pady=10, sticky="w")

        for valor_1 in valores_al:

            data_init, valor_entrada = valores_al

            ctk.CTkLabel(frame,text=f"Data: {data_init}",font=("Poppins", 14)).grid(row=9, column=0, padx=10, pady=10, sticky="w")
            ctk.CTkLabel(frame,text=f"Entrada: R$ {valor_entrada}",font=("Poppins", 14)).grid(row=10, column=0, padx=10, pady=10, sticky="w")

            

    # Informações específicas para Aluguel
    if tipo == "Aluguel":
        ctk.CTkLabel(frame, text=f"Valor 1° Aluguel: R${primeiro_aluguel}", font=("Poppins", 14)).grid(row=6, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(frame, text=f"Valor do Aluguel: R${valor_aluguel}", font=("Poppins", 14)).grid(row=7, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(frame, text=f"Calção: R${calcao}", font=("Poppins", 14)).grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        if resultado == None:
            botao_criar_meses_pg = ctk.CTkButton(frame, text="Primeiro Aluguel", font=("Poppins", 14),
                                                command=lambda:meses_pagamento(data_inic.get(),id_cliente,valor_aluguel,
                                                                               primeiro_aluguel,comissao_1,comissao_2,comissao_3,comissao_4,tipo))
            
            botao_criar_meses_pg.grid(row=12,column=0,padx=10,pady=10,sticky="w")

    
        valor_comissao1 = float(primeiro_aluguel) * (float(comissao_1)/100)
        valor_comissao2 = float(primeiro_aluguel) * (float(comissao_2)/100)
        valor_comissao3 = float(primeiro_aluguel) * (float(comissao_3)/100)
        valor_comissao4 = float(primeiro_aluguel) * (float(comissao_4)/100)
            
        
    # Informações específicas para Venda
    elif tipo == "Venda":
        ctk.CTkLabel(frame, text=f"Valor da Venda: R${valor}", font=("Poppins", 14)).grid(row=6, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(frame, text=f"Porcentagem Entrada: {entrada}%", font=("Poppins", 14)).grid(row=7, column=0, padx=10, pady=10, sticky="w")
        
        if resultado == None:
            botao_criar_meses_pg = ctk.CTkButton(frame, text="Iniciar", font=("Poppins", 14),
                                                command=lambda:meses_pagamento(data_inic.get(),id_cliente,valor,entrada,
                                                                               comissao_1,comissao_2,comissao_3,comissao_4,tipo))
            
            botao_criar_meses_pg.grid(row=12,column=0,padx=10,pady=10,sticky="w")

        valor_trab = float(valor) * (float(entrada)/100)

        valor_comissao1 = float(valor_trab) * (float(comissao_1)/100)
        valor_comissao2 = float(valor_trab) * (float(comissao_2)/100)
        valor_comissao3 = float(valor_trab) * (float(comissao_3)/100)
        valor_comissao4 = float(valor_trab) * (float(comissao_4)/100)

    comissao_1_ = 0
    comissao_2_ = 0
    comissao_3_ = 0
    comissao_4_ = 0

    if comissao_1 == 22.5 or comissao_1 == 15 or comissao_1 == 7.5:
        comissao_1_ = float(comissao_1) * 2

    if comissao_2 == 22.5 or comissao_2 == 15 or comissao_2 == 7.5:
        comissao_2_ = float(comissao_2) * 2

    if comissao_3 == 22.5 or comissao_3 == 15 or comissao_3 == 7.5:
        comissao_3_ = float(comissao_3) * 2

    if comissao_4 == 22.5 or comissao_4 == 15 or comissao_4 == 7.5:
        comissao_4_ = float(comissao_4) * 2

   

    ctk.CTkLabel(frame, text=f"Corretor 1: {corretor_1} / {comissao_1_}% / R$ {valor_comissao1} ", font=("Poppins", 14)).grid(row=3, column=1, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Corretor 2: {corretor_2} / {comissao_2_}% / R$ {valor_comissao2}", font=("Poppins", 14)).grid(row=4, column=1, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Corretor 3: {corretor_3} / {comissao_3_}% / R$ {valor_comissao3}", font=("Poppins", 14)).grid(row=5, column=1, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Corretor 4: {corretor_4} / {comissao_4_}% / R$ {valor_comissao4}", font=("Poppins", 14)).grid(row=6, column=1, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Royalties: {royalties}", font=("Poppins", 14)).grid(row=7, column=1, pady=10, sticky="w")




def exibir_informacoes_clientes():

    destruir_widgets(criar_frame)

    main_frame = ctk.CTkFrame(criar_frame,fg_color="transparent")
    main_frame.pack(fill="both", expand=True)

    left_frame = ctk.CTkScrollableFrame(main_frame,fg_color="transparent")
    left_frame.pack(side="left", fill="both",expand=True,ipadx=10,padx=5)

    id_frame = ctk.CTkScrollableFrame(main_frame,fg_color="transparent")
    id_frame.pack(expand=True,side="left", fill="both",ipadx=40,padx=30)

    info_frame = ctk.CTkScrollableFrame(main_frame,fg_color="transparent",orientation="horizontal")
    info_frame.pack(side="left", expand=True, fill="both",ipadx=500)
    
    ctk.CTkLabel(left_frame,text="Clientes Geral",font=("Poppins Bold", 16)).grid(row=0,column=0,sticky="w",padx=40,pady=15)

    botao_mostrar_todos_clientes = ctk.CTkButton(left_frame,text="Todos Clientes",font=("Poppins", 15), 
                                                 command=lambda:mostrar_clientes("Clientes",id_frame,info_frame,None,None))
    botao_mostrar_todos_clientes.grid(row=1,column=0,sticky="w",padx=40)


    ctk.CTkLabel(left_frame,text="Filtrar ID",font=("Poppins Bold", 15)).grid(row=2,column=0,sticky="w",padx=40,pady=5)
    filtro_id = ctk.CTkEntry(left_frame)
    filtro_id.grid(row=3,column=0,sticky="w",padx=40,pady=5)

    botao_mostrar_clientes_id = ctk.CTkButton(left_frame,text="Filtrar",font=("Poppins", 15), 
                                              command=lambda:mostrar_clientes("Clientes",id_frame,info_frame,"id",filtro_id.get()))
    botao_mostrar_clientes_id.grid(row=4,column=0,sticky="w",padx=40)

    #Label Auxiliar
    ctk.CTkLabel(left_frame,text="").grid(row=5,column=0,padx=40,pady=10)
    
    ctk.CTkLabel(left_frame,text="Status Clientes",font=("Poppins Bold", 16)).grid(row=6,column=0,sticky="w",padx=40)

    botao_mostrar_situa = ctk.CTkButton(left_frame,text="Todos os Status",font=("Poppins", 15),command=lambda:verificar_situacao(None, None, None))
    botao_mostrar_situa.grid(row=7,column=0,sticky="w",padx=40,pady=10)

    botao_mostrar_pagos = ctk.CTkButton(left_frame,text="Pagos",font=("Poppins", 15),command=lambda:verificar_situacao(None, "Status", "Pago!"))
    botao_mostrar_pagos.grid(row=8,column=0,sticky="w",padx=40,pady=10)

    botao_mostrar_npagos = ctk.CTkButton(left_frame,text="Não Pagos",font=("Poppins", 15),command=lambda:verificar_situacao(None, "Status", "Aguardando Pg."))
    botao_mostrar_npagos.grid(row=9,column=0,sticky="w",padx=40,pady=10)

    ctk.CTkLabel(left_frame,text="",font=("Poppins Bold", 15)).grid(row=10,column=0,sticky="w",padx=40,pady=10)

    ctk.CTkLabel(left_frame,text=" Filtrar Mês (Status)",font=("Poppins Bold", 15)).grid(row=11,column=0,sticky="w",padx=40,pady=5)

    filtro_mes = ctk.CTkEntry(left_frame,placeholder_text="01,02,03...", placeholder_text_color="gray")
    filtro_mes.grid(row=12,column=0,sticky="w",padx=40,pady=5)
    botao_filtrar_mes = ctk.CTkButton(left_frame,text="Filtrar", font=("Poppins", 15),command=lambda:verificar_situacao(None,"Data",filtro_mes.get()))
    botao_filtrar_mes.grid(row=13,column=0,sticky="w",padx=40)

    ctk.CTkLabel(left_frame,text="",font=("Poppins Bold", 15)).grid(row=14,column=0,sticky="w",padx=40,pady=0)

    ctk.CTkLabel(left_frame,text=" Filtrar dia (Status)",font=("Poppins Bold", 15)).grid(row=15,column=0,sticky="w",padx=40,pady=5)
    filtro_dia = ctk.CTkEntry(left_frame)
    filtro_dia.grid(row=16,column=0,sticky="w",padx=40,pady=5)

    filtro_dia.bind("<KeyRelease>", lambda event: formatar_data_entry(filtro_dia,event))

    botao_filtrar_dia = ctk.CTkButton(left_frame,text="Filtrar", font=("Poppins", 15),command=lambda:verificar_situacao(None,"Dia",filtro_dia.get()))
    botao_filtrar_dia.grid(row=17,column=0,sticky="w",padx=40)

    mostrar_clientes("Clientes",id_frame,info_frame,None,None)


def gerar_entradas_saidas():

    def atualizar_tipo(escolha):

        global tipo_salvar

        tipo.configure(text=f"Tipo Selecionado: {escolha}")
        tipo_salvar = escolha
    
    def salvar():

        conn = sqlite3.connect("Banco_de_Dados.db")
        cursor = conn.cursor()

        try:

            cursor.execute("""
            INSERT INTO movimentacao (tipo, tipo1, descricao, valor, data) 
            VALUES (?, ?,  ?, ?, ?)
            """, (tipo_salvar, "Saida/Entrada Rápida", descricao.get(), valor.get(), data_completa.get()))

            arquivo = "saldo.json"
            with open(arquivo, 'r') as f:
                dados = json.load(f)
                saldo = dados.get('saldo', 0)

            if tipo_salvar == "Entrada":
            
                entrada = float(valor.get())
                novo_saldo = saldo + entrada

            elif tipo_salvar == "Saida":
            
                saida = float(valor.get())
                novo_saldo = saldo - saida

            with open(arquivo, 'w') as f:
                json.dump({'saldo': novo_saldo}, f)
        
            
            conn.commit()

            messagebox.showinfo("Sucesso!", "Dados Enviados ao banco de dados com sucesso!")

            atualizar_saldo(arquivo='saldo.json')
            solicitar_saldo(arquivo='saldo.json')
        
        except NameError:
            messagebox.showinfo("Erro!", "Selecione o tipo da movimentação!")
        
        
        finally:
            conn.close()
        
      

    destruir_widgets(criar_frame)
    
    frame_principal = ctk.CTkFrame(criar_frame,fg_color="transparent")
    frame_principal.pack(fill="both",expand=True)

    label_tipo = ctk.CTkLabel(frame_principal, text='Tipo Movimentação', font=('Poppins Bold', 16))
    label_tipo.place(x=50,y=30)

    opcoes = ["Entrada", "Saida"]
    tipo_selecionado = ctk.StringVar(value="Selecionar")

    option_menu = ctk.CTkOptionMenu(frame_principal, 
    font=("Poppins", 15),
    width=150,
    values=opcoes, 
    variable=tipo_selecionado,
    dropdown_font=("Poppins", 15),  
    button_color="lightblue",  
    dropdown_fg_color="#3c8cd4",
    dropdown_text_color="white", 
    command=atualizar_tipo)
    option_menu.place(x=50,y=70)

    tipo = ctk.CTkLabel(frame_principal, text="Tipo: Escolher",font=('Poppins', 16))
    tipo.place(x=240,y=70)

    label_descricao = ctk.CTkLabel(frame_principal, text='Descrição', font=('Poppins', 16))
    label_descricao.place(x=50,y=130)
    descricao = ctk.CTkEntry(frame_principal,font=("Poppins", 15),width=300)
    descricao.place(x=50,y=170)

    label_valor = ctk.CTkLabel(frame_principal, text='Valor',  font=('Poppins', 16))
    label_valor.place(x=50,y=230)
    valor = ctk.CTkEntry(frame_principal,font=("Poppins", 15),width=300)
    valor.place(x=50,y=270)

    label_data = ctk.CTkLabel(frame_principal, text='Data',  font=('Poppins', 16))
    label_data.place(x=50,y=330)
    data_completa = ctk.CTkEntry(frame_principal,font=("Poppins",15),width=300)
    data_completa.place(x=50,y=370)

    data_completa.bind("<KeyRelease>", lambda event: formatar_data_entry(data_completa,event))
    descricao.bind("<Return>", lambda event: ir_para_proximo_entry(event, valor))
    valor.bind("<Return>", lambda event: ir_para_proximo_entry(event, data_completa))

    ctk.CTkLabel(frame_principal, text="OBS: Usar para registrar saidas/entradas rapidas, ou simples.",font=("Poppins Bold",16)).place(x=50,y=430)

    botao_salvar = ctk.CTkButton(frame_principal, text='Salvar',font=("Poppins",17),width=170,height=40,corner_radius=15, command=salvar)
    botao_salvar.place(x=400, y=600)


def mostrar_entradas_saidas():

    destruir_widgets(criar_frame)
    
    frame_principal = ctk.CTkScrollableFrame(criar_frame,fg_color="transparent")
    frame_principal.pack(fill="both",expand=True,side="right",ipadx=350)

    left_frame = ctk.CTkFrame(criar_frame,fg_color="transparent",border_width=5,border_color="#C0C0C0")
    left_frame.pack(fill="both",expand=True, side="left")

    frame_filtro = ctk.CTkFrame(left_frame, fg_color="gray",width=140,height=200)
    frame_filtro.place(x=14, y=300)


    def mostrar_todos(filtro,valor_filtro):

        destruir_widgets(frame_principal)

        conn = sqlite3.connect("Banco_de_Dados.db")
        cursor = conn.cursor()

        if filtro == None and valor_filtro == None:
            cursor.execute("SELECT * FROM movimentacao")
            resultados = cursor.fetchall()

        elif (valor_filtro == "Entrada" and filtro == "tipo1") or (valor_filtro == "Saída" and filtro == "tipo1"):
            cursor.execute(f"SELECT * FROM movimentacao WHERE {filtro} = ?", (valor_filtro,))
            resultados = cursor.fetchall()

        elif valor_filtro == "Comissão" and filtro == "tipo1":
            cursor.execute(f"SELECT * FROM movimentacao WHERE substr(tipo1, 1, 8) = ?", (valor_filtro,))
            resultados = cursor.fetchall()
        
        elif valor_filtro == "Aluguel" and filtro == "tipo1":
            cursor.execute(f"SELECT * FROM movimentacao WHERE tipo1 IN ('Entrada Aluguel', 'Entrada do 1° Aluguel')")
            resultados = cursor.fetchall()

        elif valor_filtro == "Venda" and filtro == "tipo1":
            cursor.execute(f"SELECT * FROM movimentacao WHERE substr(tipo1, 17, 21)= ?", (valor_filtro,))
            resultados = cursor.fetchall()
        
        elif valor_filtro == "Rápida" and filtro == "tipo1":
            cursor.execute(f"SELECT * FROM movimentacao WHERE substr(tipo1, 15, 20)= ?", (valor_filtro,))
            resultados = cursor.fetchall()
        
        elif filtro == "Mês":
            cursor.execute(f"SELECT * FROM movimentacao WHERE substr(data, 4, 5) = ?", (valor_filtro,))
            resultados = cursor.fetchall()
 

        else:
            cursor.execute(f"SELECT * FROM movimentacao WHERE {filtro} = ?", (valor_filtro,))
            resultados = cursor.fetchall()

        conn.close()


        headers = ["Marcar","Entrada/Saída","Tipo", "Descrição", "Valor", "Data"]

        checkbox_vars = []
        ids = []

        for i, header in enumerate(headers):
            label = ctk.CTkLabel(frame_principal, text=header, width=5, corner_radius=5, fg_color="gray70", font=("Poppins Bold", 14))
            label.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")

        for row_index, row_data in enumerate(resultados, start=1):
            chk_var = ctk.IntVar()
            checkbox = ctk.CTkCheckBox(frame_principal, variable=chk_var, text="",width=10)
            checkbox.grid(row=row_index, column=0, pady=5)
            
            checkbox_vars.append(chk_var)
            
            ids.append(row_data[0])
            
            for col_index, data in enumerate(row_data[1:]):  
                label = ctk.CTkLabel(frame_principal, text=data, corner_radius=5, font=("Poppins", 13))
                label.grid(row=row_index, column=col_index + 1, padx=5, pady=5, sticky="nsew")

        def deletar_selecionados():

            ids_selecionados = [id_var for id_var, chk_var in zip(ids, checkbox_vars) if chk_var.get() == 1]
            
            if ids_selecionados:

                conn = sqlite3.connect("Banco_de_Dados.db")
                cursor = conn.cursor()
                
                for id_selecionado in ids_selecionados:
                    cursor.execute("DELETE FROM movimentacao WHERE id=?", (id_selecionado,))
                
                conn.commit()
                conn.close()

                messagebox.showinfo("Sucesso!", "Selecionados Removidos com Sucesso!")
        
        botao_deletar = ctk.CTkButton(left_frame, text="Deletar",font=('Poppins',15),corner_radius=10,
                                        fg_color="#b95557", hover_color="#bd3038", command=deletar_selecionados)
        botao_deletar.place(x=20, y=500)




    def filtrar(selected_value):

        destruir_widgets(frame_filtro)

        
        if selected_value == "Dia":

            ctk.CTkLabel(frame_filtro,text="Dia",font=('Poppins Bold',15),text_color= "#484E55").place(x=0,y=0)
            data = ctk.CTkEntry(frame_filtro)
            data.place(x=0,y=30)

            data.bind("<KeyRelease>", lambda event: formatar_data_entry(data,event))

            botao_filtro = ctk.CTkButton(frame_filtro,text="Filtrar", font=("Poppins",15),width=130,corner_radius=15,command=lambda:mostrar_todos("data", data.get()))
            botao_filtro.place(x=0,y=80)

        if selected_value == "Mês":
        
            ctk.CTkLabel(frame_filtro,text="Mês",font=('Poppins Bold',15),text_color= "#484E55").place(x=0,y=0)
            meses = {
                "Janeiro": "01", "Fevereiro": "02", "Março": "03", "Abril": "04",
                "Maio": "05", "Junho": "06", "Julho": "07", "Agosto": "08",
                "Setembro": "09", "Outubro": "10", "Novembro": "11", "Dezembro": "12"
            }
            
            mes_selecionado = ctk.StringVar(value="Janeiro") 

            option_menu = ctk.CTkOptionMenu(
                frame_filtro,
                variable=mes_selecionado,
                values=list(meses.keys()),  # Exibe os nomes dos meses
                font=("Poppins", 15),
                corner_radius=15
            )
            option_menu.pack(pady=(0, 10))



            ctk.CTkLabel(frame_filtro,text="Ano",font=('Poppins Bold',15),text_color= "#484E55").place(x=0,y=0)
            ano = ctk.CTkEntry(frame_filtro, font=('Poppins Bold',15), placeholder_text="24,25,..")
            ano.place(x=0,y=30)



           





        if selected_value == "Tipo":

            ctk.CTkLabel(frame_filtro, text="Escolha o Tipo",font=('Poppins Bold', 15), text_color= "#484E55").place(x=0, y=0)

            opcoes = ["Comissão", "Aluguel", "Venda", "Royalties ", "Contas", "Rápida"]
    
            data = ctk.CTkEntry(frame_filtro, placeholder_text="Digite o tipo da conta...")
            data.place_forget()  

            def option_selected(choice):
                if choice == "Outros":
                    data.place(x=0, y=60)  
                else:
                    data.delete(0, ctk.END)
                    data.insert(0,choice)
                    filtro_lab.configure(text=f"Tipo: {choice}")
                    filtro_lab.place(x=0,y=120)

                

            filtro_lab = ctk.CTkLabel(frame_filtro,font=("Poppins", 15))
            filtro_lab.place_forget()

            conta_option_menu = ctk.CTkOptionMenu(frame_filtro, values=opcoes, 
            command=option_selected,
            font=("Poppins", 13),
            dropdown_font=("Poppins", 13),  
            button_color="lightblue",  
            dropdown_fg_color="#3c8cd4",
            dropdown_text_color="white")

            conta_option_menu.place(x=0, y=30)

            botao_filtro = ctk.CTkButton(frame_filtro,text="Filtrar", font=("Poppins",15),width=130,corner_radius=15, command=lambda:mostrar_todos("tipo1", data.get()))
            botao_filtro.place(x=0,y=80)

        
        if selected_value == "Valor":

            ctk.CTkLabel(frame_filtro,text="Valor",font=('Poppins Bold',15),text_color= "#484E55").place(x=0,y=0)
            data = ctk.CTkEntry(frame_filtro)
            data.place(x=0,y=30)

            botao_filtro = ctk.CTkButton(frame_filtro,text="Filtrar", font=("Poppins",15), width=130,corner_radius=15, command=lambda:mostrar_todos("Valor", data.get()))
            botao_filtro.place(x=0,y=80)

    

    ctk.CTkLabel(left_frame, text="Registros",font=('Poppins Bold',16),anchor="w", image= edit_image, height=20,
                compound="left").place(x=14, y=10)


    botao_todos = ctk.CTkButton(left_frame, text="Todas",font=('Poppins',15), width=165, command=lambda:mostrar_todos(None,None))
    botao_todos.place(x=10, y=50)

    botao_entradas = ctk.CTkButton(left_frame, text="Entradas",font=('Poppins',15),width=165,command=lambda:mostrar_todos("tipo","Entrada"))
    botao_entradas.place(x=10, y=90)

    botao_saidas = ctk.CTkButton(left_frame, text="Saídas",font=('Poppins',15),width=165,command=lambda:mostrar_todos("tipo","Saída"))
    botao_saidas.place(x=10, y=130)

    

    ctk.CTkLabel(left_frame, text="Filtrar", font=('Poppins Bold',16)).place(x=20, y=215)


    def on_option_change_filtros(choice):
        filtrar(choice)
    
    filtros_options = ["Dia", "Mês", "Tipo", "Valor"] 
    filtros_menu = ctk.CTkOptionMenu(    
    master=left_frame, 
    values=filtros_options, 
    font=('Poppins', 15),
    command=on_option_change_filtros,
    dropdown_font=("Poppins", 12),  
    button_color="lightblue",  
    dropdown_fg_color="#3c8cd4",
    dropdown_text_color="white"
    )
    filtros_menu.place(x=14, y=250)
    

    mostrar_todos(None,None)


def formatar_contato(entry_widget, event):
    texto = entry_widget.get()

    # Remove qualquer caractere que não seja numérico
    texto = ''.join([char for char in texto if char.isdigit()])

    # Aplica a formatação
    if len(texto) > 2 and len(texto) <= 7:
        texto = f"({texto[:2]}) {texto[2:]}"
    elif len(texto) > 7:
        texto = f"({texto[:2]}) {texto[2:7]}-{texto[7:]}"

    # Limite de 11 dígitos
    texto = texto[:15]

    # Atualiza o texto no entry
    entry_widget.delete(0, 'end')
    entry_widget.insert(0, texto)



def formatar_cpf(entry_widget, event):
    texto = entry_widget.get()

    # Remove qualquer caractere que não seja numérico
    texto = ''.join([char for char in texto if char.isdigit()])

    if len(texto) > 3 and len(texto) <= 6:
        texto = f"{texto[:3]}.{texto[3:]}"
    elif len(texto) > 6 and len(texto) <= 9:
        texto = f"{texto[:3]}.{texto[3:6]}.{texto[6:]}"
    elif len(texto) > 9:
        texto = f"{texto[:3]}.{texto[3:6]}.{texto[6:9]}-{texto[9:]}"

    # Limite de 11 dígitos
    texto = texto[:14]

    # Atualiza o texto no entry
    entry_widget.delete(0, 'end')
    entry_widget.insert(0, texto)


def mostrar_imagem(caminho,label,x,y):
   
    img = Image.open(caminho)
    img = img.resize((x, y)) 
    img_tk = ImageTk.PhotoImage(img)  

    # Atualiza o label com a nova imagem
    label.configure(image=img_tk)
    label.image = img_tk  




def cadastrar_corretor():

    def salvar_corretor():

        conn = sqlite3.connect('Banco_de_Dados.db')
        cursor = conn.cursor()
        
        # Criar a tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS corretores (
                cpf TEXT PRIMARY KEY,
                nome TEXT,
                data_nascimento TEXT,
                telefone TEXT,
                observacao TEXT,
                estagiario TEXT,
                foto TEXT,
                comissao_total FLOAT,
                qtd_vendas INT,
                qtd_aluguel INT
            )
        ''')


        nome = nome_corretor.get()
        cpf_value = cpf.get()
        data_nasc = data_nascimento.get()
        contato = telefone.get()
        observacao = obs.get()
        estagiario_value = estagiario.get()
        comissao_tot = 0
        qtd_ven = 0
        qtd_alu = 0
        
        try:
            cursor.execute('''
                INSERT INTO corretores (cpf, nome, data_nascimento, telefone, observacao, estagiario, foto, comissao_total, qtd_vendas, qtd_aluguel)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (cpf_value, nome, data_nasc, contato, observacao, estagiario_value, foto_corretor,comissao_tot,qtd_ven,qtd_alu))
            
            conn.commit()  # Salva as alterações
            messagebox.showinfo("Sucesso!","Dados salvos com sucesso!")

            conn.commit()

        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "CPF já cadastrado.")

        
        finally: 
            conn.close()


    destruir_widgets(criar_frame)

    label_nome_corretor = ctk.CTkLabel(criar_frame, text='Nome do Corretor', font=('Poppins Bold', 16))
    label_nome_corretor.place(x=50, y=30)
    nome_corretor = ctk.CTkEntry(criar_frame, width=300, font=('Poppins', 15))
    nome_corretor.place(x=50, y=70)  


    label_cpf = ctk.CTkLabel(criar_frame, text='CPF', font=('Poppins Bold', 16))
    label_cpf.place(x=50, y=130)  
    cpf = ctk.CTkEntry(criar_frame, width=300, font=('Poppins', 15))
    cpf.place(x=50, y=170) 
    cpf.bind("<KeyRelease>", lambda event: [formatar_cpf(cpf, event)])

    label_data_nascimento = ctk.CTkLabel(criar_frame, text='Data Nascimento', font=('Poppins', 16))
    label_data_nascimento.place(x=50, y=230)  
    data_nascimento = ctk.CTkEntry(criar_frame, width=300, font=('Poppins', 15))
    data_nascimento.place(x=50, y=270)  
    data_nascimento.bind("<KeyRelease>", lambda event: [formatar_data_entry(data_nascimento, event)])

    label_telefone = ctk.CTkLabel(criar_frame, text='Contato', font=('Poppins', 16))
    label_telefone.place(x=50, y=330)  
    telefone = ctk.CTkEntry(criar_frame, width=300, font=('Poppins', 15))
    telefone.place(x=50, y=370) 
    telefone.bind("<KeyRelease>", lambda event: [formatar_contato(telefone, event)])

    label_obs = ctk.CTkLabel(criar_frame, text='Observação (Opcional)', font=('Poppins', 16))
    label_obs.place(x=50, y=430)  
    obs = ctk.CTkEntry(criar_frame, width=300, font=('Poppins', 15))
    obs.place(x=50, y=470) 

    nome_corretor.bind("<Return>", lambda event: ir_para_proximo_entry(event, cpf))
    cpf.bind("<Return>", lambda event: ir_para_proximo_entry(event, data_nascimento))
    data_nascimento.bind("<Return>", lambda event: ir_para_proximo_entry(event, telefone))
    telefone.bind("<Return>", lambda event: ir_para_proximo_entry(event, obs))
    
 

    def atualizar_estagiario():

        global resultado

        escolha = estagiario.get()

        if escolha == "Sim":
            resultado = "Estagiario"
        else:
            resultado = "Nao Estagiario"


    estagiario = ctk.StringVar(value="Nao")  
    
    label_estagiario = ctk.CTkLabel(criar_frame, text="- Estagiario?", font=('Poppins Bold', 16))
    label_estagiario.place(x=50, y=530)

    radio_sim = ctk.CTkRadioButton(criar_frame, text="Sim", variable=estagiario, value="Sim", font=('Poppins', 15),
                               command=atualizar_estagiario)
    radio_sim.place(x=50, y=570)

    radio_nao = ctk.CTkRadioButton(criar_frame, text="Não", variable=estagiario, value="Não", font=('Poppins', 15),
                                command=atualizar_estagiario)
    radio_nao.place(x=50, y=610)



    def adicionar_foto():

        global foto_corretor  
       
        foto_corretor = filedialog.askopenfilename(title="Selecionar Foto", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])

        if foto_corretor:
            mostrar_imagem(foto_corretor,label_imagem,300,400)  


    botao_adicionar_foto = ctk.CTkButton(criar_frame, text="Selecionar Foto", font=('Poppins ', 17),width=170,height=40,corner_radius=15,command=adicionar_foto)
    botao_adicionar_foto.place(x=495, y=20)

    label_imagem = ctk.CTkLabel(criar_frame, text="")  
    label_imagem.place(x=495, y=90)  

    botao_salvar = ctk.CTkButton(criar_frame, text="Salvar", font=('Poppins', 17),width=170,height=40,corner_radius=15,command=salvar_corretor)
    botao_salvar.place(x=400, y=600)



def mostrar_corretores():
        
    destruir_widgets(criar_frame)
    
    frame_main = ctk.CTkFrame(criar_frame,fg_color="transparent")
    frame_main.pack(fill="both", expand=True)

    frame_left = ctk.CTkScrollableFrame(frame_main,fg_color="transparent")
    frame_left.pack(side="left", fill="both",expand=True,ipadx=10)

    info_frame = ctk.CTkFrame(frame_main,fg_color="transparent",border_width=5,border_color="#C0C0C0")
    info_frame.pack(side="left", expand=True, fill="both",ipadx=250)
    
    
    conn = sqlite3.connect('Banco_de_Dados.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM corretores")

    corretores = cursor.fetchall()
    conn.close() 

    ctk.CTkLabel(frame_left,text=" Corretores:",font=('Poppins Bold', 20)).grid(row=0,column=0,pady=25,sticky="w")

    i=0
    
    for corr in corretores:

        cpf_corr = corr[0]  
        nome_corr = corr[1]
        text_nome = f"{nome_corr}"

        button = ctk.CTkButton(frame_left,text=text_nome,image=add_image,compound="left",anchor="w",corner_radius=15,
                                font=('Poppins', 14),width=280, command=partial(info_corretor,cpf_corr,info_frame))
        
        button.grid(row=i+2,column=0,pady=10,sticky="w")

        ctk.CTkLabel(frame_left,text="").grid(row=i+3,column=0)

        i+=4


def gerar_relatorio_comissoes(cpf_corretor):

    janela1 = ctk.CTkToplevel(tela)
    janela1.geometry("1100x400+200+100")
    janela1.attributes('-topmost', True)

    main_frame = ctk.CTkScrollableFrame(janela1, fg_color="transparent")
    main_frame.pack(fill="both", expand=True, side="right", ipadx=300)

    frame_filtrar = ctk.CTkFrame(janela1, border_color="#C0C0C0")
    frame_filtrar.pack(fill="both", expand=True, side="left", padx=10, pady=10)

    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mes_selecionado = ctk.StringVar()
    mes_selecionado.set("Janeiro")

    label_mes = ctk.CTkLabel(frame_filtrar, text="Selecione o Mês:", font=("Poppins", 15))
    label_mes.pack(pady=(5, 2))

    option_mes = ctk.CTkOptionMenu(
        frame_filtrar,
        variable=mes_selecionado,
        font=('Poppins', 15),
        dropdown_font=("Poppins", 12),
        button_color="lightblue",
        dropdown_fg_color="#3c8cd4",
        dropdown_text_color="white",
        corner_radius=15,
        values=meses
    )
    option_mes.pack(pady=(0, 10))

    label_ano = ctk.CTkLabel(frame_filtrar, text="Digite o Ano:", font=("Poppins", 15))
    label_ano.pack(pady=(5, 2))
    entry_ano = ctk.CTkEntry(frame_filtrar)
    entry_ano.pack(pady=(0, 10))

    botao_filtrar = ctk.CTkButton(frame_filtrar, text="Filtrar", font=("Poppins", 15), corner_radius=15,
                                  command=lambda: filtrar_comissoes(cpf_corretor, mes_selecionado.get(), entry_ano.get(), main_frame))
    botao_filtrar.pack(pady=(10, 5))

    botao_mostrar_todos = ctk.CTkButton(frame_filtrar, text="Mostrar Todos", font=("Poppins", 15), corner_radius=15,
                                        command=lambda: mostrar_todas_comissoes(cpf_corretor, main_frame))
    botao_mostrar_todos.pack(pady=(5, 5))

    headers = ["ID", "CPF", "Tipo", "Valor Comissão", "Data", "ID Cliente", "Nome Cliente", "Descrição"]
    for i, header in enumerate(headers):
        label = ctk.CTkLabel(main_frame, text=header, corner_radius=5, fg_color="gray70", font=("Poppins Bold", 13))
        label.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")

def filtrar_comissoes(cpf_corretor, mes, ano, frame):
    meses_numeros = {
        "Janeiro": "01", "Fevereiro": "02", "Março": "03", "Abril": "04",
        "Maio": "05", "Junho": "06", "Julho": "07", "Agosto": "08",
        "Setembro": "09", "Outubro": "10", "Novembro": "11", "Dezembro": "12"
    }
    numero_mes = meses_numeros.get(mes)
    data_filtrada = f"{numero_mes}/{ano}"

    for widget in frame.winfo_children():
        widget.destroy()

    headers = ["ID", "CPF", "Tipo", "Valor Comissão", "Data", "ID Cliente", "Nome Cliente"]
    for i, header in enumerate(headers):
        label = ctk.CTkLabel(frame, text=header, corner_radius=5, fg_color="gray70", font=("Poppins Bold", 13))
        label.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")

    conex = sqlite3.connect('Banco_de_Dados.db')
    cursor = conex.cursor()
    cursor.execute('''
        SELECT id, cpf_corretor, tipo_operacao, valor_comissao, data_comissao, id_cliente, nome_cliente
        FROM comissoes 
        WHERE cpf_corretor = ? AND substr(data_comissao, 4, 5) = ?
    ''', (cpf_corretor, data_filtrada))

    comissoes = cursor.fetchall()
    conex.close()

    for row_index, row_data in enumerate(comissoes, start=1):
        for col_index, data in enumerate(row_data):
            label = ctk.CTkLabel(frame, text=data, corner_radius=5, font=("Poppins", 13))
            label.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")


def mostrar_todas_comissoes(cpf_corretor, frame):
    for widget in frame.winfo_children():
        widget.destroy()

    headers = ["ID", "CPF", "Tipo", "Valor Comissão", "Data", "ID Cliente", "Nome Cliente"]
    for i, header in enumerate(headers):
        label = ctk.CTkLabel(frame, text=header, corner_radius=5, fg_color="gray70", font=("Poppins Bold", 13))
        label.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")

    conex = sqlite3.connect('Banco_de_Dados.db')
    cursor = conex.cursor()
    cursor.execute('''
        SELECT id, cpf_corretor, tipo_operacao, valor_comissao, data_comissao, id_cliente, nome_cliente
        FROM comissoes 
        WHERE cpf_corretor = ?
    ''', (cpf_corretor,))

    comissoes = cursor.fetchall()
    conex.close()

    for row_index, row_data in enumerate(comissoes, start=1):
        for col_index, data in enumerate(row_data):
            label = ctk.CTkLabel(frame, text=data, corner_radius=5, font=("Poppins", 13))
            label.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")


def info_corretor(cpf,frame):

    destruir_widgets(frame)

    conn = sqlite3.connect('Banco_de_Dados.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM corretores WHERE cpf=?", (cpf,))

    info = cursor.fetchone()
    conn.close()   

    if info:

        id = info[0]
        nome = info[1]
        data_nas = info[2]
        telefone = info[3]
        observa = info[4]
        estagiar = info[5]
        foto = info[6]
        com_total = info[7]
        qtd_venda = info[8]
        qtd_alug = info[9]

    ctk.CTkLabel(frame, text="Informações do Corretor", image=add_image, 
        font=('Poppins', 17), fg_color="#3c8cd4", height=30,
        corner_radius=15, text_color="white", anchor="w", compound="left").place(x=50, y=30)

    ctk.CTkLabel(frame, text=f"Nome: {nome}", font=("Poppins Bold", 17)).place(x=50, y=100)
    ctk.CTkLabel(frame, text=f"CPF: {id}", font=("Poppins Bold", 17)).place(x=50, y=160)
    ctk.CTkLabel(frame, text=f"Data Nascimento: {data_nas}", font=("Poppins", 17)).place(x=50, y=220)
    ctk.CTkLabel(frame, text=f"Telefone: {telefone}", font=("Poppins", 17)).place(x=50, y=280)
    ctk.CTkLabel(frame, text=f"Observação: {observa}", font=("Poppins", 17)).place(x=50, y=340)
    ctk.CTkLabel(frame, text=f"Estágiario: {estagiar}", font=("Poppins", 17)).place(x=50, y=400)
    ctk.CTkLabel(frame, text=f"Comissao Total Recebida: {com_total}", font=("Poppins", 17)).place(x=50, y=460)
    ctk.CTkLabel(frame, text=f"Qtd. Participação em Vendas: {qtd_venda}", font=("Poppins", 17)).place(x=50, y=520)
    ctk.CTkLabel(frame, text=f"Qtd. Participação em Alugueis: {qtd_alug}", font=("Poppins", 17)).place(x=50, y=580)

    ctk.CTkLabel(frame, text="Foto Corretor", font=("Poppins Bold", 17)).place(x=450, y=100)
    iamgem_label=ctk.CTkLabel(frame, text="")
    iamgem_label.place(x=450, y=150)

    mostrar_imagem(foto, iamgem_label, x=250,y=300)


    botao_rela = ctk.CTkButton(frame,text="Mostrar Relatório",corner_radius=15,font=('Poppins', 15),width=150,height=30,image=file_image,
                                anchor="w", compound="left", command=lambda:gerar_relatorio_comissoes(id))
    botao_rela.place(x=50,y=615)

    def deletar_corretor():

        confirmacao = messagebox.askyesno("Confirmação", "Tem certeza de que deseja deletar o corretor?")
        
        if confirmacao:

            conn = sqlite3.connect("Banco_de_Dados.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM corretores WHERE cpf = ?", (id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso!", "Corretor removido com sucesso!")
            mostrar_corretores()

    def resetar():

        confirmacao = messagebox.askyesno("Confirmação", "Tem certeza de que deseja resetar os dados do corretor?")
        
        if confirmacao:
            nova_comissao = 0
            nova_qtdv = 0
            nova_qtda = 0
            id_corretor = id

            conn = sqlite3.connect("Banco_de_Dados.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE corretores SET comissao_total = ?, qtd_vendas = ?, qtd_aluguel = ? WHERE cpf = ?", 
                        (nova_comissao, nova_qtdv, nova_qtda, id_corretor))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso!", "Dados resetados com sucesso!")
            mostrar_corretores()

       

    botao_deletar =  ctk.CTkButton(frame,text="Deletar Corretor", font=("Poppins", 15),corner_radius=15,
                                        width=150,height=30, fg_color="#b95557", hover_color="#bd3038",command= deletar_corretor)
    botao_deletar.place(x=500,y=615)

    botao_mudar = ctk.CTkButton(frame,text="Alterar Dados", font=("Poppins", 15),corner_radius=15,
                                                width=150,height=30,command=lambda:alterar_dados_corretor_ui(id))
    botao_mudar.place(x=300,y=615)

    botao_reset = ctk.CTkButton(frame,text="Resetar Dados", font=("Poppins", 15),corner_radius=15,
                                    width=160,height=30, command=resetar)
    botao_reset.place(x=500,y=500)




def alterar_dados_corretor_ui(cpf_corretor):

    def salvar_alteracoes():
        nome = entry_nome.get() if var_nome.get() else None
        telefone = entry_telefone.get() if var_telefone.get() else None
        data_nascimento = entry_data_nasc.get() if var_data_nasc.get() else None
        observacao = entry_observacao.get() if var_observacao.get() else None
        estagiario = entry_estagiario.get() if var_estagiario.get() else None

        alterar_dados_corretor(cpf_corretor, nome, data_nascimento, telefone, observacao, estagiario)
        janela.destroy()
    

    def mostrar_campos_selecionados():
        if var_nome.get():
            entry_nome.grid(row=1, column=1, padx=20, pady=5)
        else:
            entry_nome.grid_forget()
        if var_telefone.get():
            entry_telefone.grid(row=2, column=1, padx=20, pady=5)
        else:
            entry_telefone.grid_forget()
        if var_data_nasc.get():
            entry_data_nasc.grid(row=3, column=1, padx=20, pady=5)
        else:
            entry_data_nasc.grid_forget()
        if var_observacao.get():
            entry_observacao.grid(row=4, column=1, padx=20, pady=5)
        else:
            entry_observacao.grid_forget()
        if var_estagiario.get():
            entry_estagiario.grid(row=5, column=1, padx=20, pady=5)
        else:
            entry_estagiario.grid_forget()

    janela = ctk.CTk()
    janela.title("Alterar Dados do Corretor")
    janela.geometry("+700+300")

    label_instrucoes = ctk.CTkLabel(janela, text="Selecione os campos que deseja alterar:", font=("Poppins Bold", 15))
    label_instrucoes.grid(row=0, column=0, padx=20, pady=15, columnspan=2)

    var_nome = ctk.IntVar()
    var_telefone = ctk.IntVar()
    var_data_nasc = ctk.IntVar()
    var_observacao = ctk.IntVar()
    var_estagiario = ctk.IntVar()

    checkbox_nome = ctk.CTkCheckBox(janela, text="Nome", font=("Poppins", 15), variable=var_nome, command=mostrar_campos_selecionados)
    checkbox_nome.grid(row=1, column=0, padx=20, pady=5, sticky="w")

    checkbox_telefone = ctk.CTkCheckBox(janela, text="Telefone", font=("Poppins", 15), variable=var_telefone, command=mostrar_campos_selecionados)
    checkbox_telefone.grid(row=2, column=0, padx=20, pady=5, sticky="w")

    checkbox_data_nasc = ctk.CTkCheckBox(janela, text="Data de Nascimento",font=("Poppins", 15), variable=var_data_nasc, command=mostrar_campos_selecionados)
    checkbox_data_nasc.grid(row=3, column=0, padx=20, pady=5, sticky="w")

    checkbox_observacao = ctk.CTkCheckBox(janela, text="Observação",font=("Poppins", 15), variable=var_observacao, command=mostrar_campos_selecionados)
    checkbox_observacao.grid(row=4, column=0, padx=20, pady=5, sticky="w")

    checkbox_estagiario = ctk.CTkCheckBox(janela, text="Estagiário",font=("Poppins", 15), variable=var_estagiario, command=mostrar_campos_selecionados)
    checkbox_estagiario.grid(row=5, column=0, padx=20, pady=5, sticky="w")

    entry_nome = ctk.CTkEntry(janela, placeholder_text="Novo Nome",font=("Poppins", 15),width=250)
    
    entry_telefone = ctk.CTkEntry(janela, placeholder_text="Novo Telefone",font=("Poppins", 15),width=250)
    entry_telefone.bind("<KeyRelease>", lambda event: [formatar_contato(entry_telefone, event)])

    entry_data_nasc = ctk.CTkEntry(janela, placeholder_text="Nova Data de Nascimento",font=("Poppins", 15),width=250)
    entry_data_nasc.bind("<KeyRelease>", lambda event: [formatar_data_entry(entry_data_nasc, event)])

    entry_observacao = ctk.CTkEntry(janela, placeholder_text="Nova Observação",font=("Poppins", 15),width=250)
    entry_estagiario = ctk.CTkEntry(janela, placeholder_text="Estagiário (Sim/Não)",font=("Poppins", 15),width=250)

    botao_salvar = ctk.CTkButton(janela, text="Salvar Alterações",font=("Poppins", 15), command=salvar_alteracoes)
    botao_salvar.grid(row=6, column=0, columnspan=2, padx=5, pady=20)

    janela.mainloop()



def alterar_dados_corretor(cpf_corretor, nome=None, data_nascimento=None, telefone=None, observacao=None, estagiario=None):
    conex = sqlite3.connect('Banco_de_Dados.db')
    cursor = conex.cursor()

    cursor.execute("SELECT * FROM corretores WHERE cpf = ?", (cpf_corretor,))
    corretor = cursor.fetchone()

    if not corretor:
        messagebox.showerror("Erro", "Corretor não encontrado!")
        conex.close()
        return

    dados_para_atualizar = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'telefone': telefone,
        'observacao': observacao,
        'estagiario': estagiario
    }

    atualizacoes = []
    valores = []
    for campo, valor in dados_para_atualizar.items():
        if valor is not None:
            atualizacoes.append(f"{campo} = ?")
            valores.append(valor)

    if not atualizacoes:
        messagebox.showinfo("Nenhuma alteração", "Nenhum dado para atualizar.")
        conex.close()
        return

    sql_update = f"UPDATE corretores SET {', '.join(atualizacoes)} WHERE cpf = ?"
    valores.append(cpf_corretor)

    cursor.execute(sql_update, valores)
    conex.commit()
    messagebox.showinfo("Sucesso", "Dados do corretor atualizados com sucesso.")
    conex.close()

    mostrar_corretores()




def ranking():

    destruir_widgets(criar_frame)

    frame_classificar = ctk.CTkScrollableFrame(criar_frame,fg_color="transparent")
    frame_classificar.pack(side="left",fill="y",pady=20,padx=10,ipadx=140)

    frame_podio = ctk.CTkFrame(criar_frame,fg_color="transparent")
    frame_podio.pack(side="right",fill="both",padx=10,pady=20,expand=True)

    conex = sqlite3.connect('Banco_de_Dados.db')
    cursor = conex.cursor()
    cursor.execute('''
            SELECT nome, qtd_vendas + qtd_aluguel AS participacoes_totais, comissao_total, foto
            FROM corretores
            ORDER BY participacoes_totais DESC
        ''')
    ranking = cursor.fetchall() 
    conex.close()

    headers = ["Nome", "Participações", "Total Recebido"]

    for i, header in enumerate(headers):
        label_header = ctk.CTkLabel(frame_classificar, text=header, font=("Poppins Bold", 13), fg_color="gray70", corner_radius=5)
        label_header.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")

    for index, (nome, participacoes, comissao_total, _) in enumerate(ranking):
        label_nome = ctk.CTkLabel(frame_classificar, text=f"{index + 1}º {nome}", font=("Poppins", 13))
        label_nome.grid(row=index + 1, column=0, padx=5, pady=2)

        label_participacoes = ctk.CTkLabel(frame_classificar, text=f"{participacoes}", font=("Poppins", 13))
        label_participacoes.grid(row=index + 1, column=1, padx=5, pady=2)

        label_comissao = ctk.CTkLabel(frame_classificar, text=f"R$ {comissao_total:.2f}", font=("Poppins", 13))
        label_comissao.grid(row=index + 1, column=2, padx=5, pady=2)

    for podium_index, (nome, participacoes, _, imagem_path) in enumerate(ranking[:3]):
        frame_top = ctk.CTkFrame(frame_podio, corner_radius=15, fg_color="transparent")
        frame_top.pack(pady=10, padx=10, fill="both", expand=True)

        if imagem_path:
            label_img = ctk.CTkLabel(frame_top, text="")
            label_img.pack(pady=5)
            mostrar_imagem(imagem_path, label_img, 120, 120)
        
        if podium_index+1 == 1:
            label_nome_podio = ctk.CTkLabel(frame_top, text=f"{podium_index + 1}º {nome} ", font=("Poppins Bold", 15))
            label_nome_podio.pack()
            label_participacoes = ctk.CTkLabel(frame_top, text=f"{participacoes}", font=("Poppins", 14),image=primeiro_image,
                                             anchor="e", compound="right")
            label_participacoes.pack()

        elif podium_index+1 == 2:
            label_nome_podio = ctk.CTkLabel(frame_top, text=f"{podium_index + 1}º {nome} ", font=("Poppins Bold", 15))
            label_nome_podio.pack()
            label_participacoes = ctk.CTkLabel(frame_top, text=f"{participacoes}", font=("Poppins", 14),image=segundo_image,
                                                anchor="e", compound="right")
            label_participacoes.pack()

        elif podium_index+1 == 3:
            label_nome_podio = ctk.CTkLabel(frame_top, text=f"{podium_index + 1}º {nome} ", font=("Poppins Bold", 15))
            label_nome_podio.pack()
            label_participacoes = ctk.CTkLabel(frame_top, text=f"{participacoes}", font=("Poppins", 14),image=terceiro_image,
                                                anchor="e", compound="right")
            label_participacoes.pack()

       

        
    
tela = ctk.CTk()
tela.title('Sistema Imobiliaria')
tela.after(1, lambda:tela.state('zoomed'))
ctk.set_appearance_mode("light")

add_image = ctk.CTkImage(Image.open("imagens/user.png"), size=(40,40))
key_image = ctk.CTkImage(Image.open("imagens/key.png"), size=(40,40))
money_image = ctk.CTkImage(Image.open("imagens/money.png"), size=(20,20))
file_image = ctk.CTkImage(Image.open("imagens/file.png"), size=(20,20))
crown_image = ctk.CTkImage(Image.open("imagens/crown.png"), size=(20,20))
primeiro_image = ctk.CTkImage(Image.open("imagens/medal.png"), size=(30,30))
segundo_image = ctk.CTkImage(Image.open("imagens/medal2.png"), size=(30,30))
terceiro_image = ctk.CTkImage(Image.open("imagens/medal3.png"), size=(30,30))
settings_image = ctk.CTkImage(Image.open("imagens/settings.png"), size=(30,30))
info_image = ctk.CTkImage(Image.open("imagens/info.png"), size=(20,20))
corret_image = ctk.CTkImage(Image.open("imagens/corret.png"), size=(20,20))
edit_image = ctk.CTkImage(Image.open("imagens/edit.png"), size=(20,20))


main_frame = ctk.CTkFrame(tela,fg_color="transparent")
main_frame.pack(fill="both",expand=True)

left_frame = ctk.CTkScrollableFrame(main_frame, border_color="#C0C0C0")
left_frame.pack(side="left",fill="y",pady=20,padx=10)

criar_frame = ctk.CTkFrame(main_frame,fg_color="transparent", border_color="#C0C0C0")
criar_frame.pack(side="right",fill="both",padx=10,pady=20,expand=True)

solicitar_saldo(arquivo='saldo.json')


ctk.CTkLabel(left_frame, text="Ferramentas",font=('Poppins Bold',16),anchor="w", image= settings_image, height=20, 
            compound="left").grid(row=9,column=0,padx=0,pady=10,sticky="w")

botao_criar_clientes = ctk.CTkButton(left_frame, text="Adicionar Cliente",font=('Poppins',15), width=170,command=lambda:criar_clientes(criar_frame))
botao_criar_clientes.grid(row=11,column=0,padx=0,pady=5,sticky="w",ipadx=15)

botao_conta = ctk.CTkButton(left_frame,text="Adicionar Conta",font=('Poppins',15),width=170,command=lambda:criar_contas(criar_frame))
botao_conta.grid(row=12,column=0,padx=0,pady=5,sticky="w",ipadx=15)

ctk.CTkLabel(left_frame, text=" Informações",font=('Poppins Bold',16),anchor="w", image= info_image, height=20,
            compound="left").grid(row=13,column=0,padx=3,pady=10,sticky="w")

botao_exibir_inf_contas = ctk.CTkButton(left_frame, text="Exibir Info Contas",font=('Poppins',15),width=170, command=exibir_informacoes_contas)
botao_exibir_inf_contas.grid(row=14,column=0,padx=0,pady=5,sticky="w",ipadx=15)

botao_exibir_inf_clientes = ctk.CTkButton(left_frame, text="Exibir Info Clientes",font=('Poppins',15),width=170, command=exibir_informacoes_clientes)
botao_exibir_inf_clientes.grid(row=15,column=0,padx=0,pady=5,sticky="w",ipadx=15)

botao_entradas_saidas = ctk.CTkButton(left_frame, text="Gerar Registro",font=('Poppins',15), width=170, command=gerar_entradas_saidas)
botao_entradas_saidas.grid(row=10,column=0,padx=0,pady=5,ipadx=15,sticky="w")

botao_relatorio = ctk.CTkButton(left_frame, text="Relatorio Registros",font=('Poppins',15),width=170, command=mostrar_entradas_saidas)
botao_relatorio.grid(row=16,column=0,padx=0,pady=5,sticky="w",ipadx=15)

ctk.CTkLabel(left_frame, text=" Corretores",font=('Poppins Bold',16),anchor="w", image= corret_image,
             height=20,compound="left").grid(row=17,column=0,padx=3,pady=10,sticky="w")

botao_criar_corretor = ctk.CTkButton(left_frame, text="Cadastrar Corretor",font=('Poppins',15),width=170, command=cadastrar_corretor)
botao_criar_corretor.grid(row=18,column=0,padx=0,pady=5,sticky="w",ipadx=15)

botao_exibir_inf_corretores = ctk.CTkButton(left_frame, text="Info Corretores",font=('Poppins',15),width=170, command=mostrar_corretores)
botao_exibir_inf_corretores.grid(row=19,column=0,padx=0,pady=5,sticky="w",ipadx=15)


botao_ranking = ctk.CTkButton(left_frame, text="Ranking",font=('Poppins',15),width=170,image=crown_image,command=ranking)
botao_ranking.grid(row=20,column=0,padx=0,pady=5,ipadx=15,sticky="w")


tela.mainloop()


    


