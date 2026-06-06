# Home Assistant - Snapmaker Camera Keepalive

A Home Assistant Add-on that keeps the Snapmaker U1 camera stream awake by periodically sending the Moonraker `camera.start_monitor` command.

This allows the Snapmaker camera to be used reliably with:

* Home Assistant
* SimplyPrint
* OctoEverywhere
* Browser viewing
* Other MJPEG-compatible camera integrations

---

# Features

* Automatically keeps the Snapmaker U1 camera awake
* Starts automatically when Home Assistant boots
* Supports Home Assistant OS
* Simple configuration through the Home Assistant Add-on UI
* No external server required

---

# Installation

## Add the Repository

In Home Assistant:

1. Navigate to **Settings → Apps**
2. Open the **App Store**
3. Click the **three-dot menu**
4. Select **Repositories**
5. Add:

```text
https://github.com/evansmike881/Home-Assistant---Snapmaker-Camera-Keepalive
```

6. Click **Add**
7. Refresh the App Store

You should now see:

**Snapmaker Camera Keepalive**

Install the add-on.

---

# Obtaining Your Snapmaker Token

The add-on requires a Moonraker authentication token.

## Step 1 - Enable Moonraker

On your Snapmaker U1:

1. Open the touchscreen
2. Navigate to:

```text
Settings → Network
```

3. Make a note of the printer IP address

Example:

```text
192.168.1.100
```

---

## Step 2 - Open Moonraker

From a browser visit:

```text
http://PRINTER_IP
```

Example:

```text
http://192.168.1.100
```

---

## Step 3 - Generate a Token

Follow the SimplyPrint guide:

https://help.simplyprint.io/en/article/how-to-enable-webcam-streaming-on-the-snapmaker-u1-ia9os7/

Locate the Moonraker token and copy it.

It will look similar to:

```text
IROZ3VMN4Z3XYK33ST4XADSDDTBO76RK
```

---

# Add-on Configuration

Open the add-on and enter:

```yaml
printer_ip: "192.168.1.100"
token: "YOUR_TOKEN_HERE"
```

Example:

```yaml
printer_ip: "192.168.4.160"
token: "IROZ3VMN4Z3XYK33ST4XADSDDTBO76RK"
```

Save the configuration and start the add-on.

---

# Verifying Operation

Open the add-on logs.

You should see:

```text
[12:34:56] OK
[12:35:06] OK
[12:35:16] OK
```

This confirms the keepalive messages are being sent successfully.

---

# Adding the Camera to Home Assistant

This add-on keeps the Snapmaker camera awake but does not create a camera entity.

To view the camera in Home Assistant, add a Generic Camera.

## Method 1 - UI

Navigate to:

```text
Settings → Devices & Services → Add Integration
```

Search for:

```text
Generic Camera
```

---

## Method 2 - YAML

Add the following to your `configuration.yaml`:

```yaml
camera:
  - platform: generic
    name: Snapmaker Camera
    still_image_url: "http://PRINTER_IP/webcam/?action=snapshot"
    stream_source: "http://PRINTER_IP/webcam/?action=stream"
```

Example:

```yaml
camera:
  - platform: generic
    name: Snapmaker Camera
    still_image_url: "http://192.168.4.160/webcam/?action=snapshot"
    stream_source: "http://192.168.4.160/webcam/?action=stream"
```

Restart Home Assistant after saving.

---

# Using the Camera on a Dashboard

Add a Picture Entity card:

```yaml
type: picture-entity
entity: camera.snapmaker_camera
camera_view: live
show_name: true
show_state: false
```

---

# Troubleshooting

## Camera image not updating

Verify the add-on is running.

Check the logs for:

```text
OK
```

messages every 10 seconds.

---

## Cannot connect to printer

Verify:

* Printer IP address is correct
* Printer is powered on
* Home Assistant can reach the printer
* Token is valid

---

## Token no longer works

Generate a new token and update the add-on configuration.

---

# Credits

Based on the Snapmaker U1 webcam keepalive method documented by SimplyPrint.

https://help.simplyprint.io/en/article/how-to-enable-webcam-streaming-on-the-snapmaker-u1-ia9os7/

---

# License

MIT License
