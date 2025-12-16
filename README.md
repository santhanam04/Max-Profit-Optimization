🏗️ Max Profit Property Development Optimizer

An end-to-end algorithmic + Streamlit + GitHub-ready solution for the Max Profit Problem.
Live Demo https://max-profit-optimization-eythvph8e2tku8jg2bhfnw.streamlit.app/
This project calculates the optimal mix of Theatres, Pubs, and Commercial Parks to maximize total earnings given a time constraint, and provides an interactive Streamlit web app.

📌 Problem Summary

Mr. X can develop one property at a time.

Property	Build Time	Earnings
Theatre (T)	5 units	$1500
Pub (P)	4 units	$1000
Commercial Park (C)	10 units	$2000

Goal: Maximize earnings after n time units.

🧠 Optimal Strategy (Key Insight)

Instead of brute force, we observe earnings per time unit:

Property	Earnings / Time
Theatre	300 (BEST)
Pub	250
Commercial Park	200

➡️ Theatre always gives maximum profit per unit time

Strategy

Build maximum number of theatres

If remaining time ≥ 4 → build 1 Pub

Ignore Commercial Park (never optimal)

This guarantees maximum earnings.
