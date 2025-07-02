# Hand Laterality Judgement Task - Forced Response (HLJT-FR)

The HLJT is a behavioural paradigm aiming to assess the ability to manipulate movement imagery. If you are interested in assessing Movement Imagery ability, visit this [Task Platform Project](https://movementimageryability.github.io/) for an overview of open-source behavioural tasks.

Originally described in [Cooper and Shepard 1975](https://psycnet.apa.org/doiLanding?doi=10.1037%2F0096-1523.1.1.48) and later investigated in [Parsons 1987](https://www.sciencedirect.com/science/article/abs/pii/0010028587900119), it has been extensively used in cognitive and clinical neuroscience. The traditional 'reaction time' paradigm faces limitations to study information processing because: 1) they are subject to speed-accuracy trade-offs because two inherently related dependent variables are used (reaction time and accuracy); 2) only the end-point of the processing time-course is available when analysing reaction times. Conversely, 'forced response' paradigms overcome those limitations by controlling the amount of time the participant has to respond on a trial-by-trial basis, as an independent variable. In these paradigms, the evolution of accuracy throughout a range of times used to process the stimulus is analysed through speed-accuracy trade-offs.

This repository contains the materials for an **open-source (and user-friendly)** version of the HLJT-FR for local use. This repository contains an updated version of the code used in **Moreno-Verdú et. al 2025** ([Publication](https://doi.org/10.1016/j.cortex.2025.06.002) | [Preprint](https://www.biorxiv.org/content/10.1101/2025.03.17.643645v1.full) | [OSF](https://osf.io/z6b4d/)). 

Subsequent updates in native software ([PsychoPy](https://www.psychopy.org/)) may need adjustments. As developers, we are not responsible for implementing these in every use case.

An example of the setup is shown below.
![HLJT Animation](HLJT_example.gif)

## Repository information
The repository has two main folders, which contain **PsychoPy experiments (.psyexp)** and associated files to be able to run them **locally or online**. Please consult the Readme files for each version before using them (local and online versions are **NOT** equivalent in terms of configuration). The Readme files contain extensive documentation on the most relevant task settings and detailed information to allow the user further customization.

The versions provided in this repository allow flexibility in terms of key experiment parameters of the HLJT (e.g. angles of rotation, hand views, types of response, trial-to-trial feedback, number of trials, etc). The optimal protocol is at the user's discretion, but sensible defaults have been implemented.

## Language expansion
If you want to contribute to this repository by providing a language translation, or want to run the task in your own language, expansions can be done relatively easily thanks to the implementation of **language localisations** (please read each Readme to understand how to implement these). You can also see [this demo](https://github.com/mmorenoverdu/language_localisation_local) showing how to implement a language localisation in PsychoPy with virtually no code (for local use only).
