python3 main.py \
--load_model True \
--model_name agent1 \
--lr 0.0001 \
--gamma 0.99 \
--batch_size 32 \
--memory_size 5000 \
--init_e 0.8 \
--final_e 0.1 \
--observation 5000 \
--exploration 10000 \
--max_episode 20000 \
--save_checkpoint_freq 10 \
--mode Train