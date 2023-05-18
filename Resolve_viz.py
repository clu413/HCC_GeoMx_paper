#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 17:35:15 2022

@author: chenyuelu
"""
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import skimage.io
# Get the current working directory
# cwd = os.getcwd()
# os.chdir('/Users/chenyuelu/Library/Mobile Documents/com~apple~CloudDocs/Desktop/things/HST/research/HCC/')
os.chdir('/Users/chenyuelu/Dropbox (Partners HealthCare)/HCC_Resolve/UnzippedSlides')
data_path = '/Users/chenyuelu/Dropbox (Partners HealthCare)/HCC_Resolve/UnzippedSlides/'

annot = pd.DataFrame({'gene':['ACTA2','CCR7','CD8A','CXCL1','IL7R','LGALS1','LGALS9','PTPRC','VCAN','FGFR4','GPC3','HMGCR','ALDH1A1','ARG1','ASGR1','FLT4','IFIT1','PECAM1','VWF','KDR','CD34','IL33','PLVAP','VCAM1','LIVE1'],
                        'group':['S1','S1','S1','S1','S1','S1','S1','S1','S1','S2','S2','S2','S3','S3','S3','S3','S3','endothelial','endothelial','endothelial','endothelial','endothelial','endothelial','endothelial','endothelial']})

# # remove ASGR1 bc it takes up majority of S3 signal
# # annot = pd.DataFrame({'gene':['ACTA2','CCR7','CD8A','CXCL1','IL7R','LGALS1','LGALS9','PTPRC','VCAN','FGFR4','GPC3','HMGCR','ALDH1A1','FLT4','IFIT1','PECAM1','VWF','KDR','CD34','IL33','PLVAP','VCAM1','LIVE1'],
# #                       'group':['S1','S1','S1','S1','S1','S1','S1','S1','S1','S2','S2','S2','S3','S3','S3','endothelial','endothelial','endothelial','endothelial','endothelial','endothelial','endothelial','endothelial']})

# transcripts = pd.read_csv(data_path+'32779-547-slide3_submission/B/B1-1/32779-547_B1-1_results.txt', sep='\t', 
#                     index_col=False, names=['x','y','z','gene'])
# transcripts_subset = transcripts.merge(annot)

# # # dapi mask 
# dapi = skimage.io.imread(data_path+'32779-547-slide3_submission/B/B1-1/32779-547_B1-1_DAPI.tiff')
# skimage.io.imshow(dapi)
# # plt.grid(None)
# groups = transcripts_subset.groupby('group')
# for name, group in groups:
#     plt.plot(group.x, group.y, marker='.', linestyle='', markersize=0.05, alpha = 0.5, label=name)
#     plt.axis('equal')
#     plt.axis('off')
# # plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
# #           fancybox=True, shadow=True, ncol=5)
# # plt.savefig('All Data Analyses/Hoshida_gene_overlay/A1-1.png', dpi=300)

# # # just S1
# # groups = transcripts_subset[transcripts_subset['group']=='S1'].groupby('gene')
# # for name, group in groups:
# #     plt.plot(group.x, group.y, marker='o', linestyle='', markersize=0.5, alpha = 0.5, label=name)
# # plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
# #           fancybox=True, shadow=True, ncol=5)


# # # all 
# # fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(9, 7))
# # fig.suptitle('A1-1', fontsize=15)
# # plt.tight_layout()
# # axes[0,0].imshow(dapi)
# # axes[0,0].grid(None)
# # axes[0,0].axis('off')
# # axes[0,0].set_title("dapi")

# # # by S1, S2, S3, and endo
# # groups = transcripts_subset.groupby('group')
# # for name, group in groups:
# #     axes[0,1].plot(group.x, -group.y, marker='o', linestyle='', markersize=0.5, alpha = 0.5, label=name)
# # axes[0,1].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05),
# #           fancybox=False, shadow=False, ncol=5, markerscale=6, prop={'size': 6})
# # axes[0,1].axis('off')
# # axes[0,1].set_title("S1, S2, S3, and endothelial genes grouped")

# # # S1 genes only 
# # groups = transcripts_subset[transcripts_subset['group']=='S1'].groupby('gene')
# # for name, group in groups:
# #     axes[1,0].plot(group.x, -group.y, marker='o', linestyle='', markersize=0.5, alpha = 0.5, label=name)
# # axes[1,0].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=5, markerscale=6, prop={'size': 5})
# # axes[1,0].axis('off')
# # axes[1,0].set_title("S1 genes individually")

# # # S2 genes only 
# # groups = transcripts_subset[transcripts_subset['group']=='S2'].groupby('gene')
# # for name, group in groups:
# #     axes[1,1].plot(group.x, -group.y, marker='o', linestyle='', markersize=0.5, alpha = 0.5, label=name)
# # axes[1,1].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=5, markerscale=6, prop={'size': 5})
# # axes[1,1].axis('off')
# # axes[1,1].set_title("S2 genes individually")

# # # S3 genes only 
# # groups = transcripts_subset[transcripts_subset['group']=='S3'].groupby('gene')
# # for name, group in groups:
# #     axes[2,0].plot(group.x, -group.y, marker='o', linestyle='', markersize=0.5, alpha = 0.5, label=name)
# # axes[2,0].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=5, markerscale=6, prop={'size': 5})
# # axes[2,0].axis('off')
# # axes[2,0].set_title("S3 genes individually")

# # # endothelial genes only 
# # groups = transcripts_subset[transcripts_subset['group']=='endothelial'].groupby('gene')
# # for name, group in groups:
# #     axes[2,1].plot(group.x, -group.y, marker='o', linestyle='', markersize=0.5, alpha = 0.5, label=name)
# # axes[2,1].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=5, markerscale=6, prop={'size': 6})
# # axes[2,1].axis('off')
# # axes[2,1].set_title("endothelial genes individually")

# # plt.savefig('All Data Analyses/Hoshida_gene_overlay/A1-1.png', dpi=300)




# # iterate through all ROIs
# data_path = '/Users/chenyuelu/Dropbox (Partners HealthCare)/HCC_Resolve/UnzippedSlides/'
# marker_type = '.'
# marker_size = 0.5
# transparency = 0.3
# marker_scale = 6
# marker_font = 6
# # for pt in ['A','B','C','D']:
# for pt in ['B']:
#     print(pt)
#     # file_path = data_path + '32779-Slide2_submission/' + pt # slide 2
#     # file_path = data_path + '32779-slide4_20220322_submission/' + pt # slide 4
#     file_path = data_path + '32779-547-slide3_submission/' + pt # slide 3
#     for ROI in os.listdir(file_path):
#     # for ROI in ['A1-1']:
#         if os.path.isdir(file_path+'/'+ROI) == False:
#         # skip files
#             continue
#         print(ROI)
#         for file in os.listdir(file_path+'/'+ROI):
#             if file.endswith("DAPI.tiff"):
#             # dapi mask 
#                 dapi = skimage.io.imread(file_path+'/'+ROI+'/'+file)
#             if file.endswith('results.txt'):
#                 transcripts = pd.read_csv(file_path+'/'+ROI+'/'+file, sep='\t', index_col=False, names=['x','y','z','gene']) 
#         transcripts_subset = transcripts.merge(annot)
#         transcripts_subset['y_real'] = transcripts_subset['y']*(-1) # invert y coordinates
#         # all tuple(ti/2 for ti in t)
#         # fig, axes = plt.subplots(nrows=3, ncols=2, figsize=tuple(ti/1000 for ti in dapi.shape))
#         # fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(dapi.shape[1]*2/1000, dapi.shape[0]*3/1000))
#         # fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(9, 9*dapi.shape[1]/(1.5*dapi.shape[0])))
#         fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10,10))
#         fig.suptitle(ROI, fontsize=15)
#         plt.tight_layout()
#         axes[0,0].imshow(dapi)
#         # axes[0,0].grid(None)
#         axes[0,0].axis('equal')
#         axes[0,0].axis('off')
#         axes[0,0].set_title("dapi", fontdict={'fontsize': 8, 'fontweight': 'medium'})
        
#         # by S1, S2, S3 genes and endo density  
#         # endo = transcripts_subset[transcripts_subset['group']=='endothelial']
#         # sns.kdeplot(ax=axes[0,1], data = endo, x="x", y="y_real", shade=True, alpha=.3, color='red')
#         # S1S2S3 = transcripts_subset[transcripts_subset['group']!='endothelial']
#         groups = transcripts_subset.groupby('group')
#         for name, group in groups:
#             if name!='endothelial': 
#                 axes[0,1].plot(group.x, -group.y, marker=marker_type, linestyle='', markersize=0.3, alpha = transparency, label=name, zorder=10 if name=='S1' else 0) # force S1 to be on top
#                 # , color = "black" if name=='S1' else "blue" if name=='S2' else "green" - could also make colors consistently but hard to read 
#             if name=='endothelial': 
#                 sns.kdeplot(ax=axes[0,1], data = group, x="x", y="y_real", shade=True, alpha=.5, color='red')
#         axes[0,1].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=5, markerscale=marker_scale, prop={'size': marker_font})
#         axes[0,1].axis('equal')
#         axes[0,1].axis('off')
#         # axes[0,1].set_title("S1, S2, S3, and endothelial genes grouped", fontdict={'fontsize': 8, 'fontweight': 'medium'})
#         axes[0,1].set_title("S1, S2, S3 genes grouped - endothelial density", fontdict={'fontsize': 8, 'fontweight': 'medium'})
#         # plt.axis('equal')
        
#         # by S1, S2, S3, and endo genes
#         # groups = transcripts_subset.groupby('group')
#         # for name, group in groups:
#         #     axes[0,1].plot(group.x, -group.y, marker=marker_type, linestyle='', markersize=0.1, alpha = transparency, label=name)
#         # axes[0,1].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=5, markerscale=marker_scale, prop={'size': marker_font})
#         # axes[0,1].axis('equal')
#         # axes[0,1].axis('off')
#         # axes[0,1].set_title("S1, S2, S3, and endothelial genes grouped", fontdict={'fontsize': 8, 'fontweight': 'medium'})       
        
# #         # 2D density plot   
# # test_df = transcripts_subset[transcripts_subset['gene'].isin(['CXCL1','FLT4','CD34', 'IL33', 'KDR', 'PECAM1', 'PLVAP', 'VCAM1', 'VWF'])] #'CXCL1','GPC3','FLT4','PECAM1'
# # # test_df = transcripts_subset[transcripts_subset['group'].isin(['endothelial'])] #'FLT4','GPC3','FLT4','PECAM1'
# # test_df['y_real'] = test_df['y']*(-1) # invert y coordinates
# # groups = test_df.groupby('group')
# # for name, group in groups:
# #     print(name)
# #     if name!='endothelial':
# #         plt.plot(group.x, -group.y, marker=marker_type, linestyle='', markersize=1, alpha = 0.5, label=name)
# #     if name=='endothelial': 
# #         sns.kdeplot(data = group, x="x", y="y_real", shade=True, alpha=.3)
        
        
# # plt.title('Overplotting? Try 2D density graph', loc='left')
# # plt.show()
        
        
#         # S1 genes only 
#         groups = transcripts_subset[transcripts_subset['group']=='S1'].groupby('gene')
#         for name, group in groups:
#             axes[1,0].plot(group.x, -group.y, marker=marker_type, linestyle='', markersize=marker_size, alpha = transparency, label=name)
#         axes[1,0].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=5, markerscale=marker_scale, prop={'size': marker_font})
#         axes[1,0].axis('equal')
#         axes[1,0].axis('off')
#         axes[1,0].set_title("S1 genes individually", fontdict={'fontsize': 8, 'fontweight': 'medium'})
#         # plt.axis('equal')
        
#         # S2 genes only 
#         groups = transcripts_subset[transcripts_subset['group']=='S2'].groupby('gene')
#         for name, group in groups:
#             axes[1,1].plot(group.x, -group.y, marker=marker_type, linestyle='', markersize=marker_size, alpha = transparency, label=name)
#         axes[1,1].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=5, markerscale=marker_scale, prop={'size': marker_font})
#         axes[1,1].axis('equal')
#         axes[1,1].axis('off')
#         axes[1,1].set_title("S2 genes individually", fontdict={'fontsize': 8, 'fontweight': 'medium'})
#         # plt.axis('equal')
        
#         # S3 genes only 
#         groups = transcripts_subset[transcripts_subset['group']=='S3'].groupby('gene')
#         for name, group in groups:
#             axes[2,0].plot(group.x, -group.y, marker=marker_type, linestyle='', markersize=marker_size, alpha = transparency, label=name)
#         axes[2,0].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=5, markerscale=marker_scale, prop={'size': marker_font})
#         axes[2,0].axis('equal')
#         axes[2,0].axis('off')
#         axes[2,0].set_title("S3 genes individually", fontdict={'fontsize': 8, 'fontweight': 'medium'})
#         # plt.axis('equal')
        
#         # endothelial genes only 
#         groups = transcripts_subset[transcripts_subset['group']=='endothelial'].groupby('gene')
#         for name, group in groups:
#             axes[2,1].plot(group.x, -group.y, marker=marker_type, linestyle='', markersize=marker_size, alpha = transparency, label=name)
#         axes[2,1].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=5, markerscale=marker_scale, prop={'size': marker_font})
#         axes[2,1].axis('equal')
#         axes[2,1].axis('off')
#         axes[2,1].set_title("endothelial genes individually",fontdict={'fontsize': 8, 'fontweight': 'medium'})        
        
#         # endothelial density 
#         # sns.boxplot(ax=axes[1, 2], data=pokemon, x='Generation', y='HP')
#         # endo = transcripts_subset[transcripts_subset['group']=='endothelial']
#         # sns.kdeplot(ax=axes[2,1], data = endo, x="x", y="y_real", shade=True, alpha=.3, color='red')
#         # axes[2,1].axis('equal')
#         # axes[2,1].axis('off')        
#         # plt.axis('equal')
#         plt.savefig('All Data Analyses/Hoshida_gene_overlay/slide3/slide3_'+ROI+'.png', dpi=300)
            
#         del dapi, transcripts, transcripts_subset


# whole slides - slides 3 and 6

# iterate through all ROIs
data_path = '/Users/chenyuelu/Dropbox (Partners HealthCare)/HCC_Resolve/UnzippedSlides/'
marker_type = '.'
marker_size = 0.5
transparency = 0.3
marker_scale = 6
marker_font = 6
# for pt in ['A','B','C','D']:
for pt in ['B']:
    print(pt)
    file_path = data_path + '32779-547-slide3_submission/' + pt # slide 3
    # for ROI in os.listdir(file_path):
    for ROI in ['B1-1']:
        if os.path.isdir(file_path+'/'+ROI) == False:
        # skip files
            continue
        print(ROI)
        for file in os.listdir(file_path+'/'+ROI):
            if file.endswith("DAPI.tiff"):
            # dapi mask 
                dapi = skimage.io.imread(file_path+'/'+ROI+'/'+file)
            if file.endswith('results.txt'):
                transcripts = pd.read_csv(file_path+'/'+ROI+'/'+file, sep='\t', index_col=False, names=['x','y','z','gene']) 
        transcripts_subset = transcripts.merge(annot)
        transcripts_subset['y_real'] = transcripts_subset['y']*(-1) # invert y coordinates
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,10))
        fig.suptitle(ROI, fontsize=15)
        plt.tight_layout()
        axes[0].imshow(dapi)
        # axes[0,0].grid(None)
        axes[0].axis('equal')
        axes[0].axis('off')
        axes[0].set_title("dapi", fontdict={'fontsize': 8, 'fontweight': 'medium'})
        
        # by S1, S2, S3 genes and endo density  
        # endo = transcripts_subset[transcripts_subset['group']=='endothelial']
        # sns.kdeplot(ax=axes[0,1], data = endo, x="x", y="y_real", shade=True, alpha=.3, color='red')
        # S1S2S3 = transcripts_subset[transcripts_subset['group']!='endothelial']
        groups = transcripts_subset.groupby('group')
        for name, group in groups:
            if name!='endothelial': 
                axes[1].plot(group.x, -group.y, marker=marker_type, linestyle='', markersize=0.3, alpha = transparency, label=name, zorder=10 if name=='S1' else 0) # force S1 to be on top
                # , color = "black" if name=='S1' else "blue" if name=='S2' else "green" - could also make colors consistently but hard to read 
            if name=='endothelial': 
                sns.kdeplot(ax=axes[1], data = group, x="x", y="y_real", shade=True, alpha=.5, color='red')
        axes[1].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05), ncol=5, markerscale=marker_scale, prop={'size': marker_font})
        axes[1].axis('equal')
        axes[1].axis('off')
        # axes[0,1].set_title("S1, S2, S3, and endothelial genes grouped", fontdict={'fontsize': 8, 'fontweight': 'medium'})
        axes[1].set_title("S1, S2, S3 genes grouped - endothelial density", fontdict={'fontsize': 8, 'fontweight': 'medium'})
    
        plt.savefig('All Data Analyses/Hoshida_gene_overlay/slide3/slide3_'+ROI+'.png', dpi=300)
            
        del dapi, transcripts, transcripts_subset

