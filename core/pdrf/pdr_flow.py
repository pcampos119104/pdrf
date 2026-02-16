from crewai.flow import Flow, listen, start
from core.pdrf.crews.pdr.crew import PdrCrew
from pydantic import BaseModel


class RecipeState(BaseModel):
    processed_recipe: str = ""
    raw_recipe: str = ""


class PdrFlow(Flow[RecipeState]):
    @start()
    def process_unstructure_recipe(self):
        """
        Run the crew.
        """
        inputs = {
            "lista_ingredientes": "sample_value",
            "titulo_receita": "sample_value",
            "descricao_receita": "sample_value",
            "titulo": "sample_value",
            "descricao": "sample_value",
            "ingredientes_convertidos": "sample_value",
            "modo_preparo": "sample_value",
            "tags": "sample_value",
            "receita_texto": self.state.raw_recipe,
        }
        result = PdrCrew().crew().kickoff(inputs=inputs)
        self.state.processed_recipe = getattr(result, "raw", "") if result else ""
        return result
