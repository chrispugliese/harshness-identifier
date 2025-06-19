# 🎵 Harshness Identifier: CNN-Based Audio Classification Using Spectrograms

**Open in Colab**  
[Click here to open the notebook in Google Colab](https://colab.research.google.com/drive/1ZVip6krcvheP5e0y0q5wGiymRi-znqGA?usp=sharing)

> ⚠️ Be sure to run each cell individually in Colab.

## 💡 Project Overview

This project explores the classification of spectrogram images generated from music clips into two categories: `clean` and `harsh`. The primary objective was to build a convolutional neural network (CNN) capable of identifying harshness in audio signals. Given CNNs' strength in image recognition, we transformed audio into spectrograms — visual representations of audio frequency over time — to apply image-based machine learning techniques to the audio domain.

## 🎧 Motivation

The inspiration stems from our personal interest in music production. We wanted to blend our passion for sound with machine learning, particularly to detect undesirable qualities like distortion, filtering, or excessive noise — traits that may be considered "harsh" to listeners.

## 🔄 Data Collection & Preparation

Initially, we planned to use personal playlists via the Spotify API, but it proved too time-consuming. We pivoted to the [GTZAN Genre Classification Dataset](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification/data), which provided 1,000 WAV files. Using the `librosa` library, we processed these into spectrograms.

To simulate harshness, we used the [`pydub`](https://github.com/jiaaro/pydub) library to apply audio effects such as distortion and filtering to clean audio samples, effectively doubling our dataset to 1,998 spectrograms.

## ⚙️ Tech Stack

- **Language**: Python
- **Environment**: Google Colab + Google Drive
- **Libraries**:  
  - TensorFlow/Keras  
  - Librosa  
  - Pydub  
  - Matplotlib, Seaborn  
  - Scikit-learn, Pandas  
  - ImageDataGenerator for augmentation

## 🧠 Models & Architectures

We implemented and compared four CNN models:

| Model              | Description                          |
|--------------------|--------------------------------------|
| Basic_CNN_SGD      | Standard CNN using SGD optimizer     |
| Basic_CNN_Adam     | Same as Basic_CNN but with Adam      |
| Deep_CNN_Adam      | Deeper CNN with BatchNormalization   |
| Simple_CNN_Adam    | Lightweight CNN for faster training  |

Each model used a binary classification setup with sigmoid activation and binary cross-entropy loss.

## 🏁 Results

| Model              | Validation Accuracy | Parameters | Training Time |
|--------------------|---------------------|------------|----------------|
| **Basic_CNN_SGD**  | **81.4%**           | 1,694,145  | 17.4 mins      |
| Basic_CNN_Adam     | 79.6%               | 1,694,145  | 5.8 mins       |
| Simple_CNN_Adam    | 78.9%               | 107,745    | 5.8 mins       |
| Deep_CNN_Adam      | 51.3%               | 1,675,041  | 3.4 mins       |

🟢 **Best performing model**: `Basic_CNN_SGD`  
🔍 It achieved the most balanced precision/recall scores and handled overfitting better than deeper models.

## 📊 Evaluation

- **Confusion matrices** and **classification reports** were generated for each model.
- `Basic_CNN_SGD` had the highest recall for both classes and the best F1-score.
- The `Deep_CNN` underperformed, likely due to overfitting or the limited spatial resolution of 28×28 input images.

## 📁 Project Structure
```markdown
/dataset/spectrograms/
├── clean/
└── harsh/

saved_models/
├── Basic_CNN_SGD_best.h5
├── Basic_CNN_Adam_best.h5
├── Deep_CNN_Adam_best.h5
└── Simple_CNN_Adam_best.h5
```

## 📌 Key Takeaways

- Audio-to-image conversion (spectrograms) is highly effective when applying image-based deep learning methods to audio data.
- SGD optimizers may outperform Adam in longer training schedules when overfitting is a concern.
- Dataset size remains a bottleneck; more real-world samples would further improve model generalization.

## 📚 Sources & References

- [ChatGPT](https://chat.openai.com) — Assisted in debugging and model comparisons.
- [GTZAN Dataset on Kaggle](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification/data)
- [Librosa Documentation](https://librosa.org/doc/main/generated/librosa.feature.melspectrogram.html)
- [Pydub GitHub Repo](https://github.com/jiaaro/pydub)
- [CNN Architectures for Spectrograms](https://www.extrica.com/article/22271)

## ✨ Authors

- Christopher Pugliese  
- Tyler Hancock

---

> **📌 Tip:** If you're reproducing this notebook, mount your Google Drive and verify the dataset path before training begins.

> ⚠️ Considering how much data we extracted, we unfortunately cannot upload created spectrograms.


