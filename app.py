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



def solicitar_saldo(arquivo='saldo.json'):

    if not os.path.exists(arquivo):
        global label_inicial
        global entry_saldo
        global botao_salvar_saldo
        label_inicial = ctk.CTkLabel(left_frame, text='Valor inicial do saldo',font=('Poppins',15))
        label_inicial.grid(row=1,column=0,padx=20,sticky="w")
        entry_saldo = ctk.CTkEntry(left_frame)
        entry_saldo.grid(row=2,column=0)

        botao_salvar_saldo = ctk.CTkButton(left_frame, text='Salvar saldo inicial',font=('Poppins',15),
                                                command=lambda: salvar_saldo(entry_saldo.get(), arquivo))
        botao_salvar_saldo.grid(row=3,column=0,padx=20,sticky="w")

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
                
                label_saldo = ctk.CTkLabel(left_frame, text=f"Saldo: R${saldo_existente}", font=('Poppins Bold',15),image=money_image, anchor="w",
                                                        compound="left",fg_color="#3c8cd4",text_color="white",corner_radius=10)
                
                label_saldo.grid(row=4,column=0,padx=15,pady=20,ipady=5,sticky="w")

                label_alterar = ctk.CTkLabel(left_frame, text="Alterar o Saldo?",font=('Poppins',15))
                label_alterar.grid(row=6,column=0,padx=22,sticky="w")

                entry_alterar = ctk.CTkEntry(left_frame,placeholder_text="Novo Saldo",placeholder_text_color='gray',font=('Poppins Bold',15))
                entry_alterar.grid(row=7,column=0,padx=20,sticky="w")

                botao_alterar = ctk.CTkButton(left_frame, text="Alterar saldo",font=('Poppins',15),
                                              command=lambda:(alterar_saldo(entry_alterar.get(),arquivo='saldo.json'),
                                                             solicitar_saldo(arquivo='saldo.json')) )
                botao_alterar.grid(row=8,column=0,pady=10,padx=20,sticky="w")

                botao_atualizar = ctk.CTkButton(left_frame, text="Atualizar",font=('Poppins',15),
                                              command=lambda:(atualizar_saldo(arquivo='saldo.json'),
                                                             solicitar_saldo(arquivo='saldo.json')) )
                botao_atualizar.grid(row=5,column=0,pady=3,padx=20,sticky="w")

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
    frame_corretores = ctk.CTkFrame(tela, fg_color="transparent",width=200,height=180)
    frame_corretores.place(x=45,y=400)
    frame_tipo = ctk.CTkFrame(tela, fg_color="transparent",width=200,height=400)
    frame_tipo.place(x=250,y=100)

    label_id = ctk.CTkLabel(tela, text='ID do Imóvel', font=('Poppins Bold', 15))
    label_id.place(x=50,y=30)
    id = ctk.CTkEntry(tela)
    id.place(x=48,y=60)

    label_nome_locador = ctk.CTkLabel(tela, text='Nome do Locador', font=('Poppins', 15))
    label_nome_locador.place(x=50,y=100)
    nome_locador = ctk.CTkEntry(tela)
    nome_locador.place(x=50,y=130)

    label_nome_locatario = ctk.CTkLabel(tela, text='Nome do Locatario',  font=('Poppins', 15))
    label_nome_locatario.place(x=50,y=170)
    nome_locatario = ctk.CTkEntry(tela)
    nome_locatario.place(x=50,y=200)

    label_data = ctk.CTkLabel(tela, text='Data',  font=('Poppins', 15))
    label_data.place(x=50,y=240)
    dia = ctk.CTkEntry(tela, width=50, placeholder_text='Dia', placeholder_text_color='gray')
    dia.place(x=50,y=270)
    mes = ctk.CTkEntry(tela, width=50, placeholder_text='Mes', placeholder_text_color='gray')
    mes.place(x=110,y=270)
    ano = ctk.CTkEntry(tela, width=50, placeholder_text='Ano', placeholder_text_color='gray')
    ano.place(x=170,y=270)



    
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
            corretor1.place(x=5, y=0)
            comissao1 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=150,y=0)
            corretor2 = "Vazio"
            corretor3 = "Vazio"
            corretor4 = "Vazio"

        if selected_value == '2 Corretores':
            corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 1', placeholder_text_color='gray')
            corretor1.place(x=5, y=0)
            comissao1 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=150,y=0)
            
            corretor2 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 2', placeholder_text_color='gray')
            corretor2.place(x=5, y=30)
            comissao2 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=150,y=30)
            
            corretor3 = "Vazio"
            corretor4 = "Vazio"

        
        if selected_value == '3 Corretores':
            corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 1', placeholder_text_color='gray')
            corretor1.place(x=5, y=0)
            comissao1 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=150,y=0)
        
            corretor2 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 2', placeholder_text_color='gray')
            corretor2.place(x=5, y=30)
            comissao2 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=150,y=30)
            
            corretor3 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 3', placeholder_text_color='gray')
            corretor3.place(x=5, y=60)
            comissao3 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao3.place(x=150,y=60)

            corretor4 = "Vazio"

        if selected_value == '4 Corretores':
            corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 1', placeholder_text_color='gray')
            corretor1.place(x=5, y=0)
            comissao1 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=150,y=0)
        
            corretor2 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 2', placeholder_text_color='gray')
            corretor2.place(x=5, y=30)
            comissao2 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=150,y=30)
            
            corretor3 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 3', placeholder_text_color='gray')
            corretor3.place(x=5, y=60)
            comissao3 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao3.place(x=150,y=60)

            corretor4 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 4', placeholder_text_color='gray')
            corretor4.place(x=5, y=90)
            comissao4 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao4.place(x=150,y=90)


            
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

            label_valor = ctk.CTkLabel(frame_tipo,text="Valor", font=('Poppins', 15))
            label_valor.place(x=0,y=0)
            valor_venda = ctk.CTkEntry(frame_tipo, placeholder_text='R$ Valor venda', placeholder_text_color='gray')
            valor_venda.place(x=0, y=30)

            label_royal = ctk.CTkLabel(frame_tipo,text="Valor Royalties", font=('Poppins', 15))
            label_royal.place(x=0,y=60)
            entry_royal = ctk.CTkEntry(frame_tipo,placeholder_text="Em porcentagem(%)",placeholder_text_color="gray")
            entry_royal.place(x=0,y=90)

        if selected_value == "Aluguel":
            tipo_selec ="Aluguel"
            label_calcao = ctk.CTkLabel(frame_tipo,text="Valor Calção", font=('Poppins', 15))
            label_calcao.place(x=0,y=0)
            valor_calcao = ctk.CTkEntry(frame_tipo, placeholder_text='R$ Valor', placeholder_text_color='gray')
            valor_calcao.place(x=0, y=30)

            label_royal = ctk.CTkLabel(frame_tipo,text="Valor Royalties", font=('Poppins', 15))
            label_royal.place(x=0,y=60)
            entry_royal = ctk.CTkEntry(frame_tipo,placeholder_text="Em porcentagem(%)",placeholder_text_color="gray")
            entry_royal.place(x=0,y=90)


    def on_option_change_tipo(choice):
        tipo_eventos(choice)
        

    label_corretores = ctk.CTkLabel(tela, text='Corretores', font=('Poppins Bold', 15))
    label_corretores.place(x=50,y=330)
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
    corretores_menu.place(x=50, y=360)



    label_tipo = ctk.CTkLabel(tela,text="Serviço requisitado", font=('Poppins Bold', 15))
    label_tipo.place(x=250, y=30)
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
    tipo_menu.place(x=250,y=60)




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
        


    botao_salvar = ctk.CTkButton(tela, text='Salvar',width=150,height=40, command=salvar_dados_clientes)
    botao_salvar.place(x=230, y=550)








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
            ctk.CTkLabel(frame, text=header, font=('Arial Bold', 12)).grid(row=0, column=col, padx=15,pady=10)

        for i, conta in enumerate(contas, start=1):

            check = ctk.IntVar()
            checkbox = ctk.CTkCheckBox(frame,text="",width=25,variable=check)
            checkbox.grid(row=i,column=0)
            checkboxes.append((check, conta))

            for j, valor in enumerate(conta, start=1):
                ctk.CTkLabel(frame, text=str(valor)).grid(row=i, column=j)
                
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
                    ask_valor = messagebox.askyesno("Confirmaçao",f"Voce deseja mudar o valor da conta {tipo}? Valor atual:{valor}",parent=frame)

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

                    id_pago = gerar_id("PG" + id[:3])
                    cursor.execute('''
                    INSERT INTO ContasPagas(id,tipo,fornecedor,valor,data_pg)
                    VALUES (?,?,?,?,?)
                    ''',(id_pago, tipo, fornecedor, valor, data_pg))
        

                    cursor.execute("DELETE FROM Contas WHERE id=?", (id,))
                    with open(arquivo, 'w') as f:
                        json.dump({'saldo': novo_saldo}, f)
            
            
            conex.commit()
            conex.close()
            messagebox.showinfo("Sucesso", "Contas pagas com sucesso!", parent=janela)


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



