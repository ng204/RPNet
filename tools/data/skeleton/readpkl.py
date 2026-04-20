import pickle
with open('/root/mmaction2/tools/data/skeleton/my_train.pkl', 'rb') as f:
	a = pickle.load(f)
with open('//root/mmaction2/ntu60_2d.pkl', 'rb') as f:
	b = pickle.load(f)
print(0)