from asp import ASP
from const import *
from device import Device
from mpo import *
from convex_solver import *
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np


def plot_ratio_with_same_IPS_ratio():
    print("same ratio")
    ratio = [0.1, 0.3, 0.5, 0.7, 0.9]
    util_proposed = []
    social_proposed = []
    asp_util_proposed = []
    util_fix = []
    social_fix = []
    asp_util_fix = []
    for r in ratio:
        u_fix = 0
        soc_fix = 0
        asp_u_fix = 0
        u_proposed = 0
        soc_proposed = 0
        asp_u_proposed = 0
        i = 0
        pbar = tqdm(total=ITER)
        while i < ITER:
            try:
                mpo = MPO(r, 1000)
                if r > 0.9:
                    r = 0.9
                util, max_phi, social, asp_u, _ = mpo.optimize_phi()
                u_proposed += util
                soc_proposed += social
                asp_u_proposed += asp_u
                util, social, asp_u, _ = mpo.optimize_phi_with_chi(r, max_phi)
                u_fix += util
                soc_fix += social
                asp_u_fix += asp_u
                i += 1
                pbar.update(1)
            except ArithmeticError as e:
                print(e)
        pbar.close()
        util_proposed.append(u_proposed / ITER)
        social_proposed.append(soc_proposed / ITER)
        asp_util_proposed.append(asp_u_proposed / ITER)
        util_fix.append(u_fix / ITER)
        social_fix.append(soc_fix / ITER)
        asp_util_fix.append(asp_u_fix / ITER)
    plt.figure(figsize=(45, 25), dpi=400)
    plt.plot(ratio, util_proposed, marker='o', linestyle='-.', label='Proposed Scheme', linewidth=7, markersize=30)
    plt.plot(ratio, util_fix, marker='^', linestyle='-.', label='IPS ratio', linewidth=7, markersize=30)
    plt.legend(loc="best", fontsize=100)
    plt.xlabel(r'$\bf{Malicious\ Users\ to\ Normal\ Users\ Ratio}$', fontsize=100)
    plt.ylabel(r'$\bf{MPO\ Utility}$', fontsize=100)
    plt.xticks(fontsize=80)
    plt.yticks(fontsize=80)
    plt.savefig('./image/same_ips/5GDDoS_Game_MPO_ratio_with_same_IPS_ratio.jpg')
    plt.savefig('./image/same_ips/5GDDoS_Game_MPO_ratio_with_same_IPS_ratio.pdf')
    plt.close()

    plt.figure(figsize=(45, 25), dpi=400)
    plt.plot(ratio, social_proposed, marker='o', linestyle='-.', label='Proposed Scheme', linewidth=7, markersize=30)
    plt.plot(ratio, social_fix, marker='^', linestyle='-.', label='IPS ratio', linewidth=7, markersize=30)
    plt.legend(loc="best", fontsize=100)
    plt.xlabel(r'$\bf{Malicious\ Users\ to\ Normal\ Users\ Ratio}$', fontsize=100)
    plt.ylabel(r'$\bf{Social\ Welfare}$', fontsize=100)
    plt.xticks(fontsize=80)
    plt.yticks(fontsize=80)
    plt.savefig('./image/same_ips/5GDDoS_Game_social_ratio_with_same_IPS_ratio.jpg')
    plt.savefig('./image/same_ips/5GDDoS_Game_social_ratio_with_same_IPS_ratio.pdf')
    plt.close()

    plt.figure(figsize=(45, 25), dpi=400)
    plt.plot(ratio, asp_util_proposed, marker='o', linestyle='-.', label='Proposed Scheme', linewidth=7, markersize=30)
    plt.plot(ratio, asp_util_fix, marker='^', linestyle='-.', label='IPS ratio', linewidth=7, markersize=30)
    plt.xlabel(r'$\bf{Malicious\ Users\ to\ Normal\ Users\ Ratio}$', fontsize=100)
    plt.ylabel(r'$\bf{ASP\ Utility}$', fontsize=100)
    plt.xticks(fontsize=80)
    plt.yticks(fontsize=80)
    plt.savefig('./image/same_ips/5GDDoS_Game_asp_ratio_with_same_IPS_ratio.jpg')
    plt.savefig('./image/same_ips/5GDDoS_Game_asp_ratio_with_same_IPS_ratio.pdf')
    plt.close()

