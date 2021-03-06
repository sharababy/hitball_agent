# Deep Q-Learning based agent to play HitBalls

A Deep Q-Learning based agent that plays HitBalls v1.2

![](play.gif)

## Getting Started

To run the agent:  

```
chmod +x train.sh
./train.sh
```

### Prerequisites

The follow packages need to be installed:

* [pytorch](https://pytorch.org/) 
* numpy `pip install numpy`
* pygame [install instructions](https://cit.dixie.edu/cs/1410/pygame-installation.pdf)


### Arguments

The following arguments can be given:
- --load_model, default=False, If set true, train the model; otherwise, play game with pretrained model
- --model_name, default="agent1", Name of the pretrained model
- --cuda, default=False, If set true, with cuda enabled; otherwise, with CPU only
- --lr, type=float, learning rate default=0.0001
- --gamma, type=float, discount rate, default=0.99
- --batch_size, type=int, batch size, default=32
- --memory_size, type=int, memory size for experience replay, default=5000
- --init_e, type=float, initial epsilon for epsilon-greedy exploration,default=1.0
--final_e, type=float,final epsilon for epsilon-greedy exploration,default=0.1
- --observation, type=int,random observation number in the beginning before training, default=50
- --exploration, type=int,number of exploration using epsilon-greedy policy, default=10000
- --max_episode, type=int,maximum episode of training, default= 20000
- --save_checkpoint_freq, type=int, episode interval to save checkpoint, default=2000



## Actions, States and Rewards

### Actions
We assume that the agent can make 6 possible actions:
* 0 : KeyUp + KeyLeft
* 1 : KeyUp + KeyRight
* 2 : KeyUp
* 3 : KeyLeft
* 4 : KeyRight
* 5 : DoNothing

### States
The states used are the raw input pixels on the screen, in grey scale (80x60) resolution.
We use 8 consecutive frames to detect the motion of the balls.


### Rewards

The rewards for **not crashing** into a ball or wall is contant every time (= +1). 
But the reward for **crashing** into a ball or wall increases as the time per game increases in seconds (= -1 - [2 * time(in seconds)] ) .


## Deep Learning Model Architecute

The model used here is relatively simple.

Conv2d (in_channels=8, out_channels=8, kernel_size=8, stride=4, padding=2)   
  |   
  |ReLU()   
  v   
Conv2d (in_channels=8, out_channels=16, kernel_size=6, stride=3, padding=2)   
  |   
  |ReLU()   
  v   
Conv2d (in_channels=16, out_channels=32, kernel_size=4, stride=2, padding=1)   
  |   
  |ReLU()   
  v   
<!-- FullyConnected (512)   
  |   
  |ReLU()   
  v    -->
FullyConnected (256)   
  |   
  |ReLU()   
  v    
FullyConnected (128)   
  |   
  |ReLU()   
  v   
FullyConnected (6)   
  |   
  v   
Actions!   

## Tweaking the Epsilon

In some cases I had completely removed the random actions generatoi function, and purely relied on the inputs from the neural network.
This caused more variance in the performance of the model, But in general gave better results.


## Test Setup

You can set the `--mode Test` to run the agent in test mode.


## Results



## Author

* **[Vedant Bassi](https://github.com/sharababy)** - *Initial work*

<!-- See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
 -->
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Resources Used to Make this Agent

* [Flappy Bird With DQN by xmfbit](https://github.com/yenchenlin/DeepLearningFlappyBird)
* [Using Deep Q-Network to Learn How To Play Flappy Bird
 by yenchenlin](https://github.com/xmfbit/DQN-FlappyBird)
* [The HitBalls Game by Jonas Möller](https://www.pygame.org/project/3633/5723)
* [This awesome post by Intel on Deep Reinforcement Learning ](https://www.intel.ai/demystifying-deep-reinforcement-learning/)
* ML Course offered by Dr Masilamani at IIITDM Kancheepuram
