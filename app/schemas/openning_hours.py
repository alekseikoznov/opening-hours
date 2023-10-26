from typing import List
from enum import Enum

from pydantic import BaseModel, Field


class RestaurantStatus(str, Enum):
    CLOSE = 'close'
    OPEN = 'open'


class TimeEntry(BaseModel):
    type: RestaurantStatus = Field(..., title='open or close')
    value: int = Field(..., title='time', ge=0, le=86399)

    class Config:
        title = 'Class for closing/opening time'


class OpeningHours(BaseModel):
    monday: List[TimeEntry]
    tuesday: List[TimeEntry]
    wednesday: List[TimeEntry]
    thursday: List[TimeEntry]
    friday: List[TimeEntry]
    saturday: List[TimeEntry]
    sunday: List[TimeEntry]

    class Config:
        title = 'Class for days of the week'
        schema_extra = {
           'example': {
                "monday": [],
                "tuesday": [
                 {
                    "type": "open",
                    "value": 36000
                 },
                 {
                  "type": "close",
                  "value": 64800
                 }
                ],
                "wednesday": [],
                "thursday": [
                 {
                  "type": "open",
                  "value": 37800
                 },
                 {
                  "type": "close",
                  "value": 64800
                 }
                ],
                "friday": [
                 {
                  "type": "open",
                  "value": 36000
                 }
                ],
                "saturday": [
                 {
                  "type": "close",
                  "value": 3600
                 },
                 {
                  "type": "open",
                  "value": 36000
                 }
                ],
                "sunday": [
                 {
                  "type": "close",
                  "value": 3600
                 },
                 {
                  "type": "open",
                  "value": 43200
                 },
                 {
                  "type": "close",
                  "value": 75600
                 }
                ]
              }
        }
