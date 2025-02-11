import customtkinter as ctk
from config import nome_dos_wifis, senha_dos_wifis

class Home(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.wifis = nome_dos_wifis()
        self.senhas = senha_dos_wifis(self.wifis)
        self.quantidade_wifis = len(self.wifis)
        self.background_color = "#191919"
        self.title("WI-PASS")
        self.geometry("500x400")
        self.iconbitmap("images/logo_wi_pass.ico")

        self.titulo = ctk.CTkLabel(self, text="Senha dos Wifis", font=('Comic Sans MS', 20), text_color="white")
        self.titulo.place(x=180, y=10)

        self.frame = ctk.CTkFrame(self, width=500, height=230)
        self.frame.place(x=0, y=50)

        self.canva = ctk.CTkCanvas(self.frame, width=728, height=450)
        self.canva.pack(side="left", fill="both", expand=True)

        self.scrollbar = ctk.CTkScrollbar(self.frame, orientation="vertical", command=self.canva.yview, fg_color=self.background_color)
        self.scrollbar.pack(side="right", fill='y')

        self.canva.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = ctk.CTkFrame(self.canva)
        self.canva.create_window((0,0), window=self.scrollable_frame, anchor="nw")

        y_listra = 0
        for k in range(len(self.wifis)):
            self.listra = ctk.CTkFrame(self.scrollable_frame, fg_color=self.background_color, corner_radius=0, width=500, height=30)
            # self.listra.grid(row=k, column=0, pady=2)
            self.listra.place(x=0, y=y_listra)
            y_listra+=32

        x_name = 20
        y_name = 0
        for i in range(len(self.wifis)):
                self.wifi_name = ctk.CTkLabel(self.scrollable_frame, text=f'Nome: {self.wifis[i]}', font=('Comic Sans Ms', 12), fg_color=self.background_color)
                # self.wifi_name.grid(row=i, column=0, padx=x_name, pady=2)
                self.wifi_name.place(x=x_name, y=y_name)
                y_name+=32
        
        x_senha = 300
        y_senha = 0
        for n in range(len(self.senhas)):
                self.senha = ctk.CTkLabel(self.scrollable_frame, text=f'Senha: {self.senhas[n]}', font=('Comic Sans MD', 12), fg_color=self.background_color)
                self.senha.grid(row=n, column=1, padx=x_senha, pady=2)
                # self.senha.place(x=x_senha, y=y_senha)
                y_senha+=32
        
        self.scrollable_frame.update_idletasks()
        self.canva.config(scrollregion=self.canva.bbox('all'))

if __name__=="__main__":
    app = Home()
    app.mainloop()