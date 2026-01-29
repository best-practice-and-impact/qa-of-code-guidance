# Generative AI

```{figure} ./_static/copilot_output.png
---
width: 90%
name: copilot_output
alt: What if Clippy was evil?
---
What if Clippy was evil?
```

## Introduction - Machine learning and Large Lanuage Models.

Generative AI (Artifical Intelligence) is a term that refers to a class of machine learning models. A machine learning model is a piece of software that is trained on a set of data to make predictions when given new data. Machine learning has been around for a long time and it used in almost every industry to solve a wide variety of problems. As a government analyst, you may be quite familiar with machine learning already.

```{admonition} If you have never heard of machine learning before, click here
:class: dropdown
:name: ml-primer
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

How do LLMs generate novel instances of text that so closely resemble something that was written by a human? The simplest way of putting it is that LLMs are next-word-predictor machines - they continuously predict the next word in a sequence over and over again, until they have a 'finished' output, whether that is a business email, an academic essay, or an entire Python package. But how does an LLM know what word to add to the end of a sequence of words? The only way they can know what word to put at the end of a sequence of words is by learning a mathematical pattern for human text. The technology used to do this is a neural network, a form of machine learning model architecture used to find non-linear patterns in data.

Neural networks get their name because they consist of a network of model 'neurons' - computational units that take many inputs to deliver one output. Neural networks are layered constructions. They first consist of an input layer, which just takes the inputs to the model. The next set of layers in a neural network are the hidden layers, of which there can be one or more. Each hidden layer consists of one or more neurons. Each neuron of a hidden layer takes every input of the layer before it and computes a singular output. This is done by computing the linear product of the previous layer with a set of weights unique to that neuron, plus a bias, and then putting this output through an activation function that transforms the linear output into a non-linear output. An example of a commonly used activation function used is a rectified linear unit, which is defined as $f(x) = max(0, x)$. The activation function is a crucial component in neural networks, as without them they cannot learn to predict non-linearities.

```{figure} ./_static/neural_net_layers.png
---
width: 60%
name: neural_net_layers
alt: A diagram of neural network, showing two hidden layers consisting of four neurons each. The input layer takes two inputs, and the output layer produces four outputs, so this network could be trained for a classification task. If you are familiar with graph theory, the nodes of this graph represent the outputs of neurons derived from the activation function, and the edges represent the weights (and biases) that modify the inputs from the previous nodes. Credit: Wolfram Research
---
A diagram of neural network, showing two hidden layers consisting of four neurons each. The input layer takes two inputs, and the output layer produces four outputs, so this network could be trained for a classification task. If you are familiar with graph theory, the nodes of this graph represent the outputs of neurons derived from the activation function, and the edges represent the weights (and biases) that modify the inputs from the previous nodes. Credit: Wolfram Research
```

While the individual components of a neural network are performing essentially quite trivial mathematical operations, when networks are scaled up to include many hidden layers of many neurons (this is where the term deep learning comes from - deep neural networks, meaning neural networks of many layers), they can predict exceptionally complex non-linear patterns. An even more suprising feature is they can decide by themselves what these patterns are, they do not need instructions. For example, a neural network trained as an image classifier can learn on its own what constitutes an image of a car and what constitutes an image of a bicycle, just by being given examples of each - it does not need a definition of what is 'car-like' or 'bicycle-like' in advance.

Training a neural network to recognise a pattern or reproduce a non-linear function requires supplying it with enough examples that consist of an input and the desired output. From this point onwards, the neural network is trained to find the weights and biases that are needed to reproduce the desired outputs, which is done by gradient descent - loss is calculated, the weights and biases are modified in the direction that reduces loss, and the process repeats until the model converges (see [the drop down section above](#ml-primer) for a primer on loss and gradient descent). Gradient descent is implemented differently in the case of neural networks using an algorithm called backpropagation - this is because neural networks can contain a vast quantity of weights, so modifying weights needs to be done as efficiently as possible.

```{figure} ./_static/neural_net_training.png
---
width: 100%
name: neural_net_training
alt: A neural network learning to predict a non-linear function. Credit: Stephen Wolfram
---
A neural network learning to predict a non-linear function. Credit: Stephen Wolfram
```

LLMs are essentially just very large neural networks. The underlying neural network of an LLM is trained on a vast set of text, and the neural network is able to learn patterns of words and then assign probabilities to individual words occurring within sequences of other words, allowing the model to produce long sequences of text that quite accurately mimic human language.

The explanation for why LLMs are useful now (given previous language models got far less attention) is a specific type of neural network architecture called a 'transformer', that was [invented in 2017 at Google](https://research.google/pubs/attention-is-all-you-need/) for the purpose of machine translation. This architecture represented a breakthrough in language models, as it opened up the models to 'hyperscaling' - increasing the size of the neural network and increasing the size of the training data led to predictable increases in performance, so both have increased exponentionally ever since.

It's important to remember that the model that an LLM creates to predict human language is a black box - it contains billions if not trillions of terms, so nobody can say for sure why it is capable of making accurate predictions, we can only assess that it seems to do so. The creation of LLMs has been the result of engineering decisions in the machine learning research space, finding ways of doing things that seem to be effective through trial and error, rather than representations of human lanugage built from the ground up through first principles. LLMs are modelling something about the predictability of human language, but we can't say for sure yet what it is or how it relates to human cognition.

Another important point of note about LLMs is that the neural network training is only half the story. The neural network training produces the 'foundation' of the LLM, but when LLMs are released as products, they have undergone a significant post-training (also known as 'fine-tuning') phase, on top of the foundational neural network training. It can be summarised as a kind of reinforcement learning that uses human feedback, but it is much harder to discuss, as different companies have developed different methods for what seems to work, and in many cases it is less about technology and more about [substantial human labour](https://time.com/6247678/openai-chatgpt-kenya-workers/). And even though we cannot offer a discussion about it in this guide, post-training is forming an increasingingly important role in the overall training of LLMs.

Now that we have a rough handle on what LLMs are and how they work, we can discuss the benefits and risks of using them in the workplace.

## Using generative AI at work



## Conclusion