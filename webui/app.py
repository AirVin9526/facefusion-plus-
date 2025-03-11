import gradio as gr
from core.engine import EnhancedEngine

engine = EnhancedEngine()

def swap_interface(source_img, target_video):
    output = engine.process(target_video, source_img)
    return output

gr.Interface(
    fn=swap_interface,
    inputs=[gr.Image(label="源人脸"), gr.Video(label="目标视频")],
    outputs=gr.Video(label="换脸结果"),
    title="FaceFusion+ WebUI"
).launch()
