from agents.base_agent import BaseAgent

WORKOUT_PROMPT = """
You are a workout intelligent agent.

Analyze:
- workout intensity
- cardiovascular load
- recovery interaction
- workout quality
- performance trends
- training strain
"""

class WorkoutAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            system_prompt=WORKOUT_PROMPT
        )
    
    def analyze(self, workouts):

        prompt = f"""
Analyze these workout activities:

{workouts}
"""
        return self.run(prompt)