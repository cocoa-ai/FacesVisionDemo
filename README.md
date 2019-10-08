# Faces Vision Demo

iOS11 demo application for age and gender classification of facial images using `Vision` and `CoreML`.

<div align="center">
<img src="https://github.com/cocoa-ai/FacesVisionDemo/blob/master/Screenshot.png" alt="FacesVisionDemo" width="300" height="464" />
</div>

## Model

This demo is based on the age, gender and emotion neural network classifiers,
which were converted from `Caffe` models to `CoreML` models using [coremltools](https://pypi.python.org/pypi/coremltools) python package.

### Age classification

- [Paper](http://www.openu.ac.il/home/hassner/projects/cnn_agegender/)
- [CoreML model](https://drive.google.com/file/d/1PLkI4Jyg086JlvTzwHHI5EbGWgJI-Atv/view?usp=sharing)

### Gender classification

- [Paper](http://www.openu.ac.il/home/hassner/projects/cnn_agegender/)
- [CoreML model](https://drive.google.com/file/d/1IxU0E1EDjuL-sbY3wd5Wh6BsXTbYTScb/view?usp=sharing)

### Emotion Recognition

- [Paper](http://www.openu.ac.il/home/hassner/projects/cnn_emotions/)
- [CoreML model](https://drive.google.com/file/d/1ElCJvnEvhtIxZkyEzVUAFPJAMgyBXo57/view?usp=sharing)

## Requirements

- Xcode 9
- iOS 11

## Installation

```sh
git clone https://github.com/cocoa-ai/FacesVisionDemo.git
cd FacesVisionDemo
pod install
open Faces.xcworkspace/
```

## Conversion

Download [Caffe model](https://drive.google.com/open?id=0BydFau0VP3XSNVYtWnNPMU1TOGM)
and [deploy.prototxt](https://drive.google.com/open?id=0BydFau0VP3XSOFp4Ri1ITzZuUkk).
Links can also be found [here](https://gist.github.com/GilLevi/54aee1b8b0397721aa4b#emotion-classification-cnn---rgb).
Move downloaded files to `Covert/EmotionClassification` folder.

```sh
cd Convert
./download.sh
python age.py
python gender.py
python emotion.py
```

Download the [Age](https://drive.google.com/file/d/0B1ghKa_MYL6mT1J3T1BEeWx4TWc/view?usp=sharing),
[Gender](https://drive.google.com/file/d/0B1ghKa_MYL6mYkNsZHlyc2ZuaFk/view?usp=sharing) and
[Emotion](https://drive.google.com/file/d/0B1ghKa_MYL6mTlYtRGdXNFlpWDQ/view?usp=sharing)
CoreML models and add the files to "Resources" folder in the project's directory.

Build the project and run it on a simulator or a device with iOS 11.

## Author

Vadym Markov, markov.vadym@gmail.com

## Credits

- [Age and Gender Classification using Convolutional Neural Networks](http://www.openu.ac.il/home/hassner/projects/cnn_agegender/)
- [Emotion Recognition in the Wild via Convolutional Neural Networks and Mapped Binary Patterns](http://www.openu.ac.il/home/hassner/projects/cnn_emotions/)

## References
- [Caffe Model Zoo](https://github.com/caffe2/caffe2/wiki/Model-Zoo)
- [Apple Machine Learning](https://developer.apple.com/machine-learning/)
- [Vision Framework](https://developer.apple.com/documentation/vision)
- [CoreML Framework](https://developer.apple.com/documentation/coreml)
- [coremltools](https://pypi.python.org/pypi/coremltools)
