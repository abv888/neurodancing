# src/model_animation.py
import fake_bpy as bpy


class ModelAnimator:
    def __init__(self, model_path):
        bpy.ops.import_scene.obj(filepath=model_path)
        self.model = bpy.context.selected_objects[0]

    def setup_inverse_kinematics(self):
        # Настраиваем Inverse Kinematics для конечностей
        for bone in self.model.pose.bones:
            if "leg" in bone.name or "arm" in bone.name:
                # Применяем IK к ногам и рукам
                constraint = bone.constraints.new('IK')
                constraint.chain_count = 2  # Глубина цепи IK

    def animate_model(self, adapted_poses):
        bpy.context.view_layer.objects.active = self.model
        self.model.select_set(True)
        self.setup_inverse_kinematics()

        # Анимация с использованием IK
        for frame_num, pose in enumerate(adapted_poses):
            bpy.context.scene.frame_set(frame_num)

            for i, (x, y, z) in enumerate(pose):
                bone = self.model.pose.bones[f'bone_{i}']
                bone.location = (x, y, z)
                bone.keyframe_insert(data_path="location", frame=frame_num)
