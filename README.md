🤖 Automação de Cadastro de Produtos (RPA)

Este projeto utiliza Python para automatizar o processo de cadastro de produtos em um sistema web. O script realiza a leitura de dados de uma planilha (produtos.csv) e utiliza a biblioteca pyautogui para simular as ações do usuário (abrir navegador, login, preenchimento de formulários e cliques) de forma rápida e eficiente.

🎯 Objetivo

O principal objetivo é eliminar o trabalho manual e repetitivo de preencher formulários web. O robô faz a leitura da tabela de produtos e insere cada linha no sistema, aumentando a produtividade e reduzindo erros de digitação.

⚙️ Tecnologias e Bibliotecas

Python: Linguagem principal do projeto.

PyAutoGUI: Utilizado para automação de interface gráfica (cliques, escrita, pressionamento de teclas).

Pandas: Usado para importar, ler e iterar sobre os dados da planilha produtos.csv.

Time: Necessário para introduzir pausas estratégicas, garantindo que o sistema web tenha tempo de carregar entre as ações.

💻 Funcionalidades Principais

Abertura de Sistema: Abre o navegador Google Chrome e navega até a página de login do sistema alvo.

Login Automatizado: Realiza o login utilizando credenciais pré-definidas.

Importação de Dados: Lê o arquivo produtos.csv contendo os dados a serem cadastrados.

Loop de Cadastro: Itera sobre cada linha da planilha, preenchendo os campos de código, marca, tipo, categoria, preço, custo e observação (se existir) e enviando o formulário.

Scroll Automático: Garante que a tela seja ajustada para o próximo cadastro.

🚀 Como Executar o Projeto

Para rodar este robô, você deve garantir que as coordenadas de clique e a URL estejam corretas para o seu ambiente.

1. Pré-requisitos

Instale as bibliotecas necessárias:

pip install pyautogui pandas


2. Configuração de Coordenadas

O script utiliza coordenadas fixas de tela (ex: pyautogui.click(x=1081, y=369)). Essas coordenadas podem variar dependendo da resolução e do tamanho da tela do seu monitor.

Importante: Se o robô não funcionar, execute a última linha do código (time.sleep(5) seguido de print(pyautogui.position())) para descobrir as coordenadas exatas dos campos e botões na sua tela, e ajuste o script.

3. Estrutura de Arquivos

Certifique-se de ter a planilha produtos.csv no mesmo diretório do seu script Python.

.
├── produtos.csv              # Planilha com os dados dos produtos
├── [SEU_ARQUIVO].py          # O script principal de automação
└── README.md


4. Execução

Execute o script e observe o robô trabalhar:

python [NOME_DO_SEU_ARQUIVO].py


⚠️ Nota Importante

Durante a execução do script, evite mover o mouse ou usar o teclado, pois isso pode interromper ou desviar as ações automatizadas do pyautogui.
