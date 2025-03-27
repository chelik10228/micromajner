import time;
import sys;
sys.set_int_max_str_digits(0);

money = 1;

while (True):
    money *= 2.;
    print("\033[92m", money, "\033[0m");
    time.sleep(1/20);
