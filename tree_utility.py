#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import argparse
from typing import List, Optional

def list_files(
    startpath: str, 
    show_hidden: bool = False, 
    level: int = 0, 
    max_depth: Optional[int] = None
) -> None:
    if max_depth is not None and level > max_depth:
        return

    for root, dirs, files in os.walk(startpath):
        if not show_hidden:
            files = [f for f in files if not f.startswith('.')]
            dirs[:] = [d for d in dirs if not d.startswith('.')]

        if level == 0:
            print(root)
        else:
            indent = '  ' * (level - 1)
            print(f'{indent}{os.path.basename(root)}')

        sub_indent = '  ' * level
        for file in files:
            print(f'{sub_indent}{file}')

        for d in dirs:
            list_files(os.path.join(root, d), show_hidden, level + 1, max_depth)

def main() -> None:
    parser = argparse.ArgumentParser(description="Python утилита для отображения дерева каталогов")
    parser.add_argument("directory", nargs='?', default='.', help="Каталог для отображения (по умолчанию: текущий каталог)")
    parser.add_argument("-a", "--all", action="store_true", help="Показать скрытые файлы и каталоги")
    parser.add_argument("-d", "--max-depth", type=int, help="Максимальная глубина отображения")
    args = parser.parse_args()

    directory: str = args.directory
    show_hidden: bool = args.all
    max_depth: Optional[int] = args.max_depth

    if not os.path.isdir(directory):
        print(f"Ошибка: '{directory}' не является каталогом.")
        return

    print(f"Структура каталога для '{directory}':")
    list_files(directory, show_hidden, max_depth=max_depth)

if __name__ == "__main__":
    main()
