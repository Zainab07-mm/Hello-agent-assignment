from dotenv import load_dotenv
from packaged_agent.agent import Agent, Runner  
load_dotenv()

agent = Agent(
    name="hello_agent",
    instructions="You are a concise assistant that greets the user."
)

if __name__ == "__main__":
    result = Runner.run_sync(agent, "Say hello in one short sentence.")
    print(result.final_output)

