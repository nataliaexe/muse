"""
MUSE Style DNA Schema
"""

STYLE_DNA_SCHEMA = {
    "type": "object",
    "properties": {
        "aesthetic": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Main aesthetics (e.g., dark, minimal, vintage)"
        },
        "styles": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Specific styles (e.g., dark_academia, minimalism, grunge)"
        },
        "colors": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Preferred colors"
        },
        "patterns": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Preferred patterns (e.g., solid, plaid)"
        },
        "silhouettes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Preferred silhouettes (e.g., oversized, structured)"
        },
        "confidence": {
            "type": "number",
            "minimum": 0,
            "maximum": 1,
            "description": "Confidence score for the Style DNA"
        },
        "last_updated": {
            "type": "string",
            "format": "date-time",
            "description": "Last time the Style DNA was updated"
        }
    },
    "required": ["confidence"],
    "additionalProperties": True
}

class StyleDNA:
    """Style DNA class for MUSE platform"""
    
    def __init__(self):
        self.aesthetic = []
        self.styles = []
        self.colors = []
        self.patterns = []
        self.silhouettes = []
        self.confidence = 0.0
        self.last_updated = None
        self.additional_data = {}
        
    def to_dict(self):
        return {
            "aesthetic": self.aesthetic,
            "styles": self.styles,
            "colors": self.colors,
            "patterns": self.patterns,
            "silhouettes": self.silhouettes,
            "confidence": self.confidence,
            "last_updated": self.last_updated,
            **self.additional_data
        }
        
    @classmethod
    def from_dict(cls, data):
        instance = cls()
        instance.aesthetic = data.get("aesthetic", [])
        instance.styles = data.get("styles", [])
        instance.colors = data.get("colors", [])
        instance.patterns = data.get("patterns", [])
        instance.silhouettes = data.get("silhouettes", [])
        instance.confidence = data.get("confidence", 0.0)
        instance.last_updated = data.get("last_updated")
        instance.additional_data = {k: v for k, v in data.items() 
                                   if k not in ["aesthetic", "styles", "colors", 
                                               "patterns", "silhouettes", "confidence", 
                                               "last_updated"]}
        return instance
