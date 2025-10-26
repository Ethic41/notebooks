# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: notebooks
#     language: python
#     name: python3
# ---

# %%
# #!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2025-07-28 11:24:06
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.grok import GrokProvider
import nest_asyncio

nest_asyncio.apply()

# %%
grok = OpenAIModel("grok-3-latest", provider=GrokProvider()) 

roulette_agent = Agent(
    grok,
    deps_type=int,
    output_type=bool,
    system_prompt=(
        "User the `roulette_wheel` function to see if the"
        "customer has won based the number they provide."
    ),
)

@roulette_agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str:
    """Check if the square is a winner"""
    return "winner" if square == ctx.deps else "loser"

# run the agent
success_number = 18
result = roulette_agent.run_sync('Put my money on square 18', deps=success_number)
print(f"Result: {result.output}")

result1 = roulette_agent.run_sync('Put my money on square 19', deps=success_number)
print(f"Result: {result1.output}")


# %%

# %%

# %%

# %%

# %%

agent = Agent("deepseek:deepseek-chat")

result1 = agent.run_sync("who was albert einstein")
print(result1.output)


# %%
result2 = agent.run_sync("what was his famous equation")
print(result2.output)

result3 = agent.run_sync("how old was he when he died?", message_history=result1.new_messages())
print(result3.output)

# %%
from datetime import date

from pydantic_ai import Agent, RunContext

agent = Agent(
    'deepseek:deepseek-chat',
    deps_type=str,  
    instructions="Use the customer's name while replying to them, also tell them the meaning of their name.",
)


@agent.instructions  
def add_the_users_name(ctx: RunContext[str]) -> str:
    return f"Please greet the user with their name and also tell them the meaning of their name afterwards. The user's name is {ctx.deps}."


@agent.instructions
def add_the_date() -> str:  
    return f'The date is {date.today()}.'


result = agent.run_sync('What is the date?', deps='Tahir')
print(result.output)

# %%
