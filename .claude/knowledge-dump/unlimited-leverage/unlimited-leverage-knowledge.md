## 29th June 2026 Notes

UL is VTJ Brand requirement
Then APAC intercept said they wanna do it as well. 

Background on infinite leverage: 
 That infinite leverage background is our biggest boutique from Exness, they came out with this unlimited leverage feature that increase their user base. 

Exness Leverage Backend : 
Its system executes all the results of its leverage through plugins. Most likely, the customer now sees that he can choose a leverage. He can choose 1,000x . 2,000 x, But in fact, these execution results are agreed to be rewritten through plugins. So maybe in the background, Customers choose unlimited leverage or 2,000x leverage. They all uniformly obtain the leverage of unlimited reserves.

It's just that Exness uses plugins to write unlimited leverage as an execution result of 1,000 or 2,000 times. This part is fine. Actions and practices.

Now the Vantage account opening method is that our leverage is selected. Then it will hit the leverage of our MQ through the manager API. That is, it is actually to choose the leverage on the Meta call. It selects 2,000 times. That's 2,000 times on MQ. Choose 1,000 times, On MQ, it is 1,000 times. So actually, the logic is different from Exness. So if we were to choose an infinite multiple today, There will be some problems with setting unlimited times in MQ because the wireless Position Keeper budget exhibition also needs to match some other restrictions.

For example, when he is on the news, He needs a fixed lever. Or when his equity changes, His leverage also needs to be adjusted. These changes in leverage can only be achieved through plugins. That is to say, unlimited leverage needs to be matched with plugins for execution. But the rest of the badcase leverage is through the manager API to directly rewrite customer changes on our system. So the logic on both sides Vantage and Exness is actually different.


Previous Available region Access to UL: 
MT4: AU6
MT5: AU2

Currently Available for all regions: 
Premium Account will automatically become UL (Unlimited Leverage) Account
If they don''t want UL, then have to change account.

Timeline：
March 2 have premium account users close position (To implement UL for them)
March 6 Internal close position for premium account that still opened
March 7 Apply for MT4
March 9 - mt4/mt5 premium account available 

Unlimited Leverage Account:
No Copy Trading will be available.
Using Spread revenue

Margin level = equity/margin
stop out level = 20%
margin=100 always positive
equity = 20

Stop out level is 0% means equity is 0 or <0 

stop out 20% = Except for premium account types 

Dynamic Leverage apply for 
Equity 					Leverage
0 <= Equity < 5000         	Unlimited
5000 <= Equity < 30,000			1:2000
30,000 <= Equity < 100,000	1:1000
Equity >= 100,000			1:500

Previous 2 days to adjust their leverage based on Equity
Now real time detection and adjustment, it did not affect users liquidation because in Forex Stop out 20% is common

Now they remove 20% stop out 


During News Period，Leverage will dynamically change 15min before the news release.

Margin always be positive, can't be negative
Free margin can be negative.

## 1st July 2026 Meeting Updates
New Condition: 
1. During Hedge position, when trying to unlock hedge positions, this increases net exposure. So when increase exposure, if the free margin <0, The order will be rejected. 
2. However, now when users tries unlocking their hedge positions, while the market price triggering TP/SL, whether the free margin is < 0, the client should be able to execute the plan.
3. YAML file that provided is input by Admin Team, if we want to change the rules, we can reach out to Admin Team.
4. Currently QA Testing responsibility is given to Plugin Team.

