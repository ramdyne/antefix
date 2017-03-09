# antefix
Showing airplanes near you.

This small project is stading on the shoulders of giants. To be able to see all the airplanes in your area using ADS-B, you
need to receive the data first. This is done using GNU Radio and the modes_rx.py script from the gr-air-modes project on
Github.

Once this is installed and working, make sure you start it using the -P switch, example:
    modes_rx -s <source> -P
Where -s is the SDR source device to use and -P tells modes_rx to become a server on a TCP socket which another script will
connect to.

To make a webpage able to receive ADS-B messages, the information from these messages is converted into SDS-1 messages which
the adsbclient.py script from the ADS-B-funhouse repository can convert into MQTT messages.
    ./adsbclient.py -m localhost -H localhost -bdb -r antefix

This starts a script that will connect to the modes_rx SDS-1 socket and will also connect to the MQTT broker (server) on
localhost and will send messages to the /adsb/antefix/json queue.

The Antefix repository also contains an example Mosquitto configuration file, that shoudl go into /etc/mosquitto/conf.d and
will start a MQTT server process on port 1883 and an MQTT over Websocket server process on port 1884. The latter port is used
by the Javascript in the HTML page to connect to and receive position updates which will be displayed as a line on a map.


This code is heavily indebted to:
- GNU Radio
- OpenLayers
- gr-air-modes
- Mosquitoo
- kanflo/ADS-B-funhouse

Enjoy!
