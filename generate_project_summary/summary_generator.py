import os
from gui import run_gui_file_selector
from file_utils import is_binary, read_file_contents
from ignore_patterns import is_ignored, read_gitignore

def generate_project_summary(project_dir):
    project_name = os.path.basename(project_dir)
    summary = f'# {project_name}\n\n## Directory Structure\n\n'

    gitignore_patterns = read_gitignore(project_dir)
    additional_ignore_patterns = ['generate_project_summary.py', f'{project_name}_project_summary.txt', '.git']

    file_contents_section = "\n## File Contents\n\n"

    excluded_items = run_gui_file_selector(project_dir)

    def traverse_directory(root, level):
        nonlocal summary, file_contents_section
        indent = '  ' * level
        relative_path = os.path.relpath(root, project_dir)
        if not is_ignored(relative_path, project_dir, gitignore_patterns, additional_ignore_patterns, excluded_items):
            summary += f'{indent}- {os.path.basename(root)}/\n'

            subindent = '  ' * (level + 1)
            items = sorted(os.listdir(root), key=lambda x: (not os.path.isdir(os.path.join(root, x)), x))
            for item in items:
                if item == '.gitignore':
                    continue
                item_path = os.path.join(root, item)
                if os.path.isdir(item_path):
                    if not is_ignored(item_path, project_dir, gitignore_patterns, additional_ignore_patterns, excluded_items):
                        traverse_directory(item_path, level + 1)
                else:
                    if not is_ignored(item_path, project_dir, gitignore_patterns, additional_ignore_patterns, excluded_items):
                        if not is_binary(item_path):
                            summary += f'{subindent}- {item}\n'
                            content = read_file_contents(item_path)
                            if content.strip():
                                relative_file_path = os.path.relpath(item_path, project_dir)
                                file_contents_section += f'### {relative_file_path}\n\n```\n{content}\n```\n\n'
                        else:
                            summary += f'{subindent}- {item} (binary file)\n'

    traverse_directory(project_dir, 0)

    with open(f'{project_name}_project_summary.txt', 'w', encoding='utf-8') as file:
        file.write(summary + file_contents_section)