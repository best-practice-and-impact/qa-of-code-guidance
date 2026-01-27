# Generative AI

```{figure} ./_static/copilot_output.png
---
width: 90%
name: copilot_output
alt: What if Clippy was evil?
---
What if Clippy was evil?
```

## Introduction - What is generative AI and how does it work?

Generative AI (Artifical Intelligence) is a term that refers to a class of machine learning models. A machine learning model is a piece of software that is trained on a set of data to make predictions when given new data.
    
Machine learning has been around for a long time and it used in almost every industry to solve a wide variety of problems. As a government analyst, you may be quite familiar with machine learning already.

```{admonition} If you have never heard of machine learning before, click here
:class: dropdown
### Machine learning rapid primer - linear regression

Say you worked for a company that wanted to know how to value land based on land area. You could train a machine learning model on existing real estate data, using price and land area.

A linear regression model of price and land area can be given as:

$$y' = b + m_1x_1$$

Where:
    
- $y'$ is the price, the variable we want to predict, called the **label**
- $x_1$ is the land area, our predictor variable, called a **feature**
- $b$ is the model **bias**
- $m_1$ is the **weight** for our feature $x_1$

To predict $y'$ (price) from $x_1$ (land area), we need the values of $b$ and $m_1$. We can calculate these values using machine learning, by **training** a linear regression model on a dataset of price and land area. The data we will train the model on is our **training data**. Because this data contains both the label and feature, it is also called **labelled data**. Linear regression is a form of **supervised** machine learning, because it uses labelled data as training data.

The act of training the linear regression model is an iterative process to minimise **loss** - the difference between the label predicted by the model and the real label in the training data for each observation in the training data. This happens algorithimically through a process called **gradient descent**: 

- The model begins with a randomised weight and bias close to zero, and then loss is calculated via the chosen loss function. This will in most cases result in high average loss, which is to say the model does not accurately predict the label with the given weight and bias.
- The model then determines the gradient of the tangent to the loss function at the weight and the bias, by taking the derivative of the loss function with respect to the weight and the bias.
- The model then modifies the weight and bias by incrementing them a small amount in the direction of the gradient of the tangent to the loss function. The process then repeats using this new weight and bias.

    ```{figure} ./_static/gradient_descent.png
    ---
    width: 100%
    name: gradient_descent
    alt: Gradient descent in supervised learning. Credit: Google
    ---
    Gradient descent in supervised learning. Credit: Google
    ```

This iterative process ends when the model **converges** - when further changes to the weight and bias produce very small reductions in loss. At this point, we have a trained model with a weight and bias that produce the lowest possible loss for this model. The trained model can now be used to make predictions from new data.

This is how a linear regression machine learning model works! There are many different kinds of machine learning models, some are relatively simple (like linear regression), others are highly complex (such as deep learning models), but the idea of training a model by iteratively modifiying weights and bias to minimise loss is a fundamental concept that applies to a wide range of different models.
```

In a generative AI model, these predicitions are novel instances of text, images, video or audio (or any combination of these) that are produced when given some input data. This guide will focus on a particular subcategory of generative AI models called Large Language Models, or LLMs. LLMs typically take text as and generate text as an output (although most major LLMs today can take inputs and generate outputs in multiple formats, the typical use case is still text-to-text). The most well known LLMs include OpenAI's GPT series, Google's Gemini, Anthropic's Claude, and DeepSeek's DeepSeek.

How do LLMs generate novel instances of text that so closely resemble something that was written by a human? The simplest way of putting it is that LLMs are next-word-predictor machines - they continuously predict the next word in a sequence over and over again, until they have a 'finished' output, whether that is a business email, an academic essay, or an entire Python package. But how do LLMs know what words to predict? They have to model the probabilties of words with an approximation of human language. The technology used to do this is a neural network, a form of machine learning model architecture used to find non-linear patterns in data.

Neural networks have one extremely useful property - they do not require anyone to precisely devise a model of what they are trying to reproduce, they can actually learn how to recognise patterns (such as patterns in language) on their own when supplied with enough examples to learn from, resulting in a mathematical function that can make useful predictions, albeit one with billions if not trillions of parameters in the case of LLMs. From this point onwards, the neural network is trained through machine learning to find the weights of this function, which is done by gradient descent - loss is calculated, the weights are modified in the direction that reduces loss, and the process repeats until the model converges.

Neural networks are layered constructions. They first consist of an input layer, which takes the inputs to the model and multiplies them by their respective weights, just as a linear model might do. The next layer in a neural network are the hidden layers, of which there can be one or more. Each hidden layer consists of one or more neurons. Each neuron of a hidden layer takes the output of the previous layer, plus a unique weight and bias, and applies a non-linear activation function to that output.

```{figure} ./_static/neural_net_training.png
---
width: 100%
name: neural_net_training
alt: A neural network learning to predict a non-linear function. Credit: Stephen Wolfram
---
A neural network learning to predict a non-linear function. Credit: Stephen Wolfram
```

LLMs are essentially just very large neural networks. They use a specific type of neural network architecture called 'transformers' (which were originally [invented in 2017 at Google](https://research.google/pubs/attention-is-all-you-need/) for the purpose of machine translation). The underlying neural network of an LLM is trained on a vast set of text, and the neural network is able to learn patterns of words and then assign probabilities to individual words occurring within sequences of other words, allowing the model to produce long sequences of text that quite accurately mimic human language. 

It's important to remember that the model that the neural network comes up with to predict human language is essentially a black box - nobody can say for sure why it is capable of making accurate predictions, we can only assess that it seems to do so. The creation of LLMs has been the result of engineering decisions in the machine learning research space, finding ways of doing things that seem to be effective through trial and error, rather than representations of human lanugage built from the ground up through first principles. LLMs are modelling something, but we can't say for sure yet what it is or how it relates to human cognition.

Like any other form of machine learning, LLMs have their pros and cons.

## Using generative AI at work



## Conclusion