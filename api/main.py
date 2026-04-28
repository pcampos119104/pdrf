import tempfile
import os
from typing import Optional

from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel

from core.pdrf.pdr_flow import PdrFlow


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


@app.post("/recipes/process/unstructured", response_model=ProcessRecipeResponse)
def process_unstructured(request: ProcessRecipeRequest):
    """
    Process an unstructured recipe text and return structured recipe information.
    """
    try:
        pdrf = PdrFlow()
        result = pdrf.kickoff(inputs={"raw_recipe": request.raw_recipe})

        # Get the final result from the flow
        recipe_result = getattr(result, "raw", "") if result else ""

        return ProcessRecipeResponse(success=True, result=recipe_result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/recipes/process/pdf", response_model=ProcessRecipeResponse)
async def process_pdf(file: UploadFile = File(...)):
    try:
        if file.content_type != "application/pdf":
            raise HTTPException(status_code=400, detail="Only PDF files are allowed")

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            content = await file.read()
            temp_file.write(content)
            temp_path = temp_file.name

        try:
            # Process PDF to Markdown using marker-pdf
            from marker_pdf.convert import convert_single_pdf

            markdown = convert_single_pdf(temp_path, use_llm=True)
            return ProcessRecipeResponse(success=True, result=markdown)
        finally:
            # Clean up temporary file
            os.unlink(temp_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def kickoff():
    pdrf = PdrFlow()
    pdrf.kickoff()


if __name__ == "__main__":
    kickoff()
