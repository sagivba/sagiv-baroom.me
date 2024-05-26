---
layout: post
title:  "atop in nutshell"
author: "Sagiv Barhoom"
date:   2024-05-26
categories: Linux 
background: '/img/posts/be-linux.jpg.jpg'
---

# atop - cli for system and process monitoring
## overview
The atop command in Linux is used for system and process monitoring. 
It provides a detailed overview of system performance, including CPU, memory, disk, and network usage. 
Common usage involves running atop in the terminal to get a real-time view of resource utilization.
this can help in diagnosing performance issues and understanding system behavior over time. 
It can also log this information for historical analysis.

## common usage
1. Basic Usage `atop` - This command will start atop and display real-time system performance metrics.

2. Write log: `atop -w /var/log/atop.log 60`
   This command tells atop to write system performance data to /var/log/atop.log every 60 seconds.

3. Reading from a Log File: `atop -r /var/log/atop.log` - 
   This command reads the performance data from the specified log file.
   it allows you to navigate through the recorded data.

4. `atop -m

## Interactive Commands
In general:
-  lower case keys --> show other information for the active processes 
-  upper case keys --> influence the sort order of the active process list.

### get help in interactive mode
- `?` or `h`: Request for help information.

### exit | quit
- `q`: Quit the program.

### Lower Case Commands
- `g`: Show generic output (default). 
- **`m`**: Show memory-related output. 
- `d`: Show disk-related output. 
- `n`: Show network-related output. 
- `s`: Show scheduling characteristics. 
- `v`: Show various process characteristics. 
- `c`: Show the command line of the process. 
- `o`: Show the user-defined line of the process. 
- **`u`**: Show the process activity accumulated per user. 
- `p`: Show the process activity accumulated per program. 

### sorting
- `A`: automatically by the most busy system resource.
- `C`: by CPU consumption (default).
- `M`: by memory consumption.
- `D`: by disk accesses issued.
- `N`: by network packets received/transmitted.


## atop vs top
| Feature                  | `atop`                                           | `top`                                   |
|--------------------------|--------------------------------------------------|-----------------------------------------|
| **Purpose**              | system and process monitoring tool     | Real-time system and process monitoring tool |
| **Detailed Resource Usage** | Yes                                              | Basic                                  |
| **Historical Data Logging**  | Yes                                              | No                                      |
| **Overloaded Resource Highlighting** | Yes                                      | No                                      |
| **Cumulative Resource Consumption**  | Yes                                      | No                                      |
| **Daemon Mode for Continuous Logging** | Yes                                      | No                                      |
| **Process Information**  | Detailed (CPU, memory, disk, network)            | Basic (PID, user, priority, etc.)       |
| **Sorting by Resource Metrics** | Yes                                        | Yes                                     |
| **Ease of Use**          | More complex, in-depth analysis                   | Simpler, quick real-time snapshot       |



   
   