def get_combined_date(day, month, year):
    try:
        date_str = f"{int(day):02d}/{int(month):02d}/{int(year)}"
        return date_str
    except ValueError:
        return "Data inválida"
    


def gerar_id(tipo_conta):
    db_path = 'Banco_de_Dados.db'
    conex = sqlite3.connect(db_path)
    cursor = conex.cursor()
    prefixo = tipo_conta[:3].upper()
    
    while True:
        sufixo = f"{random.randint(1000, 9999)}"
    
        novo_id = f"{prefixo}{sufixo}"

        cursor.execute(f"SELECT COUNT(1) FROM Contas WHERE id = ?", (novo_id,))
        if cursor.fetchone()[0] == 0:
            conex.close()
            return novo_id


def criar_contas(tela):

    destruir_widgets(tela)
    
    label_tipoc = ctk.CTkLabel(tela, text="Tipo de conta", font=('Poppins Bold', 15))
    label_tipoc.place(x=50, y=30)

    conta_entry = ctk.CTkEntry(tela, placeholder_text="Energia, Aluguel, Etc...",placeholder_text_color='gray')
    conta_entry.place(x=50,y=60)

    label_fornecedorc = ctk.CTkLabel(tela, text="Fornecedor", font=('Poppins', 15))
    label_fornecedorc.place(x=50, y=100)

    fornecedor_entry = ctk.CTkEntry(tela)
    fornecedor_entry.place(x=50,y=130)

    label_valorc = ctk.CTkLabel(tela, text="Valor Conta", font=('Poppins', 15))
    label_valorc.place(x=50, y=160)

    valor_entry = ctk.CTkEntry(tela)
    valor_entry.place(x=50,y=190)

    label_datac = ctk.CTkLabel(tela, text="Data de Vencimento", font=('Poppins', 15))
    label_datac.place(x=50, y=230)

    dia_entry = ctk.CTkEntry(tela, width=50, placeholder_text='Dia', placeholder_text_color='gray')
    dia_entry.place(x=50,y=260)
    mes_entry = ctk.CTkEntry(tela, width=50, placeholder_text='Mes', placeholder_text_color='gray')
    mes_entry.place(x=110,y=260)  
    ano_entry = ctk.CTkEntry(tela, width=50, placeholder_text='Ano', placeholder_text_color='gray')
    ano_entry.place(x=170,y=260)
    label_ask = ctk.CTkLabel(tela,text="Deseja repetir esta conta para próximos meses?", font=('Poppins Bold', 15))
    label_ask.place(x=50, y=300)

    frame_ask= ctk.CTkFrame(tela,fg_color="transparent",width=350)
    frame_ask.place(x=50,y=360)

    def ask_eventos(selected_value):
        
        destruir_widgets(frame_ask)

        global entry_quantidade_mes
        
        if selected_value == "Sim":

            ctk.CTkLabel(frame_ask, text="Quantos meses a frente?",font=('Poppins', 15)).place(x=0, y=0)
            entry_quantidade_mes = ctk.CTkEntry(frame_ask,width=60, placeholder_text="1,2,3...", placeholder_text_color="gray")
            entry_quantidade_mes.place(x=200, y=0)



        if selected_value == "Não":
            global meses_a_frente
            meses_a_frente = 0
    


    botao_salvar_contas = ctk.CTkButton(tela,text="Salvar", width=150,height=40,command=lambda:salvar_contas(
        conta_entry.get(), fornecedor_entry.get(),
        valor_entry.get(), dia_entry.get(),
        mes_entry.get(), ano_entry.get()))
    
    botao_salvar_contas.place(x=230, y=550)

    def on_option_change_ask(choice):
        global selected_value
        selected_value = choice
        ask_eventos(selected_value)

    yes_no_options = ["Sim", "Não"]
    yes_no_menu = ctk.CTkOptionMenu(    
    master=tela, 
    values=yes_no_options, 
    command=on_option_change_ask,
    dropdown_font=("Arial", 12),  
    button_color="lightblue",  
    dropdown_fg_color="#3c8cd4",
    dropdown_text_color="white"
    )
    yes_no_menu.place(x=50,y=330)



