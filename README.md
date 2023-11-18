# F1-Lights-with-Raspberry-Pi-and-AI
![F1 Lights](https://github.com/HariAsher/F1-Lights-with-Raspberry-Pi-and-AI/assets/83194217/a57d67fa-ea6a-40b7-bc3a-584c3b11ca36)

## Overview

This project showcases an embedded system powered by a Raspberry Pi 4B, designed to control Formula F1-style lights with the assistance of AI. The hardware setup includes five LEDs, a buzzer, jumper wires, and resistors.

Chat GPT 4 played a crucial role in this project by generating the code and crafting the circuit diagram.

Upon running the program, users are presented with options to commence a race, initiate a formation lap, or exit the application. To start a race, press 'r,' to initiate a formation lap, press 'f,' and to quit, press 'q.'

## Table of Contents

- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Chat GPT Prompt](#chat-gpt-prompt)
  - [Hardware Setup](#hardware-setup)
    - [How do GPIO Pins Work](#how-do-gpio-pins-work)
    - [How Does a Breadboard Work](#how-does-a-breadboard-work)
  - [Software Setup](#software-setup)
- [Usage](#usage)
- [Circuit Diagram](#circuit-diagram)

## Getting Started

### Requirements

- 1 Raspberry Pi
- 1 Breadboard
- 5 Red Leds
- 5 220 ohm Resistors
- 1 Buzzer
- Several Jumper Wires

### Chat GPT Prompt

This project was initiated by using Chat GPT 4. The following prompt was used to kickstart the project:

Assist me in setting up a project using a Raspberry Pi 4B, focused on creating a Formula One-style lighting system. I need code that can prompt the user to choose between initiating the race's formation lap or exiting the project. Additionally, there's a buzzer integrated into the setup, which should sound whenever a light is activated. Please provide the necessary code for this project and a corresponding circuit diagram.


### Hardware Setup

1. Assemble the hardware components according to the provided circuit diagram (see [Circuit Diagram](#circuit-diagram)).
2. Ensure all connections are secure.
3. Connect your Raspberry Pi 4B to the circuit based on the pin configuration mentioned in the code.

#### How do GPIO Pins Work

GPIO (General-Purpose Input/Output) pins on the Raspberry Pi are versatile pins that can be configured as either inputs or outputs. They are used to connect external hardware components to the Raspberry Pi for input and output operations. When configured as outputs, GPIO pins can send electrical signals (high or low voltage) to control components like LEDs, motors, and buzzers. When configured as inputs, they can read the state of sensors, switches, or buttons.

For this project, GPIO pins are used to control the LEDs and the buzzer, providing signals to turn them on and off.

#### How Does a Breadboard Work

Watch this video: https://www.youtube.com/watch?v=6WReFkfrUIk&ab_channel=ScienceBuddies

A breadboard is a crucial tool in electronics prototyping that allows you to create temporary connections between electronic components without soldering. It consists of a grid of interconnected metal strips and holes. Each row of holes and the corresponding metal strip is connected, while rows are isolated from each other. 

To use a breadboard, you insert components like resistors, LEDs, and wires into its holes. The interconnected rows allow you to create circuits by connecting components without the need for soldering. This makes it easy to prototype and experiment with different circuit configurations.

In this project, a breadboard is used to build the circuit, providing a platform for connecting and organizing the electronic components.

### Software Setup

Clone this repository to your Raspberry Pi.
Make sure you've got python installed.

## Usage
When you run the program, it will prompt you with the following options:

To start a race, press 'r.'
To start a formation lap, press 'f.'
To quit the program, press 'q.'
Choose the desired option to control the Formula F1 lights.

## Circuit Diagram

![F1 Light Circuit](https://github.com/HariAsher/F1-Lights-with-Raspberry-Pi-and-AI/assets/83194217/0d5e9a73-20ff-4ae1-aa2e-8668bcfa38f9)

The circuit diagram illustrates the connections between the Raspberry Pi and the hardware components.
