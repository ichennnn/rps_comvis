# rps_comvis
**rps_comvis** is your classic, childhood game of [Rock-Paper-Scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors), but upgraded with the addition of computer vision tools. This reimagined version detects hand gestures with a computer webcam and allows for player to play with computer using real-time hand gestures.

![rps-gif-small](https://user-images.githubusercontent.com/88521066/170907001-a58083b8-0b9f-408d-ba50-6d16885bad92.gif)

This was built as a practice project to explore computer vision.

## Rules of Rock Paper Scissors
The rules of the game can be succinctly summarized as: 
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

When opponents chose the same gesture, the game is a draw. Hence, the only three outcomes are : Win, Lose and Draw. 

## Nuances of Hand Gestures 
Hand gestures are detected through the usage of OpenCV and MediaPipe. MediaPipe detects gestures through the 21 landmarks as shown below.
![image](https://user-images.githubusercontent.com/88521066/170903670-d4744cb8-8b31-485f-b39f-1cfed457e79c.png)
(Source: https://google.github.io/mediapipe/solutions/hands.html )

To avoid misreading of gestures, only one hand is detected at a time. To detect the three hand gestures, I consider the cases:
- Is the 4th finger down? (Look at Landmark 16 and 13)
- Is the 3rd finger down? (Landmark 12 and 9)
- Is the index finger down? (Landmark 8 and 6)

If 4th, 3rd, and index fingers are down, then gesture is assumed to be **rock**. If only 4th and 3rd finger are down, then gesture is assumed to be **scissors**. While if all three are not down, then gesture is assumed to be **paper**.

## Python Libraries Used, Technologies
Python 3.8.8
- OpenCV (cv2), Pygame, time, os, random, Mediapipe

## Usage, Installation
Download **rps-comvis** by cloning this repo
```
git clone https://github.com/ichennnn/rps_comvis.git
```

The necessary Python libraries may be installed as such:
 ```
 pip install mediapipe
 ```
 ```
 pip install pygame
 ```
 ```
 pip install opencv-python
 ```
 ### How to Run?
 ```
cd rps_comvis
python game_app.py
 ```
 ## Acknowledgements
 **rps-comvis** game's HandTrackingModule was based on 'Murtaza's Workshop - Robotics and AI' 's video (on [YouTube](https://www.youtube.com/watch?v=p5Z_GGRCI5s) and [here](https://www.youtube.com/watch?v=NZde8Xt78Iw)) with modifications to detect different gestures.
 
 Hand gesture images are drawn by myself.
