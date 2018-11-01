import hou
import random
import os

network = hou.selectedNodes()

sampleCount = 1000
frameNum = hou.frame()

for i in range(0, sampleCount):
    for n in network:
        t = str(n.type().name())

        if t == 'heightfield_pattern':
            n.parm('rotate').set(random.uniform(0.0, 360.0))

        elif t == 'heightfield_erode::2.0':
            hou.setFrame(frameNum)
            n.parm('resimulate').pressButton()

        elif t == 'heightfield_noise':
            n.parm('offsetx').set(random.uniform(-10000.0, 10000.0))
            n.parm('offsety').set(random.uniform(-10000.0, 10000.0))
            n.parm('offsetz').set(random.uniform(-10000.0, 10000.0))


    # ok, we've set everything, now find the output node and save the heightfield
    for n in network:
        t = str(n.type().name())

        if t == 'heightfield_output':
            orig_fname = n.parm('output').eval()
            fname = orig_fname
            p = os.path.split(fname)
            ext = os.path.splitext(p[1])
            fname = p[0] + "/" + ext[0] + str(i) + ext[1]
            print(fname)
            n.parm('output').set(fname)
            n.parm('execute').pressButton()
            n.parm('output').set(orig_fname)
