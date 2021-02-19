# Mini - Museum

A voice activated rotating museum. While the options are admittedly limited, this mini museum boasts two of the most famous paintings in the world, printed on the finest white printer paper. Simply ask to see one of the two paintings, either the Mona Lisa or The Scream. One raspberry pi, the client, will take input from a microphone, parse that into text and look for a related keyword. Once it recognizes a keyword related to either painting, it will send a request to the IP Address of a second Raspberry Pi, the server, that describes which painting was mentioned. The server pi will take that information and turn a planetary gear system either 90 degrees to the right or left to display one painting on the front window and then return.

![Demonstration of Functionality](https://media.giphy.com/media/RXd2CE7I8iJjKVYdhW/giphy.gif)

[Full Video](https://youtu.be/GzdikGhd4Ek)
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Client Python Libraries
  - [Speech Recognition](https://pypi.org/project/SpeechRecognition/) (Used to recognize speech on client)
    - [pyaudio](https://pypi.org/project/PyAudio/) (Dependency of Speech Recognition)
  - [requests](https://pypi.org/project/requests/) (To Send Information to the Server Pi)
- Server Python Libraries
  - [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) (To Communicate with Stepper Motor)
  - [Flask](https://pypi.org/project/Flask/) (To read requests from the Client Pi)
- Equipment 
  - [NEMA-17 Stepper Motor](https://www.adafruit.com/product/324) (Actuator)
    - Stepper Motor Driver
  - [Microphone](https://www.amazon.com/Lavalier-Microphone-Cardioid-Condenser-Computer/dp/B077VNGVL2/ref=sxts_sxwds-bia-wc-rsf1_0?cv_ct_cx=microphone&dchild=1&keywords=microphone&pd_rd_i=B077VNGVL2&pd_rd_r=fd342589-1272-420f-8874-4adbbfceab7e&pd_rd_w=C1Nme&pd_rd_wg=MZaFY&pf_rd_p=5168df84-062d-4bdf-8a6e-2680813bd42f&pf_rd_r=HCAYV23MEAB58FWD417P&psc=1&qid=1613717362&sr=1-1-7bf78e84-8ef2-4f13-9926-bee5153e81cb) (Sensor)
- [Raspberry Pi 4](https://www.google.com/search?q=raspberry+pi+4&sxsrf=ALeKk03vsMgGCu7PQVxu5BVM5yzeNxULQw:1613717510216&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjM7dqXrvXuAhWYWc0KHdwgBTIQ_AUoAXoECAUQAw&biw=958&bih=1087) x2
- Breadboard power supply (Accepts power from a 2.1 x 5.5 mm plug from a 12 V wall adapter. Emits 12 V, 5 V, and 3.3 V at the same time.) Custom PCB

![Components](C:/../component_box.svg)

### Installing

Simply download the files in this repository and upload the client.py code to one Raspberry Pi attached to the microphone, and the server.py code to another Raspberry Pi attached to the Stepper Motor.

### Setup Notes

In our design there was a lower box that housed the electronics, the upper box housed the gears and paintings.

## Authors

- **Sawyer Bailey Paccione** - *Client Code and Gear Design* - [Portfolio](http://sawyerbaileypaccione.tech/)
- **Olif Hordofa** - *Server Code and Box Design* 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
