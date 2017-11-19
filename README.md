# Golf-Shell

## Sample Programs
### Hello World
```
E'Hello World!
```

### Count Files
```
LlWl
```

Bash Equivalent:
```
ls -l | wc -l
```

### Reverse String
Takes an argument and prints it out in reverse order
```
E"$0"Go'.'BrTd'\n
```
Bash Equivalent:
```
echo "$0" | grep -o '.' | tail -r | tr -d '\n'
```

### Divisibility
Prints all numbers less than 1000 that are divisible by 5 and/or 7
```
R'1000'FG' [57] 'Cd':'f1
```

Bash Equivalent:
```
seq 1000 | factor | grep ' [57] ' | cut -d":" -f1
```

### BC Math
Takes an argument, n, and adds the first n numbers
```
R'$0'T'\n'':'Se's/:/+/g'e's/+/\n/$0'M
```

Bash Equivalent:
```
seq "$0" | tr '\n' ':' | sed -e 's/:/+/g' -e "s/+/\n/$0" | bc -l
```

### 2 + 2 = 5
Takes a mathmatical expression and if it is 2+2 outputs 5; otherwise outputs the correct answer
```
?[$0==2+2];E'5':E"$1"M;
```
Bash:
```
if [[ "$0" == "2+2" ]] ; then echo '2'; else echo "2+2" | bc -l; fi
``` 