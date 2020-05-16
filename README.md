<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/we-based/visuaspy">
    <img src="res/computer.png" alt="Logo" width="130" height="130">
  </a>
  <h1 align="center">microsoft-stream-checker</h1>

  <p align="center">
    Mama didn't raise no lesson skipper.
  </p>
</p>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [How it works](#how-it-works)
- [Getting Started](#getting-started)
  - [Updates](#updates)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About The Project

![Product Name Screen Shot][screenshot]

**I am tired of having to check Microsoft Stream to watch new university lessons.** I said it. It is slow and painful. This script helps you by doing exactly that.

### How it works

We're using the Selenium library to log in to Microsoft Stream, fetch the videos list and save them to a JSON. If there's something new, it notifies you via `telegram-python-api`.

<!-- GETTING STARTED -->

## Getting Started

You can just clone this repository, install the requirements by running

```
$ pip3 install -r requirements.txt
```

and then start the bot.

### Updates

Pull this repository for updates.

<!-- USAGE EXAMPLES -->

## Usage

First, you have to create a bot using the BotFather in Telegram (`@botfather`). Then, with the API key andyour uni login, just set the 3 environment variables we need:

```
$ export UNIPR_EMAIL="nome.cognome@studenti.unipr.it"
$ export UNIPR_PASSWORD="notmyrealpassword"
$ export TELEGRAM_TOKEN="yourtelegramtoken"
```

You should put these in your `.bash_profile` to avoid losing them.
Now, you need to know your telegram chat ID. Start the bot with
`python3 o-checker.py -t`
and open the telegram chat with your personal bot. Start it with `/start` and your console will print your chat ID.
Go to Microsoft Stream and copy your professor's channel URL. It will be something like `https://web.microsoftstream.com/user/92ac7988-aefb-4b2a-9e1c-2807f44c3036`
You're now ready to go: just run

```
python3 o-checker.py -u [professorlink] -c chatid
```

and the bot will check the videos.
Set it up as a cronjob and you will be notified as soon as a video gets uploaded. Use

```
0 * * * * cd /home/simone/microsoft-stream-checker && python3 o-checker.py -u [professorlink] -c chatid >/dev/null 2>&1
```

to check every hour.

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

Distributed under the GPL License. See `LICENSE` for more information.

<div>Icon made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/"             title="Flaticon">www.flaticon.com</a></div>

<!-- CONTACT -->

## Contact

[WEBased](https://webased.it)

Project Link: [https://github.com/montali/microsoft-stream-checker](https://github.com/montali/microsoft-stream-checker)

[screenshot]: res/screenshot.png "Screenshot"
[logo]: res/computer.png
