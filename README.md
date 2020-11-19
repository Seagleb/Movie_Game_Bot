<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** Seagleb, Movie_Game_Bot, SeagleBilly, seagleb@gmail.com
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Seagleb/Movie_Game_Bot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">YOUR_TITLE</h3>

  <p align="center">
    YOUR_SHORT_DESCRIPTION
    <br />
    <a href="https://github.com/Seagleb/Movie_Game_Bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Seagleb/Movie_Game_Bot">View Demo</a>
    ·
    <a href="https://github.com/Seagleb/Movie_Game_Bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/Seagleb/Movie_Game_Bot/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

Inspiration for this project came from deployments in the Navy.  It was a fun game we would play where we would just scramble up some letters and write the blanks for others on watch to unscramble.

Example:
eth bgi eoiklbws
---/---/--------
Answer:
The Big Lebowski

I also wanted to practice Web Scraping and needed a platform to interact with the game and figured practice with chat bots wouldn't hurt either.
This game can be played with friends in a discord server you are an administrator of.

### Built With

* [Python]()
    * [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    * [Discord API](https://discordpy.readthedocs.io/en/latest/api.html)
* [Discord](https://discord.com/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Beautiful Soup
```sh
pip install bs4
```
* Discord API
```sh
pip install discord.py
```


### Installation

1. Clone the repo
```sh
git clone https://github.com/Seagleb/Movie_Game_Bot.git
```
2. Install Python packages
3. Follow [these](https://realpython.com/how-to-make-a-discord-bot-python/) instructions to create the discord bot to retrieve a token
4. Edit the .env to include the discord bot token and server name



<!-- USAGE EXAMPLES -->
## Usage

If you would like to update the movie list you can run scraper.py which collects the first page's worth of the top movies from every year between 1980-2019 which is editable from scraper.py

Run bot.py to get started

Current commands are:
```sh
!newgame
!points
!giveup
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Seagleb/Movie_Game_Bot/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

William Seagle - [@SeagleBilly](https://twitter.com/SeagleBilly) - seagleb@gmail.com

Project Link: [https://github.com/Seagleb/Movie_Game_Bot](https://github.com/Seagleb/Movie_Game_Bot)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [README Template](https://github.com/othneildrew/Best-README-Template)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Seagleb/repo.svg?style=flat-square
[contributors-url]: https://github.com/Seagleb/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Seagleb/repo.svg?style=flat-square
[forks-url]: https://github.com/Seagleb/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/Seagleb/repo.svg?style=flat-square
[stars-url]: https://github.com/Seagleb/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/Seagleb/repo.svg?style=flat-square
[issues-url]: https://github.com/Seagleb/repo/issues
[license-shield]: https://img.shields.io/github/license/Seagleb/repo.svg?style=flat-square
[license-url]: https://github.com/Seagleb/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/Seagleb
[product-screenshot]: images/screenshot.png