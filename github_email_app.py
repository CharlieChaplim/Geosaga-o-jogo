import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import github3
from tkinter import messagebox
class GitHubEmailApp:
    def Raiz(self):
        self.janela = tk.Tk()
        self.janela.geometry("200x100")
        self.style = ThemedStyle(self.janela)
        self.style.set_theme("equilux")

        self.criar_widgets()

    def criar_widgets(self):
        self.entrada_usuario = ttk.Entry(self.janela)
        self.entrada_usuario.place(relx=0.5, rely=0.3, anchor="center")
        self.entrada_usuario.bind("<Return>", self.obter_email)

        self.botao_obter_email = ttk.Button(self.janela, text="Obter Email", command=self.obter_email)
        self.botao_obter_email.place(relx=0.5, rely=0.7, anchor="center")

    def obter_email(self, event=None):
        usuario = self.entrada_usuario.get()
        print("Usuário:", usuario)
        email = self.obter_email_usuario(usuario)
        if email:
            messagebox.showinfo("Email", f"O email do usuário {usuario} é: {email}")
        else:
            messagebox.showinfo("Email", f"Não foi possível obter o email do usuário {usuario}")

    def obter_email_usuario(self, usuario):
        try:
            gh = github3.login(token='SEU_TOKEN_AQUI')  # Insira seu token de acesso do GitHub
            user = gh.user(usuario)
            email = user.email
            return email

        except github3.GitHubError as e:
            print("Erro ao obter o email do usuário:", str(e))
            return None

    def executar(self):
        self.janela.mainloop()
