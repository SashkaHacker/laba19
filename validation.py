from datetime import datetime

from pydantic import BaseModel, field_validator
from typing import List


class Worker(BaseModel):
    surname: str
    name: str
    phone: int
    date: List[str]

    @field_validator('date')
    def validate_date_parts(cls, v):
        if len(v) != 3:
            raise ValueError(
                'Expected a list of 3 elements representing a date.')

        try:
            day, month, year = map(int, v)
            date = datetime(day=day, month=month, year=year)
        except ValueError as e:
            raise ValueError(f'Error parsing date: {e}')

        if not (datetime.min < date < datetime.now()):
            raise ValueError('Date is out of acceptable range.')
        return v


class ListWorkers(BaseModel):
    lst: List[Worker]