from typing import List

from pydantic import BaseModel, validator


class TimeEntry(BaseModel):
    type: str
    value: int

    class Config:
        title = 'Класс для времени закрытия/открытия'

    @validator('type')
    def check_correct_type(cls, value: str):
        if value not in ['close', 'open']:
            raise ValueError('type должен быть close или open')
        return value


class OpeningHours(BaseModel):
    monday: List[TimeEntry]
    tuesday: List[TimeEntry]
    wednesday: List[TimeEntry]
    thursday: List[TimeEntry]
    friday: List[TimeEntry]
    saturday: List[TimeEntry]
    sunday: List[TimeEntry]

    class Config:
        title = 'Класс для дней недели'
