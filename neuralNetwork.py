import tensorflow as tf

trainingImages = trainingImages / 255.0
testImages = testImages / 255.0

#define model
#for sources on how we did this, look at tensorflow tutorial 
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(96, 96),
                                    tf.keras.Dense(128, activation=tf.nn.relu),
                                    tf.keras.layers.Dense(4, activation=tf.nn.softmax)])

#build model
model.compile(optimizer = tf.keras.optimizers.Adam(),
                loss = 'sparse_categorical_crossentropy',
                metrics = ['accuracy'])

#training guidlines
model.fit(trainingImages, trainingLabels, epochs = 5)
print('done training')

#test model
model.evaluate(testImages, testLabels)
print('done testing')


