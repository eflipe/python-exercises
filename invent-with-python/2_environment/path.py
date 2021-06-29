from pathlib import Path
import os

print(Path('algo') / 'otro' / 'mas')

print(Path.home())

print(Path.cwd())
os.chdir('C:\\Windows\\System32')
print(Path.cwd())
