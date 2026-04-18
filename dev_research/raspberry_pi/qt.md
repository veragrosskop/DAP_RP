# Setting up Qt

Since we set up the 3.5 inch display using a custom driver we must interact
with the framebuffers directly when writing qt code. Thankfully Qt gives us 
some environment variables to do so. Prior to executing the python qt 
application we must set some environment variables in our shell:

> [!NOTE] 
> All of this is documented here: https://doc.qt.io/qt-6/embedded-linux.html#linuxfb

```bash
export QT_QPA_PLATFORM=linuxfb:fb=/dev/fb1
```

this tells qt to use `linuxfb` as the display platform and to write to the `/dev/fb1`
filebuffer.

> [!NOTE]
> I've already set up this environment variable in the `~/.bashrc` which is sourced whenever
> linux is started. This is just for reference if something were to ever go wrong


## Running your python project

Once that is all done, you can run your python project directly, and you should see the 
framebuffer update with your application!

```bash
python3 <your_file.py>
```