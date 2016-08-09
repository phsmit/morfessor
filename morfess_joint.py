#!/usr/bin/env python3
import logging

logging.basicConfig(level=logging.INFO)

import random
random.seed(0)
import morfessor
import sys

io = morfessor.MorfessorIO()

model = morfessor.BaselineModel(corpusweight=float(sys.argv[4]))

c = []
for line in open(sys.argv[1], encoding='utf-8'):
    word, trans = line.strip().split("\t", 1)
    trans = tuple(trans.split())
    c.append((1, (word,trans)))

model.load_data(c)

model.train_batch()

io.write_binary_model_file(sys.argv[2], model)

io.write_segmentation_file(sys.argv[3], model.get_segmentations())
