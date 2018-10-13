from textgenrnn import textgenrnn

textgen = textgenrnn('places.hdf5')
textgen.generate(500)
