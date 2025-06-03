import pytest
import sys
import os

path = sys.argv[1]
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

if os.path.isfile(path):
    pytest.main([path])
