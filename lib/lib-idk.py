import os

def batch_rename(folder_path, old_ext, new_ext, base_name="file"):
    if not os.path.exists(folder_path):
        print("Folder path does not exist.")
        return
        
    count = 1
    for filename in os.listdir(folder_path):
        if filename.endswith(old_ext):
            # Create new name: e.g., folder/file_1.html
            new_name = f"{base_name}_{count}{new_ext}"
            src = os.path.join(folder_path, filename)
            dst = os.path.join(folder_path, new_name)
            
            os.rename(src, dst)
            print(f"Renamed: {filename} -> {new_name}")
            count += 1

# Example Usage:
# batch_rename("./my_folder", ".txt", ".html", "page")
