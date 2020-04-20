#!/bin/bash
# tar czf - $1 | split -b $2 - "$1.tar.gz.part." #&& *.tar.gz.part.*
cat entities_predict_director.h5 | split -b 10m - "entities_predict_director.h5.part."
