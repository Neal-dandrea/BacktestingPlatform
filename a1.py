# Update the system architecture diagram to include both graph-based and traditional databases
diagram = Digraph(name="BacktestingPlatformHybridArchitecture", format="png")
diagram.attr(rankdir="TB", fontsize="10", nodesep="1", ranksep="1.5")

# Frontend
diagram.node("Frontend", "Frontend (React)", shape="box", style="filled", color="lightblue")

# Backend
diagram.node("Backend", "Backend (Node.js)", shape="box", style="filled", color="lightgreen")

# Databases
diagram.node("PostgreSQL", "Relational Database (PostgreSQL/InfluxDB)", shape="cylinder", style="filled", color="orange")
diagram.node("GraphDB", "Graph Database (Neo4j)", shape="cylinder", style="filled", color="yellowgreen")

# External APIs
diagram.node("APIs", "External APIs\n(Alpha Vantage, Quandl, Binance)", shape="box", style="filled", color="yellow")

# ML/AI Models
diagram.node("ML", "ML/AI Models\n(Reinforcement Learning, Forecasting)", shape="box", style="filled", color="pink")

# User Roles
diagram.node("Admin", "Admin Role\n(Manage Features)", shape="ellipse", style="filled", color="lightgrey")
diagram.node("Trader", "Trader/Researcher\n(Use Features)", shape="ellipse", style="filled", color="lightgrey")

# Connections
diagram.edges([
    ("Admin", "Frontend"),
    ("Trader", "Frontend"),
    ("Frontend", "Backend"),
    ("Backend", "PostgreSQL"),
    ("Backend", "GraphDB"),
    ("Backend", "APIs"),
    ("Backend", "ML"),
    ("APIs", "Backend"),
    ("ML", "Backend"),
    ("GraphDB", "Backend"),
    ("PostgreSQL", "Backend")
])

# Add labels to represent system workflow
diagram.attr(label="Hybrid Architecture for Backtesting Platform\n", fontsize="16")

# Render the diagram as an SVG for broader compatibility
diagram_path_svg = "/mnt/data/BacktestingPlatformHybridArchitecture.svg"
diagram.render(diagram_path_svg, view=False)
diagram_path_svg


