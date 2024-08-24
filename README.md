<h1>HamsterKombat auto cipher</h1>
This program has 2 mods. In first mode you can write text in realtime and program convert it into morse code. In second mode you write cipher in terminal and program after 3sec starting write cipher in morse code<br>
<h2>Docs</h2>
<h3>First mode (real-time)</h3>
<code>python3 main.py</code><br>
Press letters in your keyboard and program will write this letter in morse code, clicking where you keep your mouse on screen<br>
Example: You press to "a" button, and program click 1 short tap and 1 long tap (.-) in real time
<h3>Second mode (auto)</h3>
<code>python3 main.py -c "code"</code><br>
Write today's cipher in terminal, keep your mouse over hamster and program write cipher in auto-mode. But dont leave your computer - hamster kombat often lags and cipher could be clear or some letters may disappear. If you see this, clear code (if some letters disappeared) and restart program. 
in the future there may be a function that will look for the "Get a prize" button, and if it is not there, it will repeat the script (this will can be configured using a flag)<br>
Example: You write in terminal after "-c" flag following: "cat". After start program will click - long, short, long, short; short, long; long; (-.-. .- -)
<h3>Second mode without writing cipher</h3>
You can get cipher from website using "-g" flag (Beta)<br>
<code>python3 main.py -g -c</code><br>
When program starts it try to get cipher from website "www.cybersport.ru/tags/games/shifr-hamster-kombat-khomiak-na-[today, but if time more than 22:00 - tomorrow]-avgusta" (it takes 5-10 sec.). After that program show cipher in terminal and ask if should continue. If you enter "y", "yes", "д", "1", or "true" (text written in capital letters is also taken into account), program start write cipher in default auto mode with found cipher. If you enter any others texts, program will be ended.
<h3>Config</h3>
This program has configuration file (config.py), and here you can tune settings<br>
DELAY_PER_LETTER - delay after every writed letters (default - 0.7sec)<br>
DELAY_PER_CLICK - delay per taps (write -, delay, write .) (default - 0.2sec)<br>
DELAY_IN_LONG_TAP - duration of long tap (press mouse, delay, release mouse) (default - 0.5sec)<br>
UNNECESSARY_DELAYS - enable or disable micro-delays that occur when modes are enabled or disabled (default - True)<br>
CONTINUE_IF_ERROR - continue program if program see incorrect letter in your text (only in auto mode, maybe to be in real time mode soon) (default - True)
<h3>Where it can using in computer</h3>
I tried it do in phones, but for now modules created in python cant clicking in phone (this is very difficult to do even in other languages)<br>
You can install LDPlayer or other andorid simulators on your computer, download on it telegram and play hamster kombat<br>
<h2>Updates</h2>
<h3>1.6 (Latest)</h3>
Flag "-g" in auto mode. This starting find cipher in website (now website is www.cybersport.ru). Not working if you writed any text after -c or use real-time mode (Beta)
<h3>1.5.1</h3>
"0" in real-time mode (Bug)
<h3>1.5</h3>
More logs (disabling/enabling mods, writed letters, etc.)<br>
"UNNECESSARY_DELAYS" and "CONTINUE IF ERROR" variables in config<br>
Micro-delays that occur when modes are enabled or disabled. You can enable or disable in config file<br>
Alerts appear if you writed an incorrect letter in auto mode. you can enable or disable exiting the program upon such a notification<br>
Numbers (0, 1, 2, 3..., 9) in all modes.
<h3>1.0</h3>
Appearance on GitHub