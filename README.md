# CrewaiGcp Crew

Welcome to the CrewaiGcp Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

1. If you haven't already, install Poetry:

    ```bash
    pip install poetry
    ```

1. reate and activate a virtual environment to isolate the dependencies from your global Python environment.  

    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```  

1. Navigate to your project directory and install the dependencies: Start by locking the dependencies and then installing them.

    
    ```bash
    poetry lock
    ```  
    and then

    ```bash
    poetry install
    ```

### Customizing  

- Modify `src/crewai_gcp/config/agents.yaml` to define your agents
- Modify `src/crewai_gcp/config/tasks.yaml` to define your tasks
- Modify `src/crewai_gcp/crew.py` to add your own logic, tools and specific args
- Modify `src/crewai_gcp/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
poetry run crewai_gcp
```

This command initializes the `crewai-gcp` Crew, assembling the `agents` and assigning them `tasks` as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The `crewai-gcp` Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.


## Addons 

### Gemini
The following libraries and configurations enable Gemini in CrewAI.  

1. For langchain support, install the following using `poetry`

```bash
poetry add langchain-core
poetry add langchain-google-vertexai
```

1. In `src/crewai_gcp/config/agents.yaml` you can configure each agent with Gemini support by adding `llm: gemini_llm` to each agent. See example below:   

    ```yaml
    researcher:
    llm: gemini_llm
    role: >
        {topic} Senior Data Researcher
    goal: >
        Uncover cutting-edge developments in {topic}
    backstory: >
        You're a seasoned researcher with a knack for uncovering the latest
        developments in {topic}. Known for your ability to find the most relevant
        information and present it in a clear and concise manner.
    ```

1. In `src/crewai_gcp/crew.py` add the following decorator `@llm` to define the Gemini model on Vertex AI.


### Traceloop
Add the following libraries to enable tracing in your application.

```bash
poetry add traceloop-sdk
poetry add opentelemetry-exporter-gcp-trace
```

## Support

For support, questions, or feedback regarding the CrewaiGcp Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