def plot_ratio_with_same_IPS_ratio_step():
    print("same ratio step")
    ratio = [0.1, 0.3, 0.5, 0.7, 0.9]
    util_proposed = []
    social_proposed = []
    asp_util_proposed = []
    util_fix = []
    social_fix = []
    asp_util_fix = []
    for r in ratio:
        u_fix = 0
        soc_fix = 0
        asp_u_fix = 0
        u_proposed = 0
        soc_proposed = 0
        asp_u_proposed = 0
        i = 0
        pbar = tqdm(total=ITER)
        while i < ITER:
            try:
                mpo = MPO(r, 1000)
                if r > 0.9:
                    r = 0.9
                util, max_phi, social, asp_u, _ = mpo.optimize_phi_with_step(0.5)
                u_proposed += util
                soc_proposed += social
                asp_u_proposed += asp_u
                util, social, asp_u, _ = mpo.optimize_phi_with_chi(r, max_phi)
                u_fix += util
                soc_fix += social
                asp_u_fix += asp_u
                i += 1
                pbar.update(1)
            except ArithmeticError as e:
                print(e)
        pbar.close()
        util_proposed.append(u_proposed / ITER)
        social_proposed.append(soc_proposed / ITER)
        asp_util_proposed.append(asp_u_proposed / ITER)
        util_fix.append(u_fix / ITER)
        social_fix.append(soc_fix / ITER)
        asp_util_fix.append(asp_u_fix / ITER)
    plt.figure(figsize=(45, 25), dpi=400)
    plt.plot(ratio, util_proposed, marker='o', linestyle='-.', label='Proposed Scheme', linewidth=7, markersize=30)
    plt.plot(ratio, util_fix, marker='^', linestyle='-.', label='IPS ratio', linewidth=7, markersize=30)
    plt.legend(loc="best", fontsize=100)
    plt.xlabel(r'$\bf{Malicious\ Users\ to\ Normal\ Users\ Ratio}$', fontsize=100)
    plt.ylabel(r'$\bf{MPO\ Utility}$', fontsize=100)
    plt.xticks(fontsize=80)
    plt.yticks(fontsize=80)
    plt.savefig('./image/same_ips/5GDDoS_Game_MPO_ratio_with_same_IPS_ratio_step.jpg')
    plt.savefig('./image/same_ips/5GDDoS_Game_MPO_ratio_with_same_IPS_ratio_step.pdf')
    plt.close()

    plt.figure(figsize=(45, 25), dpi=400)
    plt.plot(ratio, social_proposed, marker='o', linestyle='-.', label='Proposed Scheme', linewidth=7, markersize=30)
    plt.plot(ratio, social_fix, marker='^', linestyle='-.', label='IPS ratio', linewidth=7, markersize=30)
    plt.legend(loc="best", fontsize=100)
    plt.xlabel(r'$\bf{Malicious\ Users\ to\ Normal\ Users\ Ratio}$', fontsize=100)
    plt.ylabel(r'$\bf{Social\ Welfare}$', fontsize=100)
    plt.xticks(fontsize=80)
    plt.yticks(fontsize=80)
    plt.savefig('./image/same_ips/5GDDoS_Game_social_ratio_with_same_IPS_ratio_step.jpg')
    plt.savefig('./image/same_ips/5GDDoS_Game_social_ratio_with_same_IPS_ratio_step.pdf')
    plt.close()

    plt.figure(figsize=(45, 25), dpi=400)
    plt.plot(ratio, asp_util_proposed, marker='o', linestyle='-.', label='Proposed Scheme', linewidth=7, markersize=30)
    plt.plot(ratio, asp_util_fix, marker='^', linestyle='-.', label='IPS ratio', linewidth=7, markersize=30)
    plt.xlabel(r'$\bf{Malicious\ Users\ to\ Normal\ Users\ Ratio}$', fontsize=100)
    plt.ylabel(r'$\bf{ASP\ Utility}$', fontsize=100)
    plt.xticks(fontsize=80)
    plt.yticks(fontsize=80)
    plt.savefig('./image/same_ips/5GDDoS_Game_asp_ratio_with_same_IPS_ratio_step.jpg')
    plt.savefig('./image/same_ips/5GDDoS_Game_asp_ratio_with_same_IPS_ratio_step.pdf')
    plt.close()