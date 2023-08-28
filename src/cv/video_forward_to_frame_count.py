import sys
import cv2

"""
How to run

python video_forward_to_frame_count.py 20
"""

if __name__ == "__main__":
    
    cap = cv2.VideoCapture("/Users/chiawei.lim/Documents/annotation-resources/wrist_video/0041_09.mp4")
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_count = int(sys.argv[1])
    print(f"total_frames: {total_frames}")
    
    print(f"Fast forward to frame count: {frame_count}")
    
    
    cap.set(1, frame_count)
    
    
    while True:
            
        ret, frame = cap.read()
        
        if frame is None:
            break
        
        cv2.imshow("win", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
