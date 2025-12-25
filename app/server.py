from fastapi import FastAPI
from langserve import add_routes

from app.agent.agent import create_agent
from app.agent.prompt import PROMPT_TEMPLATE, NORMALIZE_PROMPT_TEMPLATE
from app.agent.parser import get_output_parser
from app.pipeline.api_runnable import run_api


print("Starting FastAPI server...")

app = FastAPI(title="Create product information")


def build_pipeline():
    print("creating agent ....")

    extract_agent = create_agent(
        Prompt_template=PROMPT_TEMPLATE,
    )

    normalize_agent = create_agent(
        Prompt_template=NORMALIZE_PROMPT_TEMPLATE,
    )

    return run_api(extract_agent, normalize_agent)


pipeline = build_pipeline()

add_routes(
    app,
    pipeline,
    path="/extract"
)
