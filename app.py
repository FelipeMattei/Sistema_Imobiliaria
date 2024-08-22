import sqlite3
import os
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
import json




def solicitar_saldo(arquivo='saldo.json'):

    if not os.path.exists(arquivo):
        global label_inicial
        global entry_saldo
        global botao_salvar_saldo
        label_inicial = ctk.CTkLabel(tela, text='Valor inicial do saldo')
        label_inicial.place(x=420,y=80)
        entry_saldo = ctk.CTkEntry(tela)
        entry_saldo.place(x=420,y=110)

        botao_salvar_saldo = ctk.CTkButton(tela, text='Salvar saldo inicial', 
                                                command=lambda: salvar_saldo(entry_saldo.get(), arquivo))
        botao_salvar_saldo.place(x=420, y=140)

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

                label_saldo = ctk.CTkLabel(tela, text=f"Saldo: R${saldo_existente}", font=('Arial Bold', 15))
                label_saldo.place(x=420,y=80)

                label_alterar = ctk.CTkLabel(tela, text="Alterar o Saldo?",font=('Arial Bold', 15))
                label_alterar.place(x=420,y=140)

                entry_alterar = ctk.CTkEntry(tela,placeholder_text="Novo Saldo",placeholder_text_color='gray')
                entry_alterar.place(x=420,y=180)

                botao_alterar = ctk.CTkButton(tela, text="Alterar saldo",
                                              command=lambda:(alterar_saldo(entry_alterar.get(),arquivo='saldo.json'),
                                                             solicitar_saldo(arquivo='saldo.json')) )
                botao_alterar.place(x=420,y=240)


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
                comissao FLOAT,
                calcao FLOAT,
                nome_locador TEXT NOT NULL,
                nome_locatario TEXT NOT NULL,
                data TEXT NOT NULL,
                corretor1 TEXT NOT NULL,
                corretor2 TEXT,
                corretor3 TEXT
                );           
        
    ''')


    Id = id.get()
    tipo = tipo_selec

    if tipo == "Venda":
        valor = valor_venda.get()
    else:
        valor = 0
    
    royalties = entry_royal.get()
    comissao = entry_comissao.get()

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

        cursor.execute('''
        INSERT INTO Clientes (  id,tipo,valor,royalties,
                                comissao,calcao,nome_locador,
                                nome_locatario,data,corretor1,corretor2,corretor3)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        ''',(Id,tipo,valor,royalties,comissao,calcao,Nome_locador,Nome_locatario,Data,Corretor1,Corretor2,Corretor3))

        conex.commit()
        messagebox.showinfo("Sucesso!", "Dados enviados ao banco de dados com sucesso!")

    except NameError as erro:

         messagebox.showinfo("Erro!", "É necessário definir ao menos 1 corretor por ID!")
        
    finally:
        conex.close()







def get_combined_date(day, month, year):
    try:
        # Formatar a data no formato DD/MM/AAAA
        date_str = f"{day.zfill(2)}/{month.zfill(2)}/{year.zfill(4)}"
        # Validar e converter a string em um objeto datetime
        return date_str
    except ValueError:
        return "Data inválida"
    






def criar_contas():

    label_tipoc = ctk.CTkLabel(tela, text="Tipo de conta", font=('Arial Bold', 15))
    label_tipoc.place(x=600, y=80)

    conta_entry = ctk.CTkEntry(tela, placeholder_text="Energia, Aluguel, Etc...",placeholder_text_color='gray')
    conta_entry.place(x=600,y=110)

    label_fornecedorc = ctk.CTkLabel(tela, text="Fornecedor", font=('Arial Bold', 15))
    label_fornecedorc.place(x=600, y=140)

    fornecedor_entry = ctk.CTkEntry(tela)
    fornecedor_entry.place(x=600,y=170)

    label_valorc = ctk.CTkLabel(tela, text="Valor Conta", font=('Arial Bold', 15))
    label_valorc.place(x=600, y=200)

    valor_entry = ctk.CTkEntry(tela)
    valor_entry.place(x=600,y=230)

    label_datac = ctk.CTkLabel(tela, text="Data de Vencimento", font=('Arial Bold', 15))
    label_datac.place(x=600, y=260)

    dia_entry = ctk.CTkEntry(tela, width=50, placeholder_text='Dia', placeholder_text_color='gray')
    dia_entry.place(x=600,y=290)
    mes_entry = ctk.CTkEntry(tela, width=50, placeholder_text='Mes', placeholder_text_color='gray')
    mes_entry.place(x=660,y=290)  
    ano_entry = ctk.CTkEntry(tela, width=50, placeholder_text='Ano', placeholder_text_color='gray')
    ano_entry.place(x=720,y=290)

    botao_salvar_contas = ctk.CTkButton(tela,text="Salvar", command=lambda:salvar_contas(
        conta_entry.get(), fornecedor_entry.get(),
        valor_entry.get(), dia_entry.get(),
        mes_entry.get(), ano_entry.get()))
    
    botao_salvar_contas.place(x=600,y=340)







def salvar_contas(tipo,fornecedor,valor,dia,mes,ano):
    
    db_path = 'Banco_de_Dados.db'

    conex = sqlite3.connect(db_path)
    cursor = conex.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Contas (
                tipo TEXT PRIMARY KEY NOT NULL,
                fornecedor TEXT NOT NULL,
                valor FLOAT NOT NULL,
                data_pg TEXT NOT NULL
                );           
    ''')

    try:
        
        data = get_combined_date(dia,mes,ano)
        
        cursor.execute('''
            INSERT INTO Contas (tipo,fornecedor,valor,data_pg)
            VALUES (?,?,?,?)
            ''',(tipo,fornecedor,valor,data))
        
        conex.commit()
        messagebox.showinfo("Sucesso!", "Dados enviados ao banco de dados com sucesso!")

    except NameError as erro:

        messagebox.showinfo("Erro!", "Erro dados colocados de forma incorreta!")
        
    finally:
        conex.close()





