
#!/bin/bash
a=0
FILES=40
mkdir p1output
while [ $a -lt 40 ]; do
        ./glomosim config$a.in
        mv glomo.stat glomo$a.stat
        cp glomo$a.stat p1output
        let a=a+1
done
