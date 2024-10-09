---
layout: post
title:  "Proxy Users in Oracle Databases"
author: "Sagiv Barhoom"
date:   2024-10-01
categories: ORACLE 
background: ''
---

# Proxy Users in Oracle Databases

A proxy user allows one database user to act on behalf of another. 
This functionality is particularly useful for managing access in a secure and controlled way.
Somtimes improving administration and user management efficiency.

## What is a Proxy User?
A proxy user is a user account that can connect and work on behalf of another user without needing their password. 
This delegation allows for access control while still enabling multiple users or applications to interact with a single database account.

## Common Uses of Proxy Users:
1. **Application-to-database interactions:** 
   Proxy users can enable applications to connect to the database as different users while maintaining security and access control.
2. **Security and auditing:**
   By allowing specific proxy access, organizations can monitor activities performed on behalf of a user.
3. **Simplifying user management:** Administrators can create proxy users for developers, support teams, or external parties who need temporary or specific access to certain schemas.

## How to Create a Proxy User in Oracle:
1. Create the main users (schemas)
2. Create the proxy user
3. Grant proxy permissions

### 1. Create the main users (schemas)
```sql
CREATE USER schema_user1 IDENTIFIED BY password1;
CREATE USER schema_user2 IDENTIFIED BY password2;
GRANT CONNECT, RESOURCE TO schema_user1;
GRANT CONNECT, RESOURCE TO schema_user2;
```
### 2. Create the proxy user:
```sql
CREATE USER proxy_user IDENTIFIED BY proxy_password;
GRANT CONNECT TO proxy_user;
```
### 3. Grant proxy permissions:
```sql
ALTER USER schema_user1 GRANT CONNECT THROUGH proxy_user;
ALTER USER schema_user2 GRANT CONNECT THROUGH proxy_user;
```
## Connecting as a proxy
You can connect as the proxy user to act as schema_user1 or schema_user2:
```sql
CONNECT proxy_user[schema_user1]/proxy_password@db;
```
In this setup, the proxy_user can now connect and work on behalf of schema_user1 and schema_user2 without needing their passwords, providing controlled access.

## proxy user and profiles
In addition to managing proxy users, Oracle provides profiles to control session behavior and resource usage. 
See my post about users and profiles.
Here we define limits for idle time as an example  using profiles.
Idle time determines how long a session can remain inactive before being disconnected.
1. Creating Profiles with Idle Time
2. Assign profiles to users
3. Test the behavior
### Creating Profiles with Idle Time:
Let’s create three profiles, each with a different idle time, and see how they affect session behavior.
```sql
Create profiles with different idle times:
CREATE PROFILE profile_1 LIMIT IDLE_TIME 1;     --   1 minute idle time
CREATE PROFILE profile_2 LIMIT IDLE_TIME 20;     --  2 minutes idle time
CREATE PROFILE profile_proxy LIMIT IDLE_TIME 5;  --  3 minutes idle time
```
### Assign profiles to users:
```sql
ALTER USER schema_user1 PROFILE profile_1;
ALTER USER schema_user2 PROFILE profile_2;
ALTER USER proxy_user PROFILE profile_proxy;
```

### How Idle Time Affects Sessions
1. **schema_user1:** With profile_1, the session will disconnect after **1 minutes** of inactivity.
2. **schema_user2:** With profile_2, the session remains active for up to **2 minutes** of inactivity.
3. **proxy_user:** Since proxy_user has profile_proxy, any session using this user will disconnect after **3 minutes** of inactivity, **even when acting on behalf of other users!*

By controlling idle time via profiles, you can fine-tune resource usage and session management in your Oracle database.

BTWת **If no profile is assigned to the proxy_user**, Oracle will apply the `default profile`. 
The `default profile` usually has no strict resource limits unless explicitly modified by the DBA. 
This means:
1. There would be no enforced idle time limit by default, allowing sessions to remain open indefinitely unless manually disconnected.
2. Other resource limits (e.g., CPU, sessions per user) will also follow the default settings, which may lead to uncontrolled resource usage.

By not defining a profile, you're leaving session behavior and resource usage less controlled, which might affect performance or security in certain cases.
