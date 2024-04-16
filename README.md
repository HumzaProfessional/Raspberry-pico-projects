# Raspberry-pico-projects

## Table of Contents
- [What is a Raspnerry pi pico?](#What-is-a-Raspnerry-pi-pico?)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Links](#links)
  - [Installation](#installation) 
- [Understanding](#understanding)
- [Projects](#projects)
- [Contributing](#contributing)


## What is a Raspberry pi pico? 
The files in this repository are for simple projects for the Raspberry Pi Pico. A cheaper and smaller version of the Raspberry PI. It is a good alternative for the tradional Raspberry Pi to learn python, hardware/software interaction, and simple electronics. The PICO version is still very versatile and can be used to make many sorts of projects!

## Getting Started

### Prerequisites

In order to do these projects, make sure you have:
- Pico Display unit
- Raspberry Pi usb cable(most likely comes with it when you buy the PICO), 
- a micropython intrepter
- electronic componenets (wires, diodes, and a breadboard(isn't necessary but will be useful)). 

#### Links
Raspberry pi pico
https://www.amazon.com/Pico-Raspberry-Pre-Soldered-Dual-core-Processor/dp/B0BK9W4H2Q/ref=sr_1_5?keywords=raspberry+pi+pico&qid=1693333709&sr=8-5

Pico display
https://shop.pimoroni.com/products/pico-display-pack?variant=32368664215635

Thonny IDE
https://thonny.org

### Installation

Thonny is a useful and simple python intrepter useful for programming PICOs. It is also reccommended by the developers themselves. 

https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2 - The offical guide explains the steps straightforwardly.

In summary:

- Install thonny on your operating system, the website has the appropriate inscrutionss given the OS.
- Launch the IDE and find and hold the boostel button on your PICO - the tiny button. Then plug in your PICO to your computer.
- On the bottom right corner of the IDE window it should show your python version. Click it and it should show "MicroPython (Raspberry PICO)".
- Click on it and it should ask to install the firmware. Onec done, you can start programming the PICO!

## Understanding

![Raspberry Pico Diagram](https://github.com/HumzaProfessional/Raspberry-pico-projects/blob/main/Pico-R3-Pinout.png)

This showcases the layout of the PICO. Each of the numbers are different pins,and the words next to them are the their usage. There are many different functionalities on the PICO, showing how versatile it is!

### Features

#### Basic features

- GPIO

This stands for General purpose Input and Output and are pins that allow the Raspberry PI to interact with the phyiscal world. This allows it to send signals to other electronic conponents. 
When programming the PICO, the intepreter allocates each pin to a number. For example, GP0 is the first pin. If you want send a signal to to a device that is connected to GP0. You would have to specifty pin 0 as where you want send the signal out.

- GND (Ground)

Basically, the pin that directs the flow of electricity out, comepleting the circuit. If the GPIO are responsible for connections, then the ground pins are responsbile for returning those connections back to the PICO. 

In general circuit terminology, ground generally could refer to the literal ground or to the point the eletricity returns. This insight can be used as a reference point for electrical devices such as power cables. However, generally speaking, the ground refers to a point in a circuit that has 0 potential energy, thus allowing the energy to flow back safely and complete the circuit. When desigining on the PICO, just know that the ground is how the negative and positive terminals are connected.

#### Advanced features

### Components

- Wires
  - Male to female
  - Male to Male
  - Female to Female

- Resistors

- Breadboard
  
- LED

![LED](https://github.com/HumzaProfessional/Raspberry-pico-projects.github.io/blob/main/annotatedLEDSA.png)
  

## Projects

### Project 1 - Led on and off


This basic project will allow you to make an led turn off and on, a blinking light. You need to connected the negative terminal of the led to a GPIO and the postive to ground, make sure a reisisotr is connected to the negative terminal. Refer to the diagram to set this up correctly. 



``` python
from machine import Pin  # If unaware of python, machine is a library that used by the raspberry pi micropython language to allow functions such as pins usage
import time              # the time is needed to allows the led to be able behave the we want it to.
```
This is the basic setup of all program we will be writing, mention a library and call the functions we want to use. In this case the funcitons Pin and time. These two will be common.


``` python
led = Pin(25, Pin.OUT) # 25 is the pin the led's negative terminal is connnected to. Pin.OUT is any ground pin.

led.on()            # Led turns on for the first time
time.sleep(.25)     # Led stay on for .25 seconds

led.off()          # Led turns off
time.sleep(.25)    # Led stays off for .25 seconds
```
This the central part of the program where the blink of the led occurs.

The first statement defines how the led is connected to the PICO. In this case, is is powered from pin 25 and returns back to the PICO through GND.

The ```led.on()``` informs the pico to send a signal to the led, turning it on. The ```time.sleep(.25)``` make sures it stays on for .25 seconds. It sleep function ensured the next signal happens at a dealy of .25 seconds.
The ```led.of()``` is similar, turn off the signal and do so for time of .25 seconds. Give this basic setup, the last sleep function doen't mean much, since nothing follows the off signal delay.

However, we can add more on and off processeses and change the delays to get some interesting blinking behavior...

```python

from machine import Pin
import time

led = Pin(25, Pin.OUT)

led.on()
time.sleep(.25)
led.off()
time.sleep(.25) 
led.on()
time.sleep(.20)
led.off()
time.sleep(.20)
led.off
time.sleep(.15)
led.on
time.sleep(.15)
led.off()
time.sleep(.10)
led.on
time.sleep(.5)
led.off
time.sleep(.5)
led.on
time.sleep(.1)
```

## Contributing

https://projects.raspberrypi.org/en/#hardware

