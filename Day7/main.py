from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, Callable
from functools import partial
import re

@dataclass
class FileData:
    file_name: str
    file_size: int
    is_dir: bool
    parent: Optional[FileData] = field(default=None)
    children: List[FileData] = field(default_factory=list)

    @staticmethod
    def search(start_node: FileData, predicate: Callable[[FileData], bool]) -> Optional[FileData]:
        search_stack = [start_node]
        while len(search_stack):
            node = search_stack.pop()
            if predicate(node):
                return node
            
            search_stack += node.children

    @staticmethod
    def find_all(start_node: FileData, predicate: Callable[[FileData], bool]) -> List[FileData]:
        result = []
        search_stack = [start_node]
        while len(search_stack):
            node = search_stack.pop()
            if predicate(node):
                result.append(node)

            search_stack += node.children
        return result

    def get_total_size(self) -> int:
        if not self.is_dir:
            return self.file_size

        return sum(child.get_total_size() for child in self.children)
    

with open('input.txt',mode='r') as f:
    lines = f.readlines()

root = FileData('/', 0, True)

is_command = False
current_dir = root
for index,line in enumerate(lines[1:],start=1):
    if line.startswith('$ cd'):
        dirname = line.split(' ')[2].strip()
        if dirname == '..':
            current_dir = root if current_dir.parent is None else current_dir.parent
            dirname = current_dir.file_name
        data = FileData.search(current_dir, lambda fdata, dname=dirname: fdata.file_name == dname)
        if data is None:
            data = FileData(dirname, 0, True, current_dir)
            current_dir.children.append(data)
        current_dir = data
    else:
        if line.startswith('dir'):
            dirname = line.split(' ')[1].strip()
            data = FileData(dirname, 0, is_dir=True, parent=current_dir)
            current_dir.children.append(data)
        else:
            _match = re.match(r'\d+', line)
            if _match is not None:
                file_size, file_name = line.split(' ')
                file_data = FileData(file_name.strip(), int(file_size), False, current_dir)
                current_dir.children.append(file_data)

MAX_SIZE = 100000
TOTAL_SPACE = 70000000
MIN_REQUIRED_SPACE = 30000000

directories = FileData.find_all(root, lambda data: data.is_dir)
valid_dirs = list(filter(lambda dir, max_size=MAX_SIZE: dir.get_total_size() <= max_size, directories))

current_total_size = root.get_total_size()
unused_space = TOTAL_SPACE - current_total_size
to_free = MIN_REQUIRED_SPACE - unused_space

smallest_dir_to_delete = min(filter(lambda d: d.get_total_size() >= to_free, directories), key=lambda d: d.get_total_size())

print(f"part 1 result: {sum(x.get_total_size() for x in valid_dirs)}")
print(f"part 2 result: {smallest_dir_to_delete.get_total_size()}")