# Copyright © 2020 by Spectrico
# Licensed under the MIT License

import numpy as np
import MNN
import json
import cv2

def load_labels(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f.readlines()]

class Classifier():
    def __init__(self):
        self.interpreter = MNN.Interpreter("model-weights-spectrico-car-brand-recognition-mobilenet_v3-224x224-170620.mnn")
        self.session = self.interpreter.createSession()
        self.input_tensor = self.interpreter.getSessionInput(self.session)
        self.labels = load_labels('labels.txt')

    def predict(self, image):
        # change to rgb format
        image = image[..., ::-1]
        image = cv2.resize(image, (224, 224))
        image = image.astype(float)

        # preprocess image
        image = image - (127.5, 127.5, 127.5)
        image = image * (0.00784, 0.00784, 0.00784)

        # cv2 read shape is NHWC, Tensor's need is NCHW,transpose it
        image = image.transpose((2, 0, 1))

        # convert image to float32 instead of float64, otherwise MNN will throw an error
        image = image.astype(np.float32)

        # construct tensor from np.ndarray
        tmp_input = MNN.Tensor((1, 3, 224, 224), MNN.Halide_Type_Float, image, MNN.Tensor_DimensionType_Caffe)
        self.input_tensor.copyFrom(tmp_input)
        self.interpreter.runSession(self.session)
        output_tensor = self.interpreter.getSessionOutput(self.session)
        preds = output_tensor.getData()
        if isinstance(preds, np.ndarray):
            preds = preds[0]

        top = 3
        top_indices = np.array(preds).argsort()[-top:][::-1]
        classes = []
        for ix in top_indices:
            classes.append({"brand": self.labels[ix], "prob": str(float(np.array(preds)[ix]))})
        return(classes)
