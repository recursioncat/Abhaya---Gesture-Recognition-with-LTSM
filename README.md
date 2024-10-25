<h1>AbhayaV1: A Gesture Recognition Model for Indian Sign Language</h1>

<h2>Quick Links<br></h2>
[Based on: Tutorial](https://www.youtube.com/watch?v=doDUihpj6ro&t=6432s&ab_channel=NicholasRenotte)<br>
[Dataset](https://drive.google.com/file/d/1VbQK71O4wyWHBCMWBdYknM_Ymyr3rzJ5/view?usp=sharing)<br>
[Reference for Indian Sign Language](https://data.mendeley.com/datasets/kcmpdxky7p/1)<br>

<h2>A Short Note on the Name</h2>
We as people often find ourselves helpless, unable to find time or energy to fight for what is right, yet despite all odds, we must, at our own pace, in our own way. Given the tedious nature of bureaucracy and the henious nature of the crimes around us, it is important that we keep raising our voices.
I am unable to fight from the frontlines, thus I raise my voice in the tiny way I can, let this name be the reminder of the sister taken from us on the night of the 9th of August. Let this model be in her tribute, with the hope that this is able to help people like she did.

<h2>Tech Stacks</h2>
```
Python and Libraries
Mediapipe
OpenCV
Tensorflow
```

<h2>Tutorial</h2>
<h3>Step 1: Clone this Repo</h3>
<h3>Step 2: Open the `trainfromvideo.ipynb` file from the `Preparation Files` folder</h3>
<h3>Step 3: In the same directory create 3 folder like so</h3>
```
Training Data
Training npy > Training Data
```
<h3>Step 3: Put the videos that you want to train from in the `Training Data` folder. Keep in mind, the videos must be classified into their respective class folders.</h3>
```
Training Data
|- Video Class 1 Folder
    |- Video 1
    |- Video 2
|- Video Class 2 Folder
```
so on. It is recommended to keep a minimum of 30 videos per class.

<h3>Step 4: Change the model architecture, learning rate and other hyperparameters as required and Train.</h3>
<h3>Step 5: Test your model using the `test.ipynb` file. You can also use the `testingwithjson.py` file in the `Models and Testing` folder to test your model in an API form.</h3>

<h2>How it Works</h2>
1. We use mediapipe in python to extract features and pose from our gesture videos and save them into .npy files.
2. We use these files and run them through an LTSM model.

<h2>Testing AbhayaV1</h2>
To test the AbhayaV1 model, you can run the `testingwithjson.py` file. You can send a json to the uri using the following format:
```
{
"url":"Link_to_Your_Video.mp4"
}
```
Currently it supports only 15 sentences, we are working to add more.
```
'Are you free today', 
'Can you repeat that please',
'Congratulations', 
'help me please', 
'how are you', 
'I am fine',
'I love you', 
'no', 
'Please come,Welcome', 
'Talk slower please',
'Thank You', 
'What are you doing', 
'What do you do',
'What Happened', 
'yes'
```
