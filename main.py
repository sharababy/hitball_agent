import hitballs as game
import argparse
import dqn
import torch
import torch.optim as optim
import torch.nn as nn

parser = argparse.ArgumentParser(description='DQN agent for HitBall')

parser.add_argument('--load_model', type=str,  default="True",
        help='If set true, train the model; otherwise, play game with pretrained model')
parser.add_argument('--model_name',type=str, default="agent1",
        help='Name of the pretrained model')
parser.add_argument('--lr', type=float, help='learning rate', default=0.0001)
parser.add_argument('--gamma', type=float,
        help='discount rate', default=0.99)
parser.add_argument('--batch_size', type=int,
        help='batch size', default=32)
parser.add_argument('--memory_size', type=int,
        help='memory size for experience replay', default=5000)
parser.add_argument('--init_e', type=float,
        help='initial epsilon for epsilon-greedy exploration',
        default=8.0)
parser.add_argument('--final_e', type=float,
        help='final epsilon for epsilon-greedy exploration',
        default=0.1)
parser.add_argument('--observation', type=int,
        help='random observation number in the beginning before training',
        default=50)
parser.add_argument('--exploration', type=int,
        help='number of exploration using epsilon-greedy policy',
        default=10000)
parser.add_argument('--max_episode', type=int,
        help='maximum episode of training',
        default=20000)
parser.add_argument('--save_checkpoint_freq', type=int,
        help='episode interval to save checkpoint', default=2000)

parser.add_argument('--cuda', action='store_true', default=False,
        help='If set true, with cuda enabled; otherwise, with CPU only')

parser.add_argument('--mode', type=str,default="Train",
        help='Set to train(Train) or test(Test) mode')

args = parser.parse_args()


model = dqn.BrainDQN(epsilon=args.init_e, mem_size=args.memory_size, cuda=args.cuda)

print("Init Epsilon: ", args.init_e)

if args.load_model == "True":
	print("loading model",args.model_name)
	model.load_state_dict(torch.load(args.model_name))


if args.mode == "Train":
	optimizer = optim.Adam(model.parameters(), lr=args.lr)
	ceriterion = nn.MSELoss()
	model.set_train()

model.set_initial_state()
model.time_step = 0

total_reward = 0

print("Model initialized")

game.GameStart(model,args,optimizer,ceriterion)


