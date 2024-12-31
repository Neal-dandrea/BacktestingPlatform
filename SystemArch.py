from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis('off')

# Helper function to draw components
def draw_component(ax, x, y, width, height, label, color):
    rect = Rectangle((x, y), width, height, edgecolor='black', facecolor=color, lw=1.5)
    ax.add_patch(rect)
    ax.text(x + width / 2, y + height / 2, label, fontsize=10, ha='center', va='center', wrap=True)

# Set plot limits
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)

# Draw frontend
draw_component(ax, 4, 8, 4, 2, 'Frontend (React)', 'lightblue')

# Draw backend
draw_component(ax, 4, 5, 4, 2, 'Backend (Node.js)', 'lightgreen')

# Draw databases
draw_component(ax, 0, 2, 4, 2, 'Relational Database\n(PostgreSQL/InfluxDB)', 'orange')
draw_component(ax, 8, 2, 4, 2, 'Graph Database\n(Neo4j)', 'yellowgreen')

# Draw external APIs
draw_component(ax, 0, 5, 4, 2, 'External APIs\n(Alpha Vantage, Quandl, Binance)', 'yellow')

# Draw ML/AI Models
draw_component(ax, 8, 5, 4, 2, 'ML/AI Models\n(Reinforcement Learning, Forecasting)', 'pink')

# Draw user roles
draw_component(ax, 2, 10, 2, 1, 'Admin Role', 'lightgrey')
draw_component(ax, 8, 10, 2, 1, 'Trader/Researcher', 'lightgrey')

# Draw arrows
arrow_params = dict(color='black', width=0.02, head_width=0.3, length_includes_head=True)

# Arrows from users to frontend
ax.add_patch(FancyArrow(3, 10, 1, -2, **arrow_params))  # Admin -> Frontend
ax.add_patch(FancyArrow(9, 10, -1, -2, **arrow_params))  # Trader -> Frontend

# Arrows from frontend to backend
ax.add_patch(FancyArrow(6, 8, 0, -1, **arrow_params))

# Arrows from backend to databases
ax.add_patch(FancyArrow(6, 5, -3, -2, **arrow_params))  # Backend -> Relational DB
ax.add_patch(FancyArrow(6, 5, 3, -2, **arrow_params))  # Backend -> Graph DB

# Arrows from backend to APIs and ML models
ax.add_patch(FancyArrow(4, 5.5, -2, 0, **arrow_params))  # Backend -> APIs
ax.add_patch(FancyArrow(8, 5.5, 2, 0, **arrow_params))  # Backend -> ML Models

# Arrows from APIs and ML models to backend
ax.add_patch(FancyArrow(2, 5.5, 2, 0, **arrow_params))  # APIs -> Backend
ax.add_patch(FancyArrow(10, 5.5, -2, 0, **arrow_params))  # ML Models -> Backend

# Save diagram
plt.savefig('System_Architecture_Diagram.png', dpi=300, bbox_inches='tight')
plt.show()
