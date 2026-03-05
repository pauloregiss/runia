import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils


def analisar_video(video_path):

    # Inicializa o Pose DENTRO da função (evita erro no Streamlit)
    with mp_pose.Pose(
        static_image_mode=False,
        model_complexity=1,
        enable_segmentation=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as pose:

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            return "Erro ao abrir o vídeo."

        frame_count = 0
        joelho_angulos = []

        while cap.isOpened():
            ret, frame = cap.read()

            if not ret:
                break

            frame_count += 1

            # Converter para RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Processar pose
            results = pose.process(frame_rgb)

            if results.pose_landmarks:

                landmarks = results.pose_landmarks.landmark

                # Pontos da perna
                quadril = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
                joelho = landmarks[mp_pose.PoseLandmark.LEFT_KNEE]
                tornozelo = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE]

                # Coordenadas
                a = np.array([quadril.x, quadril.y])
                b = np.array([joelho.x, joelho.y])
                c = np.array([tornozelo.x, tornozelo.y])

                # Calcular ângulo do joelho
                ba = a - b
                bc = c - b

                cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
                angle = np.degrees(np.arccos(cosine_angle))

                joelho_angulos.append(angle)

        cap.release()

        if len(joelho_angulos) == 0:
            return "Nenhuma pose detectada no vídeo."

        media_angulo = np.mean(joelho_angulos)

        # Classificação simples
        if media_angulo > 170:
            resultado = "Corrida muito rígida"
        elif media_angulo > 150:
            resultado = "Boa mecânica de corrida"
        else:
            resultado = "Possível excesso de flexão"

        return f"""
Frames analisados: {frame_count}

Ângulo médio do joelho: {media_angulo:.2f}°

Avaliação: {resultado}
"""