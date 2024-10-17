# src/rendering.py
import bpy


class Renderer:
    def __init__(self, output_path):
        self.output_path = output_path

    def render(self):
        bpy.context.scene.render.filepath = self.output_path
        bpy.ops.render.render(animation=True)
