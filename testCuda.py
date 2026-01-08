import torch
print(torch.cuda.is_available())  # 应返回 True
print(torch.version.cuda)         # 应显示 '12.6'