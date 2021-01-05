# AKQ_genetic_algorithm
Uses genetic algorithm techniques to find optimal play for the AKQ game.

Version 0 uses 6-bit alleles. The first 3 bits determine play when playing as Player 1. The second 3 bits determine play when playing as Player 2.

The fitness function is determined by playing each of the alleles against the other, each taking turns playing as Player 1 and Player 2 a set number of time. The top 2 winners are deemed fittest and are used for crossover. The results of the crossover are two new allele which are added to the population (after going through a mutation function).

The AKQ game is played as follows:

A deck of 3 cards (Ace, King, Queen, no suits) is in play. Each player posts an equal ante, and then is dealt a single card from the 3-card deck.

Player 1 has two options: check and see who wins or bet. If Player 1 checks, then the cards are compared and the winner takes the antes (A always wins, Q always loses, K loses to A and wins against Q). If Player 1 bets, then Player 2 may either call (match) the bet or fold (give up). If Player 2 gives up, then Player 1 wins the antes and takes back the amount Player 1 bet. If Player 2 calls, then the cards are compared and the winner takes the antes and the bets.
