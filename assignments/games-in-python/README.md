
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construir, em Python, uma versão do jogo da Forca para praticar manipulação de strings, estruturas de repeticao, condicionais e controle de estado do jogo.

## 📝 Tarefas

### 🛠️	Implementar a logica principal do jogo

#### Descrição
Crie um programa que escolha uma palavra aleatoria de uma lista e permita ao jogador tentar adivinhar uma letra por vez ate descobrir toda a palavra ou perder todas as tentativas.

#### Requisitos
O programa concluído deve:

- Definir uma lista com pelo menos 5 palavras e selecionar uma palavra aleatoriamente
- Exibir o progresso da palavra com letras descobertas e caracteres "_" para letras ocultas
- Solicitar um palpite de uma unica letra por rodada
- Atualizar corretamente o estado do jogo quando a letra existir ou nao na palavra
- Encerrar o jogo com mensagem de vitoria ao completar a palavra
- Encerrar o jogo com mensagem de derrota ao atingir o limite de erros


### 🛠️	Melhorar a experiencia do jogador

#### Descrição
Apos implementar a versao base, melhore a interacao com o usuario para tornar o jogo mais claro, justo e facil de acompanhar durante as rodadas.

#### Requisitos
O programa concluído deve:

- Mostrar a quantidade de tentativas restantes a cada rodada
- Impedir que o jogador repita letras ja informadas
- Validar entradas invalidas (vazio, mais de uma letra, numeros ou simbolos)
- Exibir ao final qual era a palavra secreta quando houver derrota
- Manter mensagens claras de feedback para cada acerto e erro