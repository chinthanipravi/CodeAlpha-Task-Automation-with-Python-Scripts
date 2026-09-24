import os
import shutil


def move_jpg_files(source_dir, target_dir):
    """Moves all .jpg and .jpeg files from source_dir to target_dir."""
    # Create the target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Created target folder: '{target_dir}'")

    moved_count = 0

    # Scan all files in the source directory
    for filename in os.listdir(source_dir):
        if filename.lower().endswith((".jpg", ".jpeg")):
            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(target_dir, filename)

            # Move the file
            shutil.move(source_path, target_path)
            print(f"Moved: {filename}")
            moved_count += 1

    print(
        f"\nAutomation Complete: Successfully moved {moved_count} .jpg file(s)."
    )


if __name__ == "__main__":
    # Define folder paths
    SOURCE_FOLDER = "./my_photos"
    TARGET_FOLDER = "./jpg_backup"

    move_jpg_files(SOURCE_FOLDER, TARGET_FOLDER)