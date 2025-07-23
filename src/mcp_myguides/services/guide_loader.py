import httpx
from pathlib import Path
from typing import Union

async def load_guide_content(source: Union[str, Path], base_path: Path) -> str:
    """
    Loads guide content from a given source, which can be a local file path or a URL.
    """
    content = ""
    source_str = str(source)

    if source_str.startswith(('http://', 'https://')):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(source_str)
                response.raise_for_status()
                content = response.text
        except httpx.RequestError as e:
            print(f"Warning: Could not fetch remote guide {source}: {e}")
        except httpx.HTTPStatusError as e:
            print(f"Warning: HTTP error fetching remote guide {source}: {e}")
    else:
        file_path = base_path / source_str
        if file_path.is_file():
            content = file_path.read_text()
        else:
            print(f"Warning: Local guide file not found: {file_path}")
    return content
