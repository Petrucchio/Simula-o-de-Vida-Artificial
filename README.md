# Simulação de Vida Artificial

Este projeto é uma simulação de vida artificial baseada no famoso Jogo da Vida de Conway. A simulação ocorre em uma grade bidimensional onde cada célula pode estar viva ou morta. A cada iteração, o estado de cada célula é atualizado com base em regras simples.

## Funcionalidades

- Inicialização da grade com valores aleatórios.
- Simulação de várias iterações da vida na grade.
- Exibição da grade em cada iteração.

## Regras da Simulação

1. Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
2. Qualquer célula viva com dois ou três vizinhos vivos continua viva para a próxima geração.
3. Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
4. Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva, como se fosse reprodução.

## Como Executar

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Execute o script:**
    ```bash
    python main.py
    ```

## Estrutura do Código

- **initialize_random_grid(rows, cols):** Inicializa a grade com valores aleatórios.
- **count_live_neighbors(grid, row, col):** Conta o número de vizinhos vivos de uma célula.
- **get_next_generation(grid):** Gera a próxima geração da grade com base nas regras de vida/morte.
- **display_grid(grid):** Exibe a grade no console.
- **main():** Função principal que executa a simulação por um número definido de iterações.

## Exemplo de Saída

```plaintext
0 1 0 0
0 0 1 0
1 1 1 0
0 0 0 0

1 1 0 0
1 0 1 0
0 1 1 0
0 1 0 0

...
