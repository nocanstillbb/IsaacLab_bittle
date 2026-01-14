# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause


import math
import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
from isaaclab.utils.assets import ISAACLAB_NUCLEUS_DIR

##
# Configuration - Actuators.
##

BITTILE__SIMPLE_ACTUATOR_CFG  = ImplicitActuatorCfg(
    joint_names_expr=[
        "LF_HFE",
        "LF_KFE",
        "LH_HFE",
        "LH_KFE",
        "RF_HFE",
        "RF_KFE",
        "RH_HFE",
        "RH_KFE"
    ],
    stiffness={".*": 60.0},
    damping={".*": 1.5},
    effort_limit=5.0,
    velocity_limit=7.5,
)



##
# Configuration - Articulation.
##

BITTLE_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        #usd_path=f"{ISAACLAB_NUCLEUS_DIR}/Robots/ANYbotics/ANYmal-C/anymal_c.usd",
        usd_path=f"/home/cnf2025581067/source/repos/IsaacLab_bittle/source/isaaclab_assets/data/Robots/Bittle/bittle.usd",
        scale=(0.1,0.1,0.1),
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
        # collision_props=sim_utils.CollisionPropertiesCfg(contact_offset=0.02, rest_offset=0.0),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.1),
        joint_pos={
            "LF_HFE" : math.radians(45),
            "LF_KFE" : math.radians(0),
            "LH_HFE" : math.radians(45),
            "LH_KFE" : math.radians(0),
            "RF_HFE" : math.radians(45),
            "RF_KFE" : math.radians(0),
            "RH_HFE" : math.radians(45),
            "RH_KFE" : math.radians(0),
        },
    ),
    actuators={"legs": BITTILE__SIMPLE_ACTUATOR_CFG},
    soft_joint_pos_limit_factor=0.95,
)




