# LifeBot: Advanced Wearable Intelligence System

**LifeBot** is an AI-powered conversational system that analyzes wearable biometrics from Garmin devices to provide intelligent insights on recovery, performance, sleep, stress, and behavioral patterns. It uses a multi-agent architecture with specialized agents to deliver actionable coaching recommendations.

## Features

- **Wearable Data Integration**: Connects directly to Garmin Connect to fetch comprehensive health profiles and biometric data
- **Recovery Optimization**: Analyzes recovery patterns and provides personalized recommendations
- **Sleep Analysis**: Interprets sleep quality and duration data for actionable insights
- **Stress Interpretation**: Detects stress patterns and suggests mitigation strategies
- **Workout Intelligence**: Analyzes workout performance and provides coaching feedback
- **Trend Detection**: Identifies long-term behavioral and performance trends
- **Fatigue Detection**: Monitors fatigue patterns and readiness levels
- **Natural Conversation**: Engage with LifeBot through natural language queries about your health data

## Project Structure

```
ProjectXYZ/
├── app.py                           # Main application entry point
├── requirements.txt                 # Python dependencies
│
├── agents/                          # Multi-agent system
│   ├── base_agent.py               # Base agent implementation
│   ├── orchestrator/
│   │   └── router.py               # Agent routing and orchestration
│   └── specialists/
│       ├── behavioral_agent.py      # Behavioral pattern analysis
│       ├── recovery_agent.py        # Recovery optimization
│       ├── sleep_agent.py           # Sleep analysis
│       ├── stress_agent.py          # Stress detection and management
│       ├── trend_agent.py           # Long-term trend analysis
│       └── workout_agent.py         # Workout performance analysis
│
├── connectors/
│   └── garmin_client.py             # Garmin Connect API integration
│
├── data/                            # Data storage directory
│
├── models/                          # Data models
│   ├── health_profile.py            # User health profile model
│   ├── recovery.py                  # Recovery metrics model
│   └── workout.py                   # Workout data model
│
├── normalization/
│   └── parser.py                    # Data normalization from Garmin
│
├── prompts/
│   └── system_prompt.py             # LifeBot system instructions
│
├── storage/
│   ├── db.py                        # Database initialization
│   └── memory.py                    # Agent memory management
│
└── utils/
    └── formatter.py                 # Output formatting utilities
```

## Installation

### Prerequisites
- Python 3.8+
- Garmin Connect account
- Google AI API key (for LLM integration)

### Setup

1. **Clone or download the project**
   ```bash
   cd ProjectXYZ
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root with your credentials:
   ```
   GARMIN_EMAIL=your_garmin_email@example.com
   GARMIN_PASSWORD=your_garmin_password
   GOOGLE_API_KEY=your_google_api_key
   ```

## Usage

Start LifeBot by running:
```bash
python app.py
```

The application will:
1. Connect to your Garmin account
2. Pull your complete health profile and wearable data
3. Normalize and process the data
4. Initialize all specialized agents
5. Launch an interactive conversation interface

Once running, simply type your questions about your health and fitness data:
```
You: How is my recovery looking?
You: What's affecting my sleep quality?
You: Analyze my workout performance
You: Show me stress trends
You: exit  # to quit
```

## Architecture

### Multi-Agent System

LifeBot uses a specialized multi-agent architecture where each agent focuses on a specific domain:

- **Behavioral Agent**: Identifies patterns in daily behaviors and habits
- **Recovery Agent**: Analyzes recovery metrics and provides optimization strategies
- **Sleep Agent**: Interprets sleep data and suggests improvements
- **Stress Agent**: Detects stress signals and recommends management techniques
- **Trend Agent**: Identifies long-term patterns across all metrics
- **Workout Agent**: Analyzes performance metrics and training effectiveness

The **Router** orchestrates these agents, directing queries to appropriate specialists and synthesizing their insights.

### Data Flow

```
Garmin Connect
     ↓
GarminClient (fetch raw data)
     ↓
GarminNormalizer (normalize data)
     ↓
Database Storage
     ↓
Router (process user query)
     ↓
Specialist Agents (analyze data)
     ↓
Synthesis Agent (combine insights)
     ↓
User Response
```

## Key Components

### GarminClient (`connectors/garmin_client.py`)
- Authenticates with Garmin Connect
- Fetches health profiles, workouts, sleep data, stress metrics, and more
- Handles API interactions securely

### GarminNormalizer (`normalization/parser.py`)
- Normalizes raw Garmin data into consistent formats
- Prepares data for agent consumption
- Validates and cleans incoming data

### Router (`agents/orchestrator/router.py`)
- Interprets user queries
- Routes to appropriate specialist agents
- Orchestrates multi-agent workflows

### Storage (`storage/db.py`, `storage/memory.py`)
- Persists user data and metrics
- Maintains agent memory and conversation history
- Enables longitudinal analysis

## Guidelines

LifeBot follows strict guidelines:
- ❌ Never diagnoses medical conditions
- ❌ Never pretends to be a medical professional
- ✅ Explains metrics in simple terms
- ✅ Correlates multiple data sources for insights
- ✅ Prioritizes actionable, concise recommendations
- ✅ Focuses on performance optimization and awareness

## Dependencies

Key libraries used:
- **LangGraph** / **LangChain**: AI/LLM orchestration
- **Garmin Connect**: Wearable data integration
- **SQLAlchemy**: Database ORM
- **Pydantic**: Data validation
- **Pandas/NumPy**: Data processing
- **Rich**: Terminal formatting

See `requirements.txt` for complete dependency list.

## Future Enhancements

- Web interface for data visualization
- Historical trend reporting
- Personalized coaching plans
- Integration with other wearable platforms
- Advanced predictive analytics
- Export capabilities (PDF reports, CSV data)

## License

[Add your license information here]

## Support

For issues or questions, please [add contact information or repository link]
