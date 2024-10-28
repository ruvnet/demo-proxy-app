from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
from typing import List, Optional
import httpx
import json
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.stories import StoryResponse, StoryListResponse, StoryCreate, Story
from app.api.deps import get_db, get_current_user, CurrentUser
from app.crud.story import story
from app.core.config import Settings
from app.models.stories import Story as StoryModel

router = APIRouter()
settings = Settings()

def add_custom_headers():
    return {
        "X-Domain": settings.DOMAIN,
        "X-API-Key": settings.API_KEY,
        "X-User-ID": "1",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }

@router.get("/stories")
async def get_stories(
    request: Request,
    db: Session = Depends(get_db),
    search_value: str = Query(..., description="Search term"),
    limit: Optional[int] = None,
    page_size: Optional[int] = None,
    page_number: Optional[int] = None,
    sort_by: Optional[str] = None,
    descending: Optional[bool] = None,
):
    """Proxy stories request to Capitol AI API and cache results"""
    # Construct query parameters
    params = {
        "search_value": search_value,
        "limit": limit,
        "page_size": page_size, 
        "page_number": page_number,
        "sort_by": sort_by,
        "descending": descending
    }
    # Remove None values
    params = {k: v for k, v in params.items() if v is not None}
    
    headers = add_custom_headers()
    
    # Make request to Capitol API
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{settings.API_URL}/api/v1/stories",
            params=params,
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            
            # Save stories to local DB
            for story_data in data.get("stories", []):
                # Check if story exists
                existing = db.query(StoryModel).filter(StoryModel.id == story_data["id"]).first()
                
                if existing:
                    # Update existing story
                    for key, value in story_data.items():
                        setattr(existing, key, value)
                else:
                    # Create new story
                    new_story = StoryModel(**story_data)
                    db.add(new_story)
                
            try:
                db.commit()
            except Exception as e:
                db.rollback()
                print(f"Error saving to database: {e}")
        
        return Response(
            content=response.text,
            status_code=response.status_code,
            headers={"Content-Type": "application/json"}
        )

@router.post("/stories")
async def create_story(
    request: Request,
    db: Session = Depends(get_db)
):
    """Proxy story creation to Capitol AI API and save locally"""
    body = await request.body()
    headers = add_custom_headers()
    
    # Make request to Capitol API
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.API_URL}/api/v1/stories",
            content=body,
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            
            # Parse request body
            story_data = json.loads(body)
            
            try:
                # Create story in local DB
                new_story = StoryModel(**story_data)
                db.add(new_story)
                db.commit()
            except Exception as e:
                db.rollback()
                print(f"Error saving to database: {e}")
        
        return Response(
            content=response.text,
            status_code=response.status_code,
            headers={"Content-Type": "application/json"}
        )
