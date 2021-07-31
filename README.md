<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
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
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JawaBaliIBM/Gaia">
    <img src="https://github.com/JawaBaliIBM/Gaia/raw/master/web-extension/images/icon96.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Gaia - Gaia: Your Environment News Curator <br /> Call for Code 2021</h3>

  <p align="center">
    Gaia: a chrome extension that curates environmental news of a company
    <br />
    <a href="https://github.com/JawaBaliIBM/Gaia"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://youtu.be/rSZHTn9X-GY">View Demo on YouTube</a>
    ·
    <a href="https://github.com/JawaBaliIBM/Gaia/issues">Report Bug</a>
    ·
    <a href="https://github.com/JawaBaliIBM/Gaia/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#data-source">Data Source</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#standalone-scripts">Standalone Scripts</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#infrastructure">Infrastructure</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Who We Are</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Gaia Extension][product-screenshot]](https://github.com/JawaBaliIBM/Gaia/raw/master/images/product.jpg)

Gaia is a chrome extension which curates environment news of a brand. After installing the extension, you can highlight a word containing the company name or a brand name and then you get news affiliated with it.

They can keep you updated on the environmental impact of a certain brand. Gaia helps you become a wiser consumer because you can keep tabs on these brands' impact. Gaia supports consumers, specifically internet users, to be more aware of these companies’ environmental issues. 


### Built With

* [IBM Cloud Natural Language Understanding](https://cloud.ibm.com/catalog/services/natural-language-understanding)
* [IBM Cloud Foundry](https://cloud.ibm.com/cloudfoundry/overview)
* [IBM Cloudant](https://www.ibm.com/cloud/cloudant)
* [IBM Function](https://www.ibm.com/cloud/functions)
* [IBM Object Storage](https://www.ibm.com/cloud/object-storage)

### Data Source

* [The Guardian News API](https://open-platform.theguardian.com/)


<!-- GETTING STARTED -->
## Getting Started

To use the production version of Gaia, install Gaia Chrome Extension to use it directly on your Chrome browser.

Get this extension for free: []()

To get a local copy up and running follow these simple steps.

### Prerequisites

Gaia runs on Javascript with Chrome Extensions API and Python with Django. To run Gaia extension on your local machine, you need to:

#### Run Gaia Web Extension on Your Local
1. After cloning the repository, open chrome browser.
2. At the top right, click ![More](https://github.com/JawaBaliIBM/Gaia/raw/master/images/more_icon.PNG) and then More tools and then Extensions.
3. Make sure your Developer turned on.
![Developer Mode](https://github.com/JawaBaliIBM/Gaia/raw/master/images/developer_on.PNG).
4. Click Load Unpacked Button
![Developer Mode](https://github.com/JawaBaliIBM/Gaia/raw/master/images/load_unpackaged.PNG).
5. Choose `web-extension` on ![cloned repository](https://github.com/JawaBaliIBM/Gaia/tree/master/web-extension).
6. You have web extension run locally on your browser.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/JawaBaliIBM/Gaia.git
   ```
2. To run the API, run the `server` directory with Docker Compose
   ```sh
   docker-compose up
   ```
3. To run the extension, run the #### frontend


### Standalone Scripts

Several standalone scripts are available for news scraping and model training purposes.
1. [guardian_scrapping_script.py](https://github.com/JawaBaliIBM/Gaia/blob/master/scripts/guardian_scrapping_script.py) - A script to scrape The Guardian news as a JSON file. The JSON format follows the data returned by [The Guardian News API](https://open-platform.theguardian.com/).
2. [file_uploader.py](https://github.com/JawaBaliIBM/Gaia/blob/master/scripts/file_uploader.py) - A helper script to upload file objects to IBM Cloud Object Storage.
3. [nlp/train_sentiment.py](https://github.com/JawaBaliIBM/Gaia/blob/master/scripts/nlp/train_sentiment.py) - A script to train a custom sentiment model in IBM Cloud NLU. More guide on [IBM Cloud NLU Custom Sentiment Model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-custom-sentiment).

To run the scripts with Python, you can follow the steps below:

1. Create a Python virtual environment folder, and activate it
    ```sh
        python -m venv env
        source env/bin/activate
    ```
2. Install the required Python packages defined in requirements.txt
   ```sh
        pip install -r requirements.txt
   ```
3. Run the necessary scripts
   ```sh
        python <file_name.py>
   ```

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<!-- INFRASTRUCTURE -->
## Infrastructure
  <a href="https://github.com/JawaBaliIBM/Gaia">
    <img src="https://github.com/JawaBaliIBM/Gaia/raw/master/images/infrastructure.jpeg" alt="Logo" width="80" height="80">
  </a>


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/JawaBaliIBM/Gaia/issues) for a list of proposed features (and known issues).



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

Distributed under the Apache 2.0 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Who We Are

#### JavaBali Team

Fellita Candini - [canfelli25](https://github.com/canfelli25) - fellitacandini@gmail.com

May Iffah - [mayiffah](https://github.com/mayiffah) - rmayiffah@gmail.com

Nur Intan Alatas - [Nurintaaan](https://github.com/Nurintaaan) - intannnalatas@gmail.com

Valentina Artari - [valentinakania](https://github.com/valentinakania) - kaniaprameswara5@gmail.com

Project Link: [Gaia](https://github.com/JawaBaliIBM/Gaia)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/JawaBaliIBM/Gaia.svg?style=for-the-badge
[contributors-url]: https://github.com/JawaBaliIBM/Gaia.svg/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JawaBaliIBM/Gaia.svg?style=for-the-badge
[forks-url]: https://github.com/JawaBaliIBM/Gaia.svg/network/members
[stars-shield]: https://img.shields.io/github/stars/JawaBaliIBM/Gaia.svg?style=for-the-badge
[stars-url]: https://github.com/JawaBaliIBM/Gaia.svg/stargazers
[issues-shield]: https://img.shields.io/github/issues/JawaBaliIBM/Gaia.svg?style=for-the-badge
[issues-url]: https://github.com/JawaBaliIBM/Gaia.svg/issues
[license-shield]: https://img.shields.io/github/license/JawaBaliIBM/Gaia.svg?style=for-the-badge
[license-url]: https://github.com/JawaBaliIBM/Gaia.svg/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
