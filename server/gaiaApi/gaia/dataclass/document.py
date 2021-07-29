import sys
sys.path.append("..")

from typing import Dict, List, Optional
from dataclasses import dataclass, field, asdict

@dataclass
class Document:
    article: str
    date: str
    id: str
    snippet: str
    title: str
    url: str
    brand_entities: Optional[List[Dict]] = field(default_factory=list)
    sentiment: Optional[Dict] = field(default_factory=dict)
