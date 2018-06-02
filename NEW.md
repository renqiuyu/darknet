1.save precision-recall data to .csv file :
    
    
    ./darknet detector prplot cfg/voc.data cfg/brain-tiny-v0.cfg models/brain-tiny-v0_final.weights -name brain-tiny-v0 -step 0.02
    this will generate `brain-tiny-v1.csv` in folder csv/


2.plot precision-recall curve:
    cd csv/
    python3 pr-curve.py [filename].csv [output filename]

