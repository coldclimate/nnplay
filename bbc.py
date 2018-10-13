from textgenrnn import textgenrnn
textgen = textgenrnn()
# To train from file use textgen.train_from_file('bbc.learn', num_epochs=1)
textgen = textgenrnn('bbc.hdf5')
textgen.generate(50)
