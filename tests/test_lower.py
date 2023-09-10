import sys
from pathlib import Path


file = Path(__file__).resolve()
print("\nThis is the file: ", file)
parent, root = file.parent, file.parents[1]
print("\nThis is the parent: ", parent)
print("\nThis is the root: ", root)
sys.path.append(str(root))

from app.lower_text import LowerText


def test_lower_text():
    lt = LowerText()
    text_ = lt.lower_text("THIS IS THE TEXT")
    
    text_expected = 'this is the text'
    
    assert text_ == text_expected



if __name__ == '__main__':
    print(sys.path)
    