import os

def count_images_in_folder(folder_path):
    class_counts = {}
    for class_name in os.listdir(folder_path):
        class_path = os.path.join(folder_path, class_name)
        if os.path.isdir(class_path):
            count = len([f for f in os.listdir(class_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
            class_counts[class_name] = count
    return class_counts

train_path = 'datasets/train'  # 修改为你的训练集路径
test_path = 'datasets/test'    # 修改为你的测试集路径

train_counts = count_images_in_folder(train_path)
test_counts = count_images_in_folder(test_path)

print("Train set distribution:")
for cls, count in train_counts.items():
    print(f"{cls}: {count} images")

print("\nTest set distribution:")
for cls, count in test_counts.items():
    print(f"{cls}: {count} images")
