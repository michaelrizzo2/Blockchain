#!/bin/bash
curl -X POST -H "Content-Type:application/json" -d '{"amount": 1, "recipient": "9e3546b87ab9433ea934d9b70d7467af", "sender": "0"}' "http://localhost:5000/transactions/new"
