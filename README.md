# Expertkompetens 
## Project report - The Bee Hive counter that changed to a water well meter

###### tags: `planning` `examination`
---
**Table of Contents**
> - [IDEA]
> - [Objectives]
> - [Material]
> - [Environment setup]

### Idea
I started this project as a beehive counter planning to make some modifications on a already existing project called Easy Bee Counter found [here](https://github.com/hydronics2/2019-easy-bee-counter). Plan was to make it a little smaller then the original, use a [Pycom Lopy4](https://pycom.io/product/lopy4/) as main board  and  [LoRaWAN®](https://lora-alliance.org/about-lorawan/) as my communication protocol.

But sins I have problem getting all the required components in time I was forced to rethink and use what components I got at home. With that in mind I changed Idea to a measure water level in my old hand dug well.
The Idea is to use an Ultra Sonic Distance Sensor, HC-SR04. Make a box for it so I can Mount it just under the well lid and establish a “normal” water level distance.
After that I plan to trigger readings to keep track hon how much water I user in my well.
 I can then integrate these measures in my [Home Assistant](home-assistant.io) Controller to make automations based on water level ex. Stop watering my garden plants. 
I can also based on measures taken see how fast my well is refilled

### Objectives
•	Register an account on The Things Network
Figure out how to connect a Lopy4 to TTN Network and send measurements to the MQTT gateway
Recover the messages with Node-Red in on my local network and then send the values to my local Home Assistant installation.
Build some automations based on values received.

### Material

Explain all material that is needed. All sensors, where you bought them and their specifications. Please also provide pictures of what you have bought and what you are using.

- [ ] List of material
- [ ] What the different things (sensors, wires, controllers) do - short specifications
- [ ] Where you bought them and how much they cost
>| Component | Type |Price | Vendor |
>| --------- | ---------------- | ------------- |---------------------|
>| [Pycom Lopy4](https://pycom.io/product/lopy4/)   | Microcontroller| 480 kr   |[Digikey](https://www.digikey.se/products/sv?keywords=lopy4)
>|[Pycom Expansion Board 3](https://www.digikey.se/product-detail/en/pycom-ltd/UNIVERSAL-EXPANSION-BOARD/1871-1004-ND/7721842)|Expansion Board|183 kr|[Digikey](https://www.digikey.se/product-detail/en/pycom-ltd/UNIVERSAL-EXPANSION-BOARD/1871-1004-ND/7721842)
>| [Arduino Antenn för GSM och LoRa](https://www.kjell.com/se/produkter/el-verktyg/arduino/arduino-tillbehor/arduino-antenn-for-gsm-och-lora-p87287)| Antenna |99.90 kr | [Kjell och Company](https://www.kjell.com/)
>|[Ultrasonic Distance Sensor - HC-SR04](https://www.sparkfun.com/products/15569)|Sensor|39 kr|[Sparkfun](https://www.sparkfun.com/products/15569)|
>|[3st motstånd 1Ω](https://www.kjell.com/se/produkter/el-verktyg/elektronik/komponentsatser/playknowlogy-sortiment-med-resistorer-600-pack-p90646)|Resistor| 0.60 kr|[Kjell och Company](https://www.kjell.com/)|


### Environment setup
I have used *[VSCode](https://code.visualstudio.com/)* with the *[Pymakr](https://docs.pycom.io/gettingstarted/software/vscode/)* plugin and the *[Pycom Expansion Board 3](https://docs.pycom.io/datasheets/expansionboards/expansion3/)* to be able to connect and program the microcontroller. Also *[node.js](https://nodejs.org/en/)* is an requiment for the plugin to work.

### Putting everything together

How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?

- [ ] Circuit diagram (can be hand drawn)
- [ ] Electrical calculations
- [ ] Limitations of hardware depending on design choices.
- [ ] Discussion about a way forward - is it possible to scale?

### Platforms and infrastructure

Describe your choice of platform(s). You need to describe how the IoT-platform works, and also the reasoning and motivation about your choices. Have you developed your own platform, or used 

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or a free? Describe the different alternatives on going forward if you want to scale your idea.

- [ ] Describe platform in terms of functionality
- [ ] Explain and elaborate what made you choose this platform
- [ ] Provide a pricing discussion. What are the prices for different platforms, and what are the pros and cons of using a low-code platform vs. developing yourself?

### The code

Import core functions of your code here, and don't forget to explain what you have done. Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.


```python=
import this as that

def my_cool_function():
    print('not much here')

s.send(package)

# Explain your code!
```

### The physical network layer

How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.


- [ ] How often is the data sent? 
- [ ] Which wireless protocols did you use (WiFi, LoRa, etc ...)?
- [ ] Which transport protocols were used (MQTT, webhook, etc ...)
- [ ] Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.
- [ ] What alternatives did you evaluate?
- [ ] What are the design limitations of your choices?

### Visualisation and user interface

Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

- [ ] Provide visual examples on how the visualisation/UI looks. Pictures are needed.
- [ ] How often is data saved in the database. What are the design choices?
- [ ] Explain your choice of database. What kind of database. Motivate.
- [ ] Automation/triggers of the data.
- [ ] Alerting services. Are any used, what are the options and how are they in that case included.

### Finalizing the design

Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

- [ ] Show final results of the project
- [ ] Pictures
- [ ] *Video presentation

---
