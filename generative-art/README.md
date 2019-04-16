## Introduction to Autoencoders

[![Open In Colab](images/colab-badge.svg)](https://colab.research.google.com/drive/1A7_nMl9NG-cb7eTCSdSgsk89Uq9EY_uh)

In this notebook we'll get an intuitive sense of the way an [autoencoder](https://en.wikipedia.org/wiki/Autoencoder) works. Then we'll build, train, and run a very basic autoencoder to generate new face images.

[![Autoencoder output preview](images/autoencoder-output-preview.png)](minimal-autoencoder.ipynb)


## GPT-2 (Text)

[![Open In Colab](images/colab-badge.svg)](https://colab.research.google.com/drive/1vNYzs7X94cIHAGmwQ58e-msIX635lbpG)

[GPT-2](https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) is a powerful algorithm capable of generating delightfully bizarre text outputs. We'll use this notebook to create some algorithmic poetry.

**Sample Outputs:**

> A 20-year-old woman was physically raised in attic shed bags and handles. A 22-year-old man attended Duffel Island Medical Clinic treating a "sometimes debilitating issue", believed to be an underlying condition.

> Robin Hodgson, whose 17-bedroom apartment was 'identified in a similar manner to some of the areas the home does not have', and who lived close to the scene of the killings on 18 January, said they were 'ordinary household items', just like animals.

> Dream true and fill the soul of High Ketchup@


## Textgenrnn (Text)

[![Open In Colab](images/colab-badge.svg)](https://colab.research.google.com/drive/1KLWjr_MZmxnCQ9wC19kEI5JolhprdoPU)

Textgenrnn is a [recurrent neural network](https://en.wikipedia.org/wiki/Recurrent_neural_network) that lets users generate texts that resemble an input text. The sample outputs below, for example, are based on Shakespeare's plays:

**Sample Outputs:**

> DUKE VINCENTIO: <br/>
> What was not all the sup sound the sea, <br/>
> What is the more of thy strange marriage. <br/>

> LUCIO: <br/>
> I was born to the duke of mine own brother with the world be so fair a man to do the court. <br/>

> HASTINGS: <br/>
> Let's best lace? <br/>


## BigGAN (Images)

[![Open In Colab](images/colab-badge.svg)](https://colab.research.google.com/drive/1IN4JNPGcGuc5uc2QV8Ho6K1DVPvbkYKs)

[BigGAN](https://arxiv.org/abs/1809.11096) is a Generative Adversarial Network that is capable of generating large images. The default notebook allows one to explore this model and generate outputs like the ones below:

![Viola Image](./images/biggan/viola.png)

By feeding the model different paramters, one can generate more abstract images:

![BigGAN Image grid](./images/biggan/grid.png)

By exploring the model's latent space, one can also generate many image outputs then combine them into a video like the ones below:

<table>
  <tr>
    <td><img src='./images/biggan/barn.gif'></td>
    <td><img src='./images/biggan/clock.gif'></td>
  </tr>
</table>


## Multitrack Chords (Music)

[![Open In Codepen](./images/codepen-badge.svg)](https://codepen.io/duhaime/pen/yrPXbM)

Multitrack Chords is an interactive web application built by Google's [Magenta](https://magenta.tensorflow.org/) team, which specializes in building AI tools for audio production. This application uses a neural network to generate new music that conforms to user-specified chordal patterns and style imperatives:

[![multitrack chords screenshot](./images/multitrack-chords.png)](https://codepen.io/duhaime/pen/yrPXbM)

## Performance RNN (Music)

[![Open In Colab](images/colab-badge.svg)](https://colab.research.google.com/drive/1lYdPotp1dNDatsDHLaH1ZTlZ4olyYk11)

Like Multitrack Chords, Performance RNN is a tool built by Google's Magenta team that allows users to create new audio compositions. This model is trained on jazz sequences, so tends to be a bit more dissonant than the melodic multitrack chords outputs:

[![performance rnn midi screenshot](./images/performance-rnn.png)](https://colab.research.google.com/drive/1lYdPotp1dNDatsDHLaH1ZTlZ4olyYk11)

## Synth Modulation (Music)

[![Open In Colab](images/colab-badge.svg)](https://colab.research.google.com/drive/1meggrPefMyo68AQYgUcECp9c5qJwAHYq)

Synth Modulation is a third and final Google Magenta application that allows users to generate audio with nerual networks. This application lets users modulate the timber of input sequences by using a series of neural network modulations:

[![synth modulation screenshot](./images/synth-modulation.png)](https://colab.research.google.com/drive/1meggrPefMyo68AQYgUcECp9c5qJwAHYq)
