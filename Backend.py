from fastapi import FastAPI, HTTPException, UploadFile, Form
from pydantic import BaseModel
from typing import List

# Initialize FastAPI app
app = FastAPI()

# Models
class User(BaseModel):
    id: int
    name: str
    email: str

class Strategy(BaseModel):
    id: int
    name: str
    description: str

class BacktestResult(BaseModel):
    id: int
    strategy_id: int
    performance: dict

# In-memory database (for simplicity in this example)
users = []
strategies = []
backtests = []

# User Endpoints
@app.post("/users/register")
def register_user(user: User):
    users.append(user)
    return {"message": "User registered successfully!", "user": user}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Strategy Endpoints
@app.post("/strategies")
def create_strategy(strategy: Strategy):
    strategies.append(strategy)
    return {"message": "Strategy created successfully!", "strategy": strategy}

@app.get("/strategies")
def list_strategies():
    return strategies

@app.get("/strategies/{strategy_id}")
def get_strategy(strategy_id: int):
    strategy = next((s for s in strategies if s.id == strategy_id), None)
    if not strategy:
        raise HTTPException(status_code=404, detail="Strategy not found")
    return strategy

# Backtesting Endpoints
@app.post("/backtests")
def run_backtest(strategy_id: int, performance: dict = Form(...)):
    result_id = len(backtests) + 1
    result = BacktestResult(id=result_id, strategy_id=strategy_id, performance=performance)
    backtests.append(result)
    return {"message": "Backtest executed successfully!", "result": result}

@app.get("/backtests")
def list_backtests():
    return backtests

@app.get("/backtests/{backtest_id}")
def get_backtest(backtest_id: int):
    backtest = next((b for b in backtests if b.id == backtest_id), None)
    if not backtest:
        raise HTTPException(status_code=404, detail="Backtest not found")
    return backtest

# File Upload Endpoint
@app.post("/data/upload")
def upload_data(file: UploadFile):
    return {"filename": file.filename, "message": "File uploaded successfully!"}

# Run with: uvicorn <filename>:app --reload
