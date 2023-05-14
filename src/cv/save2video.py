import cv2

if __name__ == "__main__":

    invideopath = "sample.mp4"
    
    #---------------------------------------------------------------------
    outvideopath = "sampleout.avi"
    fourcc_format = "DIVX"

    #---------------------------------------------------------------------
    outvideopath = "sampleout.mp4"
    fourcc_format = "mp4v"
    #---------------------------------------------------------------------
    cap = cv2.VideoCapture(invideopath)
    
    # Get the width, height, and fps
    out_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    out_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    fourcc = cv2.VideoWriter_fourcc(*fourcc_format) 
    out = cv2.VideoWriter(outvideopath, fourcc, fps, (out_w, out_h))

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret is False:
            break

        #frame = cv2.flip(frame, 1)

        # write the flipped frame
        code = out.write(frame)

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()\

    print("Done")
