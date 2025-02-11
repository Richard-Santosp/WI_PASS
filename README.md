# Wi-Pass: Visualizador de Senhas de Redes Wi-Fi
## Descrição:
O Wi-Pass é um sistema desenvolvido com Python e a biblioteca CustomTkinter, projetado para facilitar o acesso às senhas das redes Wi-Fi que já foram conectadas ao computador do usuário. Através de uma interface gráfica simples e limpa, o usuário pode visualizar o nome das redes Wi-Fi (SSID) e as respectivas senhas.

## Funcionalidades:
**Exibição das Redes Wi-Fi**: O sistema coleta as informações das redes Wi-Fi já conectadas ao computador, mostrando o nome de cada rede (SSID) na interface. Exibição das Senhas: Para cada rede Wi-Fi, o sistema exibe a senha associada, permitindo que o usuário veja facilmente as credenciais necessárias para se reconectar a essas redes. Interface Responsiva: Utilizando o CustomTkinter, o sistema possui uma interface gráfica que se adapta ao número de redes Wi-Fi, criando um design limpo e organizado. Altura Fixa com Rolagem: Para garantir que o layout não ultrapasse o tamanho da tela, a altura da janela é fixada em 300px, com uma barra de rolagem (scrollbar) ativada quando o número de redes Wi-Fi ultrapassa 8.

## Tecnologias Utilizadas:
**Python:** Linguagem de programação utilizada para desenvolver o sistema. </br>
**CustomTkinter:** Biblioteca usada para criar a interface gráfica com aparência moderna e funcional. </br>
**Subprocess:** Usado para executar comandos do sistema e coletar as informações das redes Wi-Fi salvas no computador.

## Público-alvo:
Usuários que desejam recuperar as senhas das redes Wi-Fi que já foram conectadas ao seu computador, seja por esquecimento ou por necessidade de reconectar dispositivos.
