from app.agent.parser import get_output_parser
from app.agent.prompt import PROMPT_TEMPLATE
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from app.config.settings import MODEL_NAME, TEMPERATURE

def create_agent(Prompt_template : str):

    print("creating agent ....")
    parser = get_output_parser()

    prompt = PromptTemplate(
        template=Prompt_template,
        input_variables=["input"],
        partial_variables={
            "format_instructions": parser.get_format_instructions()
            },
    )

    # print("The Full Pormpt is : \n")
    # print(prompt)

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=TEMPERATURE
    )

    agent = (
        {"input" : RunnablePassthrough()} | prompt | llm | parser
    )

    return agent