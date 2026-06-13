from agents.base_agent import BaseAgent

STRESS_PROMPT = """
You are a stress analysis intelligence agent.

Analyze:
- stress load
- nervous system strain
- stress impact on performance
- recovery interaction
"""

class StressAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            system_prompt=STRESS_PROMPT
        )

    def analyze(self, stress_data):

        return self.run(
            f"Analyze stress profile: {stress_data}"
        )
    