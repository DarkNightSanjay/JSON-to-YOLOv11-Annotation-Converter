import os
import json

# Set up paths
folder_path = r"D:/dataset-conversion/ann"
output_labels_folder = os.path.join(folder_path, "Labels")
output_human_readable_folder = os.path.join(folder_path, "Labels_WithNames")
class_file_path = os.path.join(folder_path, "all_class_titles.txt")

# ✅ Load class mapping from all_class_titles.txt
class_mapping = {}
with open(class_file_path, "r", encoding="utf-8") as f:
    for line in f:
        if "->" in line:
            parts = line.strip().split("->")
            class_name = parts[0].strip()
            class_id = int(parts[1].strip())
            class_mapping[class_name] = class_id

# Print the loaded class mapping
print("\n Loaded Class Mapping from all_class_titles.txt:")
for name, cid in class_mapping.items():
    print(f"{name} -> {cid}")

# Create output folders
os.makedirs(output_labels_folder, exist_ok=True)
os.makedirs(output_human_readable_folder, exist_ok=True)

# Convert annotations to both YOLO and human-readable format
for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        json_path = os.path.join(folder_path, file_name)

        with open(json_path, 'r') as f:
            data = json.load(f)

        width = data["size"]["width"]
        height = data["size"]["height"]
        objects = data.get("objects", [])

        yolo_lines = []
        human_lines = []

        for obj in objects:
            class_name = obj.get("classTitle")
            if class_name not in class_mapping:
                print(f"⚠️ Unknown class '{class_name}' in {file_name}, skipping.")
                continue

            class_id = class_mapping[class_name]
            points = obj.get("points", {}).get("exterior", [])
            if len(points) != 2:
                continue

            (x1, y1), (x2, y2) = points
            x_min = min(x1, x2)
            y_min = min(y1, y2)
            w = abs(x2 - x1)
            h = abs(y2 - y1)
            x_center = x_min + w / 2
            y_center = y_min + h / 2

            # Normalize
            x_center /= width
            y_center /= height
            w /= width
            h /= height

            # Save to both formats
            yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}")
            human_lines.append(f"{class_name} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}")

        # Save YOLO-format label file
        label_file_name = file_name.replace(".json", ".txt")
        label_path = os.path.join(output_labels_folder, label_file_name)
        with open(label_path, "w") as f:
            f.write("\n".join(yolo_lines))

        # Save human-readable label file
        human_label_path = os.path.join(output_human_readable_folder, label_file_name)
        with open(human_label_path, "w") as f:
            f.write("\n".join(human_lines))

        print(f" Converted: {file_name} -> YOLO + human-readable")

print("\n All conversions complete!")
print(" YOLO labels saved to:", output_labels_folder)
print(" Human-readable labels saved to:", output_human_readable_folder)
print(" Used class list from:", class_file_path)
