class Agent:
    def __init__(self, name: str, instructions: str):
        self.name = name
        self.instructions = instructions

    def generate_response(self, prompt: str) -> str:
        """
        A simple fake response generator for testing.
        In a real project, this would call an AI model.
        """
        if "hello" in prompt.lower():
            return "Hello! Nice to meet you."
        return "I'm here and ready to help."


class Runner:
    @staticmethod
    def run_sync(agent: Agent, prompt: str):
        """
        Runs the agent synchronously and returns a result object.
        """
        class Result:
            def __init__(self, output):
                self.final_output = output

        response = agent.generate_response(prompt)
        return Result(response)
