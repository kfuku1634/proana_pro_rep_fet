#!/bin/bash -x

grep "++--  3142" ./4/protein_rep_ig_4.fet > ./4/3142++--_ig.fet
grep "++--  1324" ./4/protein_rep_ig_4.fet > ./4/1324++--_ig.fet
grep "+--+  1423" ./4/protein_rep_ig_4.fet > ./4/1423+--+_ig.fet
grep "+--+  4132" ./4/protein_rep_ig_4.fet > ./4/4132+--+_ig.fet

grep "++--  3142" ./4/protein_rep_4.fet > ./4/3142++--.fet
grep "++--  1324" ./4/protein_rep_4.fet > ./4/1324++--.fet
grep "+--+  1423" ./4/protein_rep_4.fet > ./4/1423+--+.fet
grep "+--+  4132" ./4/protein_rep_4.fet > ./4/4132+--+.fet
