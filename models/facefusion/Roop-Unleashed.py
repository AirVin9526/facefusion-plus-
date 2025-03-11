# 使用Roop-Unleashed替换原FaceFusion引擎（仅需3行核心修改）
from roop_unleashed import Core

def enhance_swap(source_img, target_video):
    core = Core(enable_face_analyser=True, enable_face_mask=True)
    return core.swap(source_img, target_video)
