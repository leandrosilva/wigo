#!/bin/sh

curl -i \
     -X POST http://127.0.0.1:5000/api/statemachines \
     -H "Content-type: application/json" \
     -d '
{
    "name": "provisioning",
    "description": "Simple Product Provisioning State Machine",
    "states": [{
        "name": "1_waiting_payment",
        "next": ["2_waiting_activation", "3_cancelled"]
    }, {
        "name": "2_waiting_activation",
        "next": ["4_activating"]
    }, {
        "name": "3_cancelled"
    }, {
        "name": "4_activating",
        "next": ["5_active"]
    }, {
        "name": "5_active",
        "next": ["6_waiting_deactivation"]
    }, {
        "name": "6_waiting_deactivation",
        "next": ["5_active", "7_deactivated"]
    }, {
        "name": "7_deactivated",
        "next": ["3_cancelled"]
    }]
}'
