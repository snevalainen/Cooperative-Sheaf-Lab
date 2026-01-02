import os

# CONFIGURATION: Files/Folders to IGNORE
IGNORE_DIRS = {'.git', 'venv', 'env', '__pycache__', '.idea', '.vscode', 'build', 'dist', 'node_modules', 'target'}
IGNORE_FILES = {'.DS_Store', 'pack_codebase.py', 'codebase_snapshot.txt', 'poetry.lock', 'package-lock.json', 'yarn.lock'}
# Only include these file types (Adjust as needed)
ALLOWED_EXTENSIONS = {'.py', '.cpp', '.c', '.h', '.hpp', '.md', '.txt', '.json', '.yaml', '.yml', '.toml', '.sh', '.js', '.ts'}

OUTPUT_FILE = "codebase_snapshot.txt"

def pack_project():
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        # 1. Write the Directory Tree
        outfile.write("=== PROJECT DIRECTORY STRUCTURE ===\n")
        for root, dirs, files in os.walk('.'):
            # Filter directories in-place
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            level = root.replace('.', '').count(os.sep)
            indent = ' ' * 4 * (level)
            outfile.write(f"{indent}{os.path.basename(root)}/\n")
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                if f not in IGNORE_FILES:
                    outfile.write(f"{subindent}{f}\n")
        
        outfile.write("\n\n=== FILE CONTENTS ===\n")
        
        # 2. Write File Contents
        for root, dirs, files in os.walk('.'):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            for file in files:
                if file in IGNORE_FILES:
                    continue
                
                ext = os.path.splitext(file)[1]
                # Include allowed extensions OR exact filenames like Dockerfile
                if ext not in ALLOWED_EXTENSIONS and file != 'Dockerfile':
                    continue
                
                file_path = os.path.join(root, file)
                # Write Header
                outfile.write(f"\n{'='*20}\nFILE: {file_path}\n{'='*20}\n")
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())
                except Exception as e:
                    outfile.write(f"[Error reading file: {e}]")
                outfile.write("\n")

if __name__ == "__main__":
    pack_project()
    print(f"✅ Codebase packed into {OUTPUT_FILE}")