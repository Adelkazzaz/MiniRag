from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
    file_id: Optional[str] = None
    chunk_size: Optional[int] = 128
    overlap_size: Optional[int] = 20
    do_reset: Optional[bool] = 0