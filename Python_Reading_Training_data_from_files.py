\begin{lstlisting}[language=python]
# Import the required libraries
import pathlib
import numpy as np
import os
import tensorflow as tf
from tensorflow import keras
from sklearn import preprocessing
import matplotlib.pyplot as plt
from google.colab import files

# Path to the T2_organized folder is saved in data_dir 
data_dir = pathlib.Path("T2_organized/Train")
# Labels are programmatically acquired with the following code
class_names_labels = np.array(sorted([item.name for item in data_dir.glob("*")]))

data_dir_str = "T2_organized/Train"
data_dir = pathlib.Path(data_dir_str)
# Path to the location/ label folders
class_names = np.array(sorted([item for item in data_dir.glob("*")]))
# Getting the path to one of the labels
internal_dir_str = (data_dir_str+"/"+class_names[1].name)
# Converting the path string to a path object
internal_dir = pathlib.Path(internal_dir_str)
# Getting all the iteration file names inside one of the labels
iteration_names = np.array(([item for item in internal_dir.glob("*")]))
# Path to the training folder as a string
train_dir="T2_organized/Train/"
#  Converting the path string to a path object
train_dir_os = os.fsencode(train_dir)
# Initializing a zero array where the data from the files can be read
# The shape of the array is (number of locations in the container, number of iterations, 
# the number of sampled points in each iteration/ file)
training_data_array = np.zeros((len(class_names),len(iteration_names),10000))
# Creating an empty list in which the sampled values read from each file will be saved temporarily
numbers = []
# Creating a list where the labels/ locations for each iteration will be saved
training_labels = []

# The outer for loop controls the iteration of label/ location folders
for idx,(root, dirs, files) in enumerate(os.walk("T2_organized/Train/")):
    dirs.sort()
    # The inner for loop controls the iteration of files within those folders
    for file_idx, file in enumerate((sorted(files))):  
      if file.endswith(".txt"):
         with open((os.path.join(root, file))) as fp:
         #Iterate through each line
          for line in fp:
             numbers.extend( #Append the list of numbers to the result array
              [float(item) #Convert each number to a float
               for item in line.split() #Split each line of whitespace
             ])
          # Append the training labels to the list for each file read
          training_labels.append((root.split(os.path.sep)[-1]))
      # Each line read is saved into the predefined array.
      # Idx is -1 because idx starts at 1 instead of 0
      training_data_array[idx-1,file_idx,:] = numbers.copy()
      # The temporary buffer is emptied.
      numbers =[]
#  Array is reshaped from 3D to 2D. 14 classes x 45 iteration/ files = 630.
training_data_array_1 = training_data_array.copy().reshape(630,10000)

# Array is reshaped again, one column is added to facillitate the implementation of the algorithm
training_data_array_1 = training_data_array_1.reshape((training_data_array_1.shape[0], training_data_array_1.shape[1], 1))

# Only the first 1700 sampled points from the 10000 are selected/ sliced.  
training_data_array_1 = training_data_array_1.copy()[:,:1700,:]

# List of labels is converted into a numpy array
training_labels = np.array(training_labels)
# training_labels = np.tile(training_labels.copy(), (10))
print(training_labels.shape)

# Max and Min values contained in the files are acquired
max_value = np.amax(training_data_array)
min_value = np.amin(training_data_array)

# A copy of the array is made and two arrays for iteration are created.
training_data_array_normalized = training_data_array[:].copy()
first_iteration_array = range(0,len(class_names))
second_iteration_array = range(0,len(iteration_names))
# Min-max normazlization is performed
for idx_1 in first_iteration_array:
  for idx_2 in second_iteration_array:
    training_data_array_normalized[idx_1, idx_2,: ] = ((training_data_array[idx_1, idx_2,: ]-min_value)/(max_value-min_value))
# Copy of an array is made
training_data_normalized_reshaped = training_data_array_normalized.copy()
#  Array is reshaped from 3D to 2D. 14 classes x 45 iteration/ files = 630.
training_data_normalized_reshaped = training_data_normalized_reshaped.reshape(630,10000)
# Checking
# training_data_normalized_reshaped = np.tile(training_data_array_normalized.copy().reshape(630,10000), (10, 1))
print("Replicated")
# print(np_check.shape)

# Array is reshaped again, one column is added to facillitate the implementation of the algorithm
training_data_normalized_reshaped = training_data_normalized_reshaped.reshape((training_data_normalized_reshaped.shape[0], training_data_normalized_reshaped.shape[1], 1))

training_data_normalized_transposed = training_data_normalized_reshaped.copy()
# Only the first 1700 sampled points from the 10000 are selected/ sliced.  
training_data_normalized_transposed = training_data_normalized_transposed[:,:1700,:]
# Sliced array is reshaped to (630,1700,1) for facillitating the implementation of the algorithm
training_data_normalized_transposed = training_data_normalized_transposed.reshape((training_data_normalized_transposed.shape[0], training_data_normalized_transposed.shape[1], 1))

# training_data_k15 = training_data_normalized_transposed.copy()[:45,:1700,:]
# # training_data_k18 = training_data_normalized_transposed.copy()[135:179,:1700,:]
# training_data_k21 = training_data_normalized_transposed.copy()[270:314,:1700,:]



num_classes = len(class_names_labels)
print(num_classes)

# Training labels are changed are assigned numbers from 0-13
le = preprocessing.LabelEncoder()
le.fit(class_names_labels)
le.classes_
training_labels = le.transform(training_labels)
training_labels_transposed = training_labels[:].copy()
training_labels_transposed = training_labels_transposed

# Data is saved into x_train
x_train = training_data_normalized_transposed
# Labels are saved into y_train
y_train = training_labels_transposed
# A random number to shuffle the data
idx = np.random.permutation(len(x_train))
# Data is shuffled
x_train = x_train.copy()[idx]
y_train = y_train.copy()[idx]


print(y_train)

original_sample = training_data_array_1[0,:,:]
normalized_sample = x_train[0,:,:]
print(y_train[44])


print("Orginal sample is: ")
print(original_sample)
print("Normalized sample is: ")
print(normalized_sample)
plt.figure(figsize=[10, 6])
plt.xlabel("Sample points")
plt.ylabel("Amplitude")
plt.plot(original_sample)
plt.title('Original')
plt.savefig("orginal.svg")
plt.figure(figsize=[10, 6])
plt.xlabel("Sample points")
plt.ylabel("Amplitude")
plt.plot(normalized_sample)
plt.title('Normalized')
plt.savefig("Normalized.svg")

# train_dataset = tf.data.Dataset.from_tensor_slices((training_data_normalized_reshaped, training_labels))

# train_dataset_transposed = tf.data.Dataset.from_tensor_slices((training_data_normalized_transposed, training_labels_transposed))