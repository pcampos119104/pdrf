import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import DallETool


@CrewBase
class PdrCrew:
    """ProcessadorDeReceitasCrewai crew"""

    @agent
    def conversor_de_medidas_culinarias(self) -> Agent:
        return Agent(
            config=self.agents_config["conversor_de_medidas_culinarias"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="ollama/qwen2.5:14b",
                temperature=0.7,
            ),
        )

    # @agent
    # def gerador_de_imagem_culinaria(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config["gerador_de_imagem_culinaria"],
    #         tools=[DallETool()],
    #         reasoning=False,
    #         max_reasoning_attempts=None,
    #         inject_date=True,
    #         allow_delegation=False,
    #         max_iter=25,
    #         max_rpm=None,
    #         max_execution_time=None,
    #         llm=LLM(
    #             model="ollama/qwen2.5:14b",
    #             temperature=0.7,
    #         ),
    #     )

    @agent
    def compilador_de_receitas(self) -> Agent:
        return Agent(
            config=self.agents_config["compilador_de_receitas"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="ollama/qwen2.5:14b",
                temperature=0.7,
            ),
        )

    @agent
    def extrator_de_titulo(self) -> Agent:
        return Agent(
            config=self.agents_config["extrator_de_titulo"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="ollama/qwen2.5:14b",
                temperature=0.7,
            ),
        )

    @agent
    def extrator_de_descricao(self) -> Agent:
        return Agent(
            config=self.agents_config["extrator_de_descricao"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="ollama/qwen2.5:14b",
                temperature=0.7,
            ),
        )

    @agent
    def extrator_de_ingredientes(self) -> Agent:
        return Agent(
            config=self.agents_config["extrator_de_ingredientes"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="ollama/qwen2.5:14b",
                temperature=0.7,
            ),
        )

    @agent
    def extrator_de_modo_de_preparo(self) -> Agent:
        return Agent(
            config=self.agents_config["extrator_de_modo_de_preparo"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="ollama/qwen2.5:14b",
                temperature=0.7,
            ),
        )

    @agent
    def gerador_de_tags(self) -> Agent:
        return Agent(
            config=self.agents_config["gerador_de_tags"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="ollama/qwen2.5:14b",
                temperature=0.7,
            ),
        )

    @task
    def extrair_ingredientes_da_receita(self) -> Task:
        return Task(
            config=self.tasks_config["extrair_ingredientes_da_receita"],
            markdown=False,
        )

    @task
    def extrair_titulo_da_receita(self) -> Task:
        return Task(
            config=self.tasks_config["extrair_titulo_da_receita"],
            markdown=False,
        )

    @task
    def extrair_descricao_da_receita(self) -> Task:
        return Task(
            config=self.tasks_config["extrair_descricao_da_receita"],
            markdown=False,
        )

    @task
    def extrair_modo_de_preparo_da_receita(self) -> Task:
        return Task(
            config=self.tasks_config["extrair_modo_de_preparo_da_receita"],
            markdown=False,
        )

    @task
    def gerar_tags_da_receita(self) -> Task:
        return Task(
            config=self.tasks_config["gerar_tags_da_receita"],
            markdown=False,
        )

    @task
    def converter_medidas_dos_ingredientes(self) -> Task:
        return Task(
            config=self.tasks_config["converter_medidas_dos_ingredientes"],
            markdown=False,
        )

    # @task
    # def gerar_imagem_da_receita(self) -> Task:
    #     return Task(
    #         config=self.tasks_config["gerar_imagem_da_receita"],
    #         markdown=False,
    #     )

    @task
    def compilar_receita_final(self) -> Task:
        return Task(
            config=self.tasks_config["compilar_receita_final"],
            markdown=False,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ProcessadorDeReceitasCrewai crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="ollama/qwen2.5:14b"),
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
