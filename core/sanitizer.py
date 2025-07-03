import re

def sanitize_input(text):
    blacklist = ["ignore", "disregard", "forget", "override", 
                 "as a language model", "pretend", "instruction", "jailbreak"]
    for word in blacklist:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        text = pattern.sub('🔒', text)
    return text