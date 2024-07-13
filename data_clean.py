import os
from pathlib import Path


def update_class_id(label_dir, target_class_name, new_class_id):
    """
    Update the class ID in label files for a given target class name.

    Args:
        label_dir (str): Path to the directory containing label files.
        target_class_name (str): The target class name to update.
        new_class_id (int): The new class ID to set.
    """
    for label_file in Path(label_dir).rglob("*.txt"):
        with open(label_file, 'r') as file:
            lines = file.readlines()

        updated_lines = []
        for line in lines:
            parts = line.strip().split()
            class_id, x_center, y_center, width, height = parts
            class_id = int(class_id)

            # Update class_id if it matches the target_class_name
            if class_id == 0:
                # Check if the file name contains the target class name
                class_id = new_class_id


            updated_line = f"{class_id} {x_center} {y_center} {width} {height}\n"
            updated_lines.append(updated_line)

        with open(label_file, 'w') as file:
            file.writelines(updated_lines)
        print(f"Updated {label_file}")


if __name__ == "__main__":
    label_dir = 'C:\\Mydrive\\datasetcoke\\Coca-Cola.v5i.yolov8\\valid\\labels'
    target_class_name = 'coca'  # This assumes 'coca' is part of the filename for CocaCola images
    new_class_id = 1

    update_class_id(label_dir, target_class_name, new_class_id)
