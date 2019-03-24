# Deep Q-Learning HitBalls v1.2 

A Deep Q-Learning based agent that plays HitBalls v1.2

## Getting Started

To run the agent : `python3 main.py`

### Prerequisites

The follow packages need to be installed:

```
pip install pytorch,numpy,pygame
```

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

```
chmod +x train.sh
./train.sh
```


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Author

* **[Vedant Bassi](https://github.com/sharababy)** - *Initial work*

<!-- See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
 -->
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
