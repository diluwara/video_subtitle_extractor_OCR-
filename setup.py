from distutils.core import setup

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='vseocr',
    packages=['vseocr'],
    version='0.1.0',
    license='MIT',
    description='Extract the textual content from videos using machine learning',
    long_description_content_type='text/markdown',
    long_description=readme,
    author=' Diluwara Khatun',
    author_email='diluwarakhatun562gmail.com',
    url='https://github.com/diluwara/vseocr',
    install_requires=[
        'thefuzz>=0.19',
        'python-Levenshtein>=0.12',
        'paddleocr==2.7.0.2',
        'paddlepaddle>=2.3'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)