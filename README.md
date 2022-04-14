# Turtle Flowers

Coming back to the original Python tutorial. [Think Python 2](https://greenteapress.com/thinkpython2/thinkpython2.pdf)

I kinda like the look of the artefacts when you conver it from an SVG to a PNG so I've included both

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

### Denser flower

<p align="center">
  <img src="./denseFlowerDarkMode.svg#gh-dark-mode-only" width="400px">
  <img src="./denseFlowerLightMode.svg#gh-light-mode-only" width="400px">
  <img src="./opacifiedDenseFlowerDarkMode.png#gh-dark-mode-only" width="400px">
  <img src="./opacifiedDenseFlowerLightMode.png#gh-light-mode-only" width="400px">
</p>