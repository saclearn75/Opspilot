import json
import re
from typing import List, Optional

from backend.app.schemas.internal import ParsedDocument, ParsedDocumentMetadata

def parse_markdown_artifact(file_path: str) -> Optional[ParsedDocument]:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split on first --- pair
    parts = re.split(r'^---', content, 2, re.MULTILINE)
    
    if len(parts) < 3: # Not enough parts for metadata + body
        return None

    metadata_str = parts[1].strip()
    body = parts[2].strip()

    try:
        metadata_dict = json.loads(metadata_str)
        metadata = ParsedDocumentMetadata(**metadata_dict)
    except json.JSONDecodeError:
        return None
    except ValueError:
        return None

    return ParsedDocument(metadata=metadata, body=body, file_path=file_path)