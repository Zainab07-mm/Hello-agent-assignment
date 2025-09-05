class Agent:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

    def run(self, prompt: str):
        return f"{self.name} says: {self.instructions} -> {prompt}"


class Runner:
    @staticmethod
    def run_sync(agent: Agent, prompt: str):
        response = agent.run(prompt)
        return type("Result", (), {"final_output": response})

