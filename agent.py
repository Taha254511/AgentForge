# from agno.agent import Agent #for openai api

# from agno.models.openai import OpenAIResponses
# from agno.models.groq import Groq

# from dotenv import load_dotenv


# load_dotenv()


# def build_agent():
#     return Agent(
#         model=OpenAIResponses(id="gpt-5-mini"),
#         markdown=True,
#         instructions="You are a helpful and expert travel agent."
#     )


# openai_agent = build_agent()

# openai_agent.print_response("My budget is 1L INR, should I travel to Goa or Phuket?")





# from agno.agent import Agent
# from agno.models.openai import OpenAIResponses
# from agno.models.groq import Groq

# from dotenv import load_dotenv

# load_dotenv()

# def build_agent():
#     return Agent(
#         model=Groq(id="openai/gpt-oss-120b"),
#         markdown=True,
#         instructions="You are a helpful and expert travel agent."
#     )

# agent = build_agent()

# agent.print_response("My budget is 1L INR, should I travel to Goa or Phuket?")





from agno.agent import Agent
from agno.models.groq import Groq

from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools # web search tool and it power the agent

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )

agent = build_agent()

agent.print_response("Is it safe to travel to UAE today?")