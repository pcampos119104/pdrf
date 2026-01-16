#!/usr/bin/env python
import sys
from pdr.crew import PdrCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'lista_ingredientes': 'sample_value',
        'titulo_receita': 'sample_value',
        'descricao_receita': 'sample_value',
        'titulo': 'sample_value',
        'descricao': 'sample_value',
        'ingredientes_convertidos': 'sample_value',
        'modo_preparo': 'sample_value',
        'tags': 'sample_value',
        'receita_texto': '''Bolo de Cenoura com Farinha de Aveia

15 Minutos Preparo

    25 Porções

Lista de ingredientes

    2 cenouras descascadas e cortadas em rodelas
    ½ xícara (chá) de óleo
    3 ovos
    2 xícaras (chá) de açúcar
    2 ½ xícaras (chá) de Farinha de Aveia Yoki
    1 colher (sopa) de Fermento em Pó
    ½ xícara (chá) de nozes picadas

Preparação

    Bata no liquidificador a cenoura, o óleo e os ovos.
    Retire a mistura do liquidificador e coloque em uma vasilha.
    Acrescente o açúcar, a farinha de aveia, o fermento e as nozes picadas. Mexa delicadamente a receita de bolo de cenoura simples.
    Unte e enfarinhe uma assadeira retangular média.
    Coloque a massa do bolo de cenoura na assadeira e leve ao forno preaquecido a 200°C por 45 minutos ou até dourar.
    Agora você já sabe como fazer bolo de cenoura simples!'''
    }
    PdrCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'lista_ingredientes': 'sample_value',
        'titulo_receita': 'sample_value',
        'descricao_receita': 'sample_value',
        'titulo': 'sample_value',
        'descricao': 'sample_value',
        'ingredientes_convertidos': 'sample_value',
        'modo_preparo': 'sample_value',
        'tags': 'sample_value',
        'receita_texto': 'sample_value'
    }
    try:
        PdrCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        PdrCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'lista_ingredientes': 'sample_value',
        'titulo_receita': 'sample_value',
        'descricao_receita': 'sample_value',
        'titulo': 'sample_value',
        'descricao': 'sample_value',
        'ingredientes_convertidos': 'sample_value',
        'modo_preparo': 'sample_value',
        'tags': 'sample_value',
        'receita_texto': 'sample_value'
    }
    try:
        PdrCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
