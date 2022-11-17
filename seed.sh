#!/bin/sh

# USERS
flask user create admin@admin.com   admin pass 2
flask user create emp@aemp.com   emp pass 1
flask user create user@user.com   user pass 0

# PETS + BREEDS
flask pet create Max 1 Bullterrier
flask pet create Uma 2 Labrador
flask pet create Olivia 2 Rottweiler
flask pet create Pepe 3 Bullterrier

# APPOINTMENTS
# pet_id, user_id, schedule
flask appointment create 2 2 2022-12-1T9:00:00
flask appointment create 3 2 2022-12-2T10:30:00
flask appointment create 4 3 2022-12-2T8:30:00
