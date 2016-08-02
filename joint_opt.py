import logging

logging.basicConfig(level=logging.INFO)

import random
random.seed(0)
import morfessor


io = morfessor.MorfessorIO()

model = morfessor.BaselineModel()

c = []
for line in open("inlist", encoding='utf-8'):
    word, trans = line.strip().split("\t", 1)
    trans = tuple(trans.split())
    c.append((1, (word,trans)))

model.load_data(c)

model.train_batch()

io.write_binary_model_file("model.out", model)

io.write_segmentation_file("model.txt", model.get_segmentations())