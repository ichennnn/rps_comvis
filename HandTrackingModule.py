#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 14:58:01 2022

@author: ichennnn
"""

import cv2
import mediapipe as mp
import time

# =============================================================================
# Detects one hand using mediapipe and draws landmarks on accordingly
# =============================================================================
class handDetector():
    def __init__(self, mode=False, maxHands=1, modelComplexity=1,
                 detectionCon= 0.5 ,trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.modelComplexity,
                                        self.detectionCon, 
                                        self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    # find the single Hand
    def findHand(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        
        # if there is a hand
        if self.results.multi_hand_landmarks:
            # get the first hand seen only
            handLMS = self.results.multi_hand_landmarks[0]
            if draw:
                self.mpDraw.draw_landmarks(img, handLMS, 
                                           self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, draw=True):
        all_lm = []
        if self.results.multi_hand_landmarks:
             theHand= self.results.multi_hand_landmarks[0]
             for n, lm in enumerate(theHand.landmark):
                 h, w, c= img.shape # height, width
                 # convert
                 cx, cy = int(lm.x * w), int(lm.y * h)
                 all_lm.append([n, cx, cy])
                 if draw:
                     cv2.circle(img, (cx, cy), 3, (255,0,0), cv2.FILLED)
        return all_lm
                
        
def main():
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    
    # measuring fps
    pTime = 0
    cTime = 0
    
    while True:
        success, img = cap.read()
        img = detector.findHand(img)
        all_lm = detector.findPosition(img)
                            
        # fps
        cTime = time.time()
        fps = int(1/(cTime-pTime))
        pTime = cTime
        cv2.putText(img, "fps: "+str(fps), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255,0,0), 3)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()