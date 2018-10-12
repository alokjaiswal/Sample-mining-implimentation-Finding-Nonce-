# Sample-mining-implimentation-Finding-Nonce

This is a simple implementation of mining(Similar to that of Bitcoin mining) written in python3.


<h2> What is Hash Function</h2>
 A hash function is a mathematical function that converts a numerical input value into another compressed numerical value. The   input to the hash function is of arbitrary length but output is always of fixed length.
 
 
 ![](/img/hash.png " Hash Function")
 
 
<h4>Features of Hash Function</h4>
 * Fixed Length Output(Hash Value).<br>
 * Efficiency of Operation.


<h2> What do mining actually mean</h2>

Mining is a process through which the verified transactions can be added to the Blockchain(public/private Ledger) in the form of blocks.

Here basically we find the string equivalent of the block and pass that string through a HASH function, Hash function used here is SHA256 (Secure Hash Function).



```
object = hashlib.sha256();
input = "Any input String";
object.update(input.encode());
input = object.hexdigest()
```



<h2>Requirements :</h2>
1. matplotlib<br>
2. hashlib

