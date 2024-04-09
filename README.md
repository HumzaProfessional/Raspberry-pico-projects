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

### Basic features

- GPIO

This stands for General purpose Input and Output and are pins that allow the Raspberry PI to interact with the phyiscal world. This allows it to send signals to other electronic conponents. 
When programming the PICO, the intepreter allocates each pin to a number. For example, GP0 is the first pin.

- Ground

Basically, the pin that directs the flow of electricity out, comepleting the circuit. If the GPIO are responsible for connections, then the ground pins are responsbile for returing those connections back to the PICO. 

In general circuit terminology, ground generally could refer to the literal ground or to the point the electity returns. This insight can be used as a refernce for Electircal devices such as power cables. However, generally speaking, the ground refers to a point in a cirucit that has 0 potential energy, thus allowing the energy to flow back safelty and complete the cirucit. When desigining on the PICO, just know that the ground is how the negative and positive temrinals are conecected.


## Projects


