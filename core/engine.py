from facefusion.processors.frame import face_swapper
from rehiface.real_time import RealTimePipeline
from roop.core import swap_face as roop_swap  # 替换FaceFusion默认换脸模块

class EnhancedEngine:
    def __init__(self):
        self.face_swapper = roop_swap  # 关键修改：仅1行代码替换为Roop算法
        self.realtime_pipe = RealTimePipeline(config="configs/hardware.yaml")
    
    def process_frame(self, frame):
        frame = self.realtime_pipe.enhance(frame)  # 实时性能优化
        frame = self.face_swapper(frame)
        return frame
```
