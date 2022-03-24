<div id="top"></div>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#Introduction">Introduction</a>
    </li>
    <li>
      <a href="#Algorithms">Algorithms</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    
    <li><a href="#Assumptions and Limitation">Assumptions and Limitation</a></li>
    <li><a href="#Remaining Errors">Remaining Errors</a></li>
    <li><a href="#Software Required">Software Required</a></li>
    <li><a href="#Input">Input</a></li>
    <li><a href="#Output">Output</a></li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#Citation">Citation</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Introduction

ONT 9.4.1 flowcell is prone to generate indel (insertion/deletion) errors in homopolymer regions (single base repeating regions). This tool is used to correct these errors appearing in the core genes of bacteria. The corrected sequence has improved allelic call results for cgMLST analysis. In our testing dataset, the number of allelic call errors was reduced by 76.5%. 

This tool is built based on the concept of NanoMLST. However, NanoMLST can only be applied to the traditional 7-gene MLST. This tool enables such concept to be applied to cgMLST. We borrowed and modified a key function of NanoMLST’s script and supplied with our own algorithms/codes to make it work for cgMLST. 

Enterobase is a widely used database that offers cgMLST schemes for most bacteria. All available schemes can be downloaded from here. However, we found some of the alleles in these schemes are actually false alleles. Occasionally, Enterobase treats a sequencing error as a new allele and added into the scheme. Therefore, we have to use chewbbaca to remove these false alleles. If the Enterobase raw scheme is used as input, our correction approach would not work well. Detailed explanation for this please see the publication paper here. 

<p align="right">(<a href="#top">back to top</a>)</p>



### Algorithms

Detailed algorithms and logical flowchart for this correction approach are described in the publication paper.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Assumptions and Limitation

For our correction approach, we assume Enterobase cgMLST schemes contain complete alleles of the bacteria species. For the DNA sequence of an isolate, if there is no allele in the scheme matching it, we assume it is always a sequencing error. However, it is possible that such no-match results from a new allele, but we assume the possibility is extremely low. 

Although we use chewbbaca adapted scheme to perform homopolymer error correction, we cannot use the adapted scheme for Enterobase cgMLST allelic call, since current Enterobase allelic calling does not support customized scheme. Chewbbaca allelic caller generates a bit different allelic call result from Enterobase. Therefore, we use chewbbaca adapted scheme to perform homopolymer error correction but use Enterobase to perform cgMLST allelic call. The discrepancy between the two schemes leads to a “mis-correction” problem (details are described in the publication paper). However, our correction approach still improves the allelic call accuracy by 70% to 80% overall. 

### Remaining Errors

The remaining errors are mostly “mis-correction” and some uncorrected homopolymer errors, mismatches and insertions. Details are presented in the publication paper.

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Software Required

* Installation of chewbbaca and its dependencies
* Installation of BLAST Command Line

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Input
* A sample directory
     - Each sample must be single-contig DNA sequence
     - In FASTA files
* Directory to the chewbbaca adapted Enterobase Scheme

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Output
* Corrected sample FASTA files placed in the same directory

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
