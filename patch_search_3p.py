# -*- coding:utf-8 -*-
import itertools
import operator
import os
import sys

import lt
from wdsp import Wdsp
from patch_search_base import PatchSearch


class PatchSearchSpecific(PatchSearch):

    def __init__(self, pros, seqs, wdsps, hotspots, cutoff=1):
        PatchSearch.__init__(self, pros, seqs, wdsps, hotspots, cutoff)

        self.shapes = {
            'shape_3_1_1_a':	((1, 2), (2, 0), (2, 1)),
            'shape_3_1_1_b':	((1, 0), (1, 2), (2, 1)),
            'shape_3_1_2_a':	((1, 2), (2, 0), (2, 2)),
            'shape_3_1_2_b':	((1, 0), (1, 1), (2, 1)),
            'shape_3_1_3_a':	((1, 0), (2, 1), (2, 2)),
            'shape_3_1_3_b':	((1, 1), (1, 2), (2, 0)),
            'shape_3_2_1_a':	((1, 0), (2, 0), (2, 1)),
            'shape_3_2_1_b':	((1, 0), (1, 2), (2, 0)),
            'shape_3_3':        ((1, 0), (1, 1), (1, 2)),
         }

        self.phos_res = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K',
                         'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
        # self.phos_res = ['R','K','Y','W','Q','H','N','S','T']
        self.phos_res = ['R', 'K', 'Y', 'H', 'S', 'T']

    # def check_patches(self, shape_k, shape_v, patches, surround_patches):
        # #do not distinguish between 'S' and 'T'
        # patches = [''.join([p.replace('S','T') for p in patch]) for patch in patches]
        # # def validify(patch):
            # # for p in patch:
                # # if not p in self.phos_res:
                    # # return 0
            # # for i, p in enumerate(patch):
                # # if shape_v[i][1] == 0 and p in ['T', 'S']:
                    # # return 0
            # # return 1
        # # def validify_surround(surround_patch):
            # # if 'D' in surround_patch or 'E' in surround_patch:
                # # return 0
            # # return 1

        # def validify(patch):
            # return 1
        # def validify_surround(surround_patch):
            # return 1

        # good_patches = []
        # for patch,surround_patch in zip(patches,surround_patches):
            # if validify(patch) and validify_surround(surround_patch):
                # good_patches.append(patch)

        # return good_patches


@lt.run_time
def main():
    with open(sys.argv[1]) as wdsp_f:
        CUTOFF = 0
        wdsp = Wdsp(wdsp_f)
        a = PatchSearchSpecific(wdsp.pros,wdsp.seqs,wdsp.wdsps,wdsp.hotspots,CUTOFF)
        a.get_patches()
        a.classify_patches()
        a.deredundant_patches()
        a.write_results()

if __name__ == "__main__":
    main()
