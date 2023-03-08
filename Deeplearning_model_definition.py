def make_model(input_shape):
    input_layer = keras.layers.Input(input_shape)

    conv1 = keras.layers.Conv1D(filters=24, kernel_size=600, padding="same")(input_layer)
    conv1 = keras.layers.BatchNormalization()(conv1)
    max_pool = tf.keras.layers.MaxPooling1D(pool_size=200, strides=30)(conv1)
    conv1 = tf.keras.activations.tanh(max_pool)

    conv2 = keras.layers.Conv1D(filters=24, kernel_size=600, padding="same")(conv1)
    conv2 = keras.layers.BatchNormalization()(conv2)
    max_pool_2 = tf.keras.layers.MaxPooling1D(pool_size=2, strides=1)(conv2)
    conv2 = tf.keras.activations.softmax(max_pool_2)

    gap = keras.layers.GlobalAveragePooling1D()(conv2)
    drop2 = keras.layers.Dropout(0.5)(gap)

    output_layer = keras.layers.Dense(num_classes, activation="softmax")(drop2)

    return keras.models.Model(inputs=input_layer, outputs=output_layer)


model = make_model(input_shape=x_train.shape[1:])
keras.utils.plot_model(model, show_shapes=True)
