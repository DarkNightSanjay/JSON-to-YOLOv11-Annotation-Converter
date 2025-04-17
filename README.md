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

