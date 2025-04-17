# JSON-to-YOLOv11-Annotation-Converter
This Python script converts JSON-based bounding box annotations into the YOLOv11 format, using a predefined class mapping file. It also optionally generates human-readable label files with class names for easier debugging or review.

---

## ✅ Features

- Converts JSON annotations to YOLOv11 label format: `[class_id x_center y_center width height]`
- Supports normalized output for direct use in YOLO training
- Uses an external `all_class_titles.txt` file for mapping class names to YOLO class IDs
- Generates **two output versions**:
  - YOLO-compatible labels (numeric class IDs)
  - Human-readable labels (class names)

---

## 📁 Directory Structure

### dataset-conversion/ └── ann/ ├── all_class_titles.txt # Required class name-to-ID mapping ├── *.json # Your annotation files ├── Labels/ # Output YOLO labels (class IDs) └── Labels_WithNames/ # Output readable labels (class names)


---

## 🧾 Input: JSON Format

Each `.json` file must include:

```json
{
  "size": {
    "width": 1280,
    "height": 720
  },
  "objects": [
    {
      "classTitle": "car",
      "points": {
        "exterior": [[x1, y1], [x2, y2]]
      }
    }
  ]
}  ```

---

- `classTitle`: the label/class of the object

- `points.exterior`: two corner points of a bounding box

# Input: Class Mapping (all_class_titles.txt)

Must contain each class and its YOLO ID like so:

car -> 0
pedestrian -> 1
truck -> 2
...

- Ensure the class names exactly match those in your JSON files

- Any class not in this list will be skipped

# How to Use

- Place all your JSON files and `all_class_titles.txt` inside a folder (e.g. `D:/dataset-conversion/ann`)

- Set the `folder_pat`h variable in the script to match your directory

- Run the script:
`python Jsonconvert_3.py`

# Output

For each .json file, the script generates:


# Folder	                     Format	                            Use Case
`Labels/`	           YOLOv11 format `(class_id x y w h)`	      ✅ Model training
`Labels_WithNames/`	  Human-readable `(class_name x y w h)`	    🔍 Debugging & review

 ## Notes
- Class IDs are not auto-generated — they must be provided in all_class_titles.txt.

- Coordinates are normalized (0 to 1 range) for YOLO compatibility.

- The script automatically creates output folders if they don’t exist.
