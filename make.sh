#!/bin/bash -x

awk '$7=="b-a-b" && $8=="b-a-b" && $4=="132" && $3=="+--" {print }' protein_rep_ig.fet>132+--_aa.fet
awk '$7=="b-c-b" && $8=="b-a-b" && $4=="132" && $3=="+--" {print }' protein_rep_ig.fet>132+--_ca.fet
awk '$7=="b-a-b" && $8=="b-c-b" && $4=="132" && $3=="+--" {print }' protein_rep_ig.fet>132+--_ac.fet
awk '$7=="b-c-b" && $8=="b-c-b" && $4=="132" && $3=="+--" {print }' protein_rep_ig.fet>132+--_cc.fet

awk '$7=="b-a-b" && $8=="b-c-b" && $4=="132" && $3=="++-" {print }' protein_rep_ig.fet>132++-_ac.fet
awk '$7=="b-a-b" && $8=="b-a-b" && $4=="132" && $3=="++-" {print }' protein_rep_ig.fet>132++-_aa.fet
awk '$7=="b-c-b" && $8=="b-c-b" && $4=="132" && $3=="++-" {print }' protein_rep_ig.fet>132++-_cc.fet
awk '$7=="b-c-b" && $8=="b-a-b" && $4=="132" && $3=="++-" {print }' protein_rep_ig.fet>132++-_ca.fet

awk '$7=="b-c-b" && $8=="b-a-b" && $4=="213" && $3=="+--" {print }' protein_rep_ig.fet>213+--_ac.fet
awk '$7=="b-a-b" && $8=="b-a-b" && $4=="213" && $3=="+--" {print }' protein_rep_ig.fet>213+--_aa.fet
awk '$7=="b-c-b" && $8=="b-c-b" && $4=="213" && $3=="+--" {print }' protein_rep_ig.fet>213+--_cc.fet
awk '$7=="b-a-b" && $8=="b-c-b" && $4=="213" && $3=="+--" {print }' protein_rep_ig.fet>213+--_ca.fet

awk '$7=="b-c-b" && $8=="b-a-b" && $4=="213" && $3=="++-" {print }' protein_rep_ig.fet>213++-_ac.fet
awk '$7=="b-a-b" && $8=="b-a-b" && $4=="213" && $3=="++-" {print }' protein_rep_ig.fet>213++-_aa.fet
awk '$7=="b-c-b" && $8=="b-c-b" && $4=="213" && $3=="++-" {print }' protein_rep_ig.fet>213++-_cc.fet
awk '$7=="b-a-b" && $8=="b-c-b" && $4=="213" && $3=="++-" {print }' protein_rep_ig.fet>213++-_ca.fet

grep "+--  132" protein_rep_ig.fet > 132+--.fet
grep "++-  132" protein_rep_ig.fet > 132++-.fet
grep "++-  213" protein_rep_ig.fet > 213++-.fet
grep "+--  213" protein_rep_ig.fet > 213+--.fet

awk '$61=="R" {print }' 213+--_ax.fet>213+--_ax_R.fet
awk '$61=="L" {print }' 213+--_ax.fet>213+--_ax_L.fet
awk '$61=="G" {print }' 213+--_ax.fet>213+--_ax_G.fet

awk '$61=="R" {print }' 132+--_ax.fet>132+--_ax_R.fet
awk '$61=="L" {print }' 132+--_ax.fet>132+--_ax_L.fet
awk '$61=="G" {print }' 132+--_ax.fet>132+--_ax_G.fet

awk '$61=="R" {print }' 213+--_cx.fet>213+--_cx_R.fet
awk '$61=="L" {print }' 213+--_cx.fet>213+--_cx_L.fet
awk '$61=="G" {print }' 213+--_cx.fet>213+--_cx_G.fet

awk '$61=="R" {print }' 132+--_cx.fet>132+--_cx_R.fet
awk '$61=="L" {print }' 132+--_cx.fet>132+--_cx_L.fet
awk '$61=="G" {print }' 132+--_cx.fet>132+--_cx_G.fet

