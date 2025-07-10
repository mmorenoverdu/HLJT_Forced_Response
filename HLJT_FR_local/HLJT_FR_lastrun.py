#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.3),
    on julio 04, 2025, at 13:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.3'
expName = 'HLJT_FR'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'language': ["English", "Spanish"],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1280, 720]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\morenoverdu\\OneDrive - UCL\\BAS-Lab\\Carla\\HLJT_FR_template\\HLJT_FR_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('welcome_adv_key') is None:
        # initialise welcome_adv_key
        welcome_adv_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='welcome_adv_key',
        )
    # create speaker 'volume_sound'
    deviceManager.addDevice(
        deviceName='volume_sound',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('inst_adv') is None:
        # initialise inst_adv
        inst_adv = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='inst_adv',
        )
    if deviceManager.getDevice('block_adv_resp') is None:
        # initialise block_adv_resp
        block_adv_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='block_adv_resp',
        )
    # create speaker 'sound_1'
    deviceManager.addDevice(
        deviceName='sound_1',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'sound_2'
    deviceManager.addDevice(
        deviceName='sound_2',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'sound_3'
    deviceManager.addDevice(
        deviceName='sound_3',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    # create speaker 'sound_4'
    deviceManager.addDevice(
        deviceName='sound_4',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "exp_settings" ---
    # Run 'Begin Experiment' code from exp_settings_code
    # block settings
    # we recommend at least 2 practice blocks to get familiar with the task timings
    practice_blocks = 2
    task_blocks = 10
    total_blocks = practice_blocks + task_blocks
    n_blocks = 0  # to be changed at will
    block_number = 0 # initialize variable for output
    
    # how many reps of the whole conditions file per block?
    # this means if you're conditions file has 4 rows
    # PsychoPy will loop through your 4 rows N times
    reps_per_block = 1
    
    # settings for max/min time of breaks between blocks
    # maximum times
    reg_max_pause = 60 # in seconds
    half_max_pause = 60*5 # we allow more time half-way through the task
    # minimum times
    min_pause = 0 # variable to be updated later
    reg_min_pause = 0 # in seconds
    half_min_pause = 1
    
    # Run 'Begin Experiment' code from conditions_order
    # list of conditions files
    cond_files_list = [f"cond_files/task_block{i}.csv" for i in range(1, 11)]
    cond_file_index = 0
    # randomize order
    import random
    random.shuffle(cond_files_list)
    thisExp.addData("cond_files_list", cond_files_list)
    thisExp.addData("cond_file_index", cond_file_index)
    
    # --- Initialize components for Routine "language_settings" ---
    # Run 'Begin Experiment' code from PY_load_messages
    ## THIS CODE ONLY WORKS IN PYTHON, NOT JAVASCRIPT ##
    # import python package to read Excel file *at the beginning of the experiment*
    import pandas as pd
    # make sure lang_code is defined and set to EN as default
    lang_code = "EN"
    # read excel file with messages according to language codes
    messages_df = pd.read_excel('messages.xlsx')
    # create an empty global dictionary with the messages
    MESSAGES = {}
    # assign each value of language to the corresponding key of language (language code)
    for idx, row in messages_df.iterrows():
        key = row['message']
        MESSAGES[key] = {}
        for col in row.index:
            if col != 'message':
                MESSAGES[key][col] = row[col]
    # create global variables with the list of messages to be usable throuhgout the experiment
    for key in MESSAGES:
        globals()[key] = MESSAGES[key].get(lang_code, MESSAGES[key]['EN'])  # fallback to English if language is not localised
    
    # --- Initialize components for Routine "welcome" ---
    welcome_text = visual.TextStim(win=win, name='welcome_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    adv_text = visual.TextStim(win=win, name='adv_text',
        text='',
        font='Open Sans',
        pos=(0, -0.45), draggable=False, height=0.045, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    welcome_adv_key = keyboard.Keyboard(deviceName='welcome_adv_key')
    
    # --- Initialize components for Routine "volume_check" ---
    # Run 'Begin Experiment' code from volume_code
    current_volume = 0.3
    vol_text = visual.TextStim(win=win, name='vol_text',
        text='',
        font='Arial',
        pos=(0, 0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    test_volume = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(0, 0.2),
        letterHeight=0.03,
        size=(0.4, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='test_volume',
        depth=-2
    )
    test_volume.buttonClock = core.Clock()
    increase_volume = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(-0.3, 0),
        letterHeight=0.05,
        size=(0.4, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='increase_volume',
        depth=-3
    )
    increase_volume.buttonClock = core.Clock()
    decrease_volume = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(0.3, 0),
        letterHeight=0.05,
        size=(0.4, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='decrease_volume',
        depth=-4
    )
    decrease_volume.buttonClock = core.Clock()
    volume_sound = sound.Sound(
        'A', 
        secs=0.3, 
        stereo=True, 
        hamming=True, 
        speaker='volume_sound',    name='volume_sound'
    )
    volume_sound.setVolume(1.0)
    proceed_to_task = visual.ButtonStim(win, 
        text='', font='Arvo',
        pos=(0.4, -0.4),
        letterHeight=0.03,
        size=(0.5, 0.1), 
        ori=0.0
        ,borderWidth=0.0,
        fillColor=[0.0824, -0.6627, 0.7725], borderColor=[0.2941, -0.6706, -0.6706],
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='proceed_to_task',
        depth=-6
    )
    proceed_to_task.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "load_inst" ---
    # Run 'Begin Experiment' code from load_inst_code
    instructions_file = ""
    
    # --- Initialize components for Routine "instructions" ---
    # Run 'Begin Experiment' code from inst_code
    instr_msg = ""
    block_welcome_msg = ""
    block_pause_msg = ""
    title_text = visual.TextStim(win=win, name='title_text',
        text='',
        font='Arial',
        pos=(0, 0.42), draggable=False, height=0.045, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    inst_text = visual.TextStim(win=win, name='inst_text',
        text='',
        font='Arial',
        pos=[0,0], draggable=False, height=0.0275, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    advance_text = visual.TextStim(win=win, name='advance_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    inst_image = visual.ImageStim(
        win=win,
        name='inst_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), draggable=False, size=1.0,
        color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    inst_adv = keyboard.Keyboard(deviceName='inst_adv')
    
    # --- Initialize components for Routine "block_start" ---
    # Run 'Begin Experiment' code from block_settings_code
    cond_file = ""
    block_main_text = visual.TextStim(win=win, name='block_main_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    block_number_text = visual.TextStim(win=win, name='block_number_text',
        text='',
        font='Arial',
        pos=(0, 0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[0.0824, -0.6627, 0.7725], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    block_adv_resp = keyboard.Keyboard(deviceName='block_adv_resp')
    block_start_adv_text = visual.TextStim(win=win, name='block_start_adv_text',
        text='',
        font='Arial',
        pos=(0, -0.45), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    timer = visual.TextStim(win=win, name='timer',
        text='',
        font='Arial',
        pos=(-0.8, -0.45), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "countdown" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='3',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_2 = visual.TextStim(win=win, name='text_2',
        text='2',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_1 = visual.TextStim(win=win, name='text_1',
        text='1',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.07, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from trial_code
    # Colors
    red = [1, 0, 0]
    white = [1, 1, 1]
    green = [0, 0.75, 0]
    black = [-1, -1, -1]
    grey = [0.0039, 0.0039, 0.0039]
    
    # Define variables
    fill_left = black
    fill_right = black
    msg_fb = ""
    msg_color = grey
    
    # Timing thresholds in seconds (+/- 100ms last tone)
    t_early_threshold = 1.9
    t_late_threshold = 2.1
    t_no_response = 2.3
    fix_cross = visual.ShapeStim(
        win=win, name='fix_cross', vertices='cross',
        size=(0.03, 0.03),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    stim_picture = visual.ImageStim(
        win=win,
        name='stim_picture', 
        image='default.png', mask=None, anchor='center',
        ori=1.0, pos=(0, 0), draggable=False, size=(0.45, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    box_left = visual.Rect(
        win=win, name='box_left',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    box_right = visual.Rect(
        win=win, name='box_right',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    sound_1 = sound.Sound(
        'A', 
        secs=0.05, 
        stereo=True, 
        hamming=True, 
        speaker='sound_1',    name='sound_1'
    )
    sound_1.setVolume(1.0)
    sound_2 = sound.Sound(
        'A', 
        secs=0.05, 
        stereo=True, 
        hamming=True, 
        speaker='sound_2',    name='sound_2'
    )
    sound_2.setVolume(1.0)
    sound_3 = sound.Sound(
        'A', 
        secs=0.05, 
        stereo=True, 
        hamming=True, 
        speaker='sound_3',    name='sound_3'
    )
    sound_3.setVolume(1.0)
    sound_4 = sound.Sound(
        'A', 
        secs=0.05, 
        stereo=True, 
        hamming=True, 
        speaker='sound_4',    name='sound_4'
    )
    sound_4.setVolume(1.0)
    fb_text = visual.TextStim(win=win, name='fb_text',
        text='',
        font='Arial',
        pos=(0, -0.25), draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "fb" ---
    textbox = visual.TextBox2(
         win, text='', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.06,
         size=(1, 0.5), borderWidth=2.0,
         color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox',
         depth=-1, autoLog=True,
    )
    box_left_2 = visual.Rect(
        win=win, name='box_left_2',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(-0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    box_right_2 = visual.Rect(
        win=win, name='box_right_2',
        width=(0.07, 0.07)[0], height=(0.07, 0.07)[1],
        ori=0.0, pos=(0.1, -0.4), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    
    # --- Initialize components for Routine "bye" ---
    bye_text = visual.TextStim(win=win, name='bye_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "exp_settings" ---
    # create an object to store info about Routine exp_settings
    exp_settings = data.Routine(
        name='exp_settings',
        components=[],
    )
    exp_settings.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for exp_settings
    exp_settings.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    exp_settings.tStart = globalClock.getTime(format='float')
    exp_settings.status = STARTED
    exp_settings.maxDuration = None
    # keep track of which components have finished
    exp_settingsComponents = exp_settings.components
    for thisComponent in exp_settings.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exp_settings" ---
    exp_settings.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            exp_settings.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp_settings.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp_settings" ---
    for thisComponent in exp_settings.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for exp_settings
    exp_settings.tStop = globalClock.getTime(format='float')
    exp_settings.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "exp_settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    language_loop = data.TrialHandler2(
        name='language_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('language_localiser.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(language_loop)  # add the loop to the experiment
    thisLanguage_loop = language_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLanguage_loop.rgb)
    if thisLanguage_loop != None:
        for paramName in thisLanguage_loop:
            globals()[paramName] = thisLanguage_loop[paramName]
    
    for thisLanguage_loop in language_loop:
        currentLoop = language_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisLanguage_loop.rgb)
        if thisLanguage_loop != None:
            for paramName in thisLanguage_loop:
                globals()[paramName] = thisLanguage_loop[paramName]
        
        # --- Prepare to start Routine "language_settings" ---
        # create an object to store info about Routine language_settings
        language_settings = data.Routine(
            name='language_settings',
            components=[],
        )
        language_settings.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from PY_load_messages
        # update language code based on the selected language in dialogue box
        if language == expInfo['language']:
            # we 'code' as a variable directly because it's already loaded in the localiser excel sheet
            lang_code = ISO_code  
            thisExp.addData("language_code", lang_code)  # add it to output
            # update global variables with new language
            # allow the messages to be used throughout the experiment by making them global variables
            for key in MESSAGES:
                globals()[key] = MESSAGES[key].get(lang_code, MESSAGES[key]['EN']) # defaults to english if something is wrong
        
        
        # store start times for language_settings
        language_settings.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        language_settings.tStart = globalClock.getTime(format='float')
        language_settings.status = STARTED
        language_settings.maxDuration = None
        # keep track of which components have finished
        language_settingsComponents = language_settings.components
        for thisComponent in language_settings.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "language_settings" ---
        # if trial has changed, end Routine now
        if isinstance(language_loop, data.TrialHandler2) and thisLanguage_loop.thisN != language_loop.thisTrial.thisN:
            continueRoutine = False
        language_settings.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                language_settings.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in language_settings.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "language_settings" ---
        for thisComponent in language_settings.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for language_settings
        language_settings.tStop = globalClock.getTime(format='float')
        language_settings.tStopRefresh = tThisFlipGlobal
        # the Routine "language_settings" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'language_loop'
    
    
    # --- Prepare to start Routine "welcome" ---
    # create an object to store info about Routine welcome
    welcome = data.Routine(
        name='welcome',
        components=[welcome_text, adv_text, welcome_adv_key],
    )
    welcome.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    welcome_text.setText(welcome_msg)
    adv_text.setText(adv_msg)
    # create starting attributes for welcome_adv_key
    welcome_adv_key.keys = []
    welcome_adv_key.rt = []
    _welcome_adv_key_allKeys = []
    # store start times for welcome
    welcome.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    welcome.tStart = globalClock.getTime(format='float')
    welcome.status = STARTED
    welcome.maxDuration = None
    # keep track of which components have finished
    welcomeComponents = welcome.components
    for thisComponent in welcome.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "welcome" ---
    welcome.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *welcome_text* updates
        
        # if welcome_text is starting this frame...
        if welcome_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            welcome_text.frameNStart = frameN  # exact frame index
            welcome_text.tStart = t  # local t and not account for scr refresh
            welcome_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            welcome_text.status = STARTED
            welcome_text.setAutoDraw(True)
        
        # if welcome_text is active this frame...
        if welcome_text.status == STARTED:
            # update params
            pass
        
        # *adv_text* updates
        
        # if adv_text is starting this frame...
        if adv_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            adv_text.frameNStart = frameN  # exact frame index
            adv_text.tStart = t  # local t and not account for scr refresh
            adv_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(adv_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            adv_text.status = STARTED
            adv_text.setAutoDraw(True)
        
        # if adv_text is active this frame...
        if adv_text.status == STARTED:
            # update params
            pass
        
        # *welcome_adv_key* updates
        waitOnFlip = False
        
        # if welcome_adv_key is starting this frame...
        if welcome_adv_key.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            welcome_adv_key.frameNStart = frameN  # exact frame index
            welcome_adv_key.tStart = t  # local t and not account for scr refresh
            welcome_adv_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(welcome_adv_key, 'tStartRefresh')  # time at next scr refresh
            # update status
            welcome_adv_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(welcome_adv_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(welcome_adv_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if welcome_adv_key.status == STARTED and not waitOnFlip:
            theseKeys = welcome_adv_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _welcome_adv_key_allKeys.extend(theseKeys)
            if len(_welcome_adv_key_allKeys):
                welcome_adv_key.keys = _welcome_adv_key_allKeys[-1].name  # just the last key pressed
                welcome_adv_key.rt = _welcome_adv_key_allKeys[-1].rt
                welcome_adv_key.duration = _welcome_adv_key_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            welcome.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in welcome.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "welcome" ---
    for thisComponent in welcome.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for welcome
    welcome.tStop = globalClock.getTime(format='float')
    welcome.tStopRefresh = tThisFlipGlobal
    thisExp.nextEntry()
    # the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    volume_loop = data.TrialHandler2(
        name='volume_loop',
        nReps=999.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(volume_loop)  # add the loop to the experiment
    thisVolume_loop = volume_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisVolume_loop.rgb)
    if thisVolume_loop != None:
        for paramName in thisVolume_loop:
            globals()[paramName] = thisVolume_loop[paramName]
    
    for thisVolume_loop in volume_loop:
        currentLoop = volume_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisVolume_loop.rgb)
        if thisVolume_loop != None:
            for paramName in thisVolume_loop:
                globals()[paramName] = thisVolume_loop[paramName]
        
        # --- Prepare to start Routine "volume_check" ---
        # create an object to store info about Routine volume_check
        volume_check = data.Routine(
            name='volume_check',
            components=[vol_text, test_volume, increase_volume, decrease_volume, volume_sound, proceed_to_task],
        )
        volume_check.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from volume_code
        # show mouse
        win.mouseVisible = True
        # ask for input in the first routine of loop
        manual_play = (volume_loop.thisN == 0)
        sound_played = False
        vol_text.setText(volume_msg)
        test_volume.setText(test_vol_msg)
        # reset test_volume to account for continued clicks & clear times on/off
        test_volume.reset()
        increase_volume.setText(increase_vol_msg)
        # reset increase_volume to account for continued clicks & clear times on/off
        increase_volume.reset()
        decrease_volume.setText(decrease_vol_msg)
        # reset decrease_volume to account for continued clicks & clear times on/off
        decrease_volume.reset()
        volume_sound.setSound('A', secs=0.3, hamming=True)
        volume_sound.setVolume(current_volume, log=False)
        volume_sound.seek(0)
        proceed_to_task.setText(proceed_task_msg)
        # reset proceed_to_task to account for continued clicks & clear times on/off
        proceed_to_task.reset()
        # store start times for volume_check
        volume_check.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        volume_check.tStart = globalClock.getTime(format='float')
        volume_check.status = STARTED
        thisExp.addData('volume_check.started', volume_check.tStart)
        volume_check.maxDuration = None
        # keep track of which components have finished
        volume_checkComponents = volume_check.components
        for thisComponent in volume_check.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "volume_check" ---
        # if trial has changed, end Routine now
        if isinstance(volume_loop, data.TrialHandler2) and thisVolume_loop.thisN != volume_loop.thisTrial.thisN:
            continueRoutine = False
        volume_check.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from volume_code
            # set so that for next iterations the sound plays automatically
            # at the beginning of the routine
            if manual_play:
                if test_volume.wasClicked and not sound_played:
                    volume_sound.play()
                    sound_played = True
            else:
                if not sound_played:
                    volume_sound.play()
                    sound_played = True
            
            # *vol_text* updates
            
            # if vol_text is starting this frame...
            if vol_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vol_text.frameNStart = frameN  # exact frame index
                vol_text.tStart = t  # local t and not account for scr refresh
                vol_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vol_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'vol_text.started')
                # update status
                vol_text.status = STARTED
                vol_text.setAutoDraw(True)
            
            # if vol_text is active this frame...
            if vol_text.status == STARTED:
                # update params
                pass
            # *test_volume* updates
            
            # if test_volume is starting this frame...
            if test_volume.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                test_volume.frameNStart = frameN  # exact frame index
                test_volume.tStart = t  # local t and not account for scr refresh
                test_volume.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_volume, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_volume.started')
                # update status
                test_volume.status = STARTED
                win.callOnFlip(test_volume.buttonClock.reset)
                test_volume.setAutoDraw(True)
            
            # if test_volume is active this frame...
            if test_volume.status == STARTED:
                # update params
                pass
                # check whether test_volume has been pressed
                if test_volume.isClicked:
                    if not test_volume.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        test_volume.timesOn.append(test_volume.buttonClock.getTime())
                        test_volume.timesOff.append(test_volume.buttonClock.getTime())
                    elif len(test_volume.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        test_volume.timesOff[-1] = test_volume.buttonClock.getTime()
                    if not test_volume.wasClicked:
                        # run callback code when test_volume is clicked
                        pass
            # take note of whether test_volume was clicked, so that next frame we know if clicks are new
            test_volume.wasClicked = test_volume.isClicked and test_volume.status == STARTED
            # *increase_volume* updates
            
            # if increase_volume is starting this frame...
            if increase_volume.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                increase_volume.frameNStart = frameN  # exact frame index
                increase_volume.tStart = t  # local t and not account for scr refresh
                increase_volume.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(increase_volume, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'increase_volume.started')
                # update status
                increase_volume.status = STARTED
                win.callOnFlip(increase_volume.buttonClock.reset)
                increase_volume.setAutoDraw(True)
            
            # if increase_volume is active this frame...
            if increase_volume.status == STARTED:
                # update params
                pass
                # check whether increase_volume has been pressed
                if increase_volume.isClicked:
                    if not increase_volume.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        increase_volume.timesOn.append(increase_volume.buttonClock.getTime())
                        increase_volume.timesOff.append(increase_volume.buttonClock.getTime())
                    elif len(increase_volume.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        increase_volume.timesOff[-1] = increase_volume.buttonClock.getTime()
                    if not increase_volume.wasClicked:
                        # end routine when increase_volume is clicked
                        continueRoutine = False
                    if not increase_volume.wasClicked:
                        # run callback code when increase_volume is clicked
                        current_volume = current_volume + 0.15
            # take note of whether increase_volume was clicked, so that next frame we know if clicks are new
            increase_volume.wasClicked = increase_volume.isClicked and increase_volume.status == STARTED
            # *decrease_volume* updates
            
            # if decrease_volume is starting this frame...
            if decrease_volume.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                decrease_volume.frameNStart = frameN  # exact frame index
                decrease_volume.tStart = t  # local t and not account for scr refresh
                decrease_volume.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(decrease_volume, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'decrease_volume.started')
                # update status
                decrease_volume.status = STARTED
                win.callOnFlip(decrease_volume.buttonClock.reset)
                decrease_volume.setAutoDraw(True)
            
            # if decrease_volume is active this frame...
            if decrease_volume.status == STARTED:
                # update params
                pass
                # check whether decrease_volume has been pressed
                if decrease_volume.isClicked:
                    if not decrease_volume.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        decrease_volume.timesOn.append(decrease_volume.buttonClock.getTime())
                        decrease_volume.timesOff.append(decrease_volume.buttonClock.getTime())
                    elif len(decrease_volume.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        decrease_volume.timesOff[-1] = decrease_volume.buttonClock.getTime()
                    if not decrease_volume.wasClicked:
                        # end routine when decrease_volume is clicked
                        continueRoutine = False
                    if not decrease_volume.wasClicked:
                        # run callback code when decrease_volume is clicked
                        current_volume = current_volume - 0.15
            # take note of whether decrease_volume was clicked, so that next frame we know if clicks are new
            decrease_volume.wasClicked = decrease_volume.isClicked and decrease_volume.status == STARTED
            
            # *volume_sound* updates
            
            # if volume_sound is stopping this frame...
            if volume_sound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > volume_sound.tStartRefresh + 0.3-frameTolerance or volume_sound.isFinished:
                    # keep track of stop time/frame for later
                    volume_sound.tStop = t  # not accounting for scr refresh
                    volume_sound.tStopRefresh = tThisFlipGlobal  # on global time
                    volume_sound.frameNStop = frameN  # exact frame index
                    # update status
                    volume_sound.status = FINISHED
                    volume_sound.stop()
            # *proceed_to_task* updates
            
            # if proceed_to_task is starting this frame...
            if proceed_to_task.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                proceed_to_task.frameNStart = frameN  # exact frame index
                proceed_to_task.tStart = t  # local t and not account for scr refresh
                proceed_to_task.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(proceed_to_task, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'proceed_to_task.started')
                # update status
                proceed_to_task.status = STARTED
                win.callOnFlip(proceed_to_task.buttonClock.reset)
                proceed_to_task.setAutoDraw(True)
            
            # if proceed_to_task is active this frame...
            if proceed_to_task.status == STARTED:
                # update params
                pass
                # check whether proceed_to_task has been pressed
                if proceed_to_task.isClicked:
                    if not proceed_to_task.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        proceed_to_task.timesOn.append(proceed_to_task.buttonClock.getTime())
                        proceed_to_task.timesOff.append(proceed_to_task.buttonClock.getTime())
                    elif len(proceed_to_task.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        proceed_to_task.timesOff[-1] = proceed_to_task.buttonClock.getTime()
                    if not proceed_to_task.wasClicked:
                        # end routine when proceed_to_task is clicked
                        continueRoutine = False
                    if not proceed_to_task.wasClicked:
                        # run callback code when proceed_to_task is clicked
                        volume_loop.finished = True
            # take note of whether proceed_to_task was clicked, so that next frame we know if clicks are new
            proceed_to_task.wasClicked = proceed_to_task.isClicked and proceed_to_task.status == STARTED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[volume_sound]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                volume_check.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in volume_check.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "volume_check" ---
        for thisComponent in volume_check.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for volume_check
        volume_check.tStop = globalClock.getTime(format='float')
        volume_check.tStopRefresh = tThisFlipGlobal
        thisExp.addData('volume_check.stopped', volume_check.tStop)
        volume_loop.addData('test_volume.numClicks', test_volume.numClicks)
        if test_volume.numClicks:
           volume_loop.addData('test_volume.timesOn', test_volume.timesOn)
           volume_loop.addData('test_volume.timesOff', test_volume.timesOff)
        else:
           volume_loop.addData('test_volume.timesOn', "")
           volume_loop.addData('test_volume.timesOff', "")
        volume_loop.addData('increase_volume.numClicks', increase_volume.numClicks)
        if increase_volume.numClicks:
           volume_loop.addData('increase_volume.timesOn', increase_volume.timesOn)
           volume_loop.addData('increase_volume.timesOff', increase_volume.timesOff)
        else:
           volume_loop.addData('increase_volume.timesOn', "")
           volume_loop.addData('increase_volume.timesOff', "")
        volume_loop.addData('decrease_volume.numClicks', decrease_volume.numClicks)
        if decrease_volume.numClicks:
           volume_loop.addData('decrease_volume.timesOn', decrease_volume.timesOn)
           volume_loop.addData('decrease_volume.timesOff', decrease_volume.timesOff)
        else:
           volume_loop.addData('decrease_volume.timesOn', "")
           volume_loop.addData('decrease_volume.timesOff', "")
        volume_sound.pause()  # ensure sound has stopped at end of Routine
        volume_loop.addData('proceed_to_task.numClicks', proceed_to_task.numClicks)
        if proceed_to_task.numClicks:
           volume_loop.addData('proceed_to_task.timesOn', proceed_to_task.timesOn)
           volume_loop.addData('proceed_to_task.timesOff', proceed_to_task.timesOff)
        else:
           volume_loop.addData('proceed_to_task.timesOn', "")
           volume_loop.addData('proceed_to_task.timesOff', "")
        # the Routine "volume_check" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 999.0 repeats of 'volume_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    task_loop = data.TrialHandler2(
        name='task_loop',
        nReps=2.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(task_loop)  # add the loop to the experiment
    thisTask_loop = task_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTask_loop.rgb)
    if thisTask_loop != None:
        for paramName in thisTask_loop:
            globals()[paramName] = thisTask_loop[paramName]
    
    for thisTask_loop in task_loop:
        currentLoop = task_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisTask_loop.rgb)
        if thisTask_loop != None:
            for paramName in thisTask_loop:
                globals()[paramName] = thisTask_loop[paramName]
        
        # --- Prepare to start Routine "load_inst" ---
        # create an object to store info about Routine load_inst
        load_inst = data.Routine(
            name='load_inst',
            components=[],
        )
        load_inst.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from load_inst_code
        
        # define instructions and number of blocks based on iteration of outer loop
        if task_loop.thisN == 0:
            instructions_file = "instructions_practice.xlsx"
            n_blocks = practice_blocks
        else:
            instructions_file = "instructions_task.xlsx"
            n_blocks = task_blocks
        # store start times for load_inst
        load_inst.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        load_inst.tStart = globalClock.getTime(format='float')
        load_inst.status = STARTED
        thisExp.addData('load_inst.started', load_inst.tStart)
        load_inst.maxDuration = None
        # keep track of which components have finished
        load_instComponents = load_inst.components
        for thisComponent in load_inst.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "load_inst" ---
        # if trial has changed, end Routine now
        if isinstance(task_loop, data.TrialHandler2) and thisTask_loop.thisN != task_loop.thisTrial.thisN:
            continueRoutine = False
        load_inst.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                load_inst.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in load_inst.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "load_inst" ---
        for thisComponent in load_inst.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for load_inst
        load_inst.tStop = globalClock.getTime(format='float')
        load_inst.tStopRefresh = tThisFlipGlobal
        thisExp.addData('load_inst.stopped', load_inst.tStop)
        # the Routine "load_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        instructions_loop = data.TrialHandler2(
            name='instructions_loop',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(instructions_file), 
            seed=None, 
        )
        thisExp.addLoop(instructions_loop)  # add the loop to the experiment
        thisInstructions_loop = instructions_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
        if thisInstructions_loop != None:
            for paramName in thisInstructions_loop:
                globals()[paramName] = thisInstructions_loop[paramName]
        
        for thisInstructions_loop in instructions_loop:
            currentLoop = instructions_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisInstructions_loop.rgb)
            if thisInstructions_loop != None:
                for paramName in thisInstructions_loop:
                    globals()[paramName] = thisInstructions_loop[paramName]
            
            # --- Prepare to start Routine "instructions" ---
            # create an object to store info about Routine instructions
            instructions = data.Routine(
                name='instructions',
                components=[title_text, inst_text, advance_text, inst_image, inst_adv],
            )
            instructions.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from inst_code
            # get column from excel sheet based on language code
            try:
                instr_msg = eval(f"instr_msg_{lang_code}")
            # default to english if this fails
            except NameError:
                instr_msg = instr_msg_EN
            
            title_text.setText(title)
            inst_text.setPos((text_pos_x, 0))
            inst_text.setText(instr_msg)
            advance_text.setText(adv_msg)
            inst_image.setSize([image_w, image_h])
            inst_image.setImage(image_file)
            # create starting attributes for inst_adv
            inst_adv.keys = []
            inst_adv.rt = []
            _inst_adv_allKeys = []
            # store start times for instructions
            instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            instructions.tStart = globalClock.getTime(format='float')
            instructions.status = STARTED
            instructions.maxDuration = None
            # keep track of which components have finished
            instructionsComponents = instructions.components
            for thisComponent in instructions.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "instructions" ---
            # if trial has changed, end Routine now
            if isinstance(instructions_loop, data.TrialHandler2) and thisInstructions_loop.thisN != instructions_loop.thisTrial.thisN:
                continueRoutine = False
            instructions.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *title_text* updates
                
                # if title_text is starting this frame...
                if title_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    title_text.frameNStart = frameN  # exact frame index
                    title_text.tStart = t  # local t and not account for scr refresh
                    title_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(title_text, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    title_text.status = STARTED
                    title_text.setAutoDraw(True)
                
                # if title_text is active this frame...
                if title_text.status == STARTED:
                    # update params
                    pass
                
                # *inst_text* updates
                
                # if inst_text is starting this frame...
                if inst_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst_text.frameNStart = frameN  # exact frame index
                    inst_text.tStart = t  # local t and not account for scr refresh
                    inst_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst_text, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst_text.status = STARTED
                    inst_text.setAutoDraw(True)
                
                # if inst_text is active this frame...
                if inst_text.status == STARTED:
                    # update params
                    pass
                
                # *advance_text* updates
                
                # if advance_text is starting this frame...
                if advance_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    advance_text.frameNStart = frameN  # exact frame index
                    advance_text.tStart = t  # local t and not account for scr refresh
                    advance_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(advance_text, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    advance_text.status = STARTED
                    advance_text.setAutoDraw(True)
                
                # if advance_text is active this frame...
                if advance_text.status == STARTED:
                    # update params
                    pass
                
                # *inst_image* updates
                
                # if inst_image is starting this frame...
                if inst_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst_image.frameNStart = frameN  # exact frame index
                    inst_image.tStart = t  # local t and not account for scr refresh
                    inst_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst_image, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst_image.status = STARTED
                    inst_image.setAutoDraw(True)
                
                # if inst_image is active this frame...
                if inst_image.status == STARTED:
                    # update params
                    pass
                
                # *inst_adv* updates
                waitOnFlip = False
                
                # if inst_adv is starting this frame...
                if inst_adv.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    inst_adv.frameNStart = frameN  # exact frame index
                    inst_adv.tStart = t  # local t and not account for scr refresh
                    inst_adv.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(inst_adv, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    inst_adv.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(inst_adv.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(inst_adv.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if inst_adv.status == STARTED and not waitOnFlip:
                    theseKeys = inst_adv.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _inst_adv_allKeys.extend(theseKeys)
                    if len(_inst_adv_allKeys):
                        inst_adv.keys = _inst_adv_allKeys[-1].name  # just the last key pressed
                        inst_adv.rt = _inst_adv_allKeys[-1].rt
                        inst_adv.duration = _inst_adv_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    instructions.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in instructions.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "instructions" ---
            for thisComponent in instructions.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for instructions
            instructions.tStop = globalClock.getTime(format='float')
            instructions.tStopRefresh = tThisFlipGlobal
            # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 1.0 repeats of 'instructions_loop'
        
        
        # set up handler to look after randomisation of conditions etc
        blocks_loop = data.TrialHandler2(
            name='blocks_loop',
            nReps=n_blocks, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(blocks_loop)  # add the loop to the experiment
        thisBlocks_loop = blocks_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
        if thisBlocks_loop != None:
            for paramName in thisBlocks_loop:
                globals()[paramName] = thisBlocks_loop[paramName]
        
        for thisBlocks_loop in blocks_loop:
            currentLoop = blocks_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
            if thisBlocks_loop != None:
                for paramName in thisBlocks_loop:
                    globals()[paramName] = thisBlocks_loop[paramName]
            
            # --- Prepare to start Routine "block_start" ---
            # create an object to store info about Routine block_start
            block_start = data.Routine(
                name='block_start',
                components=[block_main_text, block_number_text, block_adv_resp, block_start_adv_text, timer],
            )
            block_start.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from block_settings_code
            # hide mouse for the rest of the experiment
            win.mouseVisible = False
            # start block at 1 and increase every iteration
            block_number += 1
            # initialize timer
            screen_timer = core.Clock()
            # set up block settings and messages according to task progress
            # and minimum time for pauses
            # assuming we want practice blocks, which is recommended
            # if you want to set up the trial order beforehand, you would just need
            # to have separate excel sheets for each block, and specify the order with
            # elif statements OR more conveniently, have some code to randomize your
            # order of excel sheets and then proceed with the randomized list in a 
            # sequential order
            if block_number <= practice_blocks: # assuming there are practice blocks
                cond_file = "cond_files/cond_practice.xlsx"
                min_pause = reg_min_pause
                if block_number == 1:
                    block_message = block_first_msg
                else:
                    block_message = block_msg_standard
            elif block_number > practice_blocks: 
                cond_file = cond_files_list[cond_file_index] # start at 0
                cond_file_index += 1
                block_message = block_msg_standard
                min_pause = reg_min_pause
                if block_number == practice_blocks + 1:
                    block_message = block_intro_task_msg
            # halfway through the task we force a break and change the message
                elif block_number - practice_blocks == round(task_blocks / 2) + 1:
                    block_message = block_msg_half
                    min_pause = half_min_pause # set up at the start of exp!
            
            thisExp.addData("block_number", block_number)
            thisExp.addData("cond_file_index", cond_file_index)
            thisExp.addData("cond_file", cond_file)
            block_main_text.setText(block_message)
            block_number_text.setText(block_n_msg1 + ' ' + str(block_number) + ' ' + block_n_msg2 + ' ' + str(total_blocks) )
            # create starting attributes for block_adv_resp
            block_adv_resp.keys = []
            block_adv_resp.rt = []
            _block_adv_resp_allKeys = []
            block_start_adv_text.setText(adv_msg)
            # store start times for block_start
            block_start.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            block_start.tStart = globalClock.getTime(format='float')
            block_start.status = STARTED
            thisExp.addData('block_start.started', block_start.tStart)
            block_start.maxDuration = None
            # keep track of which components have finished
            block_startComponents = block_start.components
            for thisComponent in block_start.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "block_start" ---
            # if trial has changed, end Routine now
            if isinstance(blocks_loop, data.TrialHandler2) and thisBlocks_loop.thisN != blocks_loop.thisTrial.thisN:
                continueRoutine = False
            block_start.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from block_settings_code
                # show timer
                elapsed = screen_timer.getTime()
                minutes = int(elapsed // 60)
                seconds = int(elapsed % 60)
                timer_text = f"{minutes:02d}:{seconds:02d}"
                
                # depending on block number, allow 1 or 5 minutes
                if block_number == round(n_blocks / 2):
                    # halfway through, 5 minutes
                    if seconds >= half_max_pause:
                        continueRoutine = False
                else:
                    # otherwise 1 minute
                    if seconds >= reg_max_pause:
                        continueRoutine = False
                
                # *block_main_text* updates
                
                # if block_main_text is starting this frame...
                if block_main_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    block_main_text.frameNStart = frameN  # exact frame index
                    block_main_text.tStart = t  # local t and not account for scr refresh
                    block_main_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(block_main_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'block_main_text.started')
                    # update status
                    block_main_text.status = STARTED
                    block_main_text.setAutoDraw(True)
                
                # if block_main_text is active this frame...
                if block_main_text.status == STARTED:
                    # update params
                    pass
                
                # *block_number_text* updates
                
                # if block_number_text is starting this frame...
                if block_number_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    block_number_text.frameNStart = frameN  # exact frame index
                    block_number_text.tStart = t  # local t and not account for scr refresh
                    block_number_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(block_number_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'block_number_text.started')
                    # update status
                    block_number_text.status = STARTED
                    block_number_text.setAutoDraw(True)
                
                # if block_number_text is active this frame...
                if block_number_text.status == STARTED:
                    # update params
                    pass
                
                # *block_adv_resp* updates
                waitOnFlip = False
                
                # if block_adv_resp is starting this frame...
                if block_adv_resp.status == NOT_STARTED and tThisFlip >= min_pause-frameTolerance:
                    # keep track of start time/frame for later
                    block_adv_resp.frameNStart = frameN  # exact frame index
                    block_adv_resp.tStart = t  # local t and not account for scr refresh
                    block_adv_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(block_adv_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'block_adv_resp.started')
                    # update status
                    block_adv_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(block_adv_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(block_adv_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if block_adv_resp.status == STARTED and not waitOnFlip:
                    theseKeys = block_adv_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _block_adv_resp_allKeys.extend(theseKeys)
                    if len(_block_adv_resp_allKeys):
                        block_adv_resp.keys = _block_adv_resp_allKeys[-1].name  # just the last key pressed
                        block_adv_resp.rt = _block_adv_resp_allKeys[-1].rt
                        block_adv_resp.duration = _block_adv_resp_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *block_start_adv_text* updates
                
                # if block_start_adv_text is starting this frame...
                if block_start_adv_text.status == NOT_STARTED and tThisFlip >= min_pause-frameTolerance:
                    # keep track of start time/frame for later
                    block_start_adv_text.frameNStart = frameN  # exact frame index
                    block_start_adv_text.tStart = t  # local t and not account for scr refresh
                    block_start_adv_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(block_start_adv_text, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    block_start_adv_text.status = STARTED
                    block_start_adv_text.setAutoDraw(True)
                
                # if block_start_adv_text is active this frame...
                if block_start_adv_text.status == STARTED:
                    # update params
                    pass
                
                # *timer* updates
                
                # if timer is starting this frame...
                if timer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    timer.frameNStart = frameN  # exact frame index
                    timer.tStart = t  # local t and not account for scr refresh
                    timer.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(timer, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'timer.started')
                    # update status
                    timer.status = STARTED
                    timer.setAutoDraw(True)
                
                # if timer is active this frame...
                if timer.status == STARTED:
                    # update params
                    timer.setText(timer_text, log=False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    block_start.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in block_start.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "block_start" ---
            for thisComponent in block_start.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for block_start
            block_start.tStop = globalClock.getTime(format='float')
            block_start.tStopRefresh = tThisFlipGlobal
            thisExp.addData('block_start.stopped', block_start.tStop)
            # Run 'End Routine' code from block_settings_code
            thisExp.addData("block_pause", seconds)
            # check responses
            if block_adv_resp.keys in ['', [], None]:  # No response was made
                block_adv_resp.keys = None
            blocks_loop.addData('block_adv_resp.keys',block_adv_resp.keys)
            if block_adv_resp.keys != None:  # we had a response
                blocks_loop.addData('block_adv_resp.rt', block_adv_resp.rt)
                blocks_loop.addData('block_adv_resp.duration', block_adv_resp.duration)
            # the Routine "block_start" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "countdown" ---
            # create an object to store info about Routine countdown
            countdown = data.Routine(
                name='countdown',
                components=[text_3, text_2, text_1],
            )
            countdown.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for countdown
            countdown.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            countdown.tStart = globalClock.getTime(format='float')
            countdown.status = STARTED
            thisExp.addData('countdown.started', countdown.tStart)
            countdown.maxDuration = 3.5
            # keep track of which components have finished
            countdownComponents = countdown.components
            for thisComponent in countdown.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "countdown" ---
            # if trial has changed, end Routine now
            if isinstance(blocks_loop, data.TrialHandler2) and thisBlocks_loop.thisN != blocks_loop.thisTrial.thisN:
                continueRoutine = False
            countdown.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 3.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > countdown.maxDuration-frameTolerance:
                    countdown.maxDurationReached = True
                    continueRoutine = False
                
                # *text_3* updates
                
                # if text_3 is starting this frame...
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.started')
                    # update status
                    text_3.status = STARTED
                    text_3.setAutoDraw(True)
                
                # if text_3 is active this frame...
                if text_3.status == STARTED:
                    # update params
                    pass
                
                # if text_3 is stopping this frame...
                if text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        text_3.tStop = t  # not accounting for scr refresh
                        text_3.tStopRefresh = tThisFlipGlobal  # on global time
                        text_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_3.stopped')
                        # update status
                        text_3.status = FINISHED
                        text_3.setAutoDraw(False)
                
                # *text_2* updates
                
                # if text_2 is starting this frame...
                if text_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.started')
                    # update status
                    text_2.status = STARTED
                    text_2.setAutoDraw(True)
                
                # if text_2 is active this frame...
                if text_2.status == STARTED:
                    # update params
                    pass
                
                # if text_2 is stopping this frame...
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.tStopRefresh = tThisFlipGlobal  # on global time
                        text_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_2.stopped')
                        # update status
                        text_2.status = FINISHED
                        text_2.setAutoDraw(False)
                
                # *text_1* updates
                
                # if text_1 is starting this frame...
                if text_1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    text_1.frameNStart = frameN  # exact frame index
                    text_1.tStart = t  # local t and not account for scr refresh
                    text_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_1.started')
                    # update status
                    text_1.status = STARTED
                    text_1.setAutoDraw(True)
                
                # if text_1 is active this frame...
                if text_1.status == STARTED:
                    # update params
                    pass
                
                # if text_1 is stopping this frame...
                if text_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_1.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        text_1.tStop = t  # not accounting for scr refresh
                        text_1.tStopRefresh = tThisFlipGlobal  # on global time
                        text_1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_1.stopped')
                        # update status
                        text_1.status = FINISHED
                        text_1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    countdown.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in countdown.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "countdown" ---
            for thisComponent in countdown.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for countdown
            countdown.tStop = globalClock.getTime(format='float')
            countdown.tStopRefresh = tThisFlipGlobal
            thisExp.addData('countdown.stopped', countdown.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if countdown.maxDurationReached:
                routineTimer.addTime(-countdown.maxDuration)
            elif countdown.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-3.500000)
            
            # set up handler to look after randomisation of conditions etc
            trials_loop = data.TrialHandler2(
                name='trials_loop',
                nReps=reps_per_block, 
                method='sequential', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions(
                cond_file, 
                selection='0:3'
            )
            , 
                seed=None, 
            )
            thisExp.addLoop(trials_loop)  # add the loop to the experiment
            thisTrials_loop = trials_loop.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
            if thisTrials_loop != None:
                for paramName in thisTrials_loop:
                    globals()[paramName] = thisTrials_loop[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisTrials_loop in trials_loop:
                currentLoop = trials_loop
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
                if thisTrials_loop != None:
                    for paramName in thisTrials_loop:
                        globals()[paramName] = thisTrials_loop[paramName]
                
                # --- Prepare to start Routine "trial" ---
                # create an object to store info about Routine trial
                trial = data.Routine(
                    name='trial',
                    components=[fix_cross, stim_picture, box_left, box_right, sound_1, sound_2, sound_3, sound_4, fb_text, key_resp],
                )
                trial.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from trial_code
                # set variables to their starting values
                fill_left = black
                fill_right = black
                fb_msg = ""
                msg_color = grey
                stim_picture.setOri(stim_angle)
                stim_picture.setImage(stim_file)
                sound_1.setSound('A', secs=0.05, hamming=True)
                sound_1.setVolume(1.0, log=False)
                sound_1.seek(0)
                sound_2.setSound('A', secs=0.05, hamming=True)
                sound_2.setVolume(1.0, log=False)
                sound_2.seek(0)
                sound_3.setSound('A', secs=0.05, hamming=True)
                sound_3.setVolume(1.0, log=False)
                sound_3.seek(0)
                sound_4.setSound('B', secs=0.05, hamming=True)
                sound_4.setVolume(1.0, log=False)
                sound_4.seek(0)
                # create starting attributes for key_resp
                key_resp.keys = []
                key_resp.rt = []
                _key_resp_allKeys = []
                # store start times for trial
                trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                trial.tStart = globalClock.getTime(format='float')
                trial.status = STARTED
                thisExp.addData('trial.started', trial.tStart)
                trial.maxDuration = 2.4
                # keep track of which components have finished
                trialComponents = trial.components
                for thisComponent in trial.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "trial" ---
                # if trial has changed, end Routine now
                if isinstance(trials_loop, data.TrialHandler2) and thisTrials_loop.thisN != trials_loop.thisTrial.thisN:
                    continueRoutine = False
                trial.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # is it time to end the Routine? (based on local clock)
                    if tThisFlip > trial.maxDuration-frameTolerance:
                        trial.maxDurationReached = True
                        continueRoutine = False
                    # Run 'Each Frame' code from trial_code
                    # Feedback based on response time
                    if key_resp.keys is None or key_resp.rt in [None, []]:
                        fb_msg = ""
                        msg_color = grey  # Default color if no response
                    else:
                        rt = key_resp.rt[0] if isinstance(key_resp.rt, list) else key_resp.rt
                        if rt <= t_early_threshold:
                            fb_msg = early_msg
                            msg_color = black
                        elif t_early_threshold < rt < t_late_threshold:
                            fb_msg = ""
                            msg_color = grey
                        elif rt >= t_late_threshold:
                            fb_msg = late_msg
                            msg_color = black
                    
                    # Feedback based on response accuracy
                    if key_resp.keys == "s":
                        if key_resp.corr == 1:
                            fill_left = green
                            fill_right = black
                        else:
                            fill_left = red
                            fill_right = black
                    elif key_resp.keys == "l":
                        if key_resp.corr == 1:
                            fill_left = black
                            fill_right = green
                        else:
                            fill_left = black
                            fill_right = red
                    
                    # *fix_cross* updates
                    
                    # if fix_cross is starting this frame...
                    if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fix_cross.frameNStart = frameN  # exact frame index
                        fix_cross.tStart = t  # local t and not account for scr refresh
                        fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix_cross.started')
                        # update status
                        fix_cross.status = STARTED
                        fix_cross.setAutoDraw(True)
                    
                    # if fix_cross is active this frame...
                    if fix_cross.status == STARTED:
                        # update params
                        pass
                    
                    # *stim_picture* updates
                    
                    # if stim_picture is starting this frame...
                    if stim_picture.status == NOT_STARTED and tThisFlip >= stim_timing-frameTolerance:
                        # keep track of start time/frame for later
                        stim_picture.frameNStart = frameN  # exact frame index
                        stim_picture.tStart = t  # local t and not account for scr refresh
                        stim_picture.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(stim_picture, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stim_picture.started')
                        # update status
                        stim_picture.status = STARTED
                        stim_picture.setAutoDraw(True)
                    
                    # if stim_picture is active this frame...
                    if stim_picture.status == STARTED:
                        # update params
                        pass
                    
                    # if stim_picture is stopping this frame...
                    if stim_picture.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > stim_picture.tStartRefresh + 2.1-frameTolerance:
                            # keep track of stop time/frame for later
                            stim_picture.tStop = t  # not accounting for scr refresh
                            stim_picture.tStopRefresh = tThisFlipGlobal  # on global time
                            stim_picture.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'stim_picture.stopped')
                            # update status
                            stim_picture.status = FINISHED
                            stim_picture.setAutoDraw(False)
                    
                    # *box_left* updates
                    
                    # if box_left is starting this frame...
                    if box_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        box_left.frameNStart = frameN  # exact frame index
                        box_left.tStart = t  # local t and not account for scr refresh
                        box_left.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(box_left, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'box_left.started')
                        # update status
                        box_left.status = STARTED
                        box_left.setAutoDraw(True)
                    
                    # if box_left is active this frame...
                    if box_left.status == STARTED:
                        # update params
                        box_left.setFillColor(fill_left, log=False)
                        box_left.setLineColor(fill_left, log=False)
                    
                    # *box_right* updates
                    
                    # if box_right is starting this frame...
                    if box_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        box_right.frameNStart = frameN  # exact frame index
                        box_right.tStart = t  # local t and not account for scr refresh
                        box_right.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(box_right, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'box_right.started')
                        # update status
                        box_right.status = STARTED
                        box_right.setAutoDraw(True)
                    
                    # if box_right is active this frame...
                    if box_right.status == STARTED:
                        # update params
                        box_right.setFillColor(fill_right, log=False)
                        box_right.setLineColor(fill_right, log=False)
                    
                    # *sound_1* updates
                    
                    # if sound_1 is starting this frame...
                    if sound_1.status == NOT_STARTED and tThisFlip >= 0.02-frameTolerance:
                        # keep track of start time/frame for later
                        sound_1.frameNStart = frameN  # exact frame index
                        sound_1.tStart = t  # local t and not account for scr refresh
                        sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                        # add timestamp to datafile
                        thisExp.addData('sound_1.started', tThisFlipGlobal)
                        # update status
                        sound_1.status = STARTED
                        sound_1.play(when=win)  # sync with win flip
                    
                    # if sound_1 is stopping this frame...
                    if sound_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > sound_1.tStartRefresh + 0.05-frameTolerance or sound_1.isFinished:
                            # keep track of stop time/frame for later
                            sound_1.tStop = t  # not accounting for scr refresh
                            sound_1.tStopRefresh = tThisFlipGlobal  # on global time
                            sound_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'sound_1.stopped')
                            # update status
                            sound_1.status = FINISHED
                            sound_1.stop()
                    
                    # *sound_2* updates
                    
                    # if sound_2 is starting this frame...
                    if sound_2.status == NOT_STARTED and tThisFlip >= 0.68-frameTolerance:
                        # keep track of start time/frame for later
                        sound_2.frameNStart = frameN  # exact frame index
                        sound_2.tStart = t  # local t and not account for scr refresh
                        sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                        # add timestamp to datafile
                        thisExp.addData('sound_2.started', tThisFlipGlobal)
                        # update status
                        sound_2.status = STARTED
                        sound_2.play(when=win)  # sync with win flip
                    
                    # if sound_2 is stopping this frame...
                    if sound_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > sound_2.tStartRefresh + 0.05-frameTolerance or sound_2.isFinished:
                            # keep track of stop time/frame for later
                            sound_2.tStop = t  # not accounting for scr refresh
                            sound_2.tStopRefresh = tThisFlipGlobal  # on global time
                            sound_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'sound_2.stopped')
                            # update status
                            sound_2.status = FINISHED
                            sound_2.stop()
                    
                    # *sound_3* updates
                    
                    # if sound_3 is starting this frame...
                    if sound_3.status == NOT_STARTED and tThisFlip >= 1.34-frameTolerance:
                        # keep track of start time/frame for later
                        sound_3.frameNStart = frameN  # exact frame index
                        sound_3.tStart = t  # local t and not account for scr refresh
                        sound_3.tStartRefresh = tThisFlipGlobal  # on global time
                        # add timestamp to datafile
                        thisExp.addData('sound_3.started', tThisFlipGlobal)
                        # update status
                        sound_3.status = STARTED
                        sound_3.play(when=win)  # sync with win flip
                    
                    # if sound_3 is stopping this frame...
                    if sound_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > sound_3.tStartRefresh + 0.05-frameTolerance or sound_3.isFinished:
                            # keep track of stop time/frame for later
                            sound_3.tStop = t  # not accounting for scr refresh
                            sound_3.tStopRefresh = tThisFlipGlobal  # on global time
                            sound_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'sound_3.stopped')
                            # update status
                            sound_3.status = FINISHED
                            sound_3.stop()
                    
                    # *sound_4* updates
                    
                    # if sound_4 is starting this frame...
                    if sound_4.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                        # keep track of start time/frame for later
                        sound_4.frameNStart = frameN  # exact frame index
                        sound_4.tStart = t  # local t and not account for scr refresh
                        sound_4.tStartRefresh = tThisFlipGlobal  # on global time
                        # add timestamp to datafile
                        thisExp.addData('sound_4.started', tThisFlipGlobal)
                        # update status
                        sound_4.status = STARTED
                        sound_4.play(when=win)  # sync with win flip
                    
                    # if sound_4 is stopping this frame...
                    if sound_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > sound_4.tStartRefresh + 0.05-frameTolerance or sound_4.isFinished:
                            # keep track of stop time/frame for later
                            sound_4.tStop = t  # not accounting for scr refresh
                            sound_4.tStopRefresh = tThisFlipGlobal  # on global time
                            sound_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'sound_4.stopped')
                            # update status
                            sound_4.status = FINISHED
                            sound_4.stop()
                    
                    # *fb_text* updates
                    
                    # if fb_text is starting this frame...
                    if fb_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fb_text.frameNStart = frameN  # exact frame index
                        fb_text.tStart = t  # local t and not account for scr refresh
                        fb_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fb_text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fb_text.started')
                        # update status
                        fb_text.status = STARTED
                        fb_text.setAutoDraw(True)
                    
                    # if fb_text is active this frame...
                    if fb_text.status == STARTED:
                        # update params
                        fb_text.setText(fb_msg, log=False)
                    
                    # *key_resp* updates
                    waitOnFlip = False
                    
                    # if key_resp is starting this frame...
                    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp.frameNStart = frameN  # exact frame index
                        key_resp.tStart = t  # local t and not account for scr refresh
                        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp.started')
                        # update status
                        key_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp.getKeys(keyList=['s','l'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_allKeys.extend(theseKeys)
                        if len(_key_resp_allKeys):
                            key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                            key_resp.rt = _key_resp_allKeys[0].rt
                            key_resp.duration = _key_resp_allKeys[0].duration
                            # was this correct?
                            if (key_resp.keys == str(stim_correct_key)) or (key_resp.keys == stim_correct_key):
                                key_resp.corr = 1
                            else:
                                key_resp.corr = 0
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[sound_1, sound_2, sound_3, sound_4]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        trial.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trial.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "trial" ---
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for trial
                trial.tStop = globalClock.getTime(format='float')
                trial.tStopRefresh = tThisFlipGlobal
                thisExp.addData('trial.stopped', trial.tStop)
                # Run 'End Routine' code from trial_code
                # when did the stimulus actually appear?
                thisExp.addData('stim_picture.frameNStart', stim_picture.frameNStart)
                thisExp.addData('stim_picture.tStart', stim_picture.tStart)
                # when did the last tone actually sound?
                thisExp.addData('sound_4.frameNStart', sound_4.frameNStart)
                thisExp.addData('sound_4.tStart', sound_4.tStart)
                
                # save current block for more intuitive output
                thisExp.addData("block_number", block_number)
                sound_1.pause()  # ensure sound has stopped at end of Routine
                sound_2.pause()  # ensure sound has stopped at end of Routine
                sound_3.pause()  # ensure sound has stopped at end of Routine
                sound_4.pause()  # ensure sound has stopped at end of Routine
                # check responses
                if key_resp.keys in ['', [], None]:  # No response was made
                    key_resp.keys = None
                    # was no response the correct answer?!
                    if str(stim_correct_key).lower() == 'none':
                       key_resp.corr = 1;  # correct non-response
                    else:
                       key_resp.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_loop (TrialHandler)
                trials_loop.addData('key_resp.keys',key_resp.keys)
                trials_loop.addData('key_resp.corr', key_resp.corr)
                if key_resp.keys != None:  # we had a response
                    trials_loop.addData('key_resp.rt', key_resp.rt)
                    trials_loop.addData('key_resp.duration', key_resp.duration)
                # the Routine "trial" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "fb" ---
                # create an object to store info about Routine fb
                fb = data.Routine(
                    name='fb',
                    components=[textbox, box_left_2, box_right_2],
                )
                fb.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from fb_code
                # Skip routine if a key has been pressed
                if key_resp.keys != None:
                    continueRoutine = False
                else:
                    continueRoutine = True
                textbox.reset()
                textbox.setText(nr_msg)
                # store start times for fb
                fb.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                fb.tStart = globalClock.getTime(format='float')
                fb.status = STARTED
                thisExp.addData('fb.started', fb.tStart)
                fb.maxDuration = 1
                # keep track of which components have finished
                fbComponents = fb.components
                for thisComponent in fb.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "fb" ---
                # if trial has changed, end Routine now
                if isinstance(trials_loop, data.TrialHandler2) and thisTrials_loop.thisN != trials_loop.thisTrial.thisN:
                    continueRoutine = False
                fb.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # is it time to end the Routine? (based on local clock)
                    if tThisFlip > fb.maxDuration-frameTolerance:
                        fb.maxDurationReached = True
                        continueRoutine = False
                    
                    # *textbox* updates
                    
                    # if textbox is starting this frame...
                    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        textbox.frameNStart = frameN  # exact frame index
                        textbox.tStart = t  # local t and not account for scr refresh
                        textbox.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textbox.started')
                        # update status
                        textbox.status = STARTED
                        textbox.setAutoDraw(True)
                    
                    # if textbox is active this frame...
                    if textbox.status == STARTED:
                        # update params
                        pass
                    
                    # if textbox is stopping this frame...
                    if textbox.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > textbox.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            textbox.tStop = t  # not accounting for scr refresh
                            textbox.tStopRefresh = tThisFlipGlobal  # on global time
                            textbox.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'textbox.stopped')
                            # update status
                            textbox.status = FINISHED
                            textbox.setAutoDraw(False)
                    
                    # *box_left_2* updates
                    
                    # if box_left_2 is starting this frame...
                    if box_left_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        box_left_2.frameNStart = frameN  # exact frame index
                        box_left_2.tStart = t  # local t and not account for scr refresh
                        box_left_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(box_left_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'box_left_2.started')
                        # update status
                        box_left_2.status = STARTED
                        box_left_2.setAutoDraw(True)
                    
                    # if box_left_2 is active this frame...
                    if box_left_2.status == STARTED:
                        # update params
                        pass
                    
                    # if box_left_2 is stopping this frame...
                    if box_left_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > box_left_2.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            box_left_2.tStop = t  # not accounting for scr refresh
                            box_left_2.tStopRefresh = tThisFlipGlobal  # on global time
                            box_left_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'box_left_2.stopped')
                            # update status
                            box_left_2.status = FINISHED
                            box_left_2.setAutoDraw(False)
                    
                    # *box_right_2* updates
                    
                    # if box_right_2 is starting this frame...
                    if box_right_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        box_right_2.frameNStart = frameN  # exact frame index
                        box_right_2.tStart = t  # local t and not account for scr refresh
                        box_right_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(box_right_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'box_right_2.started')
                        # update status
                        box_right_2.status = STARTED
                        box_right_2.setAutoDraw(True)
                    
                    # if box_right_2 is active this frame...
                    if box_right_2.status == STARTED:
                        # update params
                        pass
                    
                    # if box_right_2 is stopping this frame...
                    if box_right_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > box_right_2.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            box_right_2.tStop = t  # not accounting for scr refresh
                            box_right_2.tStopRefresh = tThisFlipGlobal  # on global time
                            box_right_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'box_right_2.stopped')
                            # update status
                            box_right_2.status = FINISHED
                            box_right_2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        fb.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in fb.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "fb" ---
                for thisComponent in fb.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for fb
                fb.tStop = globalClock.getTime(format='float')
                fb.tStopRefresh = tThisFlipGlobal
                thisExp.addData('fb.stopped', fb.tStop)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if fb.maxDurationReached:
                    routineTimer.addTime(-fb.maxDuration)
                elif fb.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
            # completed reps_per_block repeats of 'trials_loop'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed n_blocks repeats of 'blocks_loop'
        
    # completed 2.0 repeats of 'task_loop'
    
    
    # --- Prepare to start Routine "bye" ---
    # create an object to store info about Routine bye
    bye = data.Routine(
        name='bye',
        components=[bye_text],
    )
    bye.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    bye_text.setText(bye_msg)
    # store start times for bye
    bye.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    bye.tStart = globalClock.getTime(format='float')
    bye.status = STARTED
    thisExp.addData('bye.started', bye.tStart)
    bye.maxDuration = 3
    # keep track of which components have finished
    byeComponents = bye.components
    for thisComponent in bye.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "bye" ---
    bye.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > bye.maxDuration-frameTolerance:
            bye.maxDurationReached = True
            continueRoutine = False
        
        # *bye_text* updates
        
        # if bye_text is starting this frame...
        if bye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bye_text.frameNStart = frameN  # exact frame index
            bye_text.tStart = t  # local t and not account for scr refresh
            bye_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bye_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'bye_text.started')
            # update status
            bye_text.status = STARTED
            bye_text.setAutoDraw(True)
        
        # if bye_text is active this frame...
        if bye_text.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            bye.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in bye.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "bye" ---
    for thisComponent in bye.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for bye
    bye.tStop = globalClock.getTime(format='float')
    bye.tStopRefresh = tThisFlipGlobal
    thisExp.addData('bye.stopped', bye.tStop)
    thisExp.nextEntry()
    # the Routine "bye" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
