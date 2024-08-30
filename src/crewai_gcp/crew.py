from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, llm
from langchain_google_vertexai import VertexAI

# Uncomment the following line to use an example of a custom tool
# from crewai_gcp.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool


@CrewBase
class CrewaiGcpCrew:
    """CrewaiGcp crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # defining the VertexAI Gemini model
    @llm
    def gemini_llm(self):
        return VertexAI(model_name="gemini-pro")

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            # tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
            verbose=True,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["reporting_analyst"],
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"], agent=self.researcher())

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporting_task"],
            agent=self.reporting_analyst(),
            output_file="report.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiGcp crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            share_crew=False,
            # memory=True,
            # planning=True,
            # planning_llm=self.gemini_llm(),
            # embedder={
            #     "provider": "vertexai",
            #     "config": {"model": "textembedding-gecko@003"},
            # },
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
