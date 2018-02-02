## Wifi Geolocation Without GPS

Scans the nearby wifi networks and locates the board using [Google Maps Geolocation API](https://developers.google.com/maps/documentation/geolocation/intro). Before using create a `settings.json` file with you wifi credentials and [Google Maps API key](https://developers.google.com/maps/documentation/geolocation/get-api-key). You can use `settings.json.dist` as a template.

```
$ cp firmware/settings.json.dist settings/settings.json
$ nano -w settings/settings.json
```

When done upload the everything to the board and enter REPL. You might need to reset the board after entering REPL.

```
$ make sync
$ make repl
```
