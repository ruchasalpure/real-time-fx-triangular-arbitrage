from crewai import Agent

real_time_fx_triangular_arbitrage = Agent(
    role="Real Time Fx Triangular Arbitrage",
    goal="Deliver high-precision autonomous Real Time Fx Triangular Arbitrage operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
