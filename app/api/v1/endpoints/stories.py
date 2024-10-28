from fastapi import APIRouter, Depends, HTTPException, Request, Response
from typing import List, Optional
from uuid import UUID
import httpx
import json
from app.core.config import Settings

router = APIRouter()
settings = Settings()

@router.get("/stories", response_model=dict)
async def get_stories(
    search_value: str,
    limit: Optional[int] = None,
    page_size: Optional[int] = None,
    page_number: Optional[int] = None,
    sort_by: Optional[str] = None,
    descending: Optional[bool] = None
):
    """Fetch a list of stories with pagination and sorting"""
    headers = {
        "X-Domain": settings.DOMAIN,
        "X-API-Key": settings.API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{settings.API_URL}/stories",
            headers=headers,
            params={
                "search_value": search_value,
                "limit": limit,
                "page_size": page_size,
                "page_number": page_number,
                "sort_by": sort_by,
                "descending": descending
            }
        )
        return Response(
            content=response.text,
            status_code=response.status_code,
            headers=dict(response.headers)
        )
