from distutils.core import setup

with open("README.md", encoding="utf8") as f:
    long_description = f.read()

setup(
    name = 'jiosaavn-python',
    packages = ['jiosaavn'],
    version = '0.2',
    license='MIT',
    description = 'An unofficial Python3 wrapper for JioSaavn, a popular Indian music streaming service..',
    author = 'Abhishek Chaudhari',
    author_email = 'abhichaudhari@protonmail.com',
    url = 'https://github.com/abhichaudharii/jiosaavn-python',
    download_url = 'https://github.com/abhichaudharii/jiosaavn-python/archive/refs/tags/v0.2.tar.gz',
    long_description_content_type="text/markdown",
    long_description=long_description,
    keywords = ['JioSaavn', 'JioSaavn-API', 'Saavn', 'Saavn API', 'download songs', 'lyrics', 'playlist'],
    install_requires=[
        'httpx'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
