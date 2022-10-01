README
######


**NAME**

**GOZERBOT** - python3 irc bot.


**SYNOPSIS**

``gozerbot <cmd> [key=value] [key==value]``


**DESCRIPTION**

**GOZERBOT** is a solid, non hackable, and is intended to be programmable in a
static, only code, no popen, fixed imports and no reading modules from a
directory, to not have a directory to read modules from to add
commands to the bot but include the own programmed modules directly into the
python code, so only trusted code (your own written code) is included and
runable. Reading random code from a directory is what gets avoided. As
experience tells os.popen and __import__, importlib are also avoided, direct
imports in the code is what is used, source is :ref:`here <source>`.

With **GOZERBOT** your can have the commands of a irc bot available on your cli.
Instead of having to join a irc channel and give commands to your bot, you
can run these commands on your shell.

**GOZERBOT** stores it's data on disk where objects are time versioned and the
last version saved on disk is served to the user layer. Files are JSON dumps
that are read-only so thus should provide (disk) persistence. Paths carry the
type in the path name what makes reconstruction from filename easier then
reading type from the object.

**INSTALL**

``sudo pip3 install gozerbot --upgrade --force-reinstall``


**CONFIGURATION**

**irc**

``gozerbot cfg server=<server> channel=<channel> nick=<nick>``
  
``(*) default channel/server is #gozerbot on localhost``

**sasl**

``gozerbot pwd <nickservnick> <nickservpass>``
``gozerbot cfg password=<outputfrompwd>``

**users**

``gozerbot met <userhost>``

**rss**

``gozerbot rss <url>``

**24/7**

``adduser gozerbot``
``mkdir /home/gozerbot/.gozerbot``
``cp /usr/local/share/gozerbot/gozerbot.service /etc/systemd/system``
``systemctl enable gozerbot --now``

cfg,cmd,dlt,dne,dpl,flt,fnd,ftc,log,met,mre,nme,pwd,rem,rss,sts,tdo,thr,upt

**COMMANDS**

 ::

  cfg - configuration
  cmd - commands
  dlt - remove a user
  dne - flag todo
  dpl - display items
  flt - list of instances registered to the bus
  fnd - find objects 
  ftc - runs a fetching batch
  log - log some text
  met - add a user
  mre - displays cached output, channel wise.
  nme - feed name
  pwd - combines nickserv name/password into a sasl password
  rem - removes a rss feed
  rss - add a feed
  sts - status
  tdo - todo
  thr - show the running threads
  upt - uptime

**PROGRAMMING**

The ``gozerbot`` package provides an Object class, that mimics a dict while using
attribute access and provides a save/load to/from json files on disk.
Objects can be searched with database functions and uses read-only files
to improve persistence and a type in filename for reconstruction. Methods are
factored out into functions to have a clean namespace to read JSON data into.

basic usage is this::

>>> import gozerbot
>>> o = gozerbot.Object()
>>> o.key = "value"
>>> o.key
>>> 'value'

Objects try to mimic a dictionary while trying to be an object with normal
attribute access as well. hidden methods are provided, the methods are
factored out into functions like get, items, keys, register, set, update
and values.

load/save from/to disk::

>>> from gozerbot import Object, load, save
>>> o = Object()
>>> o.key = "value"
>>> p = save(o)
>>> obj = Object()
>>> load(obj, p)
>>> obj.key
>>> 'value'

great for giving objects peristence by having their state stored in files::

 >>> from gozerbot import Object, save
 >>> o = Object()
 >>> save(o)
 'gozerbot.obj.Object/2021-08-31/15:31:05.717063'


**FILES**


 | ``/usr/local/share/doc/gozerbot/*``
 | ``/usr/local/share/gozerbot/gozerbot.service``


**AUTHOR**

Bart Thate 

**COPYRIGHT**

**GOZERBOT** is placed in the Public Domain. No Copyright, No License.
