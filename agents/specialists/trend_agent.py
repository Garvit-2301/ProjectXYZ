from agents.base_agent import BaseAgent

TREND_PROMPT = """
You are a biometric trend analysis agent.

Analyze:
- fatigue accumulation
- workout consistency
- recovery patterns
- behavioral changes
- long-term wearable trends

Find meaningful correlations.
"""

class TrendAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            system_prompt=TREND_PROMPT
        )

    def analyze(self, profile):

        prompt = f"""
Analyze biometric trends:

{profile}
"""
        return self.run(prompt)