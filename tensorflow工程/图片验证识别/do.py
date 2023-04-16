import cv2
import numpy as np
from tensorflow.keras.models import load_model

# 加载训练好的模型
model = load_model('dnn_model.h5')

# 加载待处理的图片数据
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (28, 28)) # 将图片缩放为28x28大小
image = image.astype('float32') / 255.0 # 归一化

# 进行预测
predictions = model.predict(np.expand_dims(image, axis=0))

# 解析预测结果
predicted_label = np.argmax(predictions)
confidence = np.max(predictions)

# 进行图片处理操作
# 在图片上标记识别到的数字位置等处理操作...

# 显示预测结果和处理后的图片
print("Predicted Label: ", predicted_label)
print("Confidence: ", confidence)
cv2.imshow('Processed Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
