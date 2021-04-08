
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import glob
from tamil.txt2unicode import dinakaran2unicode


# In[2]:


source_folder = "/home/nat/Desktop/metadata_swiss_knife/data/tamil_docs/"
source_txts_folder = "/home/nat/Desktop/metadata_swiss_knife/data/tamil_docs_txts_dinakaran/"
target_txts_folder = "/home/nat/Desktop/metadata_swiss_knife/data/tamil_docs_txts_unicode/"


# In[3]:


def get_txt_file(doc_file_path, output_dir):
    try:
        cmd = "soffice --headless --convert-to txt " + doc_file_path + " --outdir " + output_dir
        os.system(cmd)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


# In[4]:


def convert_font(source_file_path, target_file_path):
    fw = open(target_file_path, 'w')

    with open(source_file_path) as f:
        for line in f:
            uni = dinakaran2unicode(line)
            fw.write(uni)
    fw.close()


# In[5]:


files = glob.glob(source_txts_folder + "*.txt")
for doc_file in files:
    file_name = os.path.basename(doc_file)
    file_name_without_ext = os.path.splitext(file_name)[0]
    target_file_path = target_txts_folder + "/" + file_name_without_ext + "-unicode.txt"
    convert_font(doc_file, target_file_path)
    print(target_file_path)

