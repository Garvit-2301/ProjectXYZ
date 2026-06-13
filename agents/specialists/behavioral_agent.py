from agents.base_agent import BaseAgent

BEHAVIOR_PROMPT = """
You are a behavioral wearable intelligence agent.

Find:
- recurring patterns
- lifestyle correlations
- behavioral recovery insights
- consistency trends
"""

class BehavioralAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            system_prompt=BEHAVIOR_PROMPT
        )

    def analyze(self, profile):

        return self.run(
            f"Analyze behavioral patterns: {profile}"
        )