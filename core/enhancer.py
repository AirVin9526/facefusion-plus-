import realesrgan
from configs import default

class UltraHDEnhancer:
    def __init__(self):
        self.model = realesrgan.RealESRGAN(
            scale=8 if default.OUTPUT_RES == "4k" else 4  # 根据配置动态加载模型
        )
    
    def upscale(self, frame):
        return self.model.enhance(frame)
```
