from dotenv import load_dotenv
from agent import Agent, Runner  

load_dotenv()

agent = Agent(
    name="friendly_agent",
    instructions="You are a polite assistant that introduces yourself and greets the user warmly. (Message: Introduce yourself and say hi in one short sentence.)"
)

result = Runner.run_sync(agent, "Introduce yourself and say hi in one short sentence.")

print(result.final_output)