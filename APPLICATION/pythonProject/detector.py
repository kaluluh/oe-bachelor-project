import cv2
import numpy as np
import torch
import torchvision as torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import ssl
from base64 import b64encode
import base64

ssl._create_default_https_context = ssl._create_unverified_context
# Torchvision SSL cert. expires constantly - https://github.com/pytorch/vision/issues/1876
# Fix - https://github.com/Cadene/pretrained-models.pytorch/issues/193#issuecomment-635730515

device = torch.device('cpu')


def load_model(num_classes):
    # Load the pre-trained Faster R-CNN model
    best_model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    # get the number of input features
    in_features = best_model.roi_heads.box_predictor.cls_score.in_features
    # replace the pre-trained head with a new one with required number of classes
    best_model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes)
    best_model.to(device).eval()
    # Load best model checkpoint
    checkpoint = torch.load('bestmodel_apr10_with_dataset_after_new_augmented.pt', map_location=device)
    best_model.load_state_dict(checkpoint['state_dict'])
    best_model.to(device).eval()
    return best_model


model = load_model(3)


# Define a function to perform object detection on an image
def detect_objects(image):
    # Define threshold value
    threshold = 0.5
    # Copy the image
    orig_image = image.copy()
    # BGR to RGB
    image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB).astype(np.float32)
    # Make the pixel range between 0 and 1
    image /= 255.0
    # Bring color channels to front
    image = np.transpose(image, (2, 0, 1)).astype(np.float32)
    # Convert to tensor
    image = torch.tensor(image, dtype=torch.float)
    # Add batch dimension
    image = torch.unsqueeze(image, 0)
    # Make a prediction on the image
    with torch.no_grad():
        predictions = model(image.to(device))

    predictions = [{k: v.to('cpu') for k, v in t.items()} for t in predictions]

    cv2.imshow('image', orig_image)

    # color = np.random.uniform(255, 0, 0)
    color = [0, 0, 255]
    # Convert the prediction to JSON
    prediction_list = []
    for i in range(len(predictions[0]["boxes"])):
        # Save the predicted object if is bigger than threshold value
        if predictions[0]["scores"][i].item() > threshold:
            # Show image
            box = predictions[0]["boxes"][i]
            cv2.rectangle(orig_image,
                          (int(box[0]), int(box[1])),
                          (int(box[2]), int(box[3])),
                          color, 2)
            cv2.putText(orig_image, 'malignant',
                        (int(box[0]), int(box[1] - 5)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color,
                        2, lineType=cv2.LINE_AA)

            cv2.imshow('image', orig_image)
            cv2.waitKey(1)
            # Save predictions
            # prediction_dict = {"class": predictions[0]["labels"][i].item(),
            #                    "score": predictions[0]["scores"][i].item(),
            #                    "bbox": predictions[0]["boxes"][i].tolist()}
            prediction_dict = {"class": "malignant",
                               "score": predictions[0]["scores"][i].item(),
                               "bbox": predictions[0]["boxes"][i].tolist()}
            prediction_list.append(prediction_dict)

    # encoded_image = b64encode(orig_image)
    jpg_img = cv2.imencode('.jpg', orig_image)
    b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    # encoded_image = base64.b64encode(orig_image)
    # return prediction_list, orig_image.tolist()
    return prediction_list, b64_string