def salvar_contas(tipo,fornecedor,valor,dia,mes,ano):

    if selected_value == "Sim":
        meses_a_frente = int(entry_quantidade_mes.get())
        
    else:
        meses_a_frente = 0

    if meses_a_frente > 12:

        messagebox.showinfo("Erro!", "Não é possível adicionar a mesma conta para mais de 12 meses!")
        conex.close()

    else:      
        i=0
        while meses_a_frente >= 0:
            db_path = 'Banco_de_Dados.db'
            conex = sqlite3.connect(db_path)
            cursor = conex.cursor()
    

            cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Contas (
                        id TEXT PRIMARY KEY NOT NULL,
                        tipo TEXT NOT NULL,
                        fornecedor TEXT NOT NULL,
                        valor FLOAT NOT NULL,
                        data_pg TEXT NOT NULL
                        );           
            ''')

            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS ContasPagas (
                            id TEXT PRIMARY KEY NOT NULL,
                            tipo TEXT NOT NULL,
                            fornecedor TEXT NOT NULL,
                            valor FLOAT NOT NULL,
                            data_pg TEXT NOT NULL
                            );           
                            ''')

                    
            id=gerar_id(tipo)

            conex = sqlite3.connect(db_path)
            cursor = conex.cursor()
            try:

                mes = int(mes)

                if mes > 12:
                    mes = 1
                    ano = int(ano) + 1
                    data = get_combined_date(dia,mes,ano)

                else:
                    mes = int(mes)
                    data = get_combined_date(dia,mes,ano)
                
                cursor.execute('''
                    INSERT INTO Contas (id,tipo,fornecedor,valor,data_pg)
                    VALUES (?,?,?,?,?)
                    ''',(id,tipo,fornecedor,valor,data))
                
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
    
    janela_contas = ctk.CTkToplevel(tela)
    janela_contas.title("Contas a Pagar")
    janela_contas.geometry("1000x500+200+300")
    janela_contas.attributes('-topmost', True) # Força a janela a estar sempre no topo
    

    main_frame = ctk.CTkFrame(janela_contas,fg_color="transparent")
    main_frame.pack(fill="both", expand=True)

    left_frame = ctk.CTkFrame(main_frame,fg_color="transparent")
    left_frame.pack(side="left", fill="y")
    
    frame_contas = ctk.CTkScrollableFrame(main_frame)
    frame_contas.pack(side="right", fill="both", expand=True, padx=(0, 20))

    ctk.CTkLabel(left_frame, text="Exibir Todas:",font=('Poppins Bold', 15)).place(x=40, y=20)

    botao_todas_contas = ctk.CTkButton(left_frame, text="Contas a Pagar",font=('Poppins', 15), command=lambda:mostrar_contas("Contas", None, None, frame_contas, janela_contas))
    botao_todas_contas.place(x=40,y=50)

    botao_exibir_pagas = ctk.CTkButton(left_frame, text="Contas pagas",font=('Poppins', 15), command=lambda:mostrar_contas("ContasPagas", None, None, frame_contas, janela_contas))
    botao_exibir_pagas.place(x=40,y=100)

    label_filtro = ctk.CTkLabel(left_frame, text="Filtrar",font=('Poppins Bold', 15))
    label_filtro.place(x=40,y=150)

    frame_filtro = ctk.CTkFrame(left_frame,fg_color="transparent")
    frame_filtro.place(x=40,y=250)

    filter_var = ctk.StringVar(value="outro")

    def on_radio_change(filtro1, valor_filtro1):

        selected_option = filter_var.get()
        
        if selected_option == "Todas Contas":
            mostrar_contas("Todas",filtro1, valor_filtro1, frame_contas, janela_contas)
            
        elif selected_option == "Pagas":
            mostrar_contas("ContasPagas",filtro1, valor_filtro1, frame_contas, janela_contas)

        elif selected_option == "Não Pagas":
            mostrar_contas("Contas",filtro1, valor_filtro1, frame_contas, janela_contas)


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

            entry_data_filtro = ctk.CTkEntry(frame_filtro, placeholder_text="Energia,Agua...", placeholder_text_color="gray")
            entry_data_filtro.place(x=0,y=30)

            radio1 = ctk.CTkRadioButton(frame_filtro, text="Todas Contas",font=('Poppins', 13), variable=filter_var, value="Todas Contas")
            radio1.place(x=0,y=70)

            radio2 = ctk.CTkRadioButton(frame_filtro, text="Pagas",font=('Poppins', 13), variable=filter_var, value="Pagas")
            radio2.place(x=0,y=100)

            radio3 = ctk.CTkRadioButton(frame_filtro, text="Não Pagas",font=('Poppins', 13), variable=filter_var, value="Não Pagas")
            radio3.place(x=0,y=130)

            botao_selecionar_radio = ctk.CTkButton(frame_filtro, text="Selecionar",font=('Poppins', 15), command=lambda:on_radio_change("tipo", entry_data_filtro.get()))
            botao_selecionar_radio.place(x=0,y=160)
        
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
    filtros_menu.place(x=40,y=190)
    




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
        nome_cliente = cliente[5]
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

