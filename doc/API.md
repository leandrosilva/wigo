# wigo :: api

This is the documentation of wigo's web API.

## Introduction

Wigo API is a REST-like web API with JSON payload, which means that every single request/response is based on HTTP verbs and JSON data.

Wigo aims to be used to keep track of state machines, allowing monitoring and actions over metrics. This means you can define thresholds for each state of a state machine and then trigger actions based on them, like notify Nagios, post to a web service, and so on.

Some use cases might be:

* Product provisioning systems
* Ordering systems
* Anti-Fraud systems

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

**Example 1:**

    T1                       T2
    |------------------------|
    #1 Waiting Payment       #3 Cancelled

**Example 2:**

    T1                       T2                       T3                       T4
    |------------------------|------------------------|------------------------|
    #1 Waiting Payment       #2 Waiting Activating    #4 Activating            #5 Active

    T5                       T6                       T7                       T8                       T9
    |------------------------|------------------------|------------------------|------------------------|
    #6 Waiting Deactivation  #4 Active                #6 Waiting Deactivation  #7 Deactivated           #3 Cancelled

## Settings

* TODO

### Setting up a new state machine

**Request:**

    POST /api/setup/statemachine/new
    
    {
        "id": "PROVISIONING"
        "name": "Product Provisioning",
        "states": [{
            "id": "1"
            "name": "Waiting Payment",
            "next": ["2", "3"]
        }, {
            
        }]
    }

**Response:**

    {
        
    }

## Sending data

* TODO

## Monitoring metrics

* TODO
