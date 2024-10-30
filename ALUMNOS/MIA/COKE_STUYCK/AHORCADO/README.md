# EXTRA

### Building the image

'docker build -t ahorcado .'

### Running the image

'docker run ahorcado'

### Passing a parameter (with a volume)

'docker run -v $(pwd)/palabras.txt:/app/palabras.txt ahorcado palabras.txt'