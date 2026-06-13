from agents.specialists.recovery_agent import  RecoveryAgent
from agents.specialists.workout_agent import WorkoutAgent
from agents.specialists.trend_agent import TrendAgent
from agents.specialists.sleep_agent import SleepAgent
from agents.specialists.stress_agent import StressAgent
from agents.specialists.behavioral_agent import BehavioralAgent
from agents.synthesis.synthesis_agent import SynthesisAgent


class Router:

    def __init__(self):

        self.recovery_agent = RecoveryAgent()
        self.workout_agent = WorkoutAgent()
        self.trend_agent = TrendAgent()
        self.sleep_agent = SleepAgent()
        self.stress_agent = StressAgent()
        self.behavior_agent = BehavioralAgent()
        self.synthesis_agent = SynthesisAgent()

    def run(self, query, profile):

        recovery_output = (
            self.recovery_agent.analyze(
                profile
            )
        )

        workout_output = (
            self.workout_agent.analyze(
                profile.get(
                    "workouts",
                    []
                )
            )
        )

        trend_output = (
            self.trend_agent.analyze(
                profile
            )
        )

        sleep_output = (
            self.sleep_agent.analyze(
                profile.get(
                    "wearable_raw_data",
                    {}
                ).get(
                    "sleep",
                    {}
                )
            )
        )

        stress_output = (
            self.stress_agent.analyze(
                profile.get(
                    "wearable_raw_data",
                    {}
                ).get(
                    "stress",
                    {}
                )
            )
        )

        behavior_output = (
            self.behavior_agent.analyze(
                profile
            )
        )

        final_response = (
            self.synthesis_agent.synthesize(
                query,
                recovery_output,
                workout_output,
                trend_output,
                sleep_output,
                stress_output,
                behavior_output
            )
        )


        return final_response