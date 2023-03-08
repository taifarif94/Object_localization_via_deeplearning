import time

from google.colab import files
model = keras.models.load_model("my_model")
start_time = time.time()
predict_labels = model.predict(x_test)
print("--- %s seconds ---" % (time.time() - start_time))
test_loss, test_acc = model.evaluate(x_test[:1,:,:], y_test[:1])


print(predict_labels.argmax(axis=1))
print(y_test)

plt.plot((predict_labels.argmax(axis=1)),'bo')
plt.plot((y_test),'r+')
plt.ylabel("Location labels", fontsize="large")
plt.xlabel("Test data", fontsize="large")
plt.legend(["Predicted location", "Real location"], loc="best")
plt.title("Actual vs Predicted locations")
plt.savefig("Actual_vs_Predicted_locations.svg")

print("Test accuracy", test_acc)
print("Test loss", test_loss)

# !mkdir -p saved_model
# model.save('/content/my_model') 
# !zip -r /content/my_model.zip /content/my_model
# files.download("/content/my_model.zip")