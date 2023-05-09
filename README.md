# Empathizer-1430-final

There're three tasks specified in the `run.py`:
- Task 1: training a CNN from scratch 
- Task 2: training backbone model MobileNetV3Small with a classification head
- Task 3: training backbone model VGG16 with a classification head
- Task 4: training backbone model ResNet50 with a classification head


Download the dataset first before running the model:
https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset

You can run different model by:
```{bash}
python run.py --task 1
```
Can also find other possible arguments in `run.py`.

You can run the real-time facial expression detection demo by running `expression_detection.py`.

Note:

(1) `hyperparameter.py` includes non model-specific hyperparameters:  `img_size`, `num_classes`, `batch_size`, `preprocess_sample_size`, `num_ep_decrease`, `num_epochs`, `max_num_weights`.
Model-specific parameters are included in `models.py` in the constructor of each model.

(2) Added a scheduler in `run.py` to add more flexibility in changing learning rate along the training process, by increasing or decreasing learning rate after a certain number of epochs.

(3) There are different versions of MobileNet, can try different versions when training the model: MobileNetV2, MobileNetV3Small, MobileNetV3Large, etc.

