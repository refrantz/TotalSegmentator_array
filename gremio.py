import nibabel as nib
import numpy as np
from pathlib import Path
import json

#testfile for modified python_api

def process_segmentation():
    from totalsegmentator.python_api import totalsegmentator

    file = Path("./s0000_0000.nii.gz")
    original_nifti = nib.load(file)
    array = original_nifti.get_fdata()
    print(array.shape)
    mask = totalsegmentator(array)

    nifti_image = nib.Nifti1Image(mask, original_nifti.affine, original_nifti.header)
    nib.save(nifti_image, "./label")

if __name__ == "__main__":
    process_segmentation()
