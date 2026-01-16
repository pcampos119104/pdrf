#!/usr/bin/env python
from random import randint

from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from pdrf.crews.pdr.crew import PdrCrew


class RecipeState(BaseModel):
    recipe: str = ""


class PdrFlow(Flow[RecipeState]):

    @start()
    def process_unstructure_recipe(self, recipe: str = None):
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

    # @listen(generate_sentence_count)
    # def generate_poem(self):
    #     print("Generating poem")
    #     result = (
    #         PoemCrew()
    #         .crew()
    #         .kickoff(inputs={"sentence_count": self.state.sentence_count})
    #     )
    #
    #     print("Poem generated", result.raw)
    #     self.state.poem = result.raw
    #
    # @listen(generate_poem)
    # def save_poem(self):
    #     print("Saving poem")
    #     with open("poem.txt", "w") as f:
    #         f.write(self.state.poem)


def kickoff():
    pdrf = PdrFlow()
    pdrf.kickoff()


def plot():
    pdrf = PdrFlow()
    pdrf.plot()


def run_with_trigger():
    """
    Run the flow with trigger payload.
    """
    import json
    import sys

    # Get trigger payload from command line argument
    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    # Create flow and kickoff with trigger payload
    # The @start() methods will automatically receive crewai_trigger_payload parameter
    pdrf = PdrFlow()

    try:
        result = pdrf.kickoff({"crewai_trigger_payload": trigger_payload})
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the flow with trigger: {e}")


if __name__ == "__main__":
    kickoff()
