
#!/bin/bash

a=0
mkdir delays
while [ $a -lt 40 ]; do
        cat glomo$a.stat | grep delay > delays/out$a.txt
        let a=a+1
done
