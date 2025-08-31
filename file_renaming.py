import re

naming_patterns = [
    r"\s*[\(\[\-]?\s*Official Music Video\s*[)\]]?",
    r"\s*[\(\[\-]?\s*Official Video\s*[)\]]?",
    r"\s*[\(\[\-]?\s*Official Audio\s*[)\]]?",
    r"\s*[\(\[\-]?\s*Audio Officiel\s*[)\]]?",
    r"\s*[\(\[\-]?\s*Official Visualizer\s*[)\]]?",
    r"\s*[\(\[\-]?\s*Official Visualiser\s*[)\]]?",
    r"\s*[\(\[\-]?\s*from Arcane Season 2\s*[)\]]?",
    r"\s*[\(\[\-]?\s*Official MV\s*[)\]]?",
    r"\s*[\(\[\-]?\s*Official\s*[)\]]?",
    r'^\d+-',
]
compiled_patterns = re.compile("|".join(naming_patterns), re.IGNORECASE)


def process_file_name(name: str) -> str:
    name_without_annoying_patterns = compiled_patterns.sub("", name).strip()
    return sanitize_file_name(name_without_annoying_patterns)


def sanitize_file_name(name: str) -> str:
    return re.sub(r'[\\/:"*?<>|]+', '-', name)
