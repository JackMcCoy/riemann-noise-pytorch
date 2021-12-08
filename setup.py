from setuptools import setup, find_packages

setup(
    name = 'riemann_noise',
    packages = find_packages(),
    version = '0.0.1',
    license='MIT',
    description = 'Riemann Noise Injection - Pytorch',
    author = 'David Gill',
    author_email = 'fdrdavegill@gmail.com',
    url = 'https://github.com/jackmccoy/riemannnoise',
    keywords = [
    'artificial intelligence',
    'deep learning',
    'pytorch',
    'generative adversarial network',
    'noise injection'
    ],
    install_requires=[
    'torch'
    ],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    ],
)
