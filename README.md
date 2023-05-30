## Webscraper

Este programa é um webscraper desenvolvido em Python usando a biblioteca Scrapy. Permite obter informações sobre jogos de futebol do site "[www.redditsoccerstreams.tv/](http://www.redditsoccerstreams.tv/)" e guardar os dados num ficheiro CSV.

### Funcionalidade

O webscraper utiliza o comando "scrapy crawler soccerstreams -O soccerstreams.csv" para executar o crawler e obter os dados dos jogos de futebol do referido site. O comando deve ser executado no terminal ou na linha de comandos, na pasta onde o projeto se encontra.

O programa realiza as seguintes etapas:

1. Faz um pedido HTTP à página inicial do site "[www.redditsoccerstreams.tv/](http://www.redditsoccerstreams.tv/)".
2. Extrai as informações dos jogos de futebol presentes na página, incluindo o tempo, o nome do jogo e o link para assisti-lo.
3. Navega para as páginas seguintes, se existirem, para obter mais informações sobre os jogos.
4. Guarda as informações recolhidas num ficheiro CSV chamado "soccerstreams.csv".

### Dependências

Para executar o webscraper, é necessário ter as seguintes dependências instaladas:

```
pip install scrapy
```

Certifique-se de ter o Python instalado no seu sistema antes de instalar o Scrapy.

Além disso, é necessário ter acesso à internet para que o programa possa fazer pedidos HTTP ao site "[www.redditsoccerstreams.tv/](http://www.redditsoccerstreams.tv/)" e obter os dados.

### Como utilizar

1. Faça o download do código-fonte do webscraper e coloque-o numa pasta.
2. Abra um terminal ou linha de comandos e navegue até à pasta onde o código-fonte se encontra.
3. Execute o seguinte comando para iniciar o crawler e guardar os dados num ficheiro CSV:

```
scrapy crawler soccerstreams -O soccerstreams.csv
```

4. Aguarde até que o programa termine de recolher os dados. Os resultados serão guardados no ficheiro "soccerstreams.csv" na mesma pasta.

### Observações

Este webscraper foi projetado especificamente para o site "[www.redditsoccerstreams.tv/](http://www.redditsoccerstreams.tv/)" e  não funciona corretamente noutros sites. 









