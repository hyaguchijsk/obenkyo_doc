#!/usr/bin/env python
# coding: UTF-8

import math
import numpy

def connected_vertex(e0, e1):
    ## extract common number of 2 tuples
    for v0 in e0:
        for v1 in e1:
            if v0 == v1:
                return v0
    return -1  ## if not found

def has_vertex(v, e):
    ## return True if edge has vertex
    for vi in e:
        if v == vi:
            return True
    return False

class GDome:
    def __init__(self):
        self.vlist = []
        self.elist = []
        self.flist = []

        # make icosahedron
        self.gr = (1.0 + math.sqrt(5.0)) * 0.5  # golden ratio
        self.vn = math.sqrt(1.0 + self.gr * self.gr)  # norm(v)

        # add 12 vertices
        self.vlist.append(numpy.array((0, -1, -self.gr)))
        self.vlist.append(numpy.array((0,  1, -self.gr)))
        self.vlist.append(numpy.array((0, -1,  self.gr)))
        self.vlist.append(numpy.array((0,  1,  self.gr)))
        self.vlist.append(numpy.array((-self.gr, 0, -1)))
        self.vlist.append(numpy.array((-self.gr, 0,  1)))
        self.vlist.append(numpy.array(( self.gr, 0, -1)))
        self.vlist.append(numpy.array(( self.gr, 0,  1)))
        self.vlist.append(numpy.array((-1, -self.gr, 0)))
        self.vlist.append(numpy.array(( 1, -self.gr, 0)))
        self.vlist.append(numpy.array((-1,  self.gr, 0)))
        self.vlist.append(numpy.array(( 1,  self.gr, 0)))

        # add 30 edges
        ## v: 0-1-6-0, e: 0, 1, 2
        self.elist.append((0, 1))
        self.elist.append((1, 6))
        self.elist.append((6, 0))
        ## v: 1+0-4-1, e: 0, 3, 4
        self.elist.append((0, 4))
        self.elist.append((4, 1))
        ## v: 2-3-5-2, e: 5, 6, 7
        self.elist.append((2, 3))
        self.elist.append((3, 5))
        self.elist.append((5, 2))
        ## v: 3+2-7-3, e: 5, 8, 9
        self.elist.append((2, 7))
        self.elist.append((7, 3))
        ## v: 4-5-10-4, e: 10, 11, 12
        self.elist.append((4, 5))
        self.elist.append((5, 10))
        self.elist.append((10, 4))
        ## v: 5+4-8-5, e: 10, 13, 14
        self.elist.append((4, 8))
        self.elist.append((8, 5))
        ## v: 6-7-9-6, e: 15, 16, 17
        self.elist.append((6, 7))
        self.elist.append((7, 9))
        self.elist.append((9, 6))
        ## v: 7+6-11-7, e: 15, 18, 19
        self.elist.append((6, 11))
        self.elist.append((11, 7))
        ## v: 8-9-2-8, e: 20, 21, 22
        self.elist.append((8, 9))
        self.elist.append((9, 2))
        self.elist.append((2, 8))
        ## v: 9+8-0-9, e: 20, 23, 24
        self.elist.append((8, 0))
        self.elist.append((0, 9))
        ## v: 10-11-1-10, e: 25, 26, 27
        self.elist.append((10, 11))
        self.elist.append((11, 1))
        self.elist.append((1, 10))
        ## v: 11+10-3-11, e: 25, 28, 29
        self.elist.append((10, 3))
        self.elist.append((3, 11))
        ## v: 0+6+9+0, e: 2, 17, 24
        ## v: 0+8+4+0, e: 23, 13, 3
        ## v: 1+4+10+1, e: 4, 12, 27
        ## v: 1+11+6+1, e: 26, 18, 1
        ## v: 2+5+8+2, e: 7, 14, 22
        ## v: 2+9+7+2, e: 21, 16, 8
        ## v: 3+7+11+3, e: 9, 19, 29
        ## v: 3+10+5+3, e: 28, 11, 6

        # add 20 faces
        ## v: 0-1-6-0, e: 0, 1, 2
        self.flist.append((0, 1, 2))
        ## v: 1+0-4-1, e: 0, 3, 4
        self.flist.append((0, 3, 4))
        ## v: 2-3-5-2, e: 5, 6, 7
        self.flist.append((5, 6, 7))
        ## v: 3+2-7-3, e: 5, 8, 9
        self.flist.append((5, 8, 9))
        ## v: 4-5-10-4, e: 10, 11, 12
        self.flist.append((10, 11, 12))
        ## v: 5+4-8-5, e: 10, 13, 14
        self.flist.append((10, 13, 14))
        ## v: 6-7-9-6, e: 15, 16, 17
        self.flist.append((15, 16, 17))
        ## v: 7+6-11-7, e: 15, 18, 19
        self.flist.append((15, 18, 19))
        ## v: 8-9-2-8, e: 20, 21, 22
        self.flist.append((20, 21, 22))
        ## v: 9+8-0-9, e: 20, 23, 24
        self.flist.append((20, 23, 24))
        ## v: 10-11-1-10, e: 25, 26, 27
        self.flist.append((25, 26, 27))
        ## v: 11+10-3-11, e: 25, 28, 29
        self.flist.append((25, 28, 29))
        ## v: 0+6+9+0, e: 2, 17, 24
        self.flist.append((2, 17, 24))
        ## v: 0+8+4+0, e: 23, 13, 3
        self.flist.append((23, 13, 3))
        ## v: 1+4+10+1, e: 4, 12, 27
        self.flist.append((4, 12, 27))
        ## v: 1+11+6+1, e: 26, 18, 1
        self.flist.append((26, 18, 1))
        ## v: 2+5+8+2, e: 7, 14, 22
        self.flist.append((7, 14, 22))
        ## v: 2+9+7+2, e: 21, 16, 8
        self.flist.append((21, 16, 8))
        ## v: 3+7+11+3, e: 9, 19, 29
        self.flist.append((9, 19, 29))
        ## v: 3+10+5+3, e: 28, 11, 6
        self.flist.append((28, 11, 6))

    def sanity_check(self):
        for i in range(len(self.flist)):
            face = self.flist[i]
            e0 = self.elist[face[0]]
            e1 = self.elist[face[1]]
            e2 = self.elist[face[2]]
            # connected_vertex seeks shared vertex of 2 edges
            # if it is not found, the face is insane
            v0 = connected_vertex(e2, e0)
            v1 = connected_vertex(e0, e1)
            v2 = connected_vertex(e1, e2)
            san = True
            if v0 == -1 or v1 == -1 or v2 == -1:
                san = False
            print "{index}: {edge_list}; ({vert0}, {vert1}, {vert2}). {sanity} ".format(
                index = i,
                edge_list = face,
                vert0 = v0,
                vert1 = v1,
                vert2 = v2,
                sanity = san)


    def split(self):
        prev_vnum = len(self.vlist)
        prev_enum = len(self.elist)
        updated_elist = []
        updated_flist = []

        # add mid point for each edge
        for i in range(len(self.elist)):
            edge = self.elist[i]
            v0 = self.vlist[edge[0]]
            v1 = self.vlist[edge[1]]
            v01 = (v0 + v1)
            normv = numpy.linalg.norm(v01)
            v2 =  v01 * (self.vn / normv)
            self.vlist.append(v2)

            # divided edge -> 2 * i, 2 * i + 1
            updated_elist.append((edge[0], prev_vnum + i))
            updated_elist.append((prev_vnum + i, edge[1]))

        # create new faces for all face
        #
        #          v0
        #        /   \
        #      e00   e21
        #      /       \
        #    v01--ne2--v20
        #    /  \     /  \
        #   e01 ne0 ne1   e20
        #  /      \ /      \
        # v1--e10--v12-e11--v2
        #
        for i in range(len(self.flist)):
            face = self.flist[i]
            e0 = face[0]
            e1 = face[1]
            e2 = face[2]

            v0_idx = connected_vertex(self.elist[e2], self.elist[e0])
            v1_idx = connected_vertex(self.elist[e0], self.elist[e1])
            v2_idx = connected_vertex(self.elist[e1], self.elist[e2])

            e00 = e0 * 2
            e01 = e0 * 2 + 1
            if not has_vertex(v0_idx, updated_elist[e00]):
                tmp = e00
                e00 = e01
                e01 = tmp

            e10 = e1 * 2
            e11 = e1 * 2 + 1
            if not has_vertex(v1_idx, updated_elist[e10]):
                tmp = e10
                e10 = e11
                e11 = tmp

            e20 = e2 * 2
            e21 = e2 * 2 + 1
            if not has_vertex(v2_idx, updated_elist[e20]):
                tmp = e20
                e20 = e21
                e21 = tmp

            v01_idx = prev_vnum + e0
            v12_idx = prev_vnum + e1
            v20_idx = prev_vnum + e2
            updated_elist.append((v01_idx, v12_idx))
            updated_elist.append((v12_idx, v20_idx))
            updated_elist.append((v20_idx, v01_idx))

            # added edge -> (prev_enum * 2) +
            #               {3 * i, 3 * i + 1, 3 * i + 2}
            ne0 = (prev_enum * 2) + (3 * i)
            ne1 = ne0 + 1
            ne2 = ne1 + 1

            # update diveded faces
            updated_flist.append((e00, ne2, e21))
            updated_flist.append((e01, e10, ne0))
            updated_flist.append((ne1, e11, e20))
            updated_flist.append((ne0, ne1, ne2))

        self.elist = updated_elist
        self.flist = updated_flist

    def write_to_stl(self, fname):
        f = open(fname, 'w')
        f.write('solid\n')

        for face in self.flist:
            e0 = self.elist[face[0]]
            e1 = self.elist[face[1]]
            e2 = self.elist[face[2]]

            v0 = self.vlist[connected_vertex(e2, e0)]
            v1 = self.vlist[connected_vertex(e0, e1)]
            v2 = self.vlist[connected_vertex(e1, e2)]

            normal = v0 + v1 + v2
            normal = normal / numpy.linalg.norm(normal)

            f.write('facet normal '
                    + str(normal[0]) + ' '
                    + str(normal[1]) + ' '
                    + str(normal[2]) + '\n')
            f.write('outerloop\n')

            f.write('vertex '
                    + str(v0[0]) + ' ' + str(v0[1]) + ' ' + str(v0[2]) + '\n')
            f.write('vertex '
                    + str(v1[0]) + ' ' + str(v1[1]) + ' ' + str(v1[2]) + '\n')
            f.write('vertex '
                    + str(v2[0]) + ' ' + str(v2[1]) + ' ' + str(v2[2]) + '\n')

            f.write('endloop\n')
            f.write('endfacet\n')

        f.write('endsolid\n')
        f.close()

## usage:
##
# import gdome
## 測地ドームクラスを作る
# gd = gdome.GDome()
## 分割を行う
# gd.split()
## 何回か繰り返す
## 分割結果が正常かどうかの確認
# gd.sanity_check()
## STL出力
# gd.write_to_stl('gdome.stl')
