# main.py
from src.pose_estimation import PoseEstimator
from src.motion_adaptation import MotionAdapter
from src.model_animation import ModelAnimator
from src.physics_simulation import PhysicsSimulator
from src.rendering import Renderer


def main():
    video_path = "resources/test.mp4"
    model_path = "resources/Ch43_nonPBR.fbx"
    output_path = "results"

    # Шаг 1. Извлечение поз
    estimator = PoseEstimator()
    poses = estimator.extract_pose(video_path)

    # Шаг 2. Адаптация движений
    model_dimensions = {'height': 2.0, 'width': 1.2, 'depth': 0.8}
    adapter = MotionAdapter(model_dimensions)
    adapted_poses = adapter.adapt_motion(poses)

    # Шаг 3. Анимация модели
    animator = ModelAnimator(model_path)
    animator.animate_model(adapted_poses)

    # Шаг 4. Применение физической симуляции
    simulator = PhysicsSimulator(animator.model)
    simulator.apply_soft_body_simulation()
    simulator.apply_collision_simulation()

    # Шаг 5. Рендеринг финального видео
    renderer = Renderer(output_path)
    renderer.render()


if __name__ == "__main__":
    main()
