# Projeto final de Sistemas Embarcados em Tempo Real

## Objetivo

Gerar um sistema embarcado que faça comunicação entre ao menos duas placas, utilizando algum protocolo discutido em aulas, ou protocolo de mercado que converse entre si, dois sistemas embarcados com aplicações eletrônicas e/ou industriais complementares.

## Materiais utilizados

- Nucleo F439ZI
- Computador do laboratório ENG-61
- Roteador de wi-fi
- Potenciômetro Slider-Pot

## Arquitetura de rede do projeto

<img src="./diagram-and-fluxograma/Diagrama de rede.png" alt="Diagrama de rede">

## Descrição do projeto

O projeto tem como objetivo realizar a transmissão de dados em uma rede offline local utilizando o protocolo MQTT e o broker Mosquitto. O mesmo é composto por 5 partes principais:

1. Broker MQTT
2. Roteador
3. Nucleo F439ZI
4. Backend + Banco de dados
5. Frontend

### 1. Broker MQTT

O broker utilizado foi o Mosquitto, um broker open source gratuito que pode ser baixado no site: [Mosquitto](https://mosquitto.org/download/)

Esse broker irá atuar como mediador dos subscribers e publisher que são presentes no protocolo MQTT. Os subscribers são configurações para receber dados de um determinado tópico enquanto os publisher são configurações para publicar dados em um determinado tópico. Os tópicos são o destino para onde os dados são enviados.

Por fim, para que o broker seja acessível na rede do roteador é necessario modificar o arquivo **mosquitto.conf** que fica dentro da pasta /Arquivo de Programas/mosquitto/mosquitto.conf. Deve ser inserido o campo **allow_anonymous true** no arquivo.

### 2. Roteador

O roteador é o responsavel por permitir a conexão entre os dispositivos e criar a rede offline local. Com ele todos os dispositivos ganham um IP na rede e conseguem se comunicar entre si.

### 3. Nucleo F439

A placa nucleo F439ZI é a responsavel por estabelecer uma conexão MQTT no broker da rede e fazer um publish no topico **sensor/topic**. Alem de estabelecer e manter o protocolo MQTT funcionando a nucleo tambem mantem funcionando outras duas threads importantes para o programa.

A primeira thread é a responsavel por determinar se os dados podem ou não serem enviados a partir de uma variavel de controle que é modificada pelo botão do usuario.

A segunda thread é a responsavel por fazer a leitura do sensor analogico presente no circuito e disponibilizar esse dado para ser publicado pelo MQTT.

### 4. Backend + Banco de dados

No projeto existe um servidor backend feito em python. Esse servidor é responsavel por inicializar os protocolos HTTP e MQTT, o MQTT é responsavel por se inscrever no topico que os dados estão sendo enviados e inserir cada dado que chega em um banco de dados SQLite.

O protocolo HTTP é o responsavel por disponibilizar os endpoints que o frontend vai consumir, esses endpoints buscam os dados inseridos no banco de dados e devolvem no formato JSON para a pagina web renderizar.

### 5. Frontend

O frontend é responsavel por buscar os dados no backend a cada 2 segundos e renderizar os dados num grafico para o usuario acompanhar em tempo real o que esta sendo publicado.

## Fluxograma MBED

<img src="./diagram-and-fluxograma/Fluxograma - Projeto Final.png" alt="Fluxograma MBED">

## Conclusão

Com a descrição acima é possivel compreender cada parte do projeto e qual a responsabilidade de cada um dentro da rede.
