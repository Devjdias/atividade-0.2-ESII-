# atividade-0.1-ESII-
Engenharia de software II - Profº Flávio Miranda

Este é um jogo simples de Pong desenvolvido em Python utilizando a biblioteca Pygame. Dois jogadores controlam as paddles (raquetes) e tentam rebater a bola para marcar pontos no adversário. O jogo termina quando um dos jogadores alcança 5 pontos.
Requisitos

Para rodar este jogo, você precisa ter o Python instalado em sua máquina. Além disso, a biblioteca Pygame deve estar instalada. Caso não tenha, instale com o seguinte comando:

pip install pygame

Como Jogar

    Jogador da Esquerda:

        Subir: W

        Descer: S

    Jogador da Direita:

        Subir: Seta para cima

        Descer: Seta para baixo

O jogo inicia automaticamente e termina quando um jogador atinge 5 pontos.
Pontuação

A pontuação é exibida na parte superior da tela e salva automaticamente em um arquivo pontuacoes.txt ao final de cada partida.
Executando o Jogo

Para rodar o jogo, basta executar o script Python:

python pong.py

Personalização

Você pode modificar variáveis como:

    SCREEN_WIDTH e SCREEN_HEIGHT para alterar o tamanho da tela.

    self.velocity na classe Ball para ajustar a velocidade da bola.

    if left_score == 5 or right_score == 5: para mudar a pontuação máxima.

Licença

Este projeto é de código aberto e pode ser modificado livremente. Sinta-se à vontade para contribuir! 🚀
