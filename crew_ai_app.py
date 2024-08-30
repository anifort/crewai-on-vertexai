from typing import Dict, List, Union
from src.crewai_gcp.crew import CrewaiGcpCrew
from traceloop.sdk import Traceloop
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from traceloop.sdk.decorators import workflow
from traceloop.sdk.instruments import Instruments

# from google.cloud import trace_v1 as trace

# client = trace.TraceServiceClient()


class CrewAIApp:

    def __init__(self, project: str, location: str) -> None:
        self.project_id = project
        self.location = location

    def set_up(self) -> None:
        Traceloop.init(
            app_name="CrewAI_Research",
            exporter=CloudTraceSpanExporter("sa-org-project"),
            instruments=[Instruments.VERTEXAI, Instruments.LANGCHAIN],
        )
        return

    @workflow(name="CrewAI_Trace")
    def query(self, question: str) -> Union[str, List[Union[str, Dict]]]:
        res = CrewaiGcpCrew().crew().kickoff(inputs={"topic": question})
        return res.__str__()
