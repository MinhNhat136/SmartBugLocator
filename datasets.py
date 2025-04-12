from collections import namedtuple
from pathlib import Path

# Dataset root directory
_DATASET_ROOT = Path('data')

Dataset = namedtuple('Dataset', ['name', 'src', 'bug_repo', 'repo_url', 'features'])

# Source codes and bug repositories
aspectj = Dataset(
    'aspectj',
    'source_files/org.aspectj-bug433351/',
    _DATASET_ROOT / 'AspectJ.txt',
    "https://github.com/eclipse/org.aspectj/tree/bug433351.git",
    _DATASET_ROOT / 'features_aspectj.csv'
)

eclipse = Dataset(
    'eclipse',
    'source_files/eclipse.platform.ui-johna-402445/',
    _DATASET_ROOT / 'Eclipse_Platform_UI.txt',
    "https://github.com/eclipse/eclipse.platform.ui.git",
    _DATASET_ROOT / 'features_eclipse.csv'
)

swt = Dataset(
    'swt',
    'source_files/eclipse.platform.swt-xulrunner-31/',
    _DATASET_ROOT / 'SWT.txt',
    "https://github.com/eclipse/eclipse.platform.swt.git",
    _DATASET_ROOT / 'features_swt.csv'
)

tomcat = Dataset(
    'tomcat',
    'source_files/tomcat-7.0.51/',
    _DATASET_ROOT / 'Tomcat.txt',
    "https://github.com/apache/tomcat.git",
    _DATASET_ROOT / 'features_tomcat/'
)

birt = Dataset(
    'birt',
    'source_files/birt-20140211-1400',
    _DATASET_ROOT / 'Birt.txt',
    "https://github.com/apache/tomcat.git",
    _DATASET_ROOT / 'features_birt/'
)

### Current dataset in use. (change this name to change the dataset)
DATASETS = [aspectj, eclipse, swt, tomcat, birt]


