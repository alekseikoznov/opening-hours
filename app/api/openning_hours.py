from app.schemas.openning_hours import OpeningHours
from app.services.format_openning_hours import week_opening_hour

from fastapi import APIRouter

router = APIRouter()


@router.post('/opening_hours', tags=['Openning Hours'])
async def render_opening_hours(opening_hours: OpeningHours) -> dict:
    formatted_hours = week_opening_hour(opening_hours)
    return formatted_hours
