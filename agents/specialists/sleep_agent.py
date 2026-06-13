from agents.base_agent import BaseAgent

SLEEP_PROMPT = """
You are a sleep intelligent agent.

Analyze:
- sleep quality
- recovery impact
- deep sleep
- REM patterns
- sleep consistency
"""

class SleepAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            system_prompt=SLEEP_PROMPT
        )
        
    def analyze(self, sleep_data):

        return self.run(
            f"Analyze sleep profile: {sleep_data}"
        )