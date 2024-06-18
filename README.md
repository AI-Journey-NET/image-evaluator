# AI Journey - Image Evaluator
This is another simple example on how to use the OpenAI API spec (with our local Ollama) to interpret images and provide a description.

## Requirements:
### Hardware
1. A GPU faster processing
 - Ollama with llava:latest (~5GB VRAM) or llava:34b (~20GB VRAM) for best results
2. Python (any 3.x version should work as we're using minimal dependencies)
 
### Software
1. Ollama with llava:latest or llava:34b installed and running (run `ollama pull llava:latest` to retrieve the model prior to executing the code)
3. Python3 Enviornment - Preferably Anaconda Distribution

## On the 'Image Evaluator'
The evaluator will:
1. Receive two inputs
2. Conver the image to Base64
3. Feed the user_input to the OpenAI API (Ollama API) together with the base64 converted image

### How to Use
Run the `image_evaluator.py` with two arguments:
1. The image URL
2. A prompt describing what you want to know about the image

Example:
```bash
python3 image_evaluator.py "tortoise.jpg" "Describe this image in detail"
```

Sample response:
```
Parsing image
Waiting for AI response...
AI Response: The image depicts a large tortoise walking on what appears to be a sandy or stony ground. The tortoise has prominent, dark-colored scales that cover its shell and body, and its head is extended forward as if it's in motion. The background of the photo is out of focus, emphasizing the tortoise as the main subject. There are no texts or other objects clearly visible in the image. The style of the image is a standard photograph with natural lighting that casts soft shadows on the ground, suggesting an outdoor environment.
```