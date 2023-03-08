data_dir_test = pathlib.Path("T2_organized/Test")
class_names_labels_test = np.array(sorted([item.name for item in data_dir_test.glob("*")]))
print(class_names_labels_test)

data_dir_str_test = "T2_organized/Test"
data_dir_test = pathlib.Path(data_dir_str_test)
class_names_test = np.array(sorted([item for item in data_dir_test.glob("*")]))
internal_dir_str_test = (data_dir_str_test+"/"+class_names_test[1].name)
internal_dir_test = pathlib.Path(internal_dir_str_test)
iteration_names_test = np.array(([item for item in internal_dir_test.glob("*")]))

test_dir="T2_organized/Test/"
test_dir_os = os.fsencode(test_dir)

test_data_array = np.zeros((len(class_names_test),len(iteration_names_test),10000))

print((iteration_names_test))

numbers_test = []
test_labels = []

for idx_test,(root, dirs, files) in enumerate(os.walk("T2_organized/Test/")):
    dirs.sort()
    for file_idx_test, file in enumerate((sorted(files))):  
      if file.endswith(".txt"):
         with open((os.path.join(root, file))) as fp:
         #Iterate through each line
          for line in fp:
             numbers_test.extend( #Append the list of numbers to the result array
              [float(item) #Convert each number to a float
               for item in line.split() #Split each line of whitespace
             ])
          test_labels.append((root.split(os.path.sep)[-1]))
      test_data_array[idx_test-1,file_idx_test,:] = numbers_test[:10000].copy()
      numbers_test = []

test_labels = np.array(test_labels)

max_value_test = np.amax(test_data_array)
min_value_test = np.amin(test_data_array)



test_data_array_normalized = test_data_array[:].copy()
first_iteration_array_test = range(0,len(class_names_test))
second_iteration_array_test = range(0,len(iteration_names_test))

for idx_1 in first_iteration_array_test:
  for idx_2 in second_iteration_array_test:
    test_data_array_normalized[idx_1, idx_2,: ] = ((test_data_array[idx_1, idx_2,: ]-min_value_test)/(max_value_test-min_value_test))

test_data_normalized_reshaped = test_data_array_normalized.copy()
test_data_normalized_reshaped = test_data_normalized_reshaped.reshape(210,10000)
test_data_normalized_reshaped = test_data_normalized_reshaped.reshape((test_data_normalized_reshaped.shape[0], test_data_normalized_reshaped.shape[1], 1))

test_data_normalized_transposed = test_data_normalized_reshaped.copy()
test_data_normalized_transposed = test_data_normalized_transposed[:,:1700,:]
test_data_normalized_transposed = test_data_normalized_transposed.reshape((test_data_normalized_transposed.shape[0], test_data_normalized_transposed.shape[1], 1))

x_test = test_data_normalized_transposed
num_classes_test = 2
print(num_classes_test)

le_test = preprocessing.LabelEncoder()
le_test.fit(class_names_labels_test)
le_test.classes_
test_labels = le_test.transform(test_labels)
test_labels_transposed = test_labels[:].copy()
test_labels_transposed = test_labels_transposed

y_test = test_labels_transposed
idx = np.random.permutation(len(x_test))

x_test = x_test.copy()
y_test = y_test.copy()


print(y_test)

original_sample_test = x_test[14,:,:]
normalized_sample_test = x_test[16,:,:]


print("Orginal sample is: ")
print(original_sample_test)
print("Normalized sample is: ")
print(normalized_sample_test)

plt.plot(original_sample_test)
plt.title('Original')

plt.figure()
plt.plot(normalized_sample_test)
plt.title('Normalized')
