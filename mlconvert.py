from coremltools.models.utils import load_spec

# Load model file
model_coreml = load_spec('example.mlmodel')
from winmltools import convert_coreml

# Convert it!
# The automatic code generator (mlgen) uses the name parameter to generate class names.
model_onnx = convert_coreml(model_coreml, name='ExampleModel') 


from winmltools.utils import save_model
# Save the produced ONNX model in binary format
save_model(model_onnx, 'example.onnx')
