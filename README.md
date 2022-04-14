# Turtle Flowers

I dug up some old code from when I first learnt to program.


(Extreme) Turtle Flowers based off of [Think Python 2 chapter 4](https://greenteapress.com/thinkpython2/thinkpython2.pdf). Which I still think is one of the best ways to introduce functions to a new programmer. After making the general flower function, younger me made the flowers have 300 petals and some pretty pictures came out of it.

I kinda like the look of the artifacts when you conver it from an SVG to a PNG so I've included both

<p align="center">
  <img src="./flowerDarkMode.svg#gh-dark-mode-only" width="400px">
  <img src="./flowerLightMode.svg#gh-light-mode-only" width="400px">
  <img src="./opacifiedFlowerDarkMode.png#gh-dark-mode-only" width="400px">
  <img src="./opacifiedFlowerLightMode.png#gh-light-mode-only" width="400px">
</p>

GitHub added an [easy way](https://github.blog/changelog/2021-11-24-specify-theme-context-for-images-in-markdown/) to query for darkmode/lightmode
```
<p align="center">
  <img src="./flower_dark.svg#gh-dark-mode-only" width="auto">
  <img src="./flower_light.svg#gh-light-mode-only" width="auto">
</p>
```

Or using markdown style links
```
![Light Mode Example](./opacifiedFlowerLightMode.png#gh-light-mode-only)
![Dark Mode Example](./opacifiedFlowerDarkMode.png#gh-dark-mode-only)
```

# Getting Started

Make sure you have pipenv installed with your local Python installation
```
pip install pipenv
```

Install packages
```
pipenv install
```

Run the main file
```
pipenv run start
```

### Sparse Flower

<p align="center">
  <img src="./sparseFlowerDarkMode.svg#gh-dark-mode-only" width="400px">
  <img src="./sparseFlowerLightMode.svg#gh-light-mode-only" width="400px">
  <img src="./opacifiedSparseFlowerDarkMode.png#gh-dark-mode-only" width="400px">
  <img src="./opacifiedSparseFlowerLightMode.png#gh-light-mode-only" width="400px">
</p>

### Dense flower

<p align="center">
  <img src="./denseFlowerDarkMode.svg#gh-dark-mode-only" width="400px">
  <img src="./denseFlowerLightMode.svg#gh-light-mode-only" width="400px">
  <img src="./opacifiedDenseFlowerDarkMode.png#gh-dark-mode-only" width="400px">
  <img src="./opacifiedDenseFlowerLightMode.png#gh-light-mode-only" width="400px">
</p>

