from keras.preprocessing import image

test_image = image.load_img('Pics/cat.jpg', target_size=(64, 64))

test_image = image.img_to_array(test_image)

print(test_image)