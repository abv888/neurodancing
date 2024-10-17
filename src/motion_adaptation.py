# src/motion_adaptation.py
import numpy as np


class MotionAdapter:
    def __init__(self, model_dimensions):
        self.model_dimensions = model_dimensions

    def adapt_motion(self, poses):
        adapted_poses = []

        for pose in poses:
            adapted_pose = []
            for point in pose:
                # Линейная адаптация движения с учетом веса и пропорций модели
                adapted_x = point[0] * self.model_dimensions['width']
                adapted_y = point[1] * self.model_dimensions['height']
                adapted_z = point[2] * self.model_dimensions['depth']

                # Коррекция для предотвращения пересечений
                adapted_x = self.correct_for_collisions(adapted_x, adapted_y, adapted_z)
                adapted_pose.append((adapted_x, adapted_y, adapted_z))

            adapted_poses.append(adapted_pose)

        return adapted_poses

    def correct_for_collisions(self, x, y, z):
        # Логика для предотвращения пересечений частей тела
        # Например, если руки слишком близко к телу, мы корректируем их положение
        if abs(x) < self.model_dimensions['width'] * 0.2:  # Руки слишком близко
            x = self.model_dimensions['width'] * 0.2

        return x
