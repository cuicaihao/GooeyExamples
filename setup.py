from setuptools import setup

APP = ['subreddit.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'site_packages': True,
    # 'iconfile': 'appicon.icns',
    'packages': ['wx', 'requests'],
    'plist': {
        'CFBundleName': 'Subreddit Viewer',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
