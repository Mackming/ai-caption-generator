import re

def parse_captions(raw_text, count):
    patterns = [
        r'\d+[\.\)]\s*(.+)',
        r'[-•*]\s*(.+)',
        r'\"([^\"]+)\"',
        r'^(.+)$'
    ]
    captions = []
    for pattern in patterns:
        if len(captions) >= count:
            break
        matches = re.findall(pattern, raw_text, re.MULTILINE)
        for match in matches:
            if isinstance(match, tuple):
                match = match[0]
            if match.strip() and len(match.split()) >= 3:
                captions.append(match.strip())
    return captions[:count]