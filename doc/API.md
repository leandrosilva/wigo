# wigo :: api

This is the documentation of wigo's web API.

## Introduction

Wigo API is a REST-like web API with JSON payload, which means that every single request/response is based on HTTP verbs and JSON data.

Wigo aims to be used to keep track of state machines, allowing to build monitoring dashboards and also taking action over metrics. This means one can define thresholds for each state of a given state machine and then trigger actions based on them, like notify Nagios, post to a web service, or something like so.

Some use cases that might come in mind are:

* Ordering systems
* Anti-Fraud systems
* Product provisioning systems

### An Imaginary Product Provisioning System

Here, in this documentation, I've decided to adopt a simplified use case on **product provisioning**, which is quite common in Internet companies, like those who provide IaaS, PaaS, and SaaS.

This imaginary product provisioning system has seven states for each provisioning, as follow:

    #1 Waiting Payment      -> { #2 Waiting Activation, #3 Cancelled }
    #2 Waiting Activation   -> { #4 Activating }
    #3 Canceled             -> END
    #4 Activating           -> { #5 Active }
    #5 Active               -> { #6 Waiting Deactivation }
    #6 Waiting Deactivation -> { #4 Active, #7 Deactivated }
    #7 Deactivated          -> { #3 Canceled }

If you're not familiarised with this kind of system, essentially they work like so: A provisioning is an instance of a product that should be delivered to a given customer who ordered it; as such, every provisioning has a limited life cycle, and may passing through many of those seven states during its life.

Let's see some examples:

**Example 1**

    T1                       T2
    |------------------------|
    #1 Waiting Payment       #3 Cancelled

**Example 2**

    T1                       T2                       T3                       T4
    |------------------------|------------------------|------------------------|
    #1 Waiting Payment       #2 Waiting Activating    #4 Activating            #5 Active

    T5                       T6                       T7                       T8                       T9
    |------------------------|------------------------|------------------------|------------------------|
    #6 Waiting Deactivation  #4 Active                #6 Waiting Deactivation  #7 Deactivated           #3 Cancelled

**Example 3**

    T1                       T2                       T3                       T4
    |------------------------|------------------------|------------------------|
    #1 Waiting Payment       #2 Waiting Activating    #4 Activating            #5 Active

    T5                       T6                       T7
    |------------------------|------------------------|
    #6 Waiting Deactivation  #7 Deactivated           #3 Cancelled

OK. So now I think we have matter to go forward and walk through the API.

## Settings

* TODO

### Setting up a new state machine

**Request:**

    POST /api/statemachines
    
    {
        "name": "Provisioning",
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
    }
    
**Response:**

    {
        
    }

## Sending data

* TODO

## Monitoring metrics

* TODO
