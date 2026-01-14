#/bind/bash

./isaaclab.sh -p scripts/tools/convert_urdf.py \
  /home/cnf2025581067/source/repos/Bittle_URDF/urdf/bittle.urdf \
  source/isaaclab_assets/data/Robots/Bittle/bittle.usd \
  --merge-joints \
  --joint-stiffness 1.0 \
  --joint-damping 0.1 \
  --joint-target-type position

