import os
import cv2
import numpy as np
from PIL import Image

# Assuming faces is a previously defined object in dataset_creator
from dataset_creator import faces

recognizer = cv2.LBPHFaceRecognizer_create()
path = "dataset"


def get_images_with_id(path):
    if not os.path.exists(path):
        raise ValueError(f"The path {path} does not exist.")

    images_paths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []

    for single_image_path in images_paths:
        try:
            faceImg = Image.open(single_image_path).convert('L')
            faceNp = np.array(faceImg, np.uint8)
            id = int(os.path.split(single_image_path)[-1].split(".")[1])
            print(id)
            faces.append(faceNp)
            ids.append(id)
            cv2.imshow("Training", faceNp)
            cv2.waitKey(10)
        except Exception as e:
            print(f"Error processing {single_image_path}: {e}")

    cv2.destroyAllWindows()  # Clean up window display
    return np.array(ids), np.array(faces)  # Convert faces to a NumPy array


ids, faces = get_images_with_id(path)
recognizer.train(faces,id)
recognizer.save("recognizer/trainingdata.yml")
cv2.destroyAllWindows()