import coremltools

folder = 'cnn_age_gender_models_and_data.0.0.2'

coreml_model = coremltools.converters.caffe.convert(
    (folder + '/age_net.caffemodel', folder + '/deploy_age.prototxt'),
    image_input_names = 'data',
    class_labels = 'ages.txt'
)
coreml_model.author = 'Gil Levi and Tal Hassner'
coreml_model.license = 'Unknown'
coreml_model.short_description = 'Age Classification using Convolutional Neural Networks'
coreml_model.input_description['data'] = 'An image with a face.'
coreml_model.output_description['prob'] = 'The probabilities for each age, for the given input.'
coreml_model.output_description['classLabel'] = 'The most likely age, for the given input.'
coreml_model.save('AgeNet.mlmodel')
