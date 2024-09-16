# Assignment 2 - Knight Isolation

# 程序代做代写辅导

# 专业辅导，已辅导上千名留学生，帮助其获得高分

# Contact Me:

# WeChat: robotclx

# CS Professional Tutoring

# I can help you for Python,Java,C,C#,C++,Javascript,html,go,rust,database......

# 英国，澳洲，美国，日本，韩国等各国均可辅导，均可提供服务

# 在要求的范围内，可免费售后，可走平台

# 记得备注您是从github来的哦~

# Email: bu32221@163.com

## Instructor: Dr. Thomas Ploetz

## Deadline: <font color='red'>Monday, September 23rd, 7:59 am EDT</font>

#### Released: Monday, September 9th, 7:59 am EDT

This assignment will cover some of the concepts discussed in the Adversarial Search lectures. You will be implementing game playing agents for a variant of the game Isolation.

We are also implementing this through Jupyter Notebook, so you all may find it useful to spend some time getting familiar with this software. During the first week of classes, there was an assignment [Assignment 0](https://github.gatech.edu/omscs6601/assignment_0/) that spends some time going through Python and Jupyter. If you are unfamiliar with either Python or Jupyter, please go through that assignment first!

### Table of Contents
- [Setup](#setup)
- [Jupyter](#jupyter)
- [Jupyter Tips](#jupyter-tips)
- [FAQ](#faq)
- [IDE](#IDE)

<a name="setup"/></a>
## Setup

For this assignment, we **highly** recommend you to create a new environment **just** for this one assignment. 

```
conda create -n ai_env_a2 python=3.9
```

Activate the environment:
```
conda activate ai_env_a2
```

In case you used a different environment name, to get a list of all environments you have on your machine, you can run `conda env list`.

Install correct package versions that will be used for visualising the game board.

```
cd assignment_2
pip install -r requirements.txt
```

<a name="jupyter"/></a>
## Jupyter

You may wish to install the `ipykernel`. This can be done via:

```
python -m ipykernel install --user --name ai_env_a2 --display-name "Python 3.9 (AI-A2)"
```

Further instructions are provided in the `notebook.ipynb`. Run:

```
jupyter notebook
```

Once started you can access [http://localhost:8888](http://localhost:8888/) in your browser.

<a name="jupyter-tips"/></a>
## Jupyter Tips

Hopefully, [Assignment 0](https://github.gatech.edu/omscs6601/assignment_0/) got you pretty comfortable with Jupyter or at the very least addressed the major things that you may run into during this project. That said, Jupyter can take some getting used to, so here is a compilation of some things to watch out for specifically when it comes to Jupyter in a sort-of FAQs-like style

**1. My Jupyter notebook does not seem to be starting up or my kernel is not starting correctly.**<br />
Ans: This probably has to do with activating virtual environments. If you followed the setup instructions exactly, then you should activate your conda environment using `conda activate <environment_name>` from the Anaconda Prompt and start Jupyter Notebook from there.

**2. I was running cell xxx when I opened up my notebook again and something or the other seems to have broken.**<br />
Ans: This is one thing that is very different between IDEs like PyCharm and Jupyter Notebook. In Jupyter, every time you open a notebook, you should run all the cells that a cell depends on before running that cell. This goes for cells that are out of order too (if cell 5 depends on values set in cell 4 and 6, you need to run 4 and 6 before 5). Using the "Run All" command and its variants (found in the "Cell" dropdown menu above) should help you when you're in a situation like this.

**3. The value of a variable in one of my cells is not what I expected it to be? What could have happened?** <br />
Ans: You may have run a cell that modifies that variable too many times. Look at the "counter" example in assignment 0. First, try running `counter = 0` and then `counter += 1`. This way, when you print counter, you get counter = 1, right? Now try running `counter += 1` again, and now when you try to print the variable, you see a value of 2. This is similar to the issue from Question 2. The order in which you run the cells does affect the entire program, so be careful.

<a name="faq"/></a>
## FAQ
**1. What depth does the server call my search algorithms with?**<br />
Ans: The server will not pass a depth value to your CustomPlayer; whatever you set as the default parameter value will be used on Gradescope. Modifying this default value is extremely important in changing the performance of your agent.

**2. How does Gradescope set up and run each game?**<br />
Ans: Gradescope will run 20 games in order to determine the win ratio. Your player (CustomPlayer) will be K1 for 10 of those games and K2 for 10 of those games. Each player has 1 second to make each move and the first two moves (i.e. each player's starting location) will be randomized.

**3. Can we use multithreading of multiprocessing?**<br />
Ans: Sorry, we will not allow multithreading or multiprocessing on this Assignment. It isn't necessary to successfully complete the Assignment.

**4. I have a question about the isolation API or the workings of the framework. Where should I learn more?**<br />
Ans: Firstly, watch the recorded YouTube video of assignment 2 where isolation API is covered. If this video and the docstrings inside isolation.py leave you with more questions, feel free to post a question on Ed and a TA will respond as soon as possible with clarifications, or come to office hours to discuss further.


**5. Can I add more functions to replace some of the existing functions? Can I import other packages as well?**<br />
Ans: No. Please do not add any more functions or imports. You should be able to finish the assignment by replacing the `NotImplementedError`.

**A more in-depth FAQ will be posted on Ed**

<a name="IDE"/></a>
## IDE 

In case you are willing to use IDE (e.g. Pycharm) to implement your assignment in `.py` file. Please run:

```bash
python helpers/notebook2script.py submission
```

You will get autogenerated `submission/submission.py` file where you can write your code. However, make sure you have gone through the instructions in the `notebook.ipynb` at least once.
