import os
import fnmatch

def delete_image_files():
    # Get the current directory where the script is running
    current_directory = os.getcwd()
    
    # Define patterns for common image file formats
    image_patterns = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp', '*.tiff']
    
    # Count of deleted files
    deleted_files_count = 0
    
    # Loop through each pattern and delete matching image files
    for pattern in image_patterns:
        for root, dirs, files in os.walk(current_directory):
            for filename in fnmatch.filter(files, pattern):
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    deleted_files_count += 1
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

    if deleted_files_count == 0:
        print("No image files found to delete.")
    else:
        print(f"Total {deleted_files_count} image files deleted.")

if __name__ == "__main__":
    delete_image_files()
