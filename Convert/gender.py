import coremltools

folder = 'cnn_age_gender_models_and_data.0.0.2'

coreml_model = coremltools.converters.caffe.convert(
    (folder + '/gender_net.caffemodel', folder + '/deploy_gender.prototxt'),
    image_input_names = 'data',
    class_labels = 'genders.txt'
)
coreml_model.author = 'Gil Levi and Tal Hassner'
coreml_model.license = 'Unknown'
coreml_model.short_description = 'Gender Classification using Convolutional Neural Networks'
coreml_model.input_description['data'] = 'An image with a face.'
coreml_model.output_description['prob'] = 'The probabilities for each gender, for the given input.'
coreml_model.output_description['classLabel'] = 'The most likely gender, for the given input.'
coreml_model.save('GenderNet.mlmodel')
