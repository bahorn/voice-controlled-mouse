# voice-controlled-mouse

I made the color of a gaming mouse I won at a hackathon controlled by a google
home, which I also won at a hackathon...

I wrote this for a Rival 110 and this is controlled by `rivalcfg` [1], so it
only supports mouse supported by that.

This was a speed project and was done in like 2 hours, so don't expect the best
code ever.

## Setup

* Import the configuration in `./DiaglogFlow` into DialogFlow.
* Run the server in `./server` (might require root, but you can get around this)
* Configure something like localtunnel.me [2] or ngrok [3] to expose your
instance to the world.
* Set the Fulfillment endpoint to your localtunnel.me endpoint.

## Usage 

* Say "Ok Google, talk to my test app" and you should hear "Welcome!".
* Now say "turn $COLOR" and the color will change!

## References

* [1] https://github.com/flozz/rivalcfg
* [2] https://localtunnel.github.io/www/
* [3] https://ngrok.com/
