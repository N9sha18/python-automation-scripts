import os
import shutil

# The Problem: Downloads folder gets messy.
# The Solution: Organize files by extension.

def organize_directory(path):
    # Dictionary mapping file extensions to folder names
    extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp']
    }

    # Iterate over files in the directory
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        # Skip directories, only move files
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        
        # Find the category
        moved = False
        for folder_name, ext_list in extensions.items():
            if ext.lower() in ext_list:
                # Create folder if it doesn't exist
                folder_path = os.path.join(path, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                # Move the file
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} -> {folder_name}/")
                moved = True
                break
        
        if not moved and ext:
            # Optional: Move unknown files to 'Others'
            folder_path = os.path.join(path, 'Others')
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, filename))
            print(f"Moved: {filename} -> Others/")

if __name__ == "__main__":
    # For testing, you can change '.' to a specific path like 'C:/Users/Name/Downloads'
    print("Starting organization...")
    organize_directory('.')
    print("Done!")