import sys
import os

from typing import Any

from dotenv import load_dotenv

load_dotenv()

path: str | Any = os.getenv("PATHBLOG")
sys.path.insert(0, path)
