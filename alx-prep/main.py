kik = ["good", "bad", "ugly", "smooth", "nice"]
den = [2, 4, 5, 3, 2]
tree = ["a", "c", 9, "fan", 10]

'''three different lists created with different variables'''
print(kik)
print(den)
print(tree)

slot = kik[:]  # copy items from kik to slot
slot1 = kik[:2]
slot2 = kik[2:]
# slot3 = [kik][den]
#print("the values of slot will be {}".format(slot)) # I GOT kik in return
#print("the values of slot1 will be {}".format(slot1)) # result shows [ good, bad]
#print("the values of slot2 will be {}".format(slot2)) # result shows [ ugly, smooth, nice]
''' print("the values of slot3 will be {}".format(slot3))
TypeError: list indices must be integers or slices, not list
['good', 'bad', 'ugly', 'smooth', 'nice']
[2, 4, 5, 3, 2]
['a', 'c', 9, 'fan', 10]'''

'''trying append'''
tree.append("laptop")
print("the new item added to the tree list makes it add {}".format(tree)) #['a', 'c', 9, 'fan', 10, 'laptop']
new_tree = tree[:-1]
print("taking one item from the back makes it {}".format(new_tree)) # ['a', 'c', 9, 'fan', 10]
mode_tree = tree[-1:]
print("taking one item from the front makes it {}".format(mode_tree)) # ['laptop']
mid_tree = tree[1:]
print("showing one item from the front makes it {}".format(mid_tree)) #['c', 9, 'fan', 10, 'laptop']

vid_tree = tree[:1]
print("showing one item from the front makes it {}".format(vid_tree)) #['c', 9, 'fan', 10, 'laptop'] #[a]

#den = [2]
print(f"printout the new third on the list and you will get {den[2]}") #printout the new third on the list and you will get 5

den[3] = "tower"
print(" replace the third on the list to {}".format(den)) #replace the third on the list to [2, 4, 5, 'tower', 2]
