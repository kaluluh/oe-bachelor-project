import nest_asyncio
import numpy as np
import uvicorn
import cv2
from fastapi import FastAPI, UploadFile, File
from detector import detect_objects
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    predictions, image_with_bboxes = detect_objects(image)

    # Return the predictions as JSON
    return {'predictions': predictions,
            'image': image_with_bboxes}


if __name__ == '__main__':
    nest_asyncio.apply()
    uvicorn.run(app)
