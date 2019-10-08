# RoboGym 

RoboGym is a virtual environment to train robots. 
The platform used for training is called Animal-Olympics to train animal-like behavious for our agent. 


# Animal-AI Olympics

## IMPORTANT NOTICE ABOUT PRIZES
Please remember **to submit to the competition and be considered for prizes you must also fill in [this form](https://forms.gle/PKCgp2JAWvjf4c9i6)**. You must do so before the end of September 1st to be considered for the AWS prizes!

<p align="center">
  <img height="300" src="documentation/PrefabsPictures/steampunkFOURcrop.png">
</p>

**July 1st - November 1st**

The Animal-AI Olympics is an AI competition with tests inspired by animal cognition. Participants are given a small environment with just seven different classes of objects that can be placed inside. In each test, the agent needs to retrieve the food in the environment, but to do so there are obstacles to overcome, ramps to climb, boxes to push, and areas that must be avoided. The real challenge is that we don't provide the tests in advance. It's up to you to explore the possibilities with the environment and build interesting configurations that can help create an agent that understands how the environment's physics work and the affordances that it has. The final submission should be an agent capable of robust food retrieval behaviour similar to that of many kinds of animals. We know the animals can pass these tests, it's time to see if AI can too.

## Prizes $32,000 (equivalent value)

* Overall Prizes
  * 1st place overall: **$7,500 total value** - $6,500 with up to $1,000 travel to speak at NeurIPS 2019.
  * 2nd place overall: **$6,000 total value** - $5,000 with up to $1,000 travel to speak at NeurIPS 2019.
  * 3rd place overall: **$1,500**.
* WBA-Prize: **$5,000 total value** - $4,000 with up to $1,000 travel to speak at NeurIPS 2019
* Category Prizes: **$200** For best performance in each category (cannot combine with other prizes - max 1 per team).
* **Mid-way AWS Research Credits**: The top 20 entries as of **September 1st** will be awarded **$500** of AWS credits.

See [competition launch page](https://mdcrosby.com/blog/animalailaunch.html) and official rules for further details.

**Important** Please check the competition rules [here](http://animalaiolympics.com/rules.html). **To submit to the competition and be considered for prizes you must also fill in [this form](https://forms.gle/PKCgp2JAWvjf4c9i6)**. Entry to the competition ([via EvalAI](https://evalai.cloudcv.org/web/challenges/challenge-page/396/overview)) constitutes agreement with all competition rules. 

## Requirements

The Animal-AI package works on Linux, Mac and Windows, as well as most Cloud providers. Note that for submission to the competition we only support linux-based Docker files.  
<!--, for cloud engines check out [this cloud documentation](documentation/cloud.md).-->

We recommend using a virtual environment specifically for the competition. You will need `python3.6` installed (we currently only support **python3.6**). Clone this repository to run the examples we provide.

We offer two packages for this competition:

- The main package is an API for interfacing with the Unity environment. It contains both a 
[gym environment](https://github.com/openai/gym) as well as an extension of Unity's 
[ml-agents environments](https://github.com/Unity-Technologies/ml-agents/tree/master/ml-agents-envs). You can install it
 via pip:
    ```
    pip install animalai
    ```
    Or you can install it from the source, head to `animalai/` folder and run `pip install -e .`

    In case you wish to create a conda environment you can do so by running the below command from the `animalai` folder:
    ```
    conda env create -f conda_isntall.yaml
    ```

- We also provide a package that can be used as a starting point for training, and which is required to run most of the 
example scripts found in the `examples/` folder. At the moment **we only support Linux and Mac** for the training examples. It contains an extension of 
[ml-agents' training environment](https://github.com/Unity-Technologies/ml-agents/tree/master/ml-agents) that relies on 
[OpenAI's PPO](https://openai.com/blog/openai-baselines-ppo/), as well as 
[Google's dopamine](https://github.com/google/dopamine) which implements 
[Rainbow](https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/download/17204/16680) (among others). You can also install 
this package using pip:
    ```
    pip install animalai-train
    ```
    Or you can install it from source, head to `examples/animalai_train` and run `pip install -e .`

Finally download the environment for your system:

| OS | Environment link |
| --- | --- |
| Linux |  [download trained_Linux](https://www.doc.ic.ac.uk/~bb1010/animalAI/env_linux_v1.0.0.zip) |
| MacOS |  [download trained_Mac](https://www.doc.ic.ac.uk/~bb1010/animalAI/env_mac_v1.0.0.zip) |
| Windows | [download trained_Windows](https://www.doc.ic.ac.uk/~bb1010/animalAI/env_windows_v1.0.0.zip)  |

You can now unzip the content of the archive to the `env` folder and you're ready to go! Make sure the executable 
`AnimalAI.*` is in `env/`. On linux you may have to make the file executable by running `chmod +x env/AnimalAI.x86_64`. 
Head over to [Quick Start Guide](documentation/quickstart.md) for a quick overview of how the environment works.

The Unity source files for the environment can be find on the [AnimalAI-Environment repository](https://github.com/beyretb/AnimalAI-Environment). 
Due to a lack of resources we cannot provide support on this part of the project at the moment. We recommend reading the documentation on the 
[ML-Agents repo](https://github.com/Unity-Technologies/ml-agents) too.

## Manual Control

If you launch the environment directly from the executable or through the VisualizeArena script it will launch in player 
mode. Here you can control the agent with the following:

| Keyboard Key  | Action    |
| --- | --- |
| W   | move agent forwards |
| S   | move agent backwards|
| A   | turn agent left     |
| D   | turn agent right    |
| C   | switch camera       |
| R   | reset environment   |

