
# Introduction

- `lab-kitten` is toolkit for labs / experiments originally developed by [Ding Ruiqi](https://github.com/tesla-cat) for [Yvonne Gao’s quantum computing lab](https://quantumcrew.org/) at National University of Singapore (NUS)
- Current features
    - Real-time plotting of lab data powered by the state of the art **decentralized** [WebRTC technology](https://en.wikipedia.org/wiki/WebRTC), which is the real-time technology of [highest performance](https://raw.githubusercontent.com/lab-kitten/lab-kitten/master/images/1-WebRTC.png), thus have been widely used in live-streaming, video chat applications etc.
- Upcoming features ([click me to request for a feature](https://github.com/lab-kitten/lab-kitten/issues/1))
    - Various handy calculators
    - Useful advertising / rating of scientific instruments
    - Machine learning support
    - Socializing: Chat, Q&A forum, file transfer
    - `lab-kitten` will be modular! You can [become a community contributor](https://github.com/lab-kitten/lab-kitten/issues/3) and submit addons to it!

# Disclaimer

- The first feature is developed in **4 days (2 weekends)** and this will remain a project **maintained on weekends** 
- No animals were harmed in the making of this project

# Language support

- The core functionally of `lab-kitten` is implemented in the executables (see installation below), the [`python` “package” with only 11 lines of code](https://github.com/lab-kitten/lab-kitten/blob/master/python/LabKitten/__init__.py) below only serves as a bridge
- To use `lab-kitten` in any other languages, either wait for me to implement, or implement by yourself based on the [`python` “package” with only 11 lines of code](https://github.com/lab-kitten/lab-kitten/blob/master/python/LabKitten/__init__.py)
 
# Usage (Lab side)

- **Step 1:** Download and unzip the `executable` for your system
    - [**LabKitten-linux.zip**](https://github.com/lab-kitten/lab-kitten/raw/master/executables/LabKitten-linux.zip)
    - [**LabKitten-macos.zip**](https://github.com/lab-kitten/lab-kitten/raw/master/executables/LabKitten-macos.zip)
    - [**LabKitten-win.zip**](https://github.com/lab-kitten/lab-kitten/raw/master/executables/LabKitten-win.zip)
- **Step 2:** Download the [`python` “package” with only 11 lines of code](https://github.com/lab-kitten/lab-kitten/blob/master/python/LabKitten/__init__.py) to your project directory
- **Step 3:** Follow the examples
    - [**example-1-random.py**](https://github.com/lab-kitten/lab-kitten/blob/master/python/example-1-random.py)
    - [**example-2-sin-waves.py**](https://github.com/lab-kitten/lab-kitten/blob/master/python/example-2-sin-waves.py)

[![Watch the video](images/usage-lab-side.PNG)](https://www.youtube.com/watch?v=ELzClaba8cI)

# Usage (Lab staff side)

- **Step 1:** Go to **https://lab-kitten.github.io** , that’s it !

[![Watch the video](images/usage-lab-staff-side.PNG)](https://www.youtube.com/watch?v=l3uMzQhTSMA)

# You should know

- To use the lab side program you need to register first (**I know you hate register, but the purpose is to protect your data via authentication, also only users with .edu email address can use lab-kitten**). Then you need to tell lab-kitten these credentials, the name of your experiment and the location of the executable for initialization, please refer to the following examples

# Others

- [Comments and suggestions](https://github.com/lab-kitten/lab-kitten/issues/2)
- [Join the team](https://github.com/lab-kitten/lab-kitten/issues/3)
