from agents.base_agent import BaseAgent

RECOVERY_PROMPT = """
You are a wearable recovery intelligent agent.

Analyze:
- sleep quality
- stress
- HRV
- body battery
- readiness
- fatigue accumulation

Provide:
- recovery explanation
- fatigue insights
- actionable recommendations
"""

class RecoveryAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            system_prompt=RECOVERY_PROMPT
        )

    def analyze(self, profile):
        prompt = f"""
Analyze this recovery profile:

{profile}
"""
        return self.run(prompt)