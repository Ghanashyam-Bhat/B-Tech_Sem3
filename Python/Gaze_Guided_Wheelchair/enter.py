"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
import os
import cv2
import sys
import communication
from gaze_tracking import GazeTracking
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

gaze = GazeTracking()
chrome = webdriver.Chrome()
chrome.get('http://127.0.0.1:5500/web/entertainment.html')

current = 1
l = list()
input_list = list()

webcam = cv2.VideoCapture(0)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    try:
        gaze.refresh(frame)
    except:
        pass

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"

    elif gaze.is_right():
        text = "Looking right"
  
    elif gaze.is_left():
        text = "Looking left"

    elif gaze.is_center():
        text = "Looking center"

    if len(l)==0:
        l.append(text)
    elif l[0]!=text:
        l = list()
        l.append(text)
    elif len(l)==3:
        input_list.append(text)
        l = list()
        #Buttons
        if len(input_list)>1 and input_list[len(input_list)-1]!="Looking center" :
            input_list = list()
        elif input_list[0]=='Looking left':
            input_list=list()
            if current==1:
                current = 4
            else:
                current-=1
            
        elif input_list[0]=='Looking right':
            input_list=list()
            if current==4:
                current = 1
            else:
                current+=1

        elif input_list[0]=='Blinking':
            input_list=list()
                
        elif input_list[0]=='Looking center' and len(input_list)==3:
            input_list=list()
            if current == 1:
                chrome.find_element_by_css_selector(".btn5").click()
                webcam.release()
                cv2.destroyAllWindows()
                chrome.close()
                os.system('python music_list.py')
                sys.exit()
                
            elif current == 2:
                chrome.find_element_by_css_selector(".btn6").click()
                webcam.release()
                cv2.destroyAllWindows()
                chrome.close()
                os.system('python movie_list.py')
                sys.exit()

            elif current == 3:
                chrome.find_element_by_css_selector(".btn7").click()
                webcam.release()
                cv2.destroyAllWindows()
                chrome.close()
                os.system("python dinoGame.py")
                sys.exit()

            elif current == 4:
                chrome.find_element_by_css_selector(".btn8").click()
                webcam.release()
                cv2.destroyAllWindows()
                chrome.close()
                os.system("python hover.py")
                sys.exit()
            
        else:
            continue
        
    else:
        l.append(text)
    
    
    if current == 1:
        element_to_hover_over = chrome.find_element_by_css_selector(".btn5")
    if current == 2:
        element_to_hover_over = chrome.find_element_by_css_selector(".btn6")
    if current == 3:
        element_to_hover_over = chrome.find_element_by_css_selector(".btn7")
    if current == 4:
        element_to_hover_over = chrome.find_element_by_css_selector(".btn8")

    hover = ActionChains(chrome).move_to_element(element_to_hover_over)
    hover.perform()
    
    
    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (255,178,45), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255,178,45), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (255,178,45), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

   
webcam.release()
cv2.destroyAllWindows()

