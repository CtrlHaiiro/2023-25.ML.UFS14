import os 
model_dir = os.envirom("SM_MODEL_DIR")

with open(model_dir + "/output.txt","w" ) as f:
    f.write("Ciao")
    