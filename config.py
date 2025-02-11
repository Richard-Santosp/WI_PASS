import subprocess

def nome_dos_wifis():
    result =  subprocess.run('netsh wlan show profiles', capture_output=True, text=True, shell=True)
    output = result.stdout
    nome_dos_wifis = []
    for linha in output.splitlines():
        linha = linha.replace("\xa0", "")
        if 'Todos os Perfis de Usurios' in linha:
            profile = linha.split(":")[1].strip()
            nome_dos_wifis.append(profile)
    return nome_dos_wifis

def senha_dos_wifis(lista_de_wifis):
    senhas = []
    for wifi in lista_de_wifis:
        senha_de_casa = subprocess.run(f'netsh wlan show profile name="{wifi}" key=clear', capture_output=True ,text=True, shell=True )
        output_senha_de_casa = senha_de_casa.stdout

        for linha in output_senha_de_casa.splitlines():
            linha = linha.replace("£", "ú")
            if 'Conteúdo da Chave' in linha:
                password = linha.split(":")[-1].strip()
                senhas.append(password)
    return senhas