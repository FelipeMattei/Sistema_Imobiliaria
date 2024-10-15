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
                
                label_saldo = ctk.CTkLabel(left_frame, text=f"Saldo: R${saldo_existente}", font=('Poppins Bold',15),image=money_image, anchor="w",
                                                        compound="left",fg_color="#3c8cd4",text_color="white",corner_radius=10)
                
                label_saldo.grid(row=4,column=0,padx=15,pady=20,ipady=5,sticky="w")

                label_alterar = ctk.CTkLabel(left_frame, text="Alterar o Saldo?",font=('Poppins',15))
                label_alterar.grid(row=6,column=0,padx=22,sticky="w")

                entry_alterar = ctk.CTkEntry(left_frame,placeholder_text="Novo Saldo",placeholder_text_color='gray',font=('Poppins Bold',15))
                entry_alterar.grid(row=7,column=0,padx=20,sticky="w")

                botao_alterar = ctk.CTkButton(left_frame, text="Alterar saldo",font=('Poppins',15),corner_radius=15,
                                              command=lambda:(alterar_saldo(entry_alterar.get(),arquivo='saldo.json'),
                                                             solicitar_saldo(arquivo='saldo.json')) )
                botao_alterar.grid(row=8,column=0,pady=10,padx=20,sticky="w")

                botao_atualizar = ctk.CTkButton(left_frame, text="Atualizar",font=('Poppins',15),corner_radius=15,
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
    frame_corretores = ctk.CTkFrame(tela, fg_color="transparent",width=200,height=120)
    frame_corretores.place(x=45,y=400)
    frame_tipo = ctk.CTkFrame(tela, fg_color="transparent",width=220,height=400)
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

    label_data = ctk.CTkLabel(tela, text='Data Inicio',  font=('Poppins', 15))
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
            comissao1.place(x=150, y=0)

            # Variáveis para os corretores que não foram utilizados
            corretor2 = None
            corretor3 = None
            corretor4 = None
            comissao2 = None
            comissao3 = None
            comissao4 = None

        # Para 2 corretores
        elif selected_value == '2 Corretores':
            corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 1', placeholder_text_color='gray')
            corretor1.place(x=5, y=0)
            comissao1 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=150, y=0)

            corretor2 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 2', placeholder_text_color='gray')
            corretor2.place(x=5, y=30)
            comissao2 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=150, y=30)

            corretor3 = None
            corretor4 = None
            comissao3 = None
            comissao4 = None

        # Para 3 corretores
        elif selected_value == '3 Corretores':
            corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 1', placeholder_text_color='gray')
            corretor1.place(x=5, y=0)
            comissao1 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=150, y=0)

            corretor2 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 2', placeholder_text_color='gray')
            corretor2.place(x=5, y=30)
            comissao2 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=150, y=30)

            corretor3 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 3', placeholder_text_color='gray')
            corretor3.place(x=5, y=60)
            comissao3 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao3.place(x=150, y=60)

            corretor4 = None
            comissao4 = None

        # Para 4 corretores
        elif selected_value == '4 Corretores':
            corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 1', placeholder_text_color='gray')
            corretor1.place(x=5, y=0)
            comissao1 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao1.place(x=150, y=0)

            corretor2 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 2', placeholder_text_color='gray')
            corretor2.place(x=5, y=30)
            comissao2 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao2.place(x=150, y=30)

            corretor3 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 3', placeholder_text_color='gray')
            corretor3.place(x=5, y=60)
            comissao3 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao3.place(x=150, y=60)

            corretor4 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 4', placeholder_text_color='gray')
            corretor4.place(x=5, y=90)
            comissao4 = ctk.CTkEntry(frame_corretores, width=30, placeholder_text='(%)', placeholder_text_color='gray')
            comissao4.place(x=150, y=90)


            
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

            label_valor = ctk.CTkLabel(frame_tipo,text="Valor", font=('Poppins', 15))
            label_valor.place(x=0,y=0)
            valor_venda = ctk.CTkEntry(frame_tipo, placeholder_text='R$ Valor', placeholder_text_color='gray',width=100)
            valor_venda.place(x=0, y=30)

            entry_entrada = ctk.CTkEntry(frame_tipo,width=30)
            entry_entrada.place(x=110,y=30)
            ctk.CTkLabel(frame_tipo,text="%",font=("Poppins", 15)).place(x=145,y=30)

            ctk.CTkLabel(frame_tipo,text="OBS: Colocar o Valor Total, e a",
                         font=("Poppins Bold", 13)).place(x=0,y=80)
            ctk.CTkLabel(frame_tipo,text="porcentagem desse valor que",
                         font=("Poppins Bold", 13)).place(x=0,y=100)
            ctk.CTkLabel(frame_tipo,text="será retirada",
                         font=("Poppins Bold", 13)).place(x=0,y=120)




        if selected_value == "Aluguel":
            tipo_selec ="Aluguel"

            label_aluguel = ctk.CTkLabel(frame_tipo,text="Valor Aluguel", font=('Poppins', 15))
            label_aluguel.place(x=0,y=0)
            valor_aluguel = ctk.CTkEntry(frame_tipo,placeholder_text='R$ Valor',placeholder_text_color="gray")
            valor_aluguel.place(x=0, y=30)
            label_pri_aluguel = ctk.CTkLabel(frame_tipo,text="Valor 1° Aluguel", font=('Poppins', 15))
            label_pri_aluguel.place(x=0,y=60)
            valor_pri_aluguel = ctk.CTkEntry(frame_tipo,placeholder_text='R$ Valor',placeholder_text_color="gray")
            valor_pri_aluguel.place(x=0, y=90)
            label_caucao = ctk.CTkLabel(frame_tipo,text="Valor Caução", font=('Poppins', 15))
            label_caucao.place(x=0,y=120)
            valor_caucao = ctk.CTkEntry(frame_tipo,placeholder_text='R$ Valor',placeholder_text_color="gray")
            valor_caucao.place(x=0, y=150)





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
                    comissao4 FLOAT
                );           
            
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Entradas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente TEXT,
                    data TEXT NOT NULL,
                    valor FLOAT NOT NULL,
                    valor_entrada FLOAT NOT NULL,
                    status TEXT NULL,
                    FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
                );             
            ''')


        Id = id.get()
        tipo = tipo_selec

        #VENDA
        if tipo_selec == "Venda":
            valor = valor_venda.get()
            entrada = entry_entrada.get()
            valor_al = None
            primeiro_aluguel = None
            caucao = None

        #ALUGUEL
        else:
            valor_al = valor_aluguel.get()
            primeiro_aluguel = valor_pri_aluguel.get()
            caucao = valor_caucao.get()
            valor = None
            entrada = None

        
        Nome_locador = nome_locador.get()
        Nome_locatario = nome_locatario.get()
        data_inicio = get_combined_date(dia.get(), mes.get(), ano.get())  

        try:
            Corretor1 = corretor1.get() if isinstance(corretor1, ctk.CTkEntry) else corretor1
            Corretor2 = corretor2.get() if isinstance(corretor2, ctk.CTkEntry) else corretor2
            Corretor3 = corretor3.get() if isinstance(corretor3, ctk.CTkEntry) else corretor3
            Corretor4 = corretor4.get() if isinstance(corretor4, ctk.CTkEntry) else corretor4

            Comissao1 = comissao1.get() if isinstance(comissao1, ctk.CTkEntry) else comissao1
            Comissao2 = comissao2.get() if isinstance(comissao2, ctk.CTkEntry) else comissao2
            Comissao3 = comissao3.get() if isinstance(comissao3, ctk.CTkEntry) else comissao3
            Comissao4 = comissao4.get() if isinstance(comissao4, ctk.CTkEntry) else comissao4


            cursor.execute('''
                INSERT INTO Clientes (
                id, tipo, valor, valor_aluguel, entrada,
                primeiro_aluguel, caucao, nome_locador, nome_locatario, data,
                corretor1, comissao1, corretor2, comissao2, corretor3, comissao3,
                corretor4, comissao4
                )
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''', (
                Id, tipo, valor, valor_al, entrada,
                primeiro_aluguel, caucao, Nome_locador, Nome_locatario, data_inicio,
                Corretor1, Comissao1, Corretor2, Comissao2, Corretor3, Comissao3,
                Corretor4, Comissao4
                ))

            conex.commit()
            messagebox.showinfo("Sucesso!", "Dados enviados ao banco de dados com sucesso!")

        except NameError as erro:

            messagebox.showinfo("Erro!", f"Erro ao inserir dados: {erro}")
            
        finally:
            conex.close()
        


    botao_salvar = ctk.CTkButton(tela, text='Salvar',width=150,height=40, command=salvar_dados_clientes)
    botao_salvar.place(x=300, y=500)








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

    frame_ask= ctk.CTkFrame(tela,fg_color="transparent",width=300,height=100)
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
    
    botao_salvar_contas.place(x=300, y=500)

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
        nome_cliente = cliente[9]
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
                data_inserida = get_combined_date(nova_dia_entry.get(),nova_mes_entry.get(), nova_ano_entry.get())
                tela.destroy()

            tela = ctk.CTkToplevel(janela_dados)
            tela.attributes('-topmost', True)
            janela_dados.attributes("-topmost", False)
            tela.geometry("+400+400")

            ctk.CTkLabel(tela, text="Novo Valor",font=("Poppins Bold",15)).place(x=10,y=5)
            novo_valor_entry = ctk.CTkEntry(tela)
            novo_valor_entry.place(x=10, y=35)
            ctk.CTkLabel(tela, text="Nova Data",font=("Poppins Bold",15)).place(x=10,y=65)
            nova_dia_entry = ctk.CTkEntry(tela,width=50)
            nova_dia_entry.place(x=10, y=95)
            nova_mes_entry = ctk.CTkEntry(tela,width=50)
            nova_mes_entry.place(x=60, y=95)
            nova_ano_entry = ctk.CTkEntry(tela,width=50)
            nova_ano_entry.place(x=110, y=95)



            botao_mudar = ctk.CTkButton(tela, text="Alterar", command=retornar_novo_valor)
            botao_mudar.place(x=10, y=130)

            tela.wait_window()  # Aguarda até que a janela seja fechada
        
    janela_dados = ctk.CTkToplevel(tela)
    janela_dados.title("Situaçao Cliente")
    janela_dados.geometry("800x500")
    janela_clientes.attributes('-topmost', False)
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

        else:
            cursor.execute(f"SELECT * FROM Entradas WHERE {nome_filtro} = ?",(filtro,))
            dados = cursor.fetchall()

    else:
        cursor.execute(f"SELECT * FROM Entradas WHERE id_cliente = ?",(id,))
        dados = cursor.fetchall()
        conex.close()

    checkboxes = []
    headers = [" Pagar "," ID ", " ID_Cliente ", " Data ", " Valor ", " Valor Entrada ", " Status "]

    for col, header in enumerate(headers):
        ctk.CTkLabel(principal_frame, text=header, font=('Poppins Bold', 14)).grid(row=0, column=col, padx=20,pady=20)

    for i, dado in enumerate(dados, start=1):

        check = ctk.IntVar()
        checkbox = ctk.CTkCheckBox(principal_frame,text="",width=25,variable=check)
        checkbox.grid(row=i,column=0)
        checkboxes.append((check, dado))

        for j, valor in enumerate(dado, start=1):
            ctk.CTkLabel(principal_frame, text=str(valor)).grid(row=i, column=j)


        
    def marcar_pagamento():

        conex = sqlite3.connect('Banco_de_Dados.db')
        cursor = conex.cursor()

        for check, dado in checkboxes:
            if check.get() == 1: 

                id, id_cliente, data, valor, valor_entrada, status = dado   
                
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
    
        
        conex.commit()
        conex.close()
        messagebox.showinfo("Sucesso", "Entradas Recebidas com sucesso!", parent=janela_dados)
    
    botao_receber = ctk.CTkButton(principal_frame, text="Receber Entrada",font=("Poppins",15), command=marcar_pagamento)
    botao_receber.grid(row=i+1,column=1,pady=30)
        


def mostrar_info_clientes(tabela,id_cliente,frame,):


    def meses_pagamento(dia,mes,ano,quantidade,id,valor,primeiro,com1,com2,com3,com4,tipo_cliente): 

        db_path = 'Banco_de_Dados.db'

        conex = sqlite3.connect(db_path)
        cursor = conex.cursor()

        if tipo_cliente == "Aluguel":

            quantidade = int(quantidade)
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

            primeiro = primeiro - comissa_corretor - franquia

            entrada = primeiro

            entrada_1 = valor * 0.10

            status = "Aguardando Pg."  
            status_1 = "Pago!"

            data_inicial = get_combined_date(dia,mes,ano)

            cursor.execute('''
                INSERT INTO Entradas (id_cliente,data,valor,valor_entrada,status)
                VALUES (?,?,?,?,?)

                ''', (id, data_inicial, valor, entrada, status_1))

            i=0
            quantidade = quantidade - 1
            for i in range(quantidade):

                mes += 1

                if mes > 12:
                    mes=1
                    ano += 1

                data_inicial = get_combined_date(dia,mes,ano)

                cursor.execute('''
                    INSERT INTO Entradas (id_cliente,data,valor,valor_entrada,status)
                    VALUES (?,?,?,?,?)

                    ''', (id, data_inicial, valor, entrada_1, status))


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

            saida_total = (com_total + franquia) * valor_trabalhar
            entrada_total = valor_trabalhar - saida_total

            status = "Aguardando Pg."  
            status_1 = "Pago!"

            data_inicial = get_combined_date(dia,mes,ano)

            cursor.execute('''
                INSERT INTO Entradas (id_cliente,data,valor,valor_entrada,status)
                VALUES (?,?,?,?,?)

                ''', (id, data_inicial, valor, entrada_total, status_1))
            
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

    conex = sqlite3.connect('Banco_de_Dados.db')
    cursor = conex.cursor()
    cursor.execute('SELECT id FROM Entradas WHERE id_cliente = ?', (id_cliente,))
    resultado = cursor.fetchone()

    cursor.execute('SELECT data,valor_entrada FROM Entradas WHERE id_cliente = ?', (id_cliente,))
    valores_al = cursor.fetchone()
    
    conex.close

    if resultado == None:
        ctk.CTkLabel(frame, text="< Data do 1° Pagamento (Aluguel/Venda) >", font=("Poppins Bold", 14)).grid(row=8, column=0, padx=10, pady=10, sticky="w")
        dia_inicial = ctk.CTkEntry(frame, placeholder_text="Dia",placeholder_text_color="gray")
        dia_inicial.grid(row=9, column=0, padx=10, sticky="w")
        mes_inicial = ctk.CTkEntry(frame, placeholder_text="Mês",placeholder_text_color="gray")
        mes_inicial.grid(row=10, column=0, padx=10,pady=10, sticky="w")
        ano_inicial = ctk.CTkEntry(frame, placeholder_text="ano",placeholder_text_color="gray")
        ano_inicial.grid(row=11, column=0, padx=10, sticky="w")

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
                                                command=lambda:meses_pagamento(dia_inicial.get(),mes_inicial.get(),ano_inicial.get(),12,
                                                id_cliente,valor_aluguel,primeiro_aluguel,comissao_1,comissao_2,comissao_3,comissao_4,tipo))
            
            botao_criar_meses_pg.grid(row=12,column=0,padx=10,pady=10,sticky="w")
        
            
        
    # Informações específicas para Venda
    elif tipo == "Venda":
        ctk.CTkLabel(frame, text=f"Valor da Venda: R${valor}", font=("Poppins", 14)).grid(row=6, column=0, padx=10, pady=10, sticky="w")
        ctk.CTkLabel(frame, text=f"Porcentagem Entrada: {entrada}%", font=("Poppins", 14)).grid(row=7, column=0, padx=10, pady=10, sticky="w")
        
        if resultado == None:
            botao_criar_meses_pg = ctk.CTkButton(frame, text="Iniciar", font=("Poppins", 14),
                                                command=lambda:meses_pagamento(dia_inicial.get(),mes_inicial.get(),ano_inicial.get(),0,
                                                                               id_cliente,valor,entrada,comissao_1,comissao_2,comissao_3,comissao_4,tipo))
            
            botao_criar_meses_pg.grid(row=12,column=0,padx=10,pady=10,sticky="w")

   
    ctk.CTkLabel(frame, text=f"Corretor 1: {corretor_1} / {comissao_1}%", font=("Poppins", 14)).grid(row=3, column=1, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Corretor 2: {corretor_2} / {comissao_2}%", font=("Poppins", 14)).grid(row=4, column=1, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Corretor 3: {corretor_3} / {comissao_3}%", font=("Poppins", 14)).grid(row=5, column=1, padx=10, pady=10, sticky="w")
    ctk.CTkLabel(frame, text=f"Corretor 4: {corretor_4} / {comissao_4}%", font=("Poppins", 14)).grid(row=6, column=1, padx=10, pady=10, sticky="w")




def exibir_informacoes_clientes():

    global janela_clientes
    janela_clientes = ctk.CTkToplevel(tela)
    janela_clientes.title("Clientes")
    janela_clientes.geometry("1100x600")
    janela_clientes.attributes('-topmost', True)
    

    main_frame = ctk.CTkFrame(janela_clientes)
    main_frame.pack(fill="both", expand=True)

    left_frame = ctk.CTkFrame(main_frame, border_width=5, border_color="#C0C0C0")
    left_frame.pack(side="left", fill="both",expand=True,ipadx=10,padx=10,pady=20)

    id_frame = ctk.CTkScrollableFrame(main_frame,border_width=5,border_color="#C0C0C0")
    id_frame.pack(expand=True,side="left", fill="both",ipadx=50,pady=20,padx=10)

    info_frame = ctk.CTkScrollableFrame(main_frame,fg_color="transparent",border_width=5,border_color="#C0C0C0")
    info_frame.pack(side="left", expand=True, fill="both",ipadx=700,pady=20)
    
    ctk.CTkLabel(left_frame,text="< Clientes Geral >",font=("Poppins Bold", 15)).grid(row=0,column=0,sticky="w",padx=20,pady=10)

    botao_mostrar_todos_clientes = ctk.CTkButton(left_frame,text="Todos Clientes",font=("Poppins", 15), 
                                                 command=lambda:mostrar_clientes("Clientes",id_frame,info_frame,None,None))
    botao_mostrar_todos_clientes.grid(row=1,column=0,sticky="w",padx=20,pady=10)

    ctk.CTkLabel(left_frame,text="Filtrar ID",font=("Poppins Bold", 15)).grid(row=2,column=0,sticky="w",padx=20,pady=5)
    filtro_id = ctk.CTkEntry(left_frame)
    filtro_id.grid(row=3,column=0,sticky="w",padx=20,pady=5)

    botao_mostrar_clientes_id = ctk.CTkButton(left_frame,text="Filtrar",font=("Poppins", 15), 
                                              command=lambda:mostrar_clientes("Clientes",id_frame,info_frame,"id",filtro_id.get()))
    botao_mostrar_clientes_id.grid(row=4,column=0,sticky="w",padx=20)

    #Label Auxiliar
    ctk.CTkLabel(left_frame,text="").grid(row=5,column=0,padx=20,pady=10)
    
    ctk.CTkLabel(left_frame,text="< Status Clientes >",font=("Poppins Bold", 15)).grid(row=6,column=0,sticky="w",padx=20)

    botao_mostrar_situa = ctk.CTkButton(left_frame,text="Todos os Status",font=("Poppins", 15),command=lambda:verificar_situacao(None, None, None))
    botao_mostrar_situa.grid(row=7,column=0,sticky="w",padx=20,pady=10)

    ctk.CTkLabel(left_frame,text=" Filtrar Mês",font=("Poppins Bold", 15)).grid(row=8,column=0,sticky="w",padx=20,pady=5)

    filtro_mes = ctk.CTkEntry(left_frame,placeholder_text="01,02,03...", placeholder_text_color="gray")
    filtro_mes.grid(row=9,column=0,sticky="w",padx=20,pady=5)
    botao_filtrar_mes = ctk.CTkButton(left_frame,text="Filtrar", font=("Poppins", 15),command=lambda:verificar_situacao(None,"Data",filtro_mes.get()))
    botao_filtrar_mes.grid(row=10,column=0,sticky="w",padx=20)




tela = ctk.CTk()
tela.title('Sistema Imobiliaria')
tela.geometry('1000x600')
ctk.set_appearance_mode("light")

add_image = ctk.CTkImage(Image.open("imagens/user.png"), size=(40,40))
key_image = ctk.CTkImage(Image.open("imagens/key.png"), size=(40,40))
money_image = ctk.CTkImage(Image.open("imagens/money.png"), size=(20,20))

main_frame = ctk.CTkFrame(tela,fg_color="transparent")
main_frame.pack(fill="both",expand=True)

left_frame = ctk.CTkFrame(main_frame,border_width=5, border_color="#C0C0C0")
left_frame.pack(side="left",fill="y",pady=20,padx=10)

criar_frame = ctk.CTkFrame(main_frame,fg_color="transparent",border_width=5, border_color="#C0C0C0")
criar_frame.pack(side="right",fill="both",padx=10,pady=20,expand=True)

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


