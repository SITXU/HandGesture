.. code:: ipython3

    import cv2
    import mediapipe as mp
    import numpy as np
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    
    mp_drawing = mp.solutions.drawing_utils
    
    cap = cv2.VideoCapture(0)
    
    cs = np.zeros((1000, 1000, 3), dtype=np.uint8)
    points = []
    
    while True:
    
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
           
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
                for i in range(0, 21):
                    x = int(landmarks.landmark[i].x * frame.shape[1])
                    y = int(landmarks.landmark[i].y * frame.shape[0])
                    
           
                    if i == 8:  # The tip of the index finger (landmark 8)
                        points.append((x, y))
        if len(points) > 1:
            for i in range(1, len(points)):
                cv2.line(cs, points[i-1], points[i], (0, 255, 255), 10)
        
    
        cv2.imshow("Frame", frame)
        cv2.imshow("Canvas", cs)
    
     
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    
    cap.release()
    cv2.destroyAllWindows()


