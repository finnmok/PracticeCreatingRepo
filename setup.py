from setuptools import setup, find_packages

setup(
    name='PracticeCreatingRepo',
    version='1.0',
    author='Your Name',  # Add your name
    author_email='your.email@example.com',  # Add your email
    description='A short description of your package',
    url='https://github.com/finnmok/PracticeCreatingRepo',  # Replace with your GitHub URL
    packages=find_packages(),  # Automatically find packages in the project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your dependencies here, e.g., 'numpy>=1.18.0'
    ],
)
