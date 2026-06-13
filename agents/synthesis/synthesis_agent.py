from agents.base_agent import BaseAgent

SYNTHESIS_PROMPT = """
You are LifeBot.

Combine outputs from multiple wearable intelligence agents.

Generate:
- final coaching response
- concise recommendations
- meaningful insights
- unified reasoning

Avoid repitition.
Prioritize usefulness.
"""

class SynthesisAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            system_prompt=SYNTHESIS_PROMPT
        )

    def synthesize(self, query, recovery, workout, trend, sleep, stress, behavior):

        prompt = f"""

USER QUESTION:
{query}

RECOVERY AGENT:
{recovery}

WORKOUT AGENT:
{workout}

TREND AGENT:
{trend}

SLEEP AGENT:
{sleep}

STRESS AGENT:
{stress}

BEHAVIORAL AGENT:
{behavior}

Generate final LifeBot response.
"""
        
        return self.run(prompt)