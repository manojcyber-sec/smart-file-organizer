import os
import shutil

# change this path to the folder you want to organize
TARGET_FOLDER = "test_folder"


FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".py", ".c", ".cpp", ".java", ".js"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"]
}


def organize_folder(path):
    if not os.path.exists(path):
        print("Folder not found.")
        return

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)

        moved = False

        for folder, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                dest_folder = os.path.join(path, folder)
                os.makedirs(dest_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved {filename} → {folder}/")
                moved = True
                break

        if not moved:
            other = os.path.join(path, "Others")
            os.makedirs(other, exist_ok=True)
            shutil.move(file_path, os.path.join(other, filename))
            print(f"Moved {filename} → Others/")


if __name__ == "__main__":
    organize_folder(TARGET_FOLDER)
    print("\nDone organizing.")
