# Lloyd-Max-Quantizer
Numpy version of Lloyd-Max quantizer. <br />
Currently, support only for Lloyd-Max quantizer for the normal distribution. <br />

## The libraries:<br /> 
1. numpy <br />
2. matplot <br />
3. python3 <br />

## Usage: <br /> 
In case of quantization with 3-bit with 1,000 iterations. <br />
~~~shell
python3 main.py -b 3 -i 1000
~~~

<p align="center">
  <img width="50%" height="50%" src="https://github.com/FuengfusinNinnart/lloyd-max-quantizer/blob/master/results.png">
</p>

## Result of quantization with 3-bit (8 possibles) <br /> 
The top one shows the noise with the normal distribution (zero mean, unit variance). <br />
The middle one shows discrete quantization points of the input. <br />
The last one is the output or the quantized signal. <br />
