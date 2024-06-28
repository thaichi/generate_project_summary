import os
import fnmatch

def is_ignored(path, project_dir, gitignore_patterns, additional_ignore_patterns, excluded_items):
    relative_path = os.path.relpath(path, project_dir)
    if relative_path in excluded_items:
        return True
    for pattern in gitignore_patterns + additional_ignore_patterns:
        pattern = f"*{pattern}*"
        if fnmatch.fnmatch(relative_path, pattern) or fnmatch.fnmatch(f'{os.sep}{relative_path}', pattern):
            return True
    return False

def read_gitignore(project_dir):
    gitignore_path = os.path.join(project_dir, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as file:
            patterns = [line.strip() for line in file if line.strip() and not line.startswith('#')]
            expanded_patterns = []
            for pattern in patterns:
                expanded_patterns.append(pattern)
                if '/' in pattern:
                    expanded_patterns.append(pattern.replace('/', '\\'))
                if '\\' in pattern:
                    expanded_patterns.append(pattern.replace('\\', '/'))
            return expanded_patterns
    return []