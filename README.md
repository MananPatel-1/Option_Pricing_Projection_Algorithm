# Trading Bot 
- This is a stock call/put option projection algorithm to find the theoretical price of an option and option Greeks.
- All the orders are automated using Interactive Brokers <a href="https://interactivebrokers.github.io/tws-api/introduction.html">TWS API</a> by building a network socket to IB client application.

##  Black Scholes Model
Black-Scholes is a pricing model that uses six factors to calculate the theoretical value of a call or put option, including volatility, option type, underlying stock price, period, strike price, and risk-free rate.

## Option Pricing 
Premiums are made up of the total of the intrinsic and time values of an option. The price difference between the current stock price and the strike price is known as intrinsic value. The amount of premium over an option's inherent value is known as the time value or extrinsic value of an option. Moreover, hedging a portfolio is accomplished through the use of options contracts. In other words, the purpose is to counteract any adverse movements in other assets. Option contracts are sometimes used to speculate on whether the price of an asset will rise or decline.
- Intrinsic value is the amount of money that each given option would be worth if it were exercised today. The intrinsic value of an option is the amount by which the strike price is profitable or in-the-money as compared to the market price of the stock.
- Extrinsic value refers to the difference between an option's market price, or premium, and its intrinsic value. Extrinsic value is the part of an option's worth that has been allocated to it by variables other than the price of the underlying asset.

<img width="1336" alt="Screen Shot 2021-12-24 " src="https://user-images.githubusercontent.com/74301587/148841406-c3b9d9ae-d739-4e63-b4e0-b181c046d760.png">

## Option Greeks
The price of an option may be impacted by a variety of variables, which can assist or hinder traders depending on the sort of positions they have taken. Successful traders are aware of the elements that impact option pricing, including the so-called option greeks.

<img width="939" alt="Screen Shot 2021-12-24 at 2 15 45 PM" src="https://user-images.githubusercontent.com/74301587/148850136-8b3a925b-4042-45e6-be34-7ba3eee75812.png">

- Delta: The rate of change of the option price respected to the rate of the change of underlying asset price.
- Gamma: The rate of change of delta respected to the rate of change of underlying asset price.
- Vega: The rate of change of the option price respected to the volatility of the underlying asset.
- Rho: The rate of the option price respected to the interest rate.
- Theta: The rate of change of the option price respected to the passage of time.

# Monte Carlo simulation
Monte-Carlo simulation is a computerised mathematical approach that permits quantitative analysis to account for risk. Furthermore, they are a vast category of computer algorithms that produce numerical results by repeated random sampling. The basic idea is to utilize randomness to solve problems that are in essence deterministic.

Financial derivatives such as options are dependent on the underlying asset, stocks which follows a Brownian motion or Wiener process. So, by simulating these stochastic processes we could determine the prices of financial instrument(option in this case)
<div align="center" ><img width="254" alt="Screen Shot 2022-01-12 at 10 34 38 PM" src="https://user-images.githubusercontent.com/74301587/149261334-551ab483-5d2d-4e64-a252-f571697ccc57.png"></div>
Now we could obtain the log S(t) because we know that stock prices can not be negative. By Ito's lemma we could say that F(S) = log S(t)
<div align="center" ><img width="275" alt="Screen Shot 2022-01-12 at 10 40 16 PM" src="https://user-images.githubusercontent.com/74301587/149261813-008eb29c-c5ab-41c7-b938-0e788f9f26c9.png"></div>
<div align="center" ><img width="354" alt="Screen Shot 2022-01-12 at 10 41 10 PM" src="https://user-images.githubusercontent.com/74301587/149261891-227d1ac5-c514-4a81-8c8c-cb85477e72dc.png"></div>

Here the Brownian motion is a random walk with mean 0 and variance t so, N(0,t) which could be re-writen as √t N(0,1)
Now, if we make a risk-netural assumption the μ drift becomes r risk-free interest rate and we get
<div align="center" ><img width="315" alt="Screen Shot 2022-01-12 at 10 50 25 PM" src="https://user-images.githubusercontent.com/74301587/149262718-7cd60150-5ec5-4cb9-bfce-e4c5bb9d4b48.png"></div>
The exponential function defined stock price at T maturity
For a call option we would calculate max(S - E, 0) and for a put option we would calculate max(E - S, 0)
