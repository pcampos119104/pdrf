from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from core.pdrf.flow import PdrFlow


class ProcessRecipeRequest(BaseModel):
    raw_recipe: str


class ProcessRecipeResponse(BaseModel):
    success: bool
    result: Optional[str] = None
    error: Optional[str] = None




# Create FastAPI app
app = FastAPI(
    title="PDRF Recipe Processor API",
    description="API for processing unstructured recipes using CrewAI",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "PDRF Recipe Processor API", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/recipes/process", response_model=ProcessRecipeResponse)
def process_recipe(request: ProcessRecipeRequest):
    """
    Process an unstructured recipe text and return structured recipe information.
    """
    try:
        pdrf = PdrFlow()
        print('#################################################################')
        print(request.raw_recipe)
        print('#################################################################')
        result = pdrf.kickoff(inputs={"raw_recipe": request.raw_recipe})

        # Get the final result from the flow
        recipe_result = getattr(result, "raw", "") if result else ""

        return ProcessRecipeResponse(success=True, result=recipe_result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def kickoff():
    pdrf = PdrFlow()
    pdrf.kickoff()


def plot():
    pdrf = PdrFlow()
    pdrf.plot()


def run_api():
    """
    Run the FastAPI server.
    """
    uvicorn.run("pdrf.main:app", host="0.0.0.0", port=8000, reload=True)


def run_with_trigger():
    """
    Run the flow with trigger payload.
    """
    import json
    import sys

    # Get trigger payload from command line argument
    if len(sys.argv) < 2:
        raise Exception(
            "No trigger payload provided. Please provide JSON payload as argument."
        )

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    # Create flow and kickoff with trigger payload
    # The @start() methods will automatically receive crewai_trigger_payload parameter
    pdrf = PdrFlow()

    try:
        result = pdrf.kickoff({"crewai_trigger_payload": trigger_payload})
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the flow with trigger: {e}")


if __name__ == "__main__":
    kickoff()
