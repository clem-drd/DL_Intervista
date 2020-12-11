from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
import api
import os
import numpy as np
import random
import keras as ks

def ml_script(datasetName, new_line) :
   
   tst = new_line + ',2' 

   #if troubles with the wrinting on the dataset re put the dataset name harcoded !

   f=open(datasetName, "a+")
   f.write('\n' + tst)
   f.close()

   dataset = loadtxt(datasetName, delimiter=',')
   revelant_datas = dataset[:,0:8]
   class_variable = dataset[:,8]

   import sys

   def progressbar(it, prefix="", size=60, file=sys.stdout):
      count = len(it)
      def show(j):
         x = int(size*j/count)
         file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
         file.flush()        
      show(0)
      for i, item in enumerate(it):
         yield item
         show(i+1)
      file.write("\n")
      file.flush()

   import time

   for i in progressbar(range(15), "Computing: ", 40):
      time.sleep(0.1) # any calculation you need
##############################################################################

   #input dim represent the number of element who will be given in the input and will serve to create the neuronal network here ye give to him 8 columns because for each line
   # we have 9 - 1 column

   #here we just setup the model

   model = Sequential()
   model.add(Dense(12, input_dim=8, activation='relu'))
   model.add(Dense(8, activation='relu'))
   model.add(Dense(1, activation='sigmoid'))

   #remove the line below later

   model.build((None, 16))

   model.compile(loss='binary_crossentropy', optimizer='adam', metrics=[ks.metrics.SparseCategoricalAccuracy()]) # replace by original => metrics=['accuracy'])
   
   #remove the tyo lines below

   # here we make the prediction


   # The validation split will randomly split the data into use for training and testing.
   # During training, we will be able to see the validation loss, which give the mean squared error of our model on the validation set. 
   # We will set the validation split at 0.2, which means that 20% of the training data we provide in the model will be set aside for testing model performance.

   #early_stopping_monitor = EarlyStopping(patience=3)
   # , callbacks=[early_stopping_monitor] to qdd into model.fit in order to make it quicker the script will stop if the algo dont improve

   # add this => validation_split=0.3 to chqnge the amount of data tested


   model.train_on_batch(revelant_datas, class_variable)
   model.fit(revelant_datas, class_variable, epochs=150, batch_size=10, verbose=2) 

   model.fit(revelant_datas, class_variable, epochs=150, batch_size=10, verbose=2)

   predictions = model.predict_classes(revelant_datas)

   model.summary()
   

##############################################################################


   result = []
   result_file = open("result.csv", "w+")
   limit = len(revelant_datas)

   print("list lenght is =" + str(limit))

   for i in range(limit):
      output = "Datas Received : %s || Prediction made => %d || (expected result for the dataset %d)" % (revelant_datas[i].tolist(), predictions[i], class_variable[i])
      result.append(output)
      if(i == 250):
         result_file.write(output)
      else:
         result_file.write(output + "\n")
      #print(output)
      if(i == limit - 1):
         print(revelant_datas[i])
         
   return(result)


if __name__ == "__main__":

   ml_script(datasetName="", new_line="")