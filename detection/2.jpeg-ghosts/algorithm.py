#source: https://github.com/kalinkinisaac/auto-forgery-detection/tree/master
import os
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from scipy.stats import linregress
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
from joblib import dump, load
import imageio
import argparse
from manage import *

from image_tools import to_jpeg, color_box
from random import randint


# =========================
# Core Difference Functions
# =========================

def difference(i_q1: np.ndarray, i_q2: np.ndarray, x: int, y: int, w: int = 8) -> float:
    block = i_q1[x:x+w, y:y+w] - i_q2[x:x+w, y:y+w]
    return np.sum(block ** 2) / (3 * w**2)


def difference_curve(image: Image.Image, x=0, y=0, w=16, q_min=30, q1=95) -> np.ndarray:
    i_q1 = np.asarray(image, dtype=np.float64)
    qualities = np.arange(q_min, q1 + 1)

    result = np.zeros(len(qualities), dtype=np.float64)

    for idx, q in enumerate(qualities):
        i_q2 = np.asarray(to_jpeg(image, q), dtype=np.float64)
        result[idx] = difference(i_q1, i_q2, x, y, w)

    max_val = result.max()
    if max_val > 0:
        result /= max_val

    return result


# =========================
# Curve Aggregation
# =========================

def get_curves(image: Image.Image, q_min=30, q1=95, w=8) -> np.ndarray:
    width, height = image.size
    n_cols = width // w
    n_rows = height // w

    cropped = image.crop((0, 0, n_cols * w, n_rows * w))
    i_q1 = np.asarray(cropped, dtype=np.float64)

    qualities = np.arange(q_min, q1 + 1)
    differences = np.zeros((len(qualities), n_rows * w, n_cols * w), dtype=np.float64)

    for idx, q in enumerate(qualities):
        i_q2 = np.asarray(to_jpeg(cropped, q), dtype=np.float64)
        differences[idx] = np.sum((i_q1 - i_q2) ** 2, axis=2) / 3

    # Block aggregation (vectorized)
    reshaped = differences.reshape(len(qualities), n_rows, w, n_cols, w)
    block_sum = reshaped.sum(axis=(2, 4))

    # Normalize per-block
    max_vals = block_sum.max(axis=0)
    max_vals[max_vals == 0] = 1
    block_sum /= max_vals

    return block_sum


# =========================
# Feature Extraction
# =========================

def get_features(curve: np.ndarray, q1: int, q_min=30):
    qualities = np.arange(q_min, q1 + 1)
    w1 = (qualities - q_min) / (q1 - q_min)
    w2 = 1 - w1

    f1 = np.dot(w1, curve) / w1.sum()
    f2 = np.median(curve)

    slope, intercept, *_ = linregress(qualities, curve)
    f3 = slope
    f4 = intercept

    t = 0.5
    g5 = (curve < t).astype(float)
    f5 = np.dot(w2, g5) / w2.sum()

    g6 = np.maximum(w2 - curve, 0)
    f6 = np.sum(g6**2)

    return f1, f2, f3, f4, f5, f6


# =========================
# Machine Learning
# =========================

def train_model():
    X = np.load("X.npy")
    Y = np.load("Y.npy")

    x_train, x_test, y_train, y_test = train_test_split(
        X, Y,
        train_size=0.8,
        random_state=42,
        stratify=Y
    )

    clf = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        random_state=42,
        n_jobs=-1
    )

    clf.fit(x_train, y_train)

    # Use probabilities for ROC
    y_proba = clf.predict_proba(x_test)[:, 1]

    fpr, tpr, _ = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
    plt.plot([0, 1], [0, 1], "--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend()
    plt.show()

    print("Test Accuracy:", clf.score(x_test, y_test))
    print("AUC:", roc_auc)

    dump(clf, "model.joblib")


# =========================
# Prediction
# =========================

def predict(image: Image.Image, w, in_path):

    clf = load("model.joblib")

    q1 = 84  # or call predict_q1(image)
    curves = get_curves(image, q1=q1, w=w)

    for i in range(curves.shape[1]):
        for j in range(curves.shape[2]):
            features = get_features(curves[:, i, j], q1=q1)
            pred = clf.predict([features])[0]

            box = (j*w, i*w, j*w+w, i*w+w)

            if pred == 1:
                image = color_box(image, box=box, color=(0, 255, 0))
            else:
                image = color_box(image, box=box)
    out_path = in_path + "_jpeg_" + str(w) + ".jpg"
    imageio.v2.imwrite(out_path, image)

    #plt.imshow(np.asarray(image))
    #plt.axis("off")
    #plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--train", action="store_true")
    parser.add_argument("in_path", metavar='input_img', type=str, help='path to input image')
    parser.add_argument("w", metavar='jpeg_quality', type=int, help='...')
    args = parser.parse_args()

    if args.train:
        train_model()
    if args.in_path:
        img = Image.open(args.in_path).convert('RGB')
        print('\t %%%%%% \t starting analisys process \t %%%%%% \t')
        predict(img, args.w, args.in_path)
        print('\t %%%%%% \t done \t %%%%%% \t')