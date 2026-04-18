# Setting up the 3.5 inch display from scratch

> [!NOTE]
> This is a summary of the following guide: https://techlogics.net/setting-up-a-3-5-inch-ili9486-touchscreen-lcd-on-raspberry-pi-zero-2-w-full-working-guide/

This guide assumes you already have the raspberry pi set up via ssh and can successfully ssh into it.

## Setting up the driver

Once you've set up your raspberry pi, we will now install
the drivers for the display

> [!NOTE]
> Once this is done the built-in hdmi will no longer work!


```bash
cd ~
sudo rm -rf LCD-show
git clone https://github.com/goodtft/LCD-show.git
cd LCD-show
chmod +x LCD35-show
sudo ./LCD35-show
```

Let's run through those step by step:

These commands go into the home directory, remove an existing directory called LCD-show, then
clone it from source again after which we go into the folder

```bash
cd ~
sudo rm -rf LCD-show
git clone https://github.com/goodtft/LCD-show.git
cd LCD-show
```

This command allows the `LCD-show/LCD35-show` to be executed by linux

```bash
chmod +x LCD35-show
```

Finally, we execute the `LCD-show/LCD35-show` script using root permissions (admin). This will
set up the driver and finally reboot the raspberry pi

```bash
sudo ./LCD35-show
```

# Permissions

To give the user permissions to write to the framebuffers, use this snippet:

```bash
sudo usermod -a -G video pizero
```

where `pizero` is the username.

That's it!