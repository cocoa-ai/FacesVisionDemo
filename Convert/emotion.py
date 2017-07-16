import coremltools

folder = 'DemoDir/VGG_S_rgb'

coreml_model = coremltools.converters.caffe.convert(
    (folder + '/EmotiW_VGG_S.caffemodel', folder + '/deploy.prototxt'),
    image_input_names = 'data',
    class_labels = 'emotions.txt'
)
coreml_model.author = 'Gil Levi and Tal Hassner'
coreml_model.license = 'Unknown'
coreml_model.short_description = 'Emotion Recognition in the Wild via Convolutional Neural Networks and Mapped Binary Patterns'
coreml_model.input_description['data'] = 'An image with a face.'
coreml_model.output_description['prob'] = 'The probabilities for each emotion, for the given input.'
coreml_model.output_description['classLabel'] = 'The most likely type of emotion, for the given input.'
coreml_model.save('CNNEmotions.mlmodel')
