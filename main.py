from dotenv import load_dotenv
import os
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf import usa_engine
from pdf2 import origins_engine
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
# Load population data
population_path = os.path.join("data", "population.csv")
population_df = pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})

# Define tools
tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="this gives information at the world population and demographics",
        ),
    ),
    QueryEngineTool(
        query_engine=usa_engine,
        metadata=ToolMetadata(
            name="usa_data",
            description="this gives detailed information about usa the country",
        ),
    ),
    QueryEngineTool(
        query_engine=origins_engine,
        metadata=ToolMetadata(
            name="origins_data",
            description="this is a book written by Neil Degrasse Tyson named Origins",
        ),
    ),
]

# Initialize LLM and Agent
llm = OpenAI(model="gpt-4o-mini")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

# FastAPI App
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from all origins (change if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Request body model
class QueryRequest(BaseModel):
    prompt: str

@app.post("/query")
async def query_model(request: QueryRequest):
    """Endpoint to query the ReActAgent model."""
    try:
        result = agent.query(request.prompt)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "message": "Server is running"}

#uvicorn main:app --host 0.0.0.0 --port $PORT
#Use the above line to run the code
