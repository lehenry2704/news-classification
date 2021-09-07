{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "447bc834-b4f9-4354-a69c-4754f1af3775",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request, redirect, url_for\n",
    "from joblib import load"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e592f653-749a-44ef-92b3-9d3551b0096d",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = load \"text_classification.joblob\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
