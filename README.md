# Word Counter
Teste de Contagem de palavras usando docker.

## Arquitetura
A Solução é composta de 3 containers:
- Um Container rodando uma aplicação em Python responsável por monitorar uma pasta. Ler arquivos novos nesta pastas, executar a contagem de palavras e atualiza o resultado da contagem em um banco de dados.
- Um container Redis para armazenar o resultado das contagens anteriores salvando os resultados no disco da máquina host
- Um container rodando uma restapi em flask que lê o banco de dados o resultado atual da contagem.

## Justificativa da Arquitetura e Escalabilidade
A solução foi feita para otimizar a velocidade do retorno da contagem, sendo assim é feito um pré-processamento dos arquivos e a contagem atual é salva e atualizada para cada palavras. Quando é adicionado um novo arquivo ele é automaticamente processado pelos containers de pré-processamento e os dados são atualizados. Sendo assim, o custo de consulta é o custo de consulta em uma tabela de banco de dados já tendo as palavras como chave. Sendo assim, é muito rápida (menos de 10 ms).

OBS: A versão anterior estava feita com Postgres, porém ele foi alterada para aumentar a performance de input e de output

Além disto, como a solução foi desenvolvida em microserviços é possível adicionar mais containers de cada serviço em caso de necessidade. Se houver lentidão no processamento dos dados de entrada pode-se subir mais containers deste serviço de importação e após o aumento da carga eles podem ser derrubados e o mesmo vale para o container Redis. Casa haja um aumento do número de solicitações de entrada seria necessário adicionar um container NGINX para fazer o balanceamento de carga e então subir mais containers do serviço de consultas.

No entanto caso a entrada de dados ainda assim seja muito grande será necessário substituir o sistema de armazenamento de arquivos por um Hadoop e utilizar serviços de MapReduce para alimentar o Banco Redis. Porém, este só seria o caso para caso a quantidade de informações seja muito grande ou grande quantidade de arquivos. Como este não é o caso dos exemplos enviados não houve necessidade de criar o cluster hadoop. Até porque isto impactaria no prazo que me foi dado.

## Processo de Build
A solução foi constuida com a utilização do Docker-Compose, sendo assim o processo de build é simplesmente:
```console
$ docker-compose build
```
Para realizar o deploy no próprio sistema
```console
$ docker-compose up -d
```
Os arquivos para serem processados deve ser colocados em:
```console
$  ./words
```
Os logs de importação serão colocados em:
```console
$  ./words/logs
```
Os arquivos já processados ficarão em:
```console
$  ./words/processed```

Para Testar a API:
```console
$  curl -X GET localhost:5000/value?word=contrafortar
```
O Retorno da API será composto em um JSON no tempo necessário para a Query em segundos e o resultado da Query:
```json
{
    "elapsed": 0.0006933212280273438, 
    "value": 38
}
```

Para derrubar a solução
```console
$ docker-compose down
```
