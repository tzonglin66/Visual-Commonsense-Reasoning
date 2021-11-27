import os
root_dir = '../dataset/update_data/train'
ants_dir = 'ants_image'
ants_label = ants_dir.split('_')[0]
bees_dir = 'bees_image'
bees_label = bees_dir.split('_')[0]
ants_path = os.listdir(os.path.join(root_dir, ants_dir))
bees_path = os.listdir(os.path.join(root_dir, bees_dir))
ants_label_target = 'ants_label'
bees_label_target = 'bees_label'

for ant in ants_path:
    ant_name = ant.split('.jpg')[0]
    with open(os.path.join(root_dir, ants_label_target, '{0}.txt'.format(ant_name)), 'w') as ant_label:
        ant_label.write(ants_label)

for bee in bees_path:
    bee_name = bee.split('.jpg')[0]
    with open(os.path.join(root_dir, bees_label_target, '{0}.txt'.format(bee_name)), 'w') as bee_label:
        bee_label.write(bees_label)
