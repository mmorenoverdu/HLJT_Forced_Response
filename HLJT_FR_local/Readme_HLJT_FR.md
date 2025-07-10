# HAND LATERALITY JUDGEMENT TASK - FORCED RESPONSE (HLJT-FR)

Marcos Moreno Verdu, 04/07/2025


PsychoPy version 2024.2.1


Local experiment


Languages supported: English, Spanish, French. Further languages can be added with no code (see Language Localisation below)


---------------------------------------
## GENERAL INSTRUCTIONS: ##

This README is not intended to explain how PsychoPy generally works, but the specific aspects of this experiment.

If you have never used PsychoPy, please have a look at the documentation on their webpage or tutorials, especially regarding conditions files, variables, routines and loops. This will save you time if you decide to modify any parameters from this experiment.

If you have never used PsychoPy, you should know that once you have decompressed the .zip file, you must not change the names of the files/folders, as the .psyexp file is going to look for specific names at specific locations. Additionally, you should avoid, wherever possible, changing any variable names, as again, the code depending on that variable name will need to be adjusted as well. Bear this in mind.

---------------------------------------
## SETUP INSTRUCTIONS ##

To run this task you need to have installed PsychoPy version 2024.2.1 or superior.

Dependencies:
- R software to generate conditions files with a pseudo-random order and balanced distributions of stimuli presentation.
- Package "random" in Python to randomize the order of conditions files.

The data output MUST be processed to obtain meaningful information (relevant columns in output files are listed below).

Step-by-step instructions:
1) Download all files from the repository
2) Unzip the file in a NEW folder WITHOUT any other PsychoPy experiments in it.
3) Open the file 'HLJT_FR.psyexp' in PsychoPy.

---------------------------------------
## LANGUAGE LOCALISATION ##

We need 2 Excel sheets (with extension type .xlsx) to store:
- The available language localisations: "language_localiser.xlsx"
- The list of messages to use as variables to display text on screen: "messages.xlsx"

In the Experiment Settings button, in the Basic tab, the Experiment Info section must have a "language" field with the list of languages. This allows to select the language **before** every run of the Experiment through a dropdown menu in the pop-up dialogue box. These languages need to be specified as in the language column of the language localiser Excel sheet.

All the text components which should be dynamically updated for language should have their "Text" field in **"Set to every repeat"**. This allows to change dynamically the value of the variable, which therefore changes the text to be shown.

**Adding a new language**

If you just want to add a new language without any further modifications (i.e., you do not want to provide other messages than the ones already used), you just need to modify 4 things:
1. In language_localiser.xlsx, add a new **ROW** with your new language and its code. Write this in English (e.g., "Chinese", "CH").
2. In messages.xlsx, add a new **COLUMN**, titled with the code you used in the previous step (e.g., "CH"). For each message, provide the corresponding translation into your desired language.
3. In PsychoPy, go to Experiment Settings and add a new language to the list of languages in the **language field**, with the name being the language you used in Step 1. It is critical that you add your language using '' (e.g., 'Chinese'). If you want your language to be the default choice every time you run the experiment, you just have to **place it at the beginning of the list**.
4. Add the corresponding columns with your language to the different instructions files and block messages (Excel sheets).

**Working online**


If you want to adapt this experiment to be able to run online WITH a language localisation, you will need to provide JavaScript code and define the messages through it at the beginning of the experiment. If you only want to provide text in a single language, you can do it through code chunks and variables.

---------------------------------------
## TECHNICAL DETAILS: ##

The experiment has the following subfolders and files:

-stimuli: It contains the four stimuli to be used in the task. This is left/right hand images in .png format. The images are divided into dorsal or palmar view.

-images: It has the images to display in the instructions of the experiment, which include:

-instructions files (.xlsx): Each file encodes the instructions for the practice or the main task.

-cond_files: It contains KEY files that are used to run the experiment.


	-cond_practice.csv: Encodes the conditions to run in the practice part.


	-task_block*.csv: Encodes the conditions to run in the main task part. There are 10 blocks with 160 trials each (for a total of 1600 trials (16 conditions x 100 timings each). See R script to understand where this comes from.
		-stim_angle: which angle to rotate the image (always clockwise).
		-stim_laterality: which side of the body (laterality) this image belongs to.
		-stim_view: which view of the hand the image is (palmar/dorsal).
		-stim_timing: which timing the stimulus is going to be presented at.
		-stim_file: the actual file to be used as stimulus
		-stim_correct_key: the actual key that stores the correct response (s for left, l for right)
---------------------------------------
## EXPERIMENT SETTINGS (parameters to choose) ##

In the folder "cond_files", there is an R script which can be used to actually modify the conditions of the experiment. The R script generates the CSV files that are used as conditions files. Therefore, modifying this script will change the actual conditions. Please read the documentation already provided in the R script to understand how the conditions are generated.

If you want to change the number of blocks for the main task (e.g. you want 5 blocks instead of 10), you will need not only to modify the R script but also the PsychoPy experiment. In the PsychoPy experiment, in the experiment settings ROUTINE, there is a code component that imports the list of conditions files and randomizes it. Therefore adjustments need to be done to this code chunk in order to change the number of blocks to run.
	
	
---------------------------------------
## PARTICIPANT WORKFLOW: ##

Once the experiment starts, it will guide the participant through it without the need for any other explicit supervision. There will be:


-A welcome screen with a brief description of the goal of the task.
	
-A screen to adjust the volume of the computer (it should be possible to do it on the computer itself as well).

-A couple of screens with instructions and practice block(s) to familiarise with the timing requirements.

-A couple of screens with the instructions for the main task to be completed.

-A number of blocks with the main task (with breaks between them).

-A goodbye screen.

---------------------------------------
## OUTPUT: ##

The output file that PsychoPy will generate will be a .csv file in a subfolder "data". This .csv will contain all the variables encoded in the experiment. It will always be named with the participant field and the date.

The output variables we will be interested in, are:
	
-key_resp.rt: Encodes the response time for each trial of the test blocks. It does it in SECONDS.

-key_resp.corr: Encodes the accuracy for each trial of the test blocks. Correct (=1) or incorrect (=0).

-stim_picture.timeStart: Encodes the time at which the stimulus was actually on screen. It does it in SECONDS.

-sound_4.tStart: Encodes the time at which the 4th tone (last tone) actually happened. It does it in SECONDS.

Aside from those, we will need to retain the variables from our conditions file for analysis:
	

	-stim_angle


	-stim_laterality


	-stim_view


	-stim_timing


	-stim_correct_key

All the variables shown in the dialog box will be saved.
