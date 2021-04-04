# Lloyd-Max Quantizer:
This is a Python implementation of Lloyd-Max Quantizer. Currently, this repository only supports for quantization of the Gaussian distribution signal.

## Requirements:
1. numpy
2. matplotlib
3. scipy


## Usage:
To quantization with 8-bit for 1,000,000 iterations, please use a command as follows:
~~~shell
python3 main.py -b 8 -i 1000000
~~~

## Result of quantization with 8-bit:
<p align="center">
  <img width="50%" height="50%" src="https://github.com/stillame96/lloyd-max-quantizer/blob/master/outputs/results.png">

From the figure, the upper-figure shows an input signal or a Gaussian noise with zero mean and a unit variance. The middle-figure shows optimized quantization locations given the input signal. The bottom-figure shows a result signal or an quantized Gaussian noise. <br>

From this implementation, mean square error of 8-bit quantization of Gaussian noise is 3.595888887954022e-05.

## License:
MIT license.
