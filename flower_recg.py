import os
import sys
from keras.layers import InputLayer
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import Model
from keras.models import Sequential
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import RMSprop
from keras.callbacks import ModelCheckpoint, EarlyStopping
model = Sequential()
def visible(x):
    model.add(InputLayer(input_shape=(x,x,3)))
    
def convolution(x,y):
    model.add(Convolution2D( filters=x , kernel_size=(y,y), activation='relu' ,padding='same') )

def pooling(x):
    model.add(MaxPooling2D( pool_size=(x,x) ))
    
def flatten():
    model.add(Flatten())

def dense(x):
    model.add(Dense(units=x, activation='relu') )
    
def output(x):
    model.add(Dense(units=x, activation='softmax'))
    
def compiler(x):
    model.compile(optimizer=Adam(learning_rate=x),loss='categorical_crossentropy', metrics=['accuracy'])
    
def train():  
    train_data_dir = '17_flowers/train/'
    validation_data_dir = '17_flowers/validation/'

    
    train_datagen = ImageDataGenerator(
          rescale=1./255,
          rotation_range=20,
          width_shift_range=0.2,
          height_shift_range=0.2,
          horizontal_flip=True,
          fill_mode='nearest')

    validation_datagen = ImageDataGenerator(
          rescale=1./255,
          rotation_range=20,
          width_shift_range=0.2,
          height_shift_range=0.2,
          horizontal_flip=True,
          fill_mode='nearest')

    # Change the batchsize according to your system RAM
    train_batchsize = 16
    val_batchsize = 10

    global history
    train_generator = train_datagen.flow_from_directory(
            train_data_dir,
            target_size=(64, 64),
            batch_size=1,
            class_mode='categorical',
            shuffle=True)

    validation_generator = validation_datagen.flow_from_directory(
            validation_data_dir,
            target_size=(64, 64),
            batch_size=1,
            class_mode='categorical',
            shuffle=True)
        
    checkpoint = ModelCheckpoint("project.h5",
                                 monitor="val_accuracy",
                                 mode="max",
                                 save_best_only = True,
                                 verbose=0)

    earlystop = EarlyStopping(monitor = 'val_accuracy', 
                              min_delta = 0, 
                              patience = 3,
                              verbose = 0,
                              restore_best_weights = True)

    # we put our call backs into a callback list
    callbacks = [earlystop, checkpoint]

    # Note we use a very small learning rate 
    model.compile(loss = 'categorical_crossentropy',
                  optimizer = RMSprop(lr = 0.001),
                  metrics = ['accuracy'])

    nb_train_samples = 1192
    nb_validation_samples = 170 
    epochs = 3
    batch_size = 16

    history = model.fit_generator(
        train_generator,
        steps_per_epoch = nb_train_samples // batch_size,
        epochs = epochs,
        validation_data = validation_generator,
        validation_steps = nb_validation_samples // batch_size,
        verbose=0)


i=0
j=0
c = 1 
d = 1 
filter=256
unit=256
visible(64)
while i<c:
    convolution(filter,3)
    pooling(2)
    filter=int(filter/2)
    i=i+1

flatten()
while j<d:
    dense(unit)
    unit=int(unit/2)
    j=j+1

output(17)
compiler(0.0001)
train()

#print accuracy after calculating
h=history.history['val_accuracy']
l=len(h)
h[l-1]

#write older and newer accuracy in accuray.txt file
file = open("accuracy.html", "r")
lines = file. readlines()

#function for string into list
def Convert(string): 
    li = list(string.split(" ")) 
    return li

l2=lines[1]
str1 = l2
l2=Convert(str1)[2]
l2=float(l2)

y=h[l-1]
y=float(y)
lines[0] = "older = {} \n".format(l2)
lines[1] = "newer = {} \n".format(y)
file = open("accuracy.html", "w")
file. writelines(lines)
file. close()
model.save('project.h5')