def mostrar_info_clientes(tabela,id_cliente,frame):

    destruir_widgets(frame)

    conex = sqlite3.connect('Banco_de_Dados.db')
    cursor = conex.cursor()
    cursor.execute(f"SELECT * FROM {tabela} WHERE id=?",(id_cliente,))
    cliente = cursor.fetchone()
    conex.close()

    if cliente:

        id_cliente = cliente[0]
        tipo = cliente[1]
        valor = cliente[2]
        royalties = cliente[3]
        calcao = cliente[4]
        nome_locador = cliente[5]
        nome_locatario = cliente[6]
        data = cliente[7]
        corretor_1 = cliente[8]
        comissao_1 = cliente[9]
        corretor_2 = cliente[10]
        comissao_2 = cliente[11]
        corretor_3 = cliente[12]
        comissao_3 = cliente[13]
        corretor_4 = cliente[14]
        comissao_4 = cliente[15]

    
    ctk.CTkLabel(frame, text="Informações do Cliente", image=add_image, 
                 font=('Poppins', 14),fg_color="#3c8cd4",
                 corner_radius=15,text_color="white",anchor="w",compound="left").grid(row=0, column=0, pady=10,sticky="w")

    ctk.CTkLabel(frame, text=f"ID: {id_cliente}", font=("Poppins", 14),
                 fg_color="#3c8cd4", image=key_image, corner_radius=10,
                 text_color="white",anchor="w",compound="left").grid(row=1, column=0, pady=10, sticky="w")
    
    ctk.CTkLabel(frame, text=f"Tipo: {tipo}", font=("Poppins", 14)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Valor: {valor}", font=("Poppins", 14)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Royalties: {royalties}", font=("Poppins", 14)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Calção: {calcao}", font=("Poppins", 14)).grid(row=5, column=0, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Locador: {nome_locador}", font=("Poppins", 14)).grid(row=6, column=0, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Locatário: {nome_locatario}", font=("Poppins", 14)).grid(row=7, column=0, padx=10, pady=10, sticky="w")

    ctk.CTkLabel(frame, text=f"Data: {data}", font=("Poppins", 14)).grid(row=1, column=1, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Corretor 1: {corretor_1} / {comissao_1}%", font=("Poppins", 14)).grid(row=2, column=1, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Corretor 2: {corretor_2} / {comissao_2}%", font=("Poppins", 14)).grid(row=3, column=1, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Corretor 3: {corretor_3} / {comissao_3}%", font=("Poppins", 14)).grid(row=4, column=1, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Corretor 4: {corretor_4} / {comissao_4}%", font=("Poppins", 14)).grid(row=5, column=1, padx=10, pady=10, sticky="w")







def exibir_informacoes_clientes():

    janela_clientes = ctk.CTkToplevel(tela)
    janela_clientes.title("Clientes")
    janela_clientes.geometry("1000x500")
    janela_clientes.attributes('-topmost', True)

    main_frame = ctk.CTkFrame(janela_clientes)
    main_frame.pack(fill="both", expand=True)

    left_frame = ctk.CTkFrame(main_frame)
    left_frame.pack(side="left", fill="both",expand=True,padx=10)

    id_frame = ctk.CTkScrollableFrame(main_frame,fg_color="transparent")
    id_frame.pack(expand=True,side="left", fill="both",ipadx=50)

    info_frame = ctk.CTkScrollableFrame(main_frame,orientation="horizontal",fg_color="transparent")
    info_frame.pack(side="left", expand=True, fill="both",ipadx=700)
    
    botao_mostrar_todos_clientes = ctk.CTkButton(left_frame,text="Todos Clientes",font=("Poppins", 15), 
                                                 command=lambda:mostrar_clientes("Clientes",id_frame,info_frame,None,None))
    botao_mostrar_todos_clientes.grid(row=0,column=0,sticky="w",padx=10,pady=20)

    ctk.CTkLabel(left_frame,text="Filtrar ID",font=("Poppins Bold", 15)).grid(row=1,column=0,sticky="w",padx=10)
    filtro_id = ctk.CTkEntry(left_frame,placeholder_text="Id",placeholder_text_color="gray")
    filtro_id.grid(row=2,column=0,sticky="w",padx=10)

    botao_mostrar_clientes_id = ctk.CTkButton(left_frame,text="Filtrar",font=("Poppins", 15), 
                                              command=lambda:mostrar_clientes("Clientes",id_frame,info_frame,"id",filtro_id.get()))
    botao_mostrar_clientes_id.grid(row=3,column=0,sticky="w",pady=10,padx=10)




tela = ctk.CTk()
tela.title('Sistema Imobiliaria')
tela.geometry('1000x600')
ctk.set_appearance_mode("light")

add_image = ctk.CTkImage(Image.open("user.png"), size=(40,40))
key_image = ctk.CTkImage(Image.open("key.png"), size=(40,40))
money_image = ctk.CTkImage(Image.open("money.png"), size=(20,20))
tool_image = ctk.CTkImage(Image.open("tool.png"), size=(30,30))

main_frame = ctk.CTkFrame(tela,fg_color="transparent")
main_frame.pack(fill="both",expand=True)

left_frame = ctk.CTkScrollableFrame(main_frame,fg_color="transparent")
left_frame.pack(side="left",fill="y")

criar_frame = ctk.CTkFrame(main_frame,fg_color="transparent")
criar_frame.pack(side="right",fill="both",expand=True)

solicitar_saldo(arquivo='saldo.json')


ctk.CTkLabel(left_frame, text="Ferramentas",font=('Poppins Bold',15),anchor="w",
                                                compound="left").grid(row=9,column=0,padx=20,pady=10,sticky="w")

botao_criar_clientes = ctk.CTkButton(left_frame, text="Adicionar Cliente",font=('Poppins',15),corner_radius=15,command=lambda:criar_clientes(criar_frame))
botao_criar_clientes.grid(row=10,column=0,padx=20,pady=10,sticky="w",ipadx=4)

botao_conta = ctk.CTkButton(left_frame,text="Adicionar Conta",font=('Poppins',15),corner_radius=15,command=lambda:criar_contas(criar_frame))
botao_conta.grid(row=11,column=0,padx=20,pady=10,sticky="w",ipadx=6)

ctk.CTkLabel(left_frame, text="Informações",font=('Poppins Bold',15),).grid(row=12,column=0,padx=20,pady=10,sticky="w")

botao_exibir_inf_contas = ctk.CTkButton(left_frame, text="Exibir Info Contas",font=('Poppins',15),corner_radius=15, command=exibir_informacoes_contas)
botao_exibir_inf_contas.grid(row=13,column=0,padx=20,pady=10,sticky="w",ipadx=4)

botao_exibir_inf_clientes = ctk.CTkButton(left_frame, text="Exibir Info Clientes",font=('Poppins',15),corner_radius=15, command=exibir_informacoes_clientes)
botao_exibir_inf_clientes.grid(row=14,column=0,padx=20,pady=10,sticky="w")




tela.mainloop()


