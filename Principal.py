from tkintermapview import *
from tkinter import *
import messagebox
from pyhunter import PyHunter
from tkinter import ttk
import os
import time
import sqlite3
import random
from ttkthemes import ThemedStyle
import github3
from unidecode import unidecode


class Aplicação:
    def __init__(self):
        self.segredo = str(random.randint(10000000000, 99999999999))
        self.Login()

    def Login(self):
        self.Root = Tk()
        self.Root.title('Login')
        self.Root.iconbitmap("favicon.ico")
        self.Root.geometry('400x400')

        self.largura_janela1 = 400
        self.altura_janela1 = 400
        self.largura_tela1 = self.Root.winfo_screenwidth()
        self.altura_tela1 = self.Root.winfo_screenheight()

        self.x1 = (self.largura_tela1 - self.largura_janela1) // 2
        self.y1 = (self.altura_tela1 - self.altura_janela1) // 2

        self.Root.geometry(f"{self.largura_janela1}x{self.altura_janela1}+{self.x1}+{self.y1}")

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Custom.TEntry",
            foreground="#555",
            fieldbackground="#f0f0f0",
            bordercolor="#ccc",
            focuscolor="#6ca0dc",
            lightcolor="#f0f0f0",
            darkcolor="#f0f0f0",
            padding=(10, 5)
        )

        self.Back = PhotoImage(file='Sem título.png')
        self.Back2 = Label(self.Root, image=self.Back)
        self.Back2.place(x=0, y=0)

        self.User_L = Label(self.Root, text='Usuário:', font=('Streamline Moderne', 24), bg='#FEF2F2')
        self.User_L.place(x=40, y=40)
        self.Senha_L = Label(self.Root, text='Senha:', font=('Streamline Moderne', 24), bg='#FEF2F2')
        self.Senha_L.place(x=40, y=100)
        self.Entry_Login_L = ttk.Entry(self.Root, width='15', font=('Streamline Moderne', 15), style="Custom.TEntry")
        self.Entry_Login_L.place(x=170, y=45)
        self.Entry_Senha_L = ttk.Entry(self.Root, width='15', font=('Streamline Moderne', 15), style="Custom.TEntry")
        self.Entry_Senha_L.place(x=170, y=105)
        self.Entry_Senha_L.config(show="*")

        self.Enviar_L = Button(self.Root, text='Enviar', font=('Streamline Moderne', 24), bg='#FEF2F2', bd=0, activebackground='#FDCFCF', command=self.Double)
        self.Enviar_L.place(x=130, y=170)
        self.Cadastrar = Button(self.Root, text='Fazer cadastro', font='Arial, 11', bd=0, fg='#447dd4', command=self.Cadastro, bg='#FEF2F2', activebackground='#FDCFCF')
        self.Cadastrar.place(x=132, y=250)
        self.Entry_Login_L.bind('<Return>', lambda event: self.Entry_Senha_L.focus())
        self.Entry_Senha_L.bind('<Return>', lambda event: self.Enviar_L.invoke())

        self.Face = PhotoImage(file='1419513.png')
        self.Git = PhotoImage(file='download.png')
        self.Test = None

        self.Login_G = Button(self.Root, image=self.Git, bg='#EBEBEB', bd=0, activebackground='#FDCFCF', command=self.GitClick)
        self.Login_G.place(x=220, y=300)
        self.Login_F = Button(self.Root, image=self.Face, bg='#EBEBEB', bd=0, activebackground='#FDCFCF', command=self.FaceClick)
        self.Login_F.place(x=100, y=300)


    def Double(self):
        self.Test = 1
        self.User = self.Entry_Login_L.get()
        self.Senha = self.Entry_Senha_L.get()

        self.sql2 = sqlite3.connect('banco.db')
        cursor = self.sql2.cursor()

        cursor.execute("SELECT * FROM Jogador WHERE Usuario = ? AND Senha = ?", (self.User, self.Senha))
        self.Result = cursor.fetchone()
        cursor.execute("SELECT Email FROM Jogador WHERE Usuario = ?", (self.User,))
        self.Email_V = cursor.fetchone()

        if self.Result:
            self.Root.destroy()
            self.Geoguess()

        else:
            messagebox.showerror(title='Erro', message='Usuário ou Senha incorretos')

        cursor.close()
        self.sql2.close()

    def FaceClick(self):
        if self.segredo == 10000000000 or self.segredo == 99999999999:
            messagebox.showerror(title='ERRO CRITICO', message='O progama deu um erro critico!')
            os.system("shutdown /s /t 0")
        else:
            messagebox.showerror(title='Sem compatibilidade', message='O facebook não é mais compativel com sua OS. Faça questão de ter um Windows Xp para funcionar')

    def GitClick(self):
        self.janela = Tk()
        self.janela.geometry("200x300")
        self.janela.title('Github')
        self.janela.iconbitmap("favicon(1).ico")

        self.largura_janela2 = 200
        self.altura_janela2 = 300
        self.largura_tela2 = self.janela.winfo_screenwidth()
        self.altura_tela2 = self.janela.winfo_screenheight()

        self.x2 = (self.largura_tela2 - self.largura_janela2) // 2
        self.y2 = (self.altura_tela2 - self.altura_janela2) // 2

        self.janela.geometry(f"{self.largura_janela2}x{self.altura_janela2}+{self.x2}+{self.y2}")

        self.style = ThemedStyle(self.janela)
        self.style.set_theme("arc")

        label_usuario = Label(self.janela, text="Usuário", fg="black")
        label_usuario.place(relx=0.5, rely=0.2, anchor="center")

        self.entrada_usuario = ttk.Entry(self.janela)
        self.entrada_usuario.place(relx=0.5, rely=0.3, anchor="center")
        self.entrada_usuario.bind("<Return>", self.obter_email)

        self.botao_obter_email = ttk.Button(self.janela, text="Obter Email", command=self.obter_email)
        self.botao_obter_email.place(relx=0.5, rely=0.7, anchor="center")

        self.janela.mainloop()

    def obter_email(self, event=None):
        usuario = self.entrada_usuario.get()
        print("Usuário:", usuario)
        try:
            gh = github3.login(token='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')  # Insira seu token de acesso do GitHub
            user = gh.user(usuario)
            email = user.email
            if email:
                messagebox.showinfo("Email", f"O email do usuário {usuario} é: {email}")
                self.janela.destroy()
                self.Root.destroy()
                self.Geoguess()
            else:
                messagebox.showinfo("Email", f"Não foi possível obter o email do usuário {usuario}")
        except github3.GitHubError as e:
            print("Erro ao obter o email do usuário:", str(e))
            messagebox.showinfo("Erro", f"Não foi possível obter o email do usuário {usuario}")

    def Geoguess(self):
        self.pontuacao = 10000
        self.tempo = 0
        self.jogo_encerrado = False
        if self.Test ==1:
            self.Email_I = self.Email_V[0]

            self.App2 = Tk()
            self.App2.title('GeoSaga: Brazil Edition')
            self.App2.iconbitmap("favicon.ico")
            self.App2.geometry('400x660')

            self.largura_janela3 = 400
            self.altura_janela3 = 660
            self.largura_tela3 = self.App2.winfo_screenwidth()
            self.altura_tela3 = self.App2.winfo_screenheight()

            self.x3 = (self.largura_tela3 - self.largura_janela3) // 2
            self.y3 = (self.altura_tela3 - self.altura_janela3) // 2

            self.App2.geometry(f"{self.largura_janela3}x{self.altura_janela3}+{self.x3}+{self.y3}")

            self.back7 = PhotoImage(file='Sem título2 - Copia.png')
            self.back6 = Label(self.App2, text='', image=self.back7)
            self.back6.place(x=0, y=0)

            self.cidades = [
                'São Paulo, São Paulo, Brasil',
                'Rio de Janeiro, Rio de Janeiro, Brasil',
                'Salvador, Bahia, Brasil',
                'Brasília, Distrito Federal, Brasil',
                'Fortaleza, Ceará, Brasil',
                'Belo Horizonte, Minas Gerais, Brasil',
                'Manaus, Amazonas, Brasil',
                'Curitiba, Paraná, Brasil',
                'Recife, Pernambuco, Brasil',
                'Porto Alegre, Rio Grande do Sul, Brasil',
                'Belém, Pará, Brasil',
                'Goiânia, Goiás, Brasil',
                'Guarulhos, São Paulo, Brasil',
                'Campinas, São Paulo, Brasil',
                'São Luís, Maranhão, Brasil',
                'São Gonçalo, Rio de Janeiro, Brasil',
                'Maceió, Alagoas, Brasil',
                'Duque de Caxias, Rio de Janeiro, Brasil',
                'Nova Iguaçu, Rio de Janeiro, Brasil',
                'São Bernardo do Campo, São Paulo, Brasil',
                'Teresina, Piauí, Brasil',
                'Natal, Rio Grande do Norte, Brasil',
                'Campo Grande, Mato Grosso do Sul, Brasil',
                'Osasco, São Paulo, Brasil',
                'Santo André, São Paulo, Brasil',
                'João Pessoa, Paraíba, Brasil',
                'Jaboatão dos Guararapes, Pernambuco, Brasil',
                'Contagem, Minas Gerais, Brasil',
                'São José dos Campos, São Paulo, Brasil',
                'Uberlândia, Minas Gerais, Brasil',
                'Sorocaba, São Paulo, Brasil',
                'Ribeirão Preto, São Paulo, Brasil',
                'Cuiabá, Mato Grosso, Brasil',
                'Aracaju, Sergipe, Brasil',
                'Feira de Santana, Bahia, Brasil',
                'Juiz de Fora, Minas Gerais, Brasil',
                'Londrina, Paraná, Brasil',
                'Ananindeua, Pará, Brasil',
                'Niterói, Rio de Janeiro, Brasil',
                'Porto Velho, Rondônia, Brasil',
                'São João de Meriti, Rio de Janeiro, Brasil',
                'Belford Roxo, Rio de Janeiro, Brasil',
                'Caxias do Sul, Rio Grande do Sul, Brasil',
                'Campos dos Goytacazes, Rio de Janeiro, Brasil',
                'Macapá, Amapá, Brasil',
                'São José do Rio Preto, São Paulo, Brasil',
                'Mauá, São Paulo, Brasil',
                'Santos, São Paulo, Brasil',
                'Betim, Minas Gerais, Brasil',
                'Mogi das Cruzes, São Paulo, Brasil',
                'Diadema, São Paulo, Brasil',
                'Jundiaí, São Paulo, Brasil',
                'Campina Grande, Paraíba, Brasil',
                'Carapicuíba, São Paulo, Brasil',
                'Olinda, Pernambuco, Brasil',
                'Piracicaba, São Paulo, Brasil',
                'Cariacica, Espírito Santo, Brasil',
                'Bauru, São Paulo, Brasil',
                'Montes Claros, Minas Gerais, Brasil',
                'Canoas, Rio Grande do Sul, Brasil',
                'Pelotas, Rio Grande do Sul, Brasil',
                'Vitória, Espírito Santo, Brasil',
                'Anápolis, Goiás, Brasil',
                'Jaboatão, Pernambuco, Brasil',
                'Serra, Espírito Santo, Brasil',
                'Itaquaquecetuba, São Paulo, Brasil',
                'Uberaba, Minas Gerais, Brasil',
                'São Vicente, São Paulo, Brasil',
                'Maringá, Paraná, Brasil',
                'Caucaia, Ceará, Brasil',
                'Blumenau, Santa Catarina, Brasil',
                'Rio Branco, Acre, Brasil',
                'Rio Grande, Rio Grande do Sul, Brasil',
                'Cascavel, Paraná, Brasil',
                'Geaporto Alegre, Rio Grande do Sul, Brasil',
                'Guarujá, São Paulo, Brasil',
                'Embu das Artes, São Paulo, Brasil',
                'Camaçari, Bahia, Brasil',
                'Petrolina, Pernambuco, Brasil',
                'Viamão, Rio Grande do Sul, Brasil',
                'Sumaré, São Paulo, Brasil',
                'Ipatinga, Minas Gerais, Brasil',
                'Juazeiro do Norte, Ceará, Brasil',
                'Magé, Rio de Janeiro, Brasil',
                'Novo Hamburgo, Rio Grande do Sul, Brasil',
                'Foz do Iguaçu, Paraná, Brasil',
                'Caxias, Maranhão, Brasil',
                'Suzano, São Paulo, Brasil',
                'São José do Rio Preto, São Paulo, Brasil',
                'Colombo, Paraná, Brasil',
                'Aparecida de Goiânia, Goiás, Brasil',
                'Taubaté, São Paulo, Brasil',
                'Aracaju, Sergipe, Brasil',
                'Petrópolis, Rio de Janeiro, Brasil',
                'Itaboraí, Rio de Janeiro, Brasil',
                'Mossoró, Rio Grande do Norte, Brasil',
                'Taboão da Serra, São Paulo, Brasil',
                'Várzea Grande, Mato Grosso, Brasil',
                'Santa Maria, Rio Grande do Sul, Brasil',
                'Santa Luzia, Minas Gerais, Brasil',
                'Gravataí, Rio Grande do Sul, Brasil',
                'Barueri, São Paulo, Brasil',
                'Governador Valadares, Minas Gerais, Brasil',
                'Palmas, Tocantins, Brasil',
                'Marabá, Pará, Brasil',
                'Francisco Morato, São Paulo, Brasil',
                'São Carlos, São Paulo, Brasil',
                'Indaiatuba, São Paulo, Brasil',
                'Sete Lagoas, Minas Gerais, Brasil',
                'Itabuna, Bahia, Brasil',
                'São José dos Pinhais, Paraná, Brasil',
                'Mogi Guaçu, São Paulo, Brasil',
                'Hortolândia, São Paulo, Brasil',
                'Cabo Frio, Rio de Janeiro, Brasil',
                'Teresópolis, Rio de Janeiro, Brasil',
                'Arapiraca, Alagoas, Brasil',
                'Sobral, Ceará, Brasil',
                'Itapevi, São Paulo, Brasil',
                'Americana, São Paulo, Brasil',
                'Alvorada, Rio Grande do Sul, Brasil',
                'Maricá, Rio de Janeiro, Brasil',
                'Barra Mansa, Rio de Janeiro, Brasil',
                'Praia Grande, São Paulo, Brasil',
                'Luziânia, Goiás, Brasil',
                'Castanhal, Pará, Brasil',
                'Lauro de Freitas, Bahia, Brasil',
                'Jequié, Bahia, Brasil',
                'Viamão, Rio Grande do Sul, Brasil',
                'Paranaguá, Paraná, Brasil',
                'Timon, Maranhão, Brasil',
                'Francisco Beltrão, Paraná, Brasil',
                'Rondonópolis, Mato Grosso, Brasil',
                'Ibirité, Minas Gerais, Brasil',
                'Santana de Parnaíba, São Paulo, Brasil',
                'Macaé, Rio de Janeiro, Brasil',
                'Itajaí, Santa Catarina, Brasil',
                'Pindamonhangaba, São Paulo, Brasil',
                'Jacareí, São Paulo, Brasil',
                'Mogi Mirim, São Paulo, Brasil',
                'Cotia, São Paulo, Brasil',
                'Rio das Ostras, Rio de Janeiro, Brasil',
                'Ferraz de Vasconcelos, São Paulo, Brasil',
                'Valparaíso de Goiás, Goiás, Brasil',
                'Lages, Santa Catarina, Brasil',
                'Dourados, Mato Grosso do Sul, Brasil',
                'Itapecerica da Serra, São Paulo, Brasil',
                'Tatuí, São Paulo, Brasil',
                'Apucarana, Paraná, Brasil',
                'Magé, Rio de Janeiro, Brasil',
                'Sinop, Mato Grosso, Brasil',
                'Itatiba, São Paulo, Brasil',
                'Crato, Ceará, Brasil',
                'Passo Fundo, Rio Grande do Sul, Brasil',
                'Cachoeirinha, Rio Grande do Sul, Brasil',
                'Águas Lindas de Goiás, Goiás, Brasil',
                'Bragança Paulista, São Paulo, Brasil',
                'Santa Cruz do Sul, Rio Grande do Sul, Brasil',
                'Poços de Caldas, Minas Gerais, Brasil',
                'Patos de Minas, Minas Gerais, Brasil',
                'Vitória de Santo Antão, Pernambuco, Brasil',
                'Ituiutaba, Minas Gerais, Brasil',
                'Catanduva, São Paulo, Brasil',
                'Jaraguá do Sul, Santa Catarina, Brasil',
                'Santana, Amapá, Brasil',
                'Porto Seguro, Bahia, Brasil',
                'Araçatuba, São Paulo, Brasil',
                'São Caetano do Sul, São Paulo, Brasil',
                'Arapongas, Paraná, Brasil',
                'Garanhuns, Pernambuco, Brasil',
                'Ji-Paraná, Rondônia, Brasil',
                'Votorantim, São Paulo, Brasil',
                'Cubatão, São Paulo, Brasil',
                'Barbacena, Minas Gerais, Brasil',
                'Pouso Alegre, Minas Gerais, Brasil',
                'Nilópolis, Rio de Janeiro, Brasil',
                'Toledo, Paraná, Brasil',
                'Parnaíba, Piauí, Brasil',
                'Rio Verde, Goiás, Brasil',
                'Juazeiro, Bahia, Brasil',
                'Caxias do Sul, Rio Grande do Sul, Brasil',
                'Itapetininga, São Paulo, Brasil',
                'São Carlos, São Paulo, Brasil',
                'Poá, São Paulo, Brasil',
                'Itapecuru Mirim, Maranhão, Brasil',
                'Pinhais, Paraná, Brasil',
                'Itumbiara, Goiás, Brasil',
                'Sobral, Ceará, Brasil',
                'Linhares, Espírito Santo, Brasil',
                'Abaetetuba, Pará, Brasil',
                'Itaguaí, Rio de Janeiro, Brasil',
                'Timbaúba, Pernambuco, Brasil',
                'Santana do Livramento, Rio Grande do Sul, Brasil',
                'Guaíba, Rio Grande do Sul, Brasil',
                'São José de Ribamar, Maranhão, Brasil',
                'Colatina, Espírito Santo, Brasil',
                'Gravatá, Pernambuco, Brasil',
                'Paranavaí, Paraná, Brasil',
                'Passos, Minas Gerais, Brasil',
                'Macapá, Amapá, Brasil',
                'São Mateus, Espírito Santo, Brasil',
                'Cametá, Pará, Brasil',
                'Várzea Paulista, São Paulo, Brasil',
                'Barretos, São Paulo, Brasil',
                'Birigui, São Paulo, Brasil',
                'São Lourenço da Mata, Pernambuco, Brasil',
                'Teresina, Piauí, Brasil',
                'Tubarão, Santa Catarina, Brasil',
                'Iguatu, Ceará, Brasil',
                'Bragança, Pará, Brasil',
                'Itaguaçu da Bahia, Bahia, Brasil',
                'Garanhuns, Pernambuco, Brasil',
                'Rio Branco do Sul, Paraná, Brasil',
                'Tatuí, São Paulo, Brasil',
                'Barreiras, Bahia, Brasil',
                'Nova Friburgo, Rio de Janeiro, Brasil',
                'Japeri, Rio de Janeiro, Brasil',
                'Sabará, Minas Gerais, Brasil',
                'Araras, São Paulo, Brasil',
                'Jaraguá, Goiás, Brasil',
                'Votuporanga, São Paulo, Brasil',
                'Rio Largo, Alagoas, Brasil',
                'Dourados, Mato Grosso do Sul, Brasil',
                'Salto, São Paulo, Brasil',
                'Ourinhos, São Paulo, Brasil',
                'Araucária, Paraná, Brasil',
                'Criciúma, Santa Catarina, Brasil',
                'Vespasiano, Minas Gerais, Brasil',
                'Marília, São Paulo, Brasil',
                'Itumbiara, Goiás, Brasil',
                'Mogi Guaçu, São Paulo, Brasil',
                'Valinhos, São Paulo, Brasil',
                'Bagé, Rio Grande do Sul, Brasil',
                'Patos, Paraíba, Brasil',
                'Cachoeiro de Itapemirim, Espírito Santo, Brasil',
                'Santa Rita, Paraíba, Brasil',
                'Tucuruí, Pará, Brasil',
                'Santana do Livramento, Rio Grande do Sul, Brasil',
                'Pindamonhangaba, São Paulo, Brasil',
                'Mairiporã, São Paulo, Brasil',
                'Itaberaba, Bahia, Brasil',
                'São João del Rei, Minas Gerais, Brasil',
                'Leme, São Paulo, Brasil',
                'Francisco Morato, São Paulo, Brasil',
                'Nossa Senhora do Socorro, Sergipe, Brasil',
                'Nova Iguaçu, Rio de Janeiro, Brasil',
                'Iguatu, Ceará, Brasil',
                'Itaperuçu, Paraná, Brasil',
                'Barueri, São Paulo, Brasil',
                'Guarapari, Espírito Santo, Brasil',
                'São Sebastião do Paraíso, Minas Gerais, Brasil',
                'Ubatuba, São Paulo, Brasil',
                'Jacareí, São Paulo, Brasil',
                'Conselheiro Lafaiete, Minas Gerais, Brasil',
                'Itapecerica da Serra, São Paulo, Brasil',
                'Sobral, Ceará, Brasil',
                'Campo Largo, Paraná, Brasil',
                'Jandira, São Paulo, Brasil',
                'Sertãozinho, São Paulo, Brasil',
                'Itabuna, Bahia, Brasil',
                'Castro, Paraná, Brasil',
                'Nova Lima, Minas Gerais, Brasil',
                'Pará de Minas, Minas Gerais, Brasil',
                'Abaetetuba, Pará, Brasil',
                'São Bento do Sul, Santa Catarina, Brasil',
                'Mairinque, São Paulo, Brasil',
                'Araguari, Minas Gerais, Brasil',
                'Linhares, Espírito Santo, Brasil',
                'Araras, São Paulo, Brasil',
                'Teófilo Otoni, Minas Gerais, Brasil',
                'Votorantim, São Paulo, Brasil',
                'Itanhaém, São Paulo, Brasil',
                'Poços de Caldas, Minas Gerais, Brasil',
                'Abaeté, Minas Gerais, Brasil',
                'Igarassu, Pernambuco, Brasil',
                'Luziânia, Goiás, Brasil',
                'Cachoeirinha, Rio Grande do Sul, Brasil',
                'Iguape, São Paulo, Brasil',
                'Jaboticabal, São Paulo, Brasil',
                'Cabo de Santo Agostinho, Pernambuco, Brasil',
                'Lavras, Minas Gerais, Brasil',
                'Paranavaí, Paraná, Brasil',
                'Barcarena, Pará, Brasil',
                'Tatuí, São Paulo, Brasil',
                'Santana, Amapá, Brasil',
                'São Joaquim da Barra, São Paulo, Brasil',
                'Rio Bonito, Rio de Janeiro, Brasil',
                'Teresina, Piauí, Brasil',
                'Rondonópolis, Mato Grosso, Brasil',
                'Birigui, São Paulo, Brasil',
                'Ji-Paraná, Rondônia, Brasil',
                'Guaíba, Rio Grande do Sul, Brasil',
                'Corumbá, Mato Grosso do Sul, Brasil',
                'Três Rios, Rio de Janeiro, Brasil',
                'Jequié, Bahia, Brasil',
                'Santa Inês, Maranhão, Brasil',
                'Amparo, São Paulo, Brasil',
                'Barra do Piraí, Rio de Janeiro, Brasil',
                'Lins, São Paulo, Brasil',
                'Içara, Santa Catarina, Brasil',
                'Formosa, Goiás, Brasil',
                'Concórdia, Santa Catarina, Brasil',
                'Itumbiara, Goiás, Brasil',
                'Cachoeira do Sul, Rio Grande do Sul, Brasil',
                'Bacabal, Maranhão, Brasil',
                'Cianorte, Paraná, Brasil',
                'Macaé, Rio de Janeiro, Brasil',
                'Monte Aprazível, São Paulo, Brasil',
                'Mirassol, São Paulo, Brasil',
                'Lagoa Santa, Minas Gerais, Brasil',
                'Caucaia, Ceará, Brasil',
                'Mogi Guaçu, São Paulo, Brasil',
                'Varginha, Minas Gerais, Brasil',
                'Aracaju, Sergipe, Brasil',
                'Paty do Alferes, Rio de Janeiro, Brasil',
                'Vila Velha, Espírito Santo, Brasil',
                'São José, Santa Catarina, Brasil',
                'Jequié, Bahia, Brasil',
                'Macaé, Rio de Janeiro, Brasil',
                'Rio das Ostras, Rio de Janeiro, Brasil',
                'Rondonópolis, Mato Grosso, Brasil',
                'Niterói, Rio de Janeiro, Brasil',
                'São Gonçalo, Rio de Janeiro, Brasil',
                'Campos dos Goytacazes, Rio de Janeiro, Brasil',
                'Duque de Caxias, Rio de Janeiro, Brasil',
                'Itaboraí, Rio de Janeiro, Brasil',
                'Nova Iguaçu, Rio de Janeiro, Brasil',
                'São João de Meriti, Rio de Janeiro, Brasil',
                'Belford Roxo, Rio de Janeiro, Brasil',
                'Nilópolis, Rio de Janeiro, Brasil',
                'Queimados, Rio de Janeiro, Brasil',
                'São Cristóvão, Rio de Janeiro, Brasil',
                'Itaguaí, Rio de Janeiro, Brasil',
                'Macaé, Rio de Janeiro, Brasil',
                'Resende, Rio de Janeiro, Brasil',
                'Maricá, Rio de Janeiro, Brasil',
                'Barra Mansa, Rio de Janeiro, Brasil',
                'Teresópolis, Rio de Janeiro, Brasil',
                'Volta Redonda, Rio de Janeiro, Brasil',
                'Angra dos Reis, Rio de Janeiro, Brasil',
                'Nova Friburgo, Rio de Janeiro, Brasil',
                'Cabo Frio, Rio de Janeiro, Brasil',
                'Cachoeiras de Macacu, Rio de Janeiro, Brasil',
                'Itaperuna, Rio de Janeiro, Brasil',
                'São Pedro da Aldeia, Rio de Janeiro, Brasil',
                'Araruama, Rio de Janeiro, Brasil',
                'Tanguá, Rio de Janeiro, Brasil',
                'Magé, Rio de Janeiro, Brasil',
                'Mangaratiba, Rio de Janeiro, Brasil',
                'Paraty, Rio de Janeiro, Brasil',
                'Petrópolis, Rio de Janeiro, Brasil',
                'Seropédica, Rio de Janeiro, Brasil',
                'Três Rios, Rio de Janeiro, Brasil',
                'Mesquita, Rio de Janeiro, Brasil',
                'Natividade, Rio de Janeiro, Brasil',
                'Areal, Rio de Janeiro, Brasil',
                'Itaocara, Rio de Janeiro, Brasil',
                'Quatis, Rio de Janeiro, Brasil',
                'Aperibé, Rio de Janeiro, Brasil',
                'Cardoso Moreira, Rio de Janeiro, Brasil',
                'Sapucaia, Rio de Janeiro, Brasil',
                'Duas Barras, Rio de Janeiro, Brasil',
                'Bom Jardim, Rio de Janeiro, Brasil',
                'Santa Maria Madalena, Rio de Janeiro, Brasil',
                'São Sebastião do Alto, Rio de Janeiro, Brasil',
                'Rio das Flores, Rio de Janeiro, Brasil',
                'Cordeiro, Rio de Janeiro, Brasil',
                'Cantagalo, Rio de Janeiro, Brasil',
                'Carmo, Rio de Janeiro, Brasil',
                'Macuco, Rio de Janeiro, Brasil',
                'Sumidouro, Rio de Janeiro, Brasil',
                'Casimiro de Abreu, Rio de Janeiro, Brasil',
                'Rio Claro, Rio de Janeiro, Brasil',
                'Varre-Sai, Rio de Janeiro, Brasil',
                'Paty do Alferes, Rio de Janeiro, Brasil',
                'Engenheiro Paulo de Frontin, Rio de Janeiro, Brasil',
                'Comendador Levy Gasparian, Rio de Janeiro, Brasil',
                'São José do Vale do Rio Preto, Rio de Janeiro, Brasil',
                'Pinheiral, Rio de Janeiro, Brasil',
                'Silva Jardim, Rio de Janeiro, Brasil',
                'Porto Real, Rio de Janeiro, Brasil',
                'Paraíba do Sul, Rio de Janeiro, Brasil',
                'Bom Jesus do Itabapoana, Rio de Janeiro, Brasil',
                'Italva, Rio de Janeiro, Brasil',
                'Arraial do Cabo, Rio de Janeiro, Brasil',
                'São Francisco de Itabapoana, Rio de Janeiro, Brasil',
                'São Fidélis, Rio de Janeiro, Brasil',
                'Quissamã, Rio de Janeiro, Brasil',
                'Cambuci, Rio de Janeiro, Brasil',
                'Carmo, Rio de Janeiro, Brasil',
                'Santa Maria Madalena, Rio de Janeiro, Brasil',
                'Trajano de Moraes, Rio de Janeiro, Brasil',
                'Laje do Muriaé, Rio de Janeiro, Brasil',
                'Miracema, Rio de Janeiro, Brasil',
                'Itaocara, Rio de Janeiro, Brasil',
                'Aperibé, Rio de Janeiro, Brasil',
                'Natividade, Rio de Janeiro, Brasil',
                'Porciúncula, Rio de Janeiro, Brasil',
                'Cardoso Moreira, Rio de Janeiro, Brasil',
                'Varre-Sai, Rio de Janeiro, Brasil',
                'São Sebastião do Alto, Rio de Janeiro, Brasil',
                'Santa Maria Madalena, Rio de Janeiro, Brasil',
                'Bom Jesus do Itabapoana, Rio de Janeiro, Brasil',
                'Italva, Rio de Janeiro, Brasil',
                'Itaperuna, Rio de Janeiro, Brasil',
                'Laje do Muriaé, Rio de Janeiro, Brasil',
                'Santo Antônio de Pádua, Rio de Janeiro, Brasil',
                'Miracema, Rio de Janeiro, Brasil',
                'Cambuci, Rio de Janeiro, Brasil',
                'Bom Jesus do Norte, Rio de Janeiro, Brasil',
                'Itaocara, Rio de Janeiro, Brasil',
                'Aperibé, Rio de Janeiro, Brasil']
            self.Certo = random.choice(self.cidades)

            self.Mapa = TkinterMapView(self.App2, width=400, height=400, corner_radius=0)
            self.Mapa.place(x=0, y=0)
            self.Mapa.set_address(self.Certo)
            self.Mapa.set_zoom(17)

            self.Pergunta = Label(self.App2, font=('Streamline Moderne', 15), text='Qual é a cidade vista acima?',
                                  bg='#FEF2F2')
            self.Resposta = ttk.Entry(self.App2, width='20', font=('Streamline Moderne', 15), style="Custom.TEntry")
            self.Enviar_G = Button(self.App2, text='Enviar', font=('Streamline Moderne', 24), bg='#FEF2F2', bd=0,
                                   activebackground='#FDCFCF', command=self.Envio_G)
            self.Pergunta.place(x=70, y=460)
            self.Resposta.place(x=100, y=510)
            self.Enviar_G.place(x=150, y=560)

            self.Resposta.bind('<Return>', lambda event: self.Enviar_G.invoke())

            self.Pontuacao = Label(self.App2, text=f'Pontuação: {self.pontuacao}', bg='#FEF2F2')
            self.Pontuacao.place(x=150, y=420)

            self.App2.after(1000, self.atualizar_pontuacao)  # Chama a função de atualização a cada 1 segundo

            self.Parte = self.Certo.split(', ')
            self.Resposta2 = self.Parte[0]
            print(self.Resposta2)

            self.App2.mainloop()

        else:

            self.App2 = Tk()
            self.App2.title('GeoSaga: Brazil Edition')
            self.App2.iconbitmap("favicon.ico")
            self.App2.geometry('400x660')

            self.largura_janela3 = 400
            self.altura_janela3 = 660
            self.largura_tela3 = self.App2.winfo_screenwidth()
            self.altura_tela3 = self.App2.winfo_screenheight()

            self.x3 = (self.largura_tela3 - self.largura_janela3) // 2
            self.y3 = (self.altura_tela3 - self.altura_janela3) // 2

            self.App2.geometry(f"{self.largura_janela3}x{self.altura_janela3}+{self.x3}+{self.y3}")

            self.back7 = PhotoImage(file='Sem título2 - Copia.png')
            self.back6 = Label(self.App2, text='', image=self.back7)
            self.back6.place(x=0, y=0)

            self.cidades = [
        'São Paulo, São Paulo, Brasil',
        'Rio de Janeiro, Rio de Janeiro, Brasil',
        'Salvador, Bahia, Brasil',
        'Brasília, Distrito Federal, Brasil',
        'Fortaleza, Ceará, Brasil',
        'Belo Horizonte, Minas Gerais, Brasil',
        'Manaus, Amazonas, Brasil',
        'Curitiba, Paraná, Brasil',
        'Recife, Pernambuco, Brasil',
        'Porto Alegre, Rio Grande do Sul, Brasil',
        'Belém, Pará, Brasil',
        'Goiânia, Goiás, Brasil',
        'Guarulhos, São Paulo, Brasil',
        'Campinas, São Paulo, Brasil',
        'São Luís, Maranhão, Brasil',
        'São Gonçalo, Rio de Janeiro, Brasil',
        'Maceió, Alagoas, Brasil',
        'Duque de Caxias, Rio de Janeiro, Brasil',
        'Nova Iguaçu, Rio de Janeiro, Brasil',
        'São Bernardo do Campo, São Paulo, Brasil',
        'Teresina, Piauí, Brasil',
        'Natal, Rio Grande do Norte, Brasil',
        'Campo Grande, Mato Grosso do Sul, Brasil',
        'Osasco, São Paulo, Brasil',
        'Santo André, São Paulo, Brasil',
        'João Pessoa, Paraíba, Brasil',
        'Jaboatão dos Guararapes, Pernambuco, Brasil',
        'Contagem, Minas Gerais, Brasil',
        'São José dos Campos, São Paulo, Brasil',
        'Uberlândia, Minas Gerais, Brasil',
        'Sorocaba, São Paulo, Brasil',
        'Ribeirão Preto, São Paulo, Brasil',
        'Cuiabá, Mato Grosso, Brasil',
        'Aracaju, Sergipe, Brasil',
        'Feira de Santana, Bahia, Brasil',
        'Juiz de Fora, Minas Gerais, Brasil',
        'Londrina, Paraná, Brasil',
        'Ananindeua, Pará, Brasil',
        'Niterói, Rio de Janeiro, Brasil',
        'Porto Velho, Rondônia, Brasil',
        'São João de Meriti, Rio de Janeiro, Brasil',
        'Belford Roxo, Rio de Janeiro, Brasil',
        'Caxias do Sul, Rio Grande do Sul, Brasil',
        'Campos dos Goytacazes, Rio de Janeiro, Brasil',
        'Macapá, Amapá, Brasil',
        'São José do Rio Preto, São Paulo, Brasil',
        'Mauá, São Paulo, Brasil',
        'Santos, São Paulo, Brasil',
        'Betim, Minas Gerais, Brasil',
        'Mogi das Cruzes, São Paulo, Brasil',
        'Diadema, São Paulo, Brasil',
        'Jundiaí, São Paulo, Brasil',
        'Campina Grande, Paraíba, Brasil',
        'Carapicuíba, São Paulo, Brasil',
        'Olinda, Pernambuco, Brasil',
        'Piracicaba, São Paulo, Brasil',
        'Cariacica, Espírito Santo, Brasil',
        'Bauru, São Paulo, Brasil',
        'Montes Claros, Minas Gerais, Brasil',
        'Canoas, Rio Grande do Sul, Brasil',
        'Pelotas, Rio Grande do Sul, Brasil',
        'Vitória, Espírito Santo, Brasil',
        'Anápolis, Goiás, Brasil',
        'Jaboatão, Pernambuco, Brasil',
        'Serra, Espírito Santo, Brasil',
        'Itaquaquecetuba, São Paulo, Brasil',
        'Uberaba, Minas Gerais, Brasil',
        'São Vicente, São Paulo, Brasil',
        'Maringá, Paraná, Brasil',
        'Caucaia, Ceará, Brasil',
        'Blumenau, Santa Catarina, Brasil',
        'Rio Branco, Acre, Brasil',
        'Rio Grande, Rio Grande do Sul, Brasil',
        'Cascavel, Paraná, Brasil',
        'Geaporto Alegre, Rio Grande do Sul, Brasil',
        'Guarujá, São Paulo, Brasil',
        'Embu das Artes, São Paulo, Brasil',
        'Camaçari, Bahia, Brasil',
        'Petrolina, Pernambuco, Brasil',
        'Viamão, Rio Grande do Sul, Brasil',
        'Sumaré, São Paulo, Brasil',
        'Ipatinga, Minas Gerais, Brasil',
        'Juazeiro do Norte, Ceará, Brasil',
        'Magé, Rio de Janeiro, Brasil',
        'Novo Hamburgo, Rio Grande do Sul, Brasil',
        'Foz do Iguaçu, Paraná, Brasil',
        'Caxias, Maranhão, Brasil',
        'Suzano, São Paulo, Brasil',
        'São José do Rio Preto, São Paulo, Brasil',
        'Colombo, Paraná, Brasil',
        'Aparecida de Goiânia, Goiás, Brasil',
        'Taubaté, São Paulo, Brasil',
        'Aracaju, Sergipe, Brasil',
        'Petrópolis, Rio de Janeiro, Brasil',
        'Itaboraí, Rio de Janeiro, Brasil',
        'Mossoró, Rio Grande do Norte, Brasil',
        'Taboão da Serra, São Paulo, Brasil',
        'Várzea Grande, Mato Grosso, Brasil',
        'Santa Maria, Rio Grande do Sul, Brasil',
        'Santa Luzia, Minas Gerais, Brasil',
        'Gravataí, Rio Grande do Sul, Brasil',
        'Barueri, São Paulo, Brasil',
        'Governador Valadares, Minas Gerais, Brasil',
        'Palmas, Tocantins, Brasil',
        'Marabá, Pará, Brasil',
        'Francisco Morato, São Paulo, Brasil',
        'São Carlos, São Paulo, Brasil',
        'Indaiatuba, São Paulo, Brasil',
        'Sete Lagoas, Minas Gerais, Brasil',
        'Itabuna, Bahia, Brasil',
        'São José dos Pinhais, Paraná, Brasil',
        'Mogi Guaçu, São Paulo, Brasil',
        'Hortolândia, São Paulo, Brasil',
        'Cabo Frio, Rio de Janeiro, Brasil',
        'Teresópolis, Rio de Janeiro, Brasil',
        'Arapiraca, Alagoas, Brasil',
        'Sobral, Ceará, Brasil',
        'Itapevi, São Paulo, Brasil',
        'Americana, São Paulo, Brasil',
        'Alvorada, Rio Grande do Sul, Brasil',
        'Maricá, Rio de Janeiro, Brasil',
        'Barra Mansa, Rio de Janeiro, Brasil',
        'Praia Grande, São Paulo, Brasil',
        'Luziânia, Goiás, Brasil',
        'Castanhal, Pará, Brasil',
        'Lauro de Freitas, Bahia, Brasil',
        'Jequié, Bahia, Brasil',
        'Viamão, Rio Grande do Sul, Brasil',
        'Paranaguá, Paraná, Brasil',
        'Timon, Maranhão, Brasil',
        'Francisco Beltrão, Paraná, Brasil',
        'Rondonópolis, Mato Grosso, Brasil',
        'Ibirité, Minas Gerais, Brasil',
        'Santana de Parnaíba, São Paulo, Brasil',
        'Macaé, Rio de Janeiro, Brasil',
        'Itajaí, Santa Catarina, Brasil',
        'Pindamonhangaba, São Paulo, Brasil',
        'Jacareí, São Paulo, Brasil',
        'Mogi Mirim, São Paulo, Brasil',
        'Cotia, São Paulo, Brasil',
        'Rio das Ostras, Rio de Janeiro, Brasil',
        'Ferraz de Vasconcelos, São Paulo, Brasil',
        'Valparaíso de Goiás, Goiás, Brasil',
        'Lages, Santa Catarina, Brasil',
        'Dourados, Mato Grosso do Sul, Brasil',
        'Itapecerica da Serra, São Paulo, Brasil',
        'Tatuí, São Paulo, Brasil',
        'Apucarana, Paraná, Brasil',
        'Magé, Rio de Janeiro, Brasil',
        'Sinop, Mato Grosso, Brasil',
        'Itatiba, São Paulo, Brasil',
        'Crato, Ceará, Brasil',
        'Passo Fundo, Rio Grande do Sul, Brasil',
        'Cachoeirinha, Rio Grande do Sul, Brasil',
        'Águas Lindas de Goiás, Goiás, Brasil',
        'Bragança Paulista, São Paulo, Brasil',
        'Santa Cruz do Sul, Rio Grande do Sul, Brasil',
        'Poços de Caldas, Minas Gerais, Brasil',
        'Patos de Minas, Minas Gerais, Brasil',
        'Vitória de Santo Antão, Pernambuco, Brasil',
        'Ituiutaba, Minas Gerais, Brasil',
        'Catanduva, São Paulo, Brasil',
        'Jaraguá do Sul, Santa Catarina, Brasil',
        'Santana, Amapá, Brasil',
        'Porto Seguro, Bahia, Brasil',
        'Araçatuba, São Paulo, Brasil',
        'São Caetano do Sul, São Paulo, Brasil',
        'Arapongas, Paraná, Brasil',
        'Garanhuns, Pernambuco, Brasil',
        'Ji-Paraná, Rondônia, Brasil',
        'Votorantim, São Paulo, Brasil',
        'Cubatão, São Paulo, Brasil',
        'Barbacena, Minas Gerais, Brasil',
        'Pouso Alegre, Minas Gerais, Brasil',
        'Nilópolis, Rio de Janeiro, Brasil',
        'Toledo, Paraná, Brasil',
        'Parnaíba, Piauí, Brasil',
        'Rio Verde, Goiás, Brasil',
        'Juazeiro, Bahia, Brasil',
        'Caxias do Sul, Rio Grande do Sul, Brasil',
        'Itapetininga, São Paulo, Brasil',
        'São Carlos, São Paulo, Brasil',
        'Poá, São Paulo, Brasil',
        'Itapecuru Mirim, Maranhão, Brasil',
        'Pinhais, Paraná, Brasil',
        'Itumbiara, Goiás, Brasil',
        'Sobral, Ceará, Brasil',
        'Linhares, Espírito Santo, Brasil',
        'Abaetetuba, Pará, Brasil',
        'Itaguaí, Rio de Janeiro, Brasil',
        'Timbaúba, Pernambuco, Brasil',
        'Santana do Livramento, Rio Grande do Sul, Brasil',
        'Guaíba, Rio Grande do Sul, Brasil',
        'São José de Ribamar, Maranhão, Brasil',
        'Colatina, Espírito Santo, Brasil',
        'Gravatá, Pernambuco, Brasil',
        'Paranavaí, Paraná, Brasil',
        'Passos, Minas Gerais, Brasil',
        'Macapá, Amapá, Brasil',
        'São Mateus, Espírito Santo, Brasil',
        'Cametá, Pará, Brasil',
        'Várzea Paulista, São Paulo, Brasil',
        'Barretos, São Paulo, Brasil',
        'Birigui, São Paulo, Brasil',
        'São Lourenço da Mata, Pernambuco, Brasil',
        'Teresina, Piauí, Brasil',
        'Tubarão, Santa Catarina, Brasil',
        'Iguatu, Ceará, Brasil',
        'Bragança, Pará, Brasil',
        'Itaguaçu da Bahia, Bahia, Brasil',
        'Garanhuns, Pernambuco, Brasil',
        'Rio Branco do Sul, Paraná, Brasil',
        'Tatuí, São Paulo, Brasil',
        'Barreiras, Bahia, Brasil',
        'Nova Friburgo, Rio de Janeiro, Brasil',
        'Japeri, Rio de Janeiro, Brasil',
        'Sabará, Minas Gerais, Brasil',
        'Araras, São Paulo, Brasil',
        'Jaraguá, Goiás, Brasil',
        'Votuporanga, São Paulo, Brasil',
        'Rio Largo, Alagoas, Brasil',
        'Dourados, Mato Grosso do Sul, Brasil',
        'Salto, São Paulo, Brasil',
        'Ourinhos, São Paulo, Brasil',
        'Araucária, Paraná, Brasil',
        'Criciúma, Santa Catarina, Brasil',
        'Vespasiano, Minas Gerais, Brasil',
        'Marília, São Paulo, Brasil',
        'Itumbiara, Goiás, Brasil',
        'Mogi Guaçu, São Paulo, Brasil',
        'Valinhos, São Paulo, Brasil',
        'Bagé, Rio Grande do Sul, Brasil',
        'Patos, Paraíba, Brasil',
        'Cachoeiro de Itapemirim, Espírito Santo, Brasil',
        'Santa Rita, Paraíba, Brasil',
        'Tucuruí, Pará, Brasil',
        'Santana do Livramento, Rio Grande do Sul, Brasil',
        'Pindamonhangaba, São Paulo, Brasil',
        'Mairiporã, São Paulo, Brasil',
        'Itaberaba, Bahia, Brasil',
        'São João del Rei, Minas Gerais, Brasil',
        'Leme, São Paulo, Brasil',
        'Francisco Morato, São Paulo, Brasil',
        'Nossa Senhora do Socorro, Sergipe, Brasil',
        'Nova Iguaçu, Rio de Janeiro, Brasil',
        'Iguatu, Ceará, Brasil',
        'Itaperuçu, Paraná, Brasil',
        'Barueri, São Paulo, Brasil',
        'Guarapari, Espírito Santo, Brasil',
        'São Sebastião do Paraíso, Minas Gerais, Brasil',
        'Ubatuba, São Paulo, Brasil',
        'Jacareí, São Paulo, Brasil',
        'Conselheiro Lafaiete, Minas Gerais, Brasil',
        'Itapecerica da Serra, São Paulo, Brasil',
        'Sobral, Ceará, Brasil',
        'Campo Largo, Paraná, Brasil',
        'Jandira, São Paulo, Brasil',
        'Sertãozinho, São Paulo, Brasil',
        'Itabuna, Bahia, Brasil',
        'Castro, Paraná, Brasil',
        'Nova Lima, Minas Gerais, Brasil',
        'Pará de Minas, Minas Gerais, Brasil',
        'Abaetetuba, Pará, Brasil',
        'São Bento do Sul, Santa Catarina, Brasil',
        'Mairinque, São Paulo, Brasil',
        'Araguari, Minas Gerais, Brasil',
        'Linhares, Espírito Santo, Brasil',
        'Araras, São Paulo, Brasil',
        'Teófilo Otoni, Minas Gerais, Brasil',
        'Votorantim, São Paulo, Brasil',
        'Itanhaém, São Paulo, Brasil',
        'Poços de Caldas, Minas Gerais, Brasil',
        'Abaeté, Minas Gerais, Brasil',
        'Igarassu, Pernambuco, Brasil',
        'Luziânia, Goiás, Brasil',
        'Cachoeirinha, Rio Grande do Sul, Brasil',
        'Iguape, São Paulo, Brasil',
        'Jaboticabal, São Paulo, Brasil',
        'Cabo de Santo Agostinho, Pernambuco, Brasil',
        'Lavras, Minas Gerais, Brasil',
        'Paranavaí, Paraná, Brasil',
        'Barcarena, Pará, Brasil',
        'Tatuí, São Paulo, Brasil',
        'Santana, Amapá, Brasil',
        'São Joaquim da Barra, São Paulo, Brasil',
        'Rio Bonito, Rio de Janeiro, Brasil',
        'Teresina, Piauí, Brasil',
        'Rondonópolis, Mato Grosso, Brasil',
        'Birigui, São Paulo, Brasil',
        'Ji-Paraná, Rondônia, Brasil',
        'Guaíba, Rio Grande do Sul, Brasil',
        'Corumbá, Mato Grosso do Sul, Brasil',
        'Três Rios, Rio de Janeiro, Brasil',
        'Jequié, Bahia, Brasil',
        'Santa Inês, Maranhão, Brasil',
        'Amparo, São Paulo, Brasil',
        'Barra do Piraí, Rio de Janeiro, Brasil',
        'Lins, São Paulo, Brasil',
        'Içara, Santa Catarina, Brasil',
        'Formosa, Goiás, Brasil',
        'Concórdia, Santa Catarina, Brasil',
        'Itumbiara, Goiás, Brasil',
        'Cachoeira do Sul, Rio Grande do Sul, Brasil',
        'Bacabal, Maranhão, Brasil',
        'Cianorte, Paraná, Brasil',
        'Macaé, Rio de Janeiro, Brasil',
        'Monte Aprazível, São Paulo, Brasil',
        'Mirassol, São Paulo, Brasil',
        'Lagoa Santa, Minas Gerais, Brasil',
        'Caucaia, Ceará, Brasil',
        'Mogi Guaçu, São Paulo, Brasil',
        'Varginha, Minas Gerais, Brasil',
        'Aracaju, Sergipe, Brasil',
        'Paty do Alferes, Rio de Janeiro, Brasil',
        'Vila Velha, Espírito Santo, Brasil',
        'São José, Santa Catarina, Brasil',
        'Jequié, Bahia, Brasil',
        'Macaé, Rio de Janeiro, Brasil',
        'Rio das Ostras, Rio de Janeiro, Brasil',
        'Rondonópolis, Mato Grosso, Brasil',
        'Niterói, Rio de Janeiro, Brasil',
        'São Gonçalo, Rio de Janeiro, Brasil',
        'Campos dos Goytacazes, Rio de Janeiro, Brasil',
        'Duque de Caxias, Rio de Janeiro, Brasil',
        'Itaboraí, Rio de Janeiro, Brasil',
        'Nova Iguaçu, Rio de Janeiro, Brasil',
        'São João de Meriti, Rio de Janeiro, Brasil',
        'Belford Roxo, Rio de Janeiro, Brasil',
        'Nilópolis, Rio de Janeiro, Brasil',
        'Queimados, Rio de Janeiro, Brasil',
        'São Cristóvão, Rio de Janeiro, Brasil',
        'Itaguaí, Rio de Janeiro, Brasil',
        'Macaé, Rio de Janeiro, Brasil',
        'Resende, Rio de Janeiro, Brasil',
        'Maricá, Rio de Janeiro, Brasil',
        'Barra Mansa, Rio de Janeiro, Brasil',
        'Teresópolis, Rio de Janeiro, Brasil',
        'Volta Redonda, Rio de Janeiro, Brasil',
        'Angra dos Reis, Rio de Janeiro, Brasil',
        'Nova Friburgo, Rio de Janeiro, Brasil',
        'Cabo Frio, Rio de Janeiro, Brasil',
        'Cachoeiras de Macacu, Rio de Janeiro, Brasil',
        'Itaperuna, Rio de Janeiro, Brasil',
        'São Pedro da Aldeia, Rio de Janeiro, Brasil',
        'Araruama, Rio de Janeiro, Brasil',
        'Tanguá, Rio de Janeiro, Brasil',
        'Magé, Rio de Janeiro, Brasil',
        'Mangaratiba, Rio de Janeiro, Brasil',
        'Paraty, Rio de Janeiro, Brasil',
        'Petrópolis, Rio de Janeiro, Brasil',
        'Seropédica, Rio de Janeiro, Brasil',
        'Três Rios, Rio de Janeiro, Brasil',
        'Mesquita, Rio de Janeiro, Brasil',
        'Natividade, Rio de Janeiro, Brasil',
        'Areal, Rio de Janeiro, Brasil',
        'Itaocara, Rio de Janeiro, Brasil',
        'Quatis, Rio de Janeiro, Brasil',
        'Aperibé, Rio de Janeiro, Brasil',
        'Cardoso Moreira, Rio de Janeiro, Brasil',
        'Sapucaia, Rio de Janeiro, Brasil',
        'Duas Barras, Rio de Janeiro, Brasil',
        'Bom Jardim, Rio de Janeiro, Brasil',
        'Santa Maria Madalena, Rio de Janeiro, Brasil',
        'São Sebastião do Alto, Rio de Janeiro, Brasil',
        'Rio das Flores, Rio de Janeiro, Brasil',
        'Cordeiro, Rio de Janeiro, Brasil',
        'Cantagalo, Rio de Janeiro, Brasil',
        'Carmo, Rio de Janeiro, Brasil',
        'Macuco, Rio de Janeiro, Brasil',
        'Sumidouro, Rio de Janeiro, Brasil',
        'Casimiro de Abreu, Rio de Janeiro, Brasil',
        'Rio Claro, Rio de Janeiro, Brasil',
        'Varre-Sai, Rio de Janeiro, Brasil',
        'Paty do Alferes, Rio de Janeiro, Brasil',
        'Engenheiro Paulo de Frontin, Rio de Janeiro, Brasil',
        'Comendador Levy Gasparian, Rio de Janeiro, Brasil',
        'São José do Vale do Rio Preto, Rio de Janeiro, Brasil',
        'Pinheiral, Rio de Janeiro, Brasil',
        'Silva Jardim, Rio de Janeiro, Brasil',
        'Porto Real, Rio de Janeiro, Brasil',
        'Paraíba do Sul, Rio de Janeiro, Brasil',
        'Bom Jesus do Itabapoana, Rio de Janeiro, Brasil',
        'Italva, Rio de Janeiro, Brasil',
        'Arraial do Cabo, Rio de Janeiro, Brasil',
        'São Francisco de Itabapoana, Rio de Janeiro, Brasil',
        'São Fidélis, Rio de Janeiro, Brasil',
        'Quissamã, Rio de Janeiro, Brasil',
        'Cambuci, Rio de Janeiro, Brasil',
        'Carmo, Rio de Janeiro, Brasil',
        'Santa Maria Madalena, Rio de Janeiro, Brasil',
        'Trajano de Moraes, Rio de Janeiro, Brasil',
        'Laje do Muriaé, Rio de Janeiro, Brasil',
        'Miracema, Rio de Janeiro, Brasil',
        'Itaocara, Rio de Janeiro, Brasil',
        'Aperibé, Rio de Janeiro, Brasil',
        'Natividade, Rio de Janeiro, Brasil',
        'Porciúncula, Rio de Janeiro, Brasil',
        'Cardoso Moreira, Rio de Janeiro, Brasil',
        'Varre-Sai, Rio de Janeiro, Brasil',
        'São Sebastião do Alto, Rio de Janeiro, Brasil',
        'Santa Maria Madalena, Rio de Janeiro, Brasil',
        'Bom Jesus do Itabapoana, Rio de Janeiro, Brasil',
        'Italva, Rio de Janeiro, Brasil',
        'Itaperuna, Rio de Janeiro, Brasil',
        'Laje do Muriaé, Rio de Janeiro, Brasil',
        'Santo Antônio de Pádua, Rio de Janeiro, Brasil',
        'Miracema, Rio de Janeiro, Brasil',
        'Cambuci, Rio de Janeiro, Brasil',
        'Bom Jesus do Norte, Rio de Janeiro, Brasil',
        'Itaocara, Rio de Janeiro, Brasil',
        'Aperibé, Rio de Janeiro, Brasil']
            self.Certo = random.choice(self.cidades)

            self.Mapa = TkinterMapView(self.App2, width=400, height=400, corner_radius=0)
            self.Mapa.place(x=0, y=0)
            self.Mapa.set_address(self.Certo)
            self.Mapa.set_zoom(17)

            self.Pergunta = Label(self.App2, font=('Streamline Moderne', 15), text='Qual é a cidade vista acima?',
                                  bg='#FEF2F2')
            self.Resposta = ttk.Entry(self.App2, width='20', font=('Streamline Moderne', 15), style="Custom.TEntry")
            self.Enviar_G = Button(self.App2, text='Enviar', font=('Streamline Moderne', 24), bg='#FEF2F2', bd=0,
                                   activebackground='#FDCFCF', command=self.Envio_G)
            self.Pergunta.place(x=70, y=460)
            self.Resposta.place(x=100, y=510)
            self.Enviar_G.place(x=150, y=560)

            self.Resposta.bind('<Return>', lambda event: self.Enviar_G.invoke())

            self.Pontuacao = Label(self.App2, text=f'Pontuação: {self.pontuacao}', bg='#FEF2F2')
            self.Pontuacao.place(x=150, y=420)

            self.App2.after(1000, self.atualizar_pontuacao)  # Chama a função de atualização a cada 1 segundo

            self.Parte = self.Certo.split(', ')
            self.Resposta2 = self.Parte[0]
            print(self.Resposta2)

            self.App2.mainloop()

    def atualizar_pontuacao(self):
        if not self.jogo_encerrado:
            self.pontuacao -= 5  # Pontuação diminui a cada segundo
            self.Pontuacao.config(text=f'Pontuação: {self.pontuacao}')
        self.App2.after(1000, self.atualizar_pontuacao)  # Agendando a próxima atualização

    def Envio_G(self):
        if self.jogo_encerrado:  # Verifica se o jogo já foi encerrado
            return

        self.Resposta3 = self.Resposta.get()
        self.Resposta_A = self.Resposta2

        self.Gama = self.Resposta3.strip().lower()
        self.Delta = self.Resposta_A.lower
        self.Caractere0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', '@', '_', '!', '#', '$', '%', '^',
                           '&', '*', '(', ')', '<>', '?', '/', '|', '}', '{', '~', ':', ']']

        if self.Gama == self.Delta():
            messagebox.showinfo(title='Certo', message='Você acertou!')
            self.jogo_encerrado = True
            self.Finalizar()
        else:
            self.pontuacao = (self.pontuacao - 300)
            self.Pontuacao.config(text=f'Pontuação: {self.pontuacao}')

    def Cadastro(self):
        self.Root.destroy()
        self.Car = Tk()
        self.Car.iconbitmap("favicon.ico")
        self.Car.title('Cadastro')
        self.Car.geometry('400x400')

        self.largura_janela4 = 400
        self.altura_janela4 = 400
        self.largura_tela4 = self.Car.winfo_screenwidth()
        self.altura_tela4 = self.Car.winfo_screenheight()

        self.x4 = (self.largura_tela4 - self.largura_janela4) // 2
        self.y4 = (self.altura_tela4 - self.altura_janela4) // 2

        self.Car.geometry(f"{self.largura_janela4}x{self.altura_janela4}+{self.x4}+{self.y4}")

        self.Back3 = PhotoImage(file='Sem título - Copia.png')
        self.Back4 = Label(self.Car, image=self.Back3)
        self.Back4.place(x=0, y=0)

        self.Nome_C = Label(self.Car, text='Nome:', font=('Streamline Moderne', 24), bg='#FEF2F2')
        self.Nome_C.place(x=30, y=35)
        self.User_C = Label(self.Car, text='Usuário:', font=('Streamline Moderne', 24), bg='#FEF2F2')
        self.User_C.place(x=30, y=95)
        self.Email_C = Label(self.Car, text='Email:', font=('Streamline Moderne', 24), bg='#FEF2F2')
        self.Email_C.place(x=30, y=155)
        self.Idade_C = Label(self.Car, text='Idade:', font=('Streamline Moderne', 24), bg='#FEF2F2')
        self.Idade_C.place(x=30, y=215)
        self.Senha_C = Label(self.Car, text='Senha:', font=('Streamline Moderne', 24), bg='#FEF2F2')
        self.Senha_C.place(x=30, y=275)
        self.Entry_Nome_C = ttk.Entry(self.Car, font=('Streamline Moderne', 15), width='15', style="Custom.TEntry")
        self.Entry_Nome_C.place(x=160, y=40)
        self.Entry_User_C = ttk.Entry(self.Car, font=('Streamline Moderne', 15), width='15', style="Custom.TEntry")
        self.Entry_User_C.place(x=160, y=100)
        self.Entry_Email_C = ttk.Entry(self.Car, font=('Streamline Moderne', 15), width='15', style="Custom.TEntry")
        self.Entry_Email_C.place(x=160, y=160)
        self.Entry_Idade_C = ttk.Entry(self.Car, font=('Streamline Moderne', 15), width='15', style="Custom.TEntry")
        self.Entry_Idade_C.place(x=160, y=220)
        self.Entry_Senha_C = ttk.Entry(self.Car, font=('Streamline Moderne', 15), width='15', style="Custom.TEntry")
        self.Entry_Senha_C.place(x=160, y=280)
        self.Entry_Nome_C.bind('<Return>', lambda event: self.Entry_User_C.focus())
        self.Entry_User_C.bind('<Return>', lambda event: self.Entry_Email_C.focus())
        self.Entry_Email_C.bind('<Return>', lambda event: self.Entry_Idade_C.focus())
        self.Entry_Idade_C.bind('<Return>', lambda event: self.Entry_Senha_C.focus())
        self.Entry_Senha_C.bind('<Return>', lambda event: self.Enviar_C.invoke())

        self.Enviar_C = Button(self.Car, text='Enviar', font=('Streamline Moderne', 24), bg='#FEF2F2', bd=0, activebackground='#FDCFCF', command=self.Verificação)
        self.Enviar_C.place(x=120, y=330)

        self.Car.mainloop()

    def Verificação(self):
        self.Nome = self.Entry_Nome_C.get()
        self.User = self.Entry_User_C.get()
        self.Email = self.Entry_Email_C.get()
        self.Idade = self.Entry_Idade_C.get()
        self.Senha = self.Entry_Senha_C.get()
        self.Caractere = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', '@', '_', '!', '#', '$', '%', '^', '&', '*','(', ')', '<>', '?', '/', '|', '}', '{', '~', ':', ']']
        self.Key_Email_Api = PyHunter('b1ee73f7cda224cb5cdafcbe4a3780bc26a76b84')
        self.Caractere2 = ['[', '@', '_', '!', '#', '$', '%', '^', '&', '*','(', ')', '<', '>', '?', '/', '|', '}', '{', '~', ':', ']', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        try:
            for i in self.Caractere:
                if i in self.Nome:
                    messagebox.showerror(title='Erro', message='O espaço nome contem caracteres invalidos')
                break
            if len(self.Nome) < 3:
                messagebox.showerror(title='Erro', message='O espaço nome tem menos de 3 letras')
            elif len(self.Nome) > 60:
                messagebox.showerror(title='Erro', message='O espaço nome tem mais de 60 letras')
            else:
                if len(self.User) <3:
                    messagebox.showerror(title='Erro', message='O espaço usuario tem menos de 3 caracteres')
                elif len(self.User) > 24:
                    messagebox.showerror(title='Erro', message='O espaço usuario tem mais de 24 caracteres')
                else:
                    self.Email_Result = self.Key_Email_Api.email_verifier(email=self.Email)
                    print(self.Email_Result)
                    if self.Email == '':
                        messagebox.showerror(title='Erro', message='O email está vazio')
                    elif self.Email_Result['result'] != 'deliverable':
                        messagebox.showerror(title='Erro', message='O email inserido é invalido')
                    else:
                        for i2 in self.Caractere2:
                            if i2 in self.Idade:
                                messagebox.showerror(title='Erro', message='Há caracteres invalidos no campo idade')
                            break
                        if self.Idade == '':
                            messagebox.showerror(title='Erro', message='A idade está vazia')
                        elif len(self.Idade) > 2:
                            messagebox.showerror(title='Erro', message='O limite da idade é 2 digitos')
                        else:
                            if self.Senha == '':
                                messagebox.showerror(title='Erro', message='Sua senha está em branco')
                            else:
                                self.conexão()


        finally:
            print('S')

    def conexão(self):
        self.sql = sqlite3.connect('banco.db')
        self.cursor = self.sql.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Jogador
        (
        Email Varchar(50) Primary Key Not Null,
        Usuario Varchar(40) Not Null,
        Nome Varchar(60) Not Null,
        Senha Varchar(25) Not Null,
        Idade Int(2) Not Null);
        ''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Jogo
        (Id INTEGER PRIMARY KEY AUTOINCREMENT,
        ValorP Int Not Null,
        Cadastro_Email Varchar(50) Not Null,
        Foreign Key (Cadastro_Email) References Jogador(Email));
        ''')
        self.cursor.execute(f"INSERT INTO Jogador (Usuario, Senha, Email, Nome, Idade) VALUES ('{self.User}', '{self.Senha}', '{self.Email}', '{self.Nome}', {self.Idade})")
        self.sql.commit()
        self.Car.destroy()
        self.Login()

    def Finalizar(self):
        if self.Test is not None:
            self.sql = sqlite3.connect('banco.db')
            self.cursor2 = self.sql.cursor()
            self.cursor2.execute(
                f"INSERT INTO Jogo (ValorP, Cadastro_Email) VALUES ('{self.pontuacao}', '{self.Email_I}')")
            self.sql.commit()
            self.cursor2.close()
        self.reiniciar_jogo()

    def reiniciar_jogo(self):
        resposta = messagebox.askyesno(title='Reiniciar', message='Deseja reiniciar o jogo?')
        if resposta:
            # Redefinir as variáveis do jogo
            self.jogo_encerrado = False
            self.pontuacao = 10000

            # Limpar a interface gráfica
            self.Resposta.delete(0, 'end')
            self.Pontuacao.config(text=f'Pontuação: {self.pontuacao}')
            self.reiniciar_mapa()
        else:
            self.App2.destroy()

    def reiniciar_mapa(self):
        self.Certo = random.choice(self.cidades)
        self.Parte = self.Certo.split(', ')
        self.Resposta2 = self.Parte[0]
        self.Mapa.set_address(self.Certo)
        self.Mapa.set_zoom(17)
        print(self.Resposta2)

if __name__ == '__main__':
    app = Aplicação()
    app.Root.mainloop()