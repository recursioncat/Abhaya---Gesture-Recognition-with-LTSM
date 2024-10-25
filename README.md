# AbhayaV1: A Gesture Recognition Model for Indian Sign Language

## Quick Links

- [Based on: Tutorial](https://www.youtube.com/watch?v=doDUihpj6ro&t=6432s&ab_channel=NicholasRenotte)
- [Reference for Indian Sign Language](https://data.mendeley.com/datasets/kcmpdxky7p/1)

## A Short Note on the Name

We as people often find ourselves helpless, unable to find time or energy to fight for what is right, yet despite all odds, we must, at our own pace, in our own way. Given the tedious nature of bureaucracy and the henious nature of the crimes around us, it is important that we keep raising our voices.
I am unable to fight from the frontlines, thus I raise my voice in the tiny way I can, let this name be the reminder of the sister taken from us on the night of the 9th of August. Let this model be in her tribute, with the hope that this is able to help people like she did.

## Tech Stack

```plaintext
- Python and Libraries
- Mediapipe
- OpenCV
- TensorFlow
```

## Tutorial

### Step 1: Clone this Repo

### Step 2: Install the Dependencies
In the root directory.
```plaintext
pip install -r requirements.txt
```

### Step 2: Open the `trainfromvideo.ipynb` file from the `Preparation Files` folder

### Step 3: In the same directory, create the following folders:

```plaintext
Training Data
Training npy > Training Data
```

### Step 4: Place the videos you want to train on in the `Training Data` folder, ensuring they are organized by class:

```plaintext
Training Data
|- Video Class 1 Folder
    |- Video 1
    |- Video 2
|- Video Class 2 Folder
```

It is recommended to keep a minimum of 30 videos per class.

### Step 5: Adjust the model architecture, learning rate, and other hyperparameters as needed, then start training.

### Step 6: Test your model using the `test.ipynb` file. Alternatively, you can use the `testingwithjson.py` file in the `Models and Testing` folder to test your model via an API.

## How it Works

1. We use Mediapipe in Python to extract features and pose from gesture videos, saving them as `.npy` files.
2. These files are then processed by an LSTM model.

## Testing AbhayaV1

To test the AbhayaV1 model, run the `testingwithjson.py` file and send a JSON request to the URI with the following format:

```json
{
    "url": "Link_to_Your_Video.mp4"
}
```

Currently, it supports only 15 sentences; we are working to add more.

Supported sentences:

```plaintext
- 'Are you free today' 
- 'Can you repeat that please'
- 'Congratulations' 
- 'Help me please' 
- 'How are you' 
- 'I am fine'
- 'I love you' 
- 'No' 
- 'Please come, Welcome' 
- 'Talk slower please'
- 'Thank you' 
- 'What are you doing' 
- 'What do you do'
- 'What happened' 
- 'Yes'
```

## Usability Note
Windows does not support tensorflow's GPU version directly without installing WSL. If you are running this on vanilla windows, you will have to run the model on your CPU. If you are using linux or WSL, the tensorflow installation process is a bit different, check out here.
- [Install Tensorflow GPU on WSL](https://medium.com/@momchilbattlenet/simple-guide-for-installing-tensorflow-gpu-version-on-wsl2-7e8aec2e3001#:~:text=Just%20install%20the%20Game%20ready,programs%20from%20your%20Windows%20PC)
- [Install Tensorflow on Linux](https://www.tensorflow.org/install/pip#linux)