def salvar_contas(tipo,fornecedor,valor,dia,mes,ano):
    
    db_path = 'Banco_de_Dados.db'

    conex = sqlite3.connect(db_path)
    cursor = conex.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Contas (
                tipo TEXT PRIMARY KEY NOT NULL,
                fornecedor TEXT NOT NULL,
                valor FLOAT NOT NULL,
                data_pg TEXT NOT NULL
                );           
    ''')

    try:
        
        data = get_combined_date(dia,mes,ano)
        
        cursor.execute('''
            INSERT INTO Contas (tipo,fornecedor,valor,data_pg)
            VALUES (?,?,?,?)
            ''',(tipo,fornecedor,valor,data))
        
        conex.commit()
        messagebox.showinfo("Sucesso!", "Dados enviados ao banco de dados com sucesso!")

    except NameError as erro:

        messagebox.showinfo("Erro!", "Erro dados colocados de forma incorreta!")
        
    finally:
        conex.close()






def exibir_informacoes_contas():
    
    janela_contas = ctk.CTkToplevel(tela)
    janela_contas.title("Contas a Pagar")
    janela_contas.geometry("900x500+200+300")
    janela_contas.attributes('-topmost', True) # Força a janela a estar sempre no topo
    

    main_frame = ctk.CTkFrame(janela_contas,fg_color="transparent")
    main_frame.pack(fill="both", expand=True)

    left_frame = ctk.CTkFrame(main_frame,fg_color="transparent")
    left_frame.pack(side="left", fill="y")
    
    ctk.CTkLabel(left_frame,text="Tipo de conta",font=('Arial Bold', 15)).place(x=40, y=20)
    entry_filtro_conta = ctk.CTkEntry(left_frame, placeholder_text="Energia, Aluguel, etc..", placeholder_text_color="grey")
    entry_filtro_conta.place(x=40, y=55)
   
    frame_contas = ctk.CTkScrollableFrame(main_frame)
    frame_contas.pack(side="right", fill="both", expand=True, padx=(0, 20))




    def exibir_todas_contas():

        for widget in frame_contas.winfo_children():
            widget.destroy()

        conex = sqlite3.connect('Banco_de_Dados.db')
        cursor = conex.cursor()
        cursor.execute("SELECT * FROM Contas")
        contas = cursor.fetchall()
        conex.close()

        checkboxes = []
        headers = ["  Pago "," Tipo ", " Fornecedor ", " Valor ", " Data "]

        for col, header in enumerate(headers):
            ctk.CTkLabel(frame_contas, text=header, font=('Arial Bold', 12)).grid(row=0, column=col, padx= 5,pady=5)

        for i, conta in enumerate(contas, start=1):

            check = ctk.IntVar()
            checkbox = ctk.CTkCheckBox(frame_contas,text="",width=25,variable=check)
            checkbox.grid(row=i,column=0)
            checkboxes.append((check, (conta[0], conta[2])))

            for j, valor in enumerate(conta, start=1):
                ctk.CTkLabel(frame_contas, text=str(valor)).grid(row=i, column=j)
                

        def marcar_pagamento():
            conex = sqlite3.connect('Banco_de_Dados.db')
            cursor = conex.cursor()
            
            for check, (tipo, valor) in checkboxes:
                if check.get() == 1: 

                    arquivo = "saldo.json"
                    with open(arquivo, 'r') as f:
                        dados = json.load(f)
                        saldo = dados.get('saldo', 0)
                    
                    saida = valor
                    novo_saldo = saldo - saida
                    
                    cursor.execute("DELETE FROM Contas WHERE tipo=?", (tipo,))
                    with open(arquivo, 'w') as f:
                        json.dump({'saldo': novo_saldo}, f)

                        
            
            conex.commit()
            conex.close()
            janela_contas.destroy()  # Fecha a janela de contas após salvar as alterações
            messagebox.showinfo("Sucesso", "Contas pagas e removidas com sucesso!")

        botao_pagar_contas = ctk.CTkButton(frame_contas, text="Pagar Contas", command=marcar_pagamento)
        botao_pagar_contas.grid(row=i+1,column=2)

    botao_todas_contas = ctk.CTkButton(left_frame, text="Todas as contas", command=exibir_todas_contas)
    botao_todas_contas.place(x=40,y=140)






    def filtro_contas(tipo):

        for widget in frame_contas.winfo_children():
            widget.destroy()
        
        conex = sqlite3.connect('Banco_de_Dados.db')
        cursor = conex.cursor()

        try:
            cursor.execute("SELECT * FROM Contas WHERE tipo = ?", (tipo,))


            contas = cursor.fetchall()
            conex.close()


            checkboxes = []
            headers = ["  Pago "," Tipo ", " Fornecedor ", " Valor ", " Data "]

            for col, header in enumerate(headers):
                    ctk.CTkLabel(frame_contas, text=header, font=('Arial Bold', 12)).grid(row=0, column=col, padx= 5,pady=5)

            for i, conta in enumerate(contas, start=1):

                check = ctk.IntVar()
                checkbox = ctk.CTkCheckBox(frame_contas,text="",width=25,variable=check)
                checkbox.grid(row=i,column=0)
                checkboxes.append((check, (conta[0], conta[2])))

                for j, valor in enumerate(conta, start=1):
                        ctk.CTkLabel(frame_contas, text=str(valor)).grid(row=i, column=j)

            def marcar_pagamento():
                conex = sqlite3.connect('Banco_de_Dados.db')
                cursor = conex.cursor()
                    
                for check, (tipo, valor) in checkboxes:
                    if check.get() == 1: 

                        arquivo = "saldo.json"
                        with open(arquivo, 'r') as f:
                            dados = json.load(f)
                            saldo = dados.get('saldo', 0)
                            
                        saida = valor
                        novo_saldo = saldo - saida
                            
                        cursor.execute("DELETE FROM Contas WHERE tipo=?", (tipo,))
                        with open(arquivo, 'w') as f:
                            json.dump({'saldo': novo_saldo}, f)

                conex.commit()
                conex.close()
                janela_contas.destroy()  
                messagebox.showinfo("Sucesso", "Contas pagas e removidas com sucesso!")


            botao_pagar_contas = ctk.CTkButton(frame_contas, text="Pagar Contas", command=marcar_pagamento)
            botao_pagar_contas.grid(row=i+1,column=2)

        except UnboundLocalError:
            messagebox.showinfo("Erro!", f"Tipo: {tipo} não encontrado no Banco de Dados! Lembre-se de Digitar o Tipo da conta exatamente da mesma forma que ele foi cadastrado.")
        
        finally:
            conex.close()

    
    botao_filtrar_contas = ctk.CTkButton(left_frame, text="Filtrar", command=lambda:filtro_contas(entry_filtro_conta.get()))
    botao_filtrar_contas.place(x=40,y=90)

        
        

        













def corretor_entries(selected_value):

    for widget in frame_corretores.winfo_children():
        widget.destroy()

    if selected_value == '1 Corretor':

        global corretor1 
        global corretor2
        global corretor3

        corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor', placeholder_text_color='gray')
        corretor1.place(x=220, y=340)
        corretor2 = "Vazio"
        corretor3 = "Vazio"

    if selected_value == '2 Corretores':
        corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 1', placeholder_text_color='gray')
        corretor1.place(x=220, y=340)
        
        corretor2 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 2', placeholder_text_color='gray')
        corretor2.place(x=220, y=370)
        
        corretor3 = "Vazio"
    
    if selected_value == '3 Corretores':
        corretor1 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 1', placeholder_text_color='gray')
        corretor1.place(x=220, y=340)
       
        corretor2 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 2', placeholder_text_color='gray')
        corretor2.place(x=220, y=370)
        
        corretor3 = ctk.CTkEntry(frame_corretores, placeholder_text='Nome corretor 3', placeholder_text_color='gray')
        corretor3.place(x=220, y=400)
        
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

        label_comissao = ctk.CTkLabel(frame_tipo,text="Comissao por Corretor", font=('Arial Bold', 15))
        label_comissao.place(x=20,y=80)
        entry_comissao = ctk.CTkEntry(frame_tipo,placeholder_text="Em porcentagem(%)",placeholder_text_color="gray")
        entry_comissao.place(x=20,y=110)

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

        label_comissao = ctk.CTkLabel(frame_tipo,text="Comissao por Corretor", font=('Arial Bold', 15))
        label_comissao.place(x=20,y=110)
        entry_comissao = ctk.CTkEntry(frame_tipo,placeholder_text="Em porcentagem(%)",placeholder_text_color="gray")
        entry_comissao.place(x=20,y=140)

        label_royal = ctk.CTkLabel(frame_tipo,text="Valor Royalties", font=('Arial Bold', 15))
        label_royal.place(x=20,y=170)
        entry_royal = ctk.CTkEntry(frame_tipo,placeholder_text="Em porcentagem(%)",placeholder_text_color="gray")
        entry_royal.place(x=20,y=200)


def on_option_change_tipo(choice):
    tipo_eventos(choice)






def exibir_informacoes_clientes():

    janela_clientes = ctk.CTkToplevel(tela)
    janela_clientes.title("Clientes")
    janela_clientes.geometry("1360x800")

    conex = sqlite3.connect('Banco_de_Dados.db')
    cursor = conex.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    conex.close()
    checkboxes = []

    frame_clientes = ctk.CTkFrame(janela_clientes)
    frame_clientes.pack(padx=20, pady=20, fill="both", expand=True)
    headers = [" Pago "," ID ", " Tipo ", " Valor ", " Royalties ", " Comissão ", " Calção ", " Nome Locador ", " Nome Locatário ", " Data ", " Corretor 1 ", " Corretor 2 ", " Corretor 3"]
    
    for col, header in enumerate(headers):
        ctk.CTkLabel(frame_clientes, text=header, font=('Arial Bold', 12)).grid(row=0, column=col, padx=20, pady=20)

    for i, cliente in enumerate(clientes, start=1):

        check = ctk.IntVar()
        checkbox = ctk.CTkCheckBox(frame_clientes,text="",width=25,variable=check)
        checkbox.grid(row=i,column=0)
        checkboxes.append((check, (cliente[0], cliente[2])))

        for j, valor in enumerate(cliente,start=1):
            ctk.CTkLabel(frame_clientes, text=str(valor)).grid(row=i, column=j, padx=5, pady=5)

    def marcar_entrada():
        conex = sqlite3.connect('Banco_de_Dados.db')
        cursor = conex.cursor()
        
        for check, (id, valor) in checkboxes:
            if check.get() == 1: 

                arquivo = "saldo.json"
                with open(arquivo, 'r') as f:
                    dados = json.load(f)
                    saldo = dados.get('saldo', 0)
                
                entrada = valor
                novo_saldo = saldo + entrada
                
                cursor.execute("DELETE FROM Clientes WHERE id=?", (id,))
                with open(arquivo, 'w') as f:
                    json.dump({'saldo': novo_saldo}, f)

                    
        conex.commit()
        conex.close()

        janela_clientes.destroy()  # Fecha a janela de contas após salvar as alterações
        messagebox.showinfo("Sucesso", "Entradas recebidas com sucesso!")

    botao_receber = ctk.CTkButton(frame_clientes, text="Receber Pagamento", command=marcar_entrada)
    botao_receber.grid(row=i+1,column=2)







tela = ctk.CTk()
tela.title('Sistema Imobiliaria')
tela.geometry('1366x768')
ctk.set_appearance_mode("light")
    

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



label_corretores = ctk.CTkLabel(tela, text='Quantidade de corretores', font=('Arial Bold', 15))
label_corretores.place(x=230,y=270)
corretores_options = ["1 Corretor", "2 Corretores", "3 Corretores"]  
corretores_menu = ctk.CTkOptionMenu(
    master=tela, 
    values=corretores_options, 
    command=on_option_change_corretores,
    dropdown_font=("Arial", 12),  
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





botao_salvar = ctk.CTkButton(tela, text='Salvar', command=salvar_dados_clientes)
botao_salvar.place(x=230, y=450)

boto_saldo = ctk.CTkButton(tela,text='Mostrar saldo', command=lambda:solicitar_saldo(arquivo='saldo.json'))
boto_saldo.place(x=420,y=50)

botao_conta = ctk.CTkButton(tela,text="Adicionar Conta", command=criar_contas)
botao_conta.place(x=600,y=50)

botao_exibir_inf_contas = ctk.CTkButton(tela, text="Exibir Informações Contas", command=exibir_informacoes_contas)
botao_exibir_inf_contas.place(x=420,y=400)

botao_exibir_inf_clientes = ctk.CTkButton(tela, text="Exibir Informações Clientes", command=exibir_informacoes_clientes)
botao_exibir_inf_clientes.place(x=420,y=450)




tela.mainloop()


