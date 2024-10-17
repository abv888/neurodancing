# src/physics_simulation.py
import bpy


class PhysicsSimulator:
    def __init__(self, model):
        self.model = model

    def apply_soft_body_simulation(self):
        # Применяем симуляцию мягких тел (мышцы, кожа)
        for mod in self.model.modifiers:
            if mod.type == 'SOFT_BODY':
                mod.settings.goal_spring = 0.5  # Настраиваем гибкость
                mod.settings.gravity = 9.8  # Настраиваем гравитацию

    def apply_collision_simulation(self):
        # Применяем симуляцию столкновений для предотвращения пересечений
        for bone in self.model.pose.bones:
            bone_rigid_body = bpy.ops.rigidbody.objects_add(type='ACTIVE')
            bone_rigid_body.settings.collision_margin = 0.05  # Минимальный зазор
