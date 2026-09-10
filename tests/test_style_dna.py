import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'packages', 'schemas'))

from style_dna import StyleDNA

def test_style_dna_creation():
    dna = StyleDNA()
    dna.aesthetic = ["dark", "minimal"]
    dna.styles = ["dark_academia"]
    dna.confidence = 0.8
    
    data = dna.to_dict()
    assert data["aesthetic"] == ["dark", "minimal"]
    assert data["confidence"] == 0.8

def test_style_dna_from_dict():
    data = {
        "aesthetic": ["vintage", "grunge"],
        "styles": ["grunge"],
        "colors": ["black", "burgundy"],
        "confidence": 0.6
    }
    
    dna = StyleDNA.from_dict(data)
    assert dna.aesthetic == ["vintage", "grunge"]
    assert dna.colors == ["black", "burgundy"]
