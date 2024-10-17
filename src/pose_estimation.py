# src/pose_estimation.py
import cv2
import mediapipe as mp


class PoseEstimator
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

    def extract_pose(self, video_path):
        cap = cv2.VideoCapture(video_path)
        poses = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Конвертация кадра в RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.pose.process(rgb_frame)

            if results.pose_landmarks:
                pose_data = [(lm.x, lm.y, lm.z) for lm in results.pose_landmarks.landmark]
                poses.append(pose_data)

        cap.release()
        return poses
