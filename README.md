# polyglots.dk

The website for Copenhagen Tech Polyglot Meetup. Hosted online at http://www.polyglots.dk/

## Developing

If you checkout the site and want to preview your changes before
creating a pull request you can run the following make target to start
a small python webserver to serve the site locally.

    make start-webserver

## Hosting the site

On your host run the following:

    git clone https://github.com/mads379/polyglots.dk.git
    cd polyglots.dk
    make start-hook

This will clone site and start a small python web-server that listens for
Github webhook events.
