# Chipless ( Teen patti / Poker)

I just wrote a small script to maintain the bets and balances for each player while in gambling games like Teen Patti or Poker so that you can play even without any chips/ cash.

Currently it does not take balance in account during bets. If the balance is over it takes it in negative ( Does not fold the player or considers all-in ).

You can run this script and it will keep track of players and their bets in each round and save the overall loss/ profit in a file. 

To use this, go to the terminal and type<br />
            `git clone https://github.com/shreyagarwal13/teen_patti.git`<br />
            `cd teen_patti`<br />
            `python3 bet_manager.py`<br />

Input y/n for yes and no to start or end each round. 

Entering -1 in the middle of a round will end the round. 

Enter the player no. who won after each round to add the pot to their balance.

You can more players at the end of each round.
