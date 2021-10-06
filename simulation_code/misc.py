from random import uniform
from const import *
from asp import *
from convex_solver import convex_solve
from mpo import *
import matplotlib
matplotlib.use('agg') 
import matplotlib.pyplot as plt
import tqdm
import numpy as np



def plot_different_step():
    print("step")
    num = [600, 800, 1000, 1200, 1400]
    phi_step_1_lst = []
    social_step_1_lst = []
    phi_step_5_lst = []
    social_step_5_lst = []
    phi_step_10_lst = []
    social_step_10_lst = []
    for n in num:
        phi_step_1 = 0
        soc_step_1 = 0
        phi_step_5 = 0
        soc_step_5 = 0
        phi_step_10 = 0
        soc_step_10 = 0
        for _ in tqdm(range(ITER)):
            mpo = MPO(DEFAULT_DEVICE_RATIO, n, load_type.AVERAGE)
            _, max_phi, social, _, _ = mpo.optimize_phi_with_step(1)
            phi_step_1 += max_phi
            soc_step_1 += social
            _, max_phi, social, _, _= mpo.optimize_phi_with_step(2)
            phi_step_5 += max_phi
            soc_step_5 += social
            _, max_phi, social, _, _ = mpo.optimize_phi_with_step(0.5)
            phi_step_10 += max_phi
            soc_step_10 += social
        phi_step_1_lst.append(phi_step_1 / ITER)
        social_step_1_lst.append(soc_step_1 / ITER)
        phi_step_5_lst.append(phi_step_5 / ITER)
        social_step_5_lst.append(soc_step_5 / ITER)
        phi_step_10_lst.append(phi_step_10 / ITER)
        social_step_10_lst.append(soc_step_10 / ITER)
    X = np.arange(5)
    plt.figure(figsize=FIG_SIZE, dpi=DPI)
    plt.plot(num, phi_step_10_lst, marker='s', linestyle='-.', label='Step = 0.5', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
    plt.plot(num, phi_step_1_lst, marker='o', linestyle='-.', label='Step = 1', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
    plt.plot(num, phi_step_5_lst, marker='^', linestyle='-.', label='Step = 2', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
    plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
    plt.xlabel(r'$\bf{Device\ Number}$', fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r'$\bf{Optimal\ MPO\ Price}$', fontsize=LABEL_FONT_SIZE)
    plt.xticks(fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.savefig('./image/step_compare/5GDDoS_Game_price_device_with_step.jpg')
    plt.savefig('./image/step_compare/5GDDoS_Game_price_device_with_step.pdf')
    plt.savefig('./image/step_compare/5GDDoS_Game_price_device_with_step.eps')
    plt.close()

    plt.figure(figsize=FIG_SIZE, dpi=DPI)
    plt.bar(X + 0.00, social_step_10_lst, label='Step = 0.5', width=0.25)
    plt.bar(X + 0.25, social_step_1_lst, label='Step = 1', width=0.25)
    plt.bar(X + 0.50, social_step_5_lst, label='Step = 2', width=0.25)
    plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
    plt.xticks(X + (0.375 / 2), (600, 800, 1000, 1200, 1400))
    plt.xlabel(r'$\bf{Device\ Number}$', fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r'$\bf{Social\ Utility}$', fontsize=LABEL_FONT_SIZE)
    plt.xticks(fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.savefig('./image/step_compare/5GDDoS_Game_social_device_with_step.jpg')
    plt.savefig('./image/step_compare/5GDDoS_Game_social_device_with_step.pdf')
    plt.savefig('./image/step_compare/5GDDoS_Game_social_device_with_step.eps')
    plt.close()

# def plot_max_vm():
#     print("max vm")
#     num = [500, 750, 1000, 1250]
#     utility_proposed_lst = []
#     social_proposed_lst = []
#     asp_utility_proposed_lst = []
#     util_max_num = []
#     social_max_num = []
#     asp_util_max_num = []
#     for n in num:
#         u_max_num = 0
#         soc_max_num = 0
#         asp_u_max_num = 0
#         utility_proposed = 0
#         social_proposed = 0
#         asp_utility_proposed = 0
#         for _ in tqdm(range(ITER)):
#             mpo = MPO(0.1, n)
#             util, _, social, asp_u = mpo.optimize_phi_with_step(0.5)
#             utility_proposed += util
#             social_proposed += social
#             asp_utility_proposed += asp_u
#             mpo.find_constraint_phi()
#             phi = mpo.constraint_phi
#             util, social, asp_u = mpo.optimize_phi_with_price(phi)
#             u_max_num += util
#             soc_max_num += social
#             asp_u_max_num += asp_u
#         utility_proposed_lst.append(utility_proposed / ITER)
#         social_proposed_lst.append(social_proposed / ITER)
#         asp_utility_proposed_lst.append(asp_utility_proposed / ITER)
#         util_max_num.append(u_max_num / ITER)
#         social_max_num.append(soc_max_num / ITER)
#         asp_util_max_num.append(asp_u_max_num / ITER)
#     plt.figure(figsize=FIG_SIZE, dpi=DPI)
#     plt.plot(num, utility_proposed_lst, marker='o', linestyle='-.', label='Proposed Scheme', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
#     plt.plot(num, util_max_num, marker='^', linestyle='-.', label='Max VM', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
#     plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
#     plt.xlabel(r'$\bf{Device\ Number}$', fontsize=LABEL_FONT_SIZE)
#     plt.ylabel(r'$\bf{MPO\ Utility}$', fontsize=LABEL_FONT_SIZE)
#     plt.xticks(fontsize=TICKS_FONT_SIZE)
#     plt.yticks(fontsize=TICKS_FONT_SIZE)
#     plt.savefig('./5GDDoS_Game_MPO_device_max_num.jpg')
#     plt.savefig('./5GDDoS_Game_MPO_device_max_num.pdf')
#     plt.close()

#     plt.figure(figsize=FIG_SIZE, dpi=DPI)
#     plt.plot(num, social_proposed_lst, marker='o', linestyle='-.', label='Proposed Scheme', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
#     plt.plot(num, social_max_num, marker='^', linestyle='-.', label='Max VM', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
#     plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
#     plt.xlabel(r'$\bf{Device\ Number}$', fontsize=LABEL_FONT_SIZE)
#     plt.ylabel(r'$\bf{Social\ Welfare}$', fontsize=LABEL_FONT_SIZE)
#     plt.xticks(fontsize=TICKS_FONT_SIZE)
#     plt.yticks(fontsize=TICKS_FONT_SIZE)
#     plt.savefig('./5GDDoS_Game_social_device_max_num.jpg')
#     plt.savefig('./5GDDoS_Game_social_device_max_num.pdf')
#     plt.close()

#     plt.figure(figsize=FIG_SIZE, dpi=DPI)
#     plt.plot(num, asp_utility_proposed_lst, marker='o', linestyle='-.', label='Proposed Scheme', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
#     plt.plot(num, asp_util_max_num, marker='^', linestyle='-.', label='Max VM', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
#     plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
#     plt.xlabel(r'$\bf{Device\ Number}$', fontsize=LABEL_FONT_SIZE)
#     plt.ylabel(r'$\bf{ASP\ Utility}$', fontsize=LABEL_FONT_SIZE)
#     plt.xticks(fontsize=TICKS_FONT_SIZE)
#     plt.yticks(fontsize=TICKS_FONT_SIZE)
#     plt.savefig('./5GDDoS_Game_asp_device_max_num.jpg')
#     plt.savefig('./5GDDoS_Game_asp_device_max_num.pdf')
#     plt.close()

def plot_different_ratio():
    ratio = [0.1, 0.3, 0.5, 0.7, 0.9]
    plt.figure(figsize=FIG_SIZE, dpi=DPI)
    step = 1
    for ra in ratio:
        ut = []
        pr = []
        phi = 30
        mpo = MPO(ra, DEFAULT_DEVICE_NUM, load_type.AVERAGE)
        vm_prior = float('inf')
        for _ in range(3000):
            mpo.set_and_check_required_vm(phi)
            vm_after = mpo.total_vm()
            welfare = 0
            for asp in mpo.asp_lst:
                welfare += asp.utility
            pr.append(phi)
            ut.append(phi * vm_after - MPO_cost(vm_after) + welfare)
            phi += step
            if vm_prior < vm_after:
                print('Total VM is not non-increasing')
            vm_prior = vm_after
        plt.plot(pr, ut, marker='.', linestyle='-.', label=f'ratio : {ra}', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
    plt.xlabel(r'$\bf{MPO\ Price}$', fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r'$\bf{Social\ Welfare}$', fontsize=LABEL_FONT_SIZE)
    plt.xticks(fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
    plt.savefig('./image/misc/5GDDoS_Game_utility_ratio.pdf')
    plt.savefig('./image/misc/5GDDoS_Game_utility_ratio.jpg')
    plt.savefig('./image/misc/5GDDoS_Game_utility_ratio.eps')
    plt.close()

def plot_flat_price():
    price = [i for i in range(50, 2000, 10)]
    mpo = MPO(DEFAULT_DEVICE_RATIO, DEFAULT_DEVICE_NUM, load_type.AVERAGE)
    utility_proposed_lst, _, _, _, _ = mpo.optimize_phi_with_step(1)
    ut_lst_proposed = []
    ut_lst_flat = []
    for p in price:
        mpo.set_and_check_required_vm(p)
        vm_num = mpo.total_vm()
        uti = p * vm_num - MPO_cost(vm_num)
        ut_lst_flat.append(uti)
        ut_lst_proposed.append(utility_proposed_lst)
    plt.figure(figsize=FIG_SIZE, dpi=DPI)
    plt.plot(price, ut_lst_proposed, marker='o', linestyle='-.', label='Proposed Scheme', linewidth=LINE_WIDTH, markersize=10)
    plt.plot(price, ut_lst_flat, marker='^', linestyle='-.', label='Flat Price', linewidth=LINE_WIDTH, markersize=10)
    plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
    plt.xlabel(r'$\bf{Flat\ Price}$', fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r'$\bf{MPO\ Utility}$', fontsize=LABEL_FONT_SIZE)
    plt.xticks(fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.savefig('./image/flat/5GDDoS_Game_utility_flat.jpg')
    plt.savefig('./image/flat/5GDDoS_Game_utility_flat.pdf')
    plt.savefig('./image/flat/5GDDoS_Game_utility_flat.eps')
    plt.close()

def plot_asp_utility():
    asp = ASP(DEFAULT_DEVICE_RATIO, DEFAULT_DEVICE_NUM, load_type.AVERAGE)
    utility_lst = []
    purchased_vm_lst = []
    utility_lst_without_constraint = []
    purchased_vm_lst_without_constraint = []
    price = [i for i in range(20, 5000, 10)]
    print(asp.malicious_arrival_rate/(asp.chi * GLOBAL_ETA))
    for i in range(20, 5000, 10):
        asp.mpo_price = i
        asp.optimize_zv()
        utility_lst.append(asp.utility)
        purchased_vm_lst.append(asp.z_v)
        # print(asp.z_h, asp.z_v)
        asp.optimize_zv_without_constraint()
        utility_lst_without_constraint.append(asp.utility)
        purchased_vm_lst_without_constraint.append(asp.z_v)
        
    plt.figure(figsize=FIG_SIZE, dpi=DPI)
    plt.plot(price, utility_lst, marker='.', linestyle='-.', label='With Constraint', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
    plt.plot(price, utility_lst_without_constraint, marker='.', linestyle='-.', label='Without Constraint', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
    plt.vlines(asp.bound, ymin=min(utility_lst_without_constraint + utility_lst), ymax=max(utility_lst_without_constraint + utility_lst), linewidth=LINE_WIDTH)
    plt.vlines(asp.qbound, ymin=min(utility_lst_without_constraint + utility_lst), ymax=max(utility_lst_without_constraint + utility_lst), linewidth=LINE_WIDTH)
    

    plt.xlabel(r'$\bf{MPO\ Price}$', fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r'$\bf{ASP\ Utility}$', fontsize=LABEL_FONT_SIZE)
    plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
    plt.xticks(fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.savefig('./image/asp/5GDDoS_Game_ASP_price.jpg')
    plt.savefig('./image/asp/5GDDoS_Game_ASP_price.pdf')
    plt.savefig('./image/asp/5GDDoS_Game_ASP_price.eps')
    plt.close()

    plt.figure(figsize=FIG_SIZE, dpi=DPI)
    plt.plot(price, purchased_vm_lst, marker='.', linestyle='-.', label='With Constraint', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
    plt.plot(price, purchased_vm_lst_without_constraint, marker='.', linestyle='-.', label='Without Constraint', linewidth=LINE_WIDTH, markersize=MARKER_SIZE)
    plt.vlines(asp.bound, ymin=min(purchased_vm_lst_without_constraint + purchased_vm_lst), ymax=max(purchased_vm_lst_without_constraint + purchased_vm_lst), linewidth=LINE_WIDTH)
    plt.vlines(asp.qbound, ymin=min(purchased_vm_lst_without_constraint + purchased_vm_lst), ymax=max(purchased_vm_lst_without_constraint + purchased_vm_lst), linewidth=LINE_WIDTH)
    plt.xlabel(r'$\bf{MPO\ Price}$', fontsize=LABEL_FONT_SIZE)
    plt.ylabel(r'$\bf{Purchased\ VM}$', fontsize=LABEL_FONT_SIZE)
    plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
    plt.xticks(fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.savefig('./image/asp/5GDDoS_Game_ASP_vm.jpg')
    plt.savefig('./image/asp/5GDDoS_Game_ASP_vm.pdf')
    plt.savefig('./image/asp/5GDDoS_Game_ASP_vm.eps')
    plt.close()