from omni.isaac.kit import SimulationApp
import os
import argparse
rep_palletjack_group = add_palletjacks()

import carb
import omni
import omni.usd
from omni.isaac.core.utils.nucleus import get_assets_root_path
from omni.isaac.core.utils.stage import get_current_stage, open_stage
from pxr import Semantics
import omni.replicator.core as rep

from omni.isaac.core.utils.semantics import get_semantics
PALLETJACKS = [ "/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxB_01_1262.usd"]
def add_palletjacks():
    rep_obj_list = [rep.create.from_usd(palletjack_path, semantics=[("class", "palletjack")], count=2) for palletjack_path in PALLETJACKS]
    rep_palletjack_group = rep.create.group(rep_obj_list)
    return rep_palletjack_group
rep_palletjack_group = add_palletjacks()
with rep.trigger.on_frame(num_frames=100):
    colors = [
            (1.0, 0.0, 0.0),   # red
            (0.0, 1.0, 0.0),   # green
            (0.0, 0.0, 1.0)    # blue
        ]
    with rep_palletjack_group:
            rep.modify.pose(position=rep.distribution.uniform((-6, -6, 0), (6, 12, 0)),
                            rotation=rep.distribution.uniform((0, 0, 0), (0, 0, 360)),
                            scale=rep.distribution.uniform((1, 1, 1), (1, 1, 1)))
            rep.modify.attribute(
                "primvars:displayColor",
                rep.distribution.choice(colors)
            )
