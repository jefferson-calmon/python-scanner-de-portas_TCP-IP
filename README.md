# Scanner de Portas TCP/IP em Python3

Esse é um script escrito em python. Ele varre as portas de um determinado ip e exibe na tela as portas abertas e os determinados serviços que estão rodando. 


Exemplo da resposta do script

<img src="images/exemplo1.png">

## Requerimentos

Para se usar esse script é nescessário ter instalado o Python e algumas bibliotecas. Veja abaixo.

* Python3 instalado
* Biblioteca Socket
* Biblioteca Time

Caso não queira instalar o Python e nem as bibliotecas, basta usar o arquivo executável que eu deixei dentro do repositório o processo dos comandos serão o mesmo, basta substituir **scano.py** por **scano.exe**.


## Comandos

* **-a** -> Nesse comando você vai especificar o alvo(ip)
* **-s** -> Com esse comando voê tem a opção de salvar os resultados em arquivo de texto. Escreva [ **--s 1**] para salvar.

Veja um exemplo de um comando abaixo:

<img src="images/comando.png" align="center" height="20px">

## Opções

Depois de executar o comando acima, irá aparecer no terminal uma espécie de "menu". Veja abaixo um exemplo.

<img src="images/exemplo2.png" align="center">

Basta escolher a opção da sua preferência e Let's go.

## Observações

Dentro do respositorio existe uma arquivo chamado *portconf.py*. Nesse arquivo é onde estão algumas configurações das portas TCP/IP, como por exemplo as nome dos serviços que cada porta está rodando. Sinta-se a vontade para fazer alterações e se quiser, me mande um pull request.

Esse script foi todo criado por mim
