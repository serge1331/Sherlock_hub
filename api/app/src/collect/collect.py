from fastapi import APIRouter , HTTPException
from pydantic import BaseModel
from ..sentiment_analyzer import result
from ..Dataset_generator import DatasetGenerator as dsg

router = APIRouter()

class Keyword(BaseModel):
    keyword: str

@router.post("/collect" , tags=["collect"])
def collect(keyword: Keyword):
    
    neg , pos , sum , res = result(keyword.keyword)
    
    if not neg and not pos and not sum:
        raise HTTPException(status_code=400, detail="Model not found.")
    return {"negative": neg, "positive": pos, "summary": sum , "data": res }