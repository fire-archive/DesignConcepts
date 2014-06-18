# Mechanics and Dynamics

*Originally posted July 13, 2009*

Until this point, we have made lots of games and game rules, but at no point have we examined what makes a *good* rule from a *bad* one. Nor have we really examined the different *kinds* of rules that form a game designer’s palette. Nor have we talked about the relationship between the game rules and the player experience. These are the things we examine today.

## Course Announcements

No major announcements today, but for your curiosity I did compile a list of tweets for the last challenge (add or change a rule to *Battleship* to make it more interesting):

-   "Reveal" was a common theme (such as, instead of firing a shot, give the number of Hits in a 3x3 square – thus turning the game from "what number am I thinking of" into "two-player competitive Minesweeper")

-   Skip a few turns for a larger shot (for example, skip 5 turns to hit everything in an entire 3x3 area). The original suggestion was an even number (skip 9 turns to nuke a 3x3 square) but note that there isn’t much of a functional difference between this and just taking one shot at a time.

-   Like *Go*, if you enclose an area with a series of shots, all squares in the enclosed area are immediately hit as well (this adds an element of risk-taking and short-term versus long-term tradeoffs to the game – do you try to block off a large area that takes many turns but has an efficient turn-to-squares-hit ratio, or do you concentrate on smaller areas that give you more immediate information but at the cost of taking longer in aggregate?)

-   When you miss but are in a square adjacent to an enemy ship, the opponent must declare it as a "near miss" (without telling you what direction the ship is in), which doesn’t exactly get around the guessing-game aspect of the original but should at least speed play by giving added information. Alternatively, with *any* miss, the opponent must give the distance in squares to the nearest ship (without specifying direction), which would allow for some deductive reasoning.

-   Skip (7-X) turns to rebuild a destroyed ship of size X. If the area in which you are building is hit in the meantime, the rebuild is canceled. (The original suggestion was skip X turns to rebuild a ship of size X, but smaller ships are actually more dangerous since they are harder to locate, so I would suggest an inverse relationship between size and cost.)

-   Each time you sink an enemy ship, you can rebuild a ship of yours of the same size that was already sunk (this gives some back-and-forth, and suggests alternate strategies of scattering your early shots to give your opponent less room to rebuild)

-   Once per game, your Battleship (the size-4 ship) can hit a 5-square cross (+) shaped area in a single turn; using this also forces you to place a Hit on your own Battleship (note that this would also give away your Battleship’s location, so it seems more like a retaliatory move when your Battleship is almost sunk anyway)


We will revisit some of these when we talk about the kinds of decisions that are made in a game, next Monday.

## Readings

This week I’m trying something new and putting one of the readings up front, because I want you to look at this first, before reading the rest of this post.

-   [*MDA Framework*](http://www.cs.northwestern.edu/~hunicke/MDA.pdf) by LeBlanc, Hunicke and Zabek. This is one of the few academic papers that achieved wide exposure within the game industry (it probably helps that the authors are experienced game designers). There are two parts of this paper that made it really influential. The first is the Mechanics/Dynamics/Aesthetics (MDA) conceptualization, which offers a way to think about the relationship of rules to player experience, and also the relationship between player and designer. The second part to pay attention to is the "8 kinds of fun" which we will return to a bit later in the course (Thursday of next week).

## Now, About That MDA Framework Thing…

LeBlanc *et al.* define a game in terms of its Mechanics, Dynamics, and Aesthetics:

-   Mechanics are a synonym for the "rules" of the game. These are the constraints under which the game operates. How is the game set up? What actions can players take, and what effects do those actions have on the game state? When does the game end, and how is a resolution determined? These are defined by the mechanics.

-   Dynamics describe the *play* of the game when the rules are set in motion. What strategies emerge from the rules? How do players interact with one another?

-   Aesthetics (in the MDA sense) do not refer to the visual elements of the game, but rather the *player experience* of the game: the effect that the dynamics have on the players themselves. Is the game "fun"? Is play frustrating, or boring, or interesting? Is the play emotionally or intellectually engaging?

Before the MDA Framework was written, the terms "mechanics" and "dynamics" were already in common use among designers. The term "aesthetics" in this sense had not, but has gained more use in recent years.

## The Process of Design

With the definitions out of the way, why is this important? This is one of the key points of the MDA paper. The game designer only creates the Mechanics directly. The Dynamics emerge from the Mechanics, and the Aesthetics arise out of the Dynamics. The game designer may *want* to design the play experience, or at least that may be the ultimate goal the designer has in mind… but as designers, we are stuck building the rules of the game and hoping that the desired experience emerges from our rules.

This is why game design is sometimes referred to as a **second-order design problem**: because we do not define the solution, we define something that creates something else that creates the solution. **This is why game design is hard**. Or at least, it is one reason. Design is not just a matter of coming up with a "Great Idea" for a game; it is about coming up with a set of rules that will implement that idea, when two-thirds of the final product (the Dynamics and Aesthetics) are not under our direct control.

## The Process of Play

Designers start with the Mechanics and follow them as they grow outward into the Aesthetics. You can think of a game as a sphere, with the Mechanics at the core, the Dynamics surrounding them, and the Aesthetics on the surface, each layer growing out of the one inside it. One thing the authors of MDA point out is that this is *not* how games are experienced from the player’s point of view.

A player sees the surface first – the Aesthetics. They may be *aware* of the Mechanics and Dynamics, but the thing that really makes an immediate impression and that is most easily understood is the Aesthetics. This is why, even with absolutely no knowledge or training in game design, *anyone* can play a game and tell you whether or not they are having a good time. They may not be able to articulate *why* they are having a good time or *what* makes the game "good" or "bad"… but anyone can tell you right away how a game makes them feel.

If a player spends enough time with a game, they may learn to appreciate the Dynamics of the game and now their experience arises from them. They may realize that they do or don’t like a game because of the specific kinds of interactions they are having with the game and/or the other players. And if a player spends even more time with that game, they may eventually have a strong enough grasp of the Mechanics to see how the Dynamics are emerging from them.

If a game is a sphere that is designed from the inside out, it is *played* from the outside in. And this, I think, is one of the key points of MDA. The designer creates the Mechanics and everything flows outward from that. The player experiences the Aesthetics and then their experience flows inward. As designers, we must be aware of **both** of these ways of interacting with a game. Otherwise, we are liable to create games that are fun for designers but not players.

## One Example of MDA in action

I mentioned the concept of "spawn camping" earlier in this course, as an example of how players with different implicit rule sets can throw around accusations of "cheating" for something that is technically allowed by the rules of the game. Let us analyze this in the context of MDA.

In a First-Person Shooter video game, a common mechanic is for players to have "spawn points" – dedicated places on the map where they re-appear after getting killed. Spawn points are a **mechanic**. This leads to the **dynamic** where a player may sit next to a spawn point and immediately kill anyone as soon as they respawn. And lastly, the **aesthetics** would likely be frustration at the prospect of coming back into play only to be killed again immediately.

Suppose you are designing a new FPS and you notice this frustration aesthetic in your game, and you want to fix this so that the game is not as frustrating. You cannot simply change the aesthetics of the game to "make it more fun" – this may be your goal, but it is not something under your direct control. You cannot even change the dynamics of spawn camping directly; you cannot tell the players how to interact with your game, except through the mechanics. So instead, you must change the mechanics of the game – maybe you try making players respawn in random locations rather than designated areas – and then you hope that the desired aesthetics emerge from your mechanics change.

How do you know if your change worked? Playtest, of course!

How do you know *what* change to make, if the effects of mechanics changes are so unpredictable? We will get into some basic tips and tricks near the end of this course. For now, the most obvious way is designer intuition. The more you practice, the more you design games, the more you make rules changes and then playtest and see the effects of your changes, the better you will get at making the right changes when you notice problems… and occasionally, even creating the right mechanics in the first place. There are few substitutes for experience… which, incidentally, is why so much of this course involves getting you off your butt and making games :).

**"If the computer or the game designer is having more fun than the player, you have made a terrible mistake."**

This seems as good a time as any to quote game designer Sid Meier. His warning is clearly directed at video game designers, but applies just as easily to non-digital projects. It is a reminder that we design the Mechanics of the game, and designing the Mechanics is fun for us. But it is *not* the Mechanics that are fun for our *players*. A common design mistake is to create rules that are fun to create, but that do not necessarily translate into fun gameplay. Always remember that you are creating games for the players and not yourself.

## Mechanics, Dynamics and Complexity

Generally, adding additional mechanics, new systems, additional game objects, and new ways for objects to interact with one another (or for players to interact with the game) will lead to a greater complexity in the dynamics of the game. For example, compare *Chess* and *Checkers*. *Chess* has six kinds of pieces (instead of two) and a greater number of actions that each piece can take, so it ends up having more strategic depth.

Is more complexity good, or bad? It depends. *Tetris* is a very simple but still very successful game. *Advanced Squad Leader* is an incredibly complex game, but still can be considered successful for what it is. Some games are so simple that they are not fun beyond a certain age, like *Tic-Tac-Toe*. Other games are too complex for their own good, and would be better if their systems were a bit more simplified and streamlined (I happen to think this about the board game *Agricola*; I’m sure you can provide examples from your own experience).

Do more complex mechanics *always* lead to more complex dynamics? No – there are some cases where very simple mechanics create extreme complexity (as is the case with *Chess*). And there are other cases where the mechanics are extremely complicated, but the dynamics are simple (imagine a modified version of the children’s card game *War* that did not just involve comparison of numbers, but lookups on complex "combat resolution" charts). The best way to gauge complexity, as you may have guessed, is to play the game.

## Feedback Loops

One kind of dynamic that is often seen in games and deserves special attention is known as the **feedback loop**. There are two types, **positive feedback loops** and **negative feedback loops**. These terms are borrowed from other fields such as control systems and biology, and they mean the same thing in games that they mean elsewhere.

A positive feedback loop can be thought of as a**reinforcing** relationship. Something happens that causes the same thing to happen again, which causes it to happen yet again, getting stronger in each iteration – like a snowball that starts out small at the top of the hill and gets larger and faster as it rolls and collects more snow.

As an example, there is a relatively obscure shooting game for the NES called *The Guardian Legend*. Once you beat the game, you got access to a special extra gameplay mode. In this mode, you got rewarded with power-ups at the end of each level based on your score: the higher your score, the more power-ups you got for the next level. This is a positive feedback loop: if you get a high score, it gives you more power-ups, which make it easier to get an even higher score in the next level, which gives you even more power-ups, and so on.

Note that in this case, the reverse is also true. Suppose you get a low score. Then you get fewer power-ups at the end of that level, which makes it harder for you to do well on the next level, which means you will probably get an even lower score, and so on until you are so far behind that it is nearly impossible for you to proceed at all.

The thing that is often confusing to people is that *both* of these scenarios are *positive* feedback loops. This seems counterintuitive; the second example seems very "negative," as the player is doing poorly and getting fewer rewards. It is "positive" in the sense that the effects get stronger in magnitude on each iteration.

There are three properties of positive feedback loops that game designers should be aware of:

1.  They tend to destabilize the game, as one player gets further and further ahead (or behind).

2.  They cause the game to end faster.

3.  The put emphasis on the early game, since the effects of early-game decisions are magnified over time.


Feedback loops usually have two steps (as in my *The Guardian Legend* example) but they can have more. For example, some Real-Time Strategy games have a positive feedback loop with four steps: players explore the map, which gives them access to more resources, which let them buy better technology, which let them build better units, which let them explore more effectively (which gives them access to more resources… and the cycle repeats). As such, detecting a positive feedback loop is not always easy.

Here are some other examples of positive feedback loops that you might be familiar with:

-   Most "4X" games, such as the *Civilization* and *Master of Orion* series, are usually built around positive feedback loops. As you grow your civilization, it lets you generate resources faster, which let you grow faster. By the time you begin conflict in earnest with your opponents, one player is usually so far ahead that it is not much of a contest, because the core positive feedback loop driving the game means that someone who got ahead of the curve early on is going to be *much* farther ahead in the late game.

-   Board games that feature building up as their primary mechanic, such as *Settlers of Catan*. In these games, players use resources to improve their resource production, which gets them more resources.

-   The physical sport *Rugby* has a minor positive feedback loop: when a team scores points, they start with the ball again, which makes it slightly more likely that they will score again. The advantage is thus given to the team who just gained an advantage. This is in contrast to most sports, which give the ball to the opposing team after a successful score.


Negative feedback loops are, predictably, the opposite of positive feedback loops in just about every way. A negative feedback loop is a balancing relationship. When something happens in the game (such as one player gaining an advantage over the others), a negative feedback loop makes it harder for that same thing to happen again. If one player gets in the lead, a negative feedback loop makes it easier for the opponents to catch up (and harder for a winning player to extend their lead).

As an example, consider a "Kart-style" racing game like *Mario Kart*. In racing games, play is more interesting if the player is in the middle of a pack of cars rather than if they are way out in front or lagging way behind on their own (after all, there is more interaction if your opponents are close by). As a result, the *de facto* standard in that genre of play is to add a negative feedback loop: as the player gets ahead of the pack, the opponents start cheating, finding better power-ups and getting impossible bursts of speed to help them catch up. This makes it more difficult for the player to maintain or extend a lead. This particular feedback loop is sometimes referred to as "rubber-banding" because the cars behave as if they are connected by rubber bands, pulling the leaders and losers back to the center of the pack.

Likewise, the reverse is true. If the player falls behind, they will find better power-ups and the opponents will slow down to allow the player to catch up. This makes it more difficult for a player who is behind to fall further behind. Again, both of these are examples of *negative* feedback loops; "negative" refers to the fact that a dynamic becomes weaker with iteration, and has nothing to do with whether it has a positive or negative effect on the player’s standing in the game.

Negative feedback loops also have three important properties:

1.  They tend to stabilize the game, causing players to tend towards the center of the pack.

2.  They cause the game to take longer.

3.  They put emphasis on the late game, since early-game decisions are reduced in their impact over time.


Some examples of negative feedback loops:

-   Most physical sports like *Football* and *Basketball*, where after your team scores, the ball is given to the opposing team and they are then given a chance to score. This makes it less likely that a single team will keep scoring over and over.

-   The board game *Starfarers of Catan* has a negative feedback loop where every player with less than a certain number of victory points gets a free resource at the start of their turn. Early on, this affects all players and speeds up the early game. Later in the game, as some players get ahead and cross the victory point threshold, the players lagging behind continue to get bonus resources. This makes it easier for the trailing players to catch up.

-   My grandfather was a decent *Chess* player, generally better than his children who he taught to play. To make it more of a challenge, he invented a rule: if he won a game, next time they played, his opponent could remove a piece of his from the board at the start of the game (first a pawn, then two pawns, then a knight or bishop, and so on as the child continued to lose). Each time my grandfather won, the next game would be more challenging for him, making it more likely that he would eventually start losing.


**Use of Feedback Loops**

Are feedback loops good or bad? Should we strive to include them, or are they to be avoided? As with most aspects of game design, it depends on the situation. Sometimes, a designer will deliberately add mechanics that cause a feedback loop. Other times, a feedback loop is discovered during play and the designer must decide what (if anything) to do about it.

Positive feedback loops can be quite useful. They end the game quickly when a player starts to emerge as the winner, without having the end game be a long, drawn-out affair. On the other hand, positive feedback loops can be frustrating for players who are trying to catch up to the leader and start feeling like they no longer have a chance.

Negative feedback loops can also be useful, for example to prevent a dominant early strategy and to keep players feeling like they always have a chance to win. On the other hand, they can also be frustrating, as players who do well early on can feel like they are being punished for succeeding, while also feeling like the players who lag behind are seemingly rewarded for doing poorly.

What makes a particular feedback loop "good" or "bad" from a player perspective? This is debatable, but I think it is largely a matter of player perception of fairness. If it feels like the game is artificially intervening to help a player win when they don’t deserve it, it can be perceived negatively by players. How do you know how players will perceive the game? Playtest, of course.

## Eliminating Feedback Loops

Suppose you identify a feedback loop in your game and you want to remove it. How do you do this? There are two ways.

The first is to shut off the feedback loop itself. All feedback loops (positive and negative) have three components:

-   A "sensor" that monitors the game state;

-   A "comparator" that decides whether to take action based on the value monitored by the sensor;

-   An "activator" that modifies the game state when the comparator decides to do so.


For example, in the earlier kart-racing negative feedback loop example, the "sensor" is how far ahead or behind the player is, relative to the rest of the pack; the "comparator" checks to see if the player is farther ahead or behind than a certain threshold value; and the "activator" causes the opposing cars to either speed up or slow down accordingly, if the player is too far ahead or behind. All of these may form a single mechanic ("If the player is more than 300 meters ahead of all opponents, multiply everyone else’s speed by 150%"). In other cases there may be three or more separate mechanics that cause the feedback loop, and changing any one of them will modify the nature of the loop.

By being aware of the mechanics causing a feedback loop, you can disrupt the effects by either removing the sensor, changing or removing the comparator, or modifying or removing the effect of the activator. Going back to our *The Guardian Legend* example (more points = more power-ups for the next level), you could deactivate the positive feedback loop by either modifying the sensor (measure something other than score… something that does not increase in proportion to how powered-up the player is), or changing the comparator (by changing the scores required so that later power-ups cost more and more, you can guarantee that even the best players will fall behind the curve eventually, leading to a more difficult end game), or changing the activator (maybe the player gets power-ups through a different method entirely, such as getting a specific set of power-ups at the end of each level, or finding them in the middle of levels).

If you do not want to remove the feedback loop from the game but you do want to reduce its effects, an alternative is to add *another* feedback loop of the opposing type. Again returning to the kart-racing example, if you wanted to keep the "rubber-banding" negative feedback loop, you could add a positive feedback loop to counteract it. For example, if the opposing cars get speed boosts when the player is ahead, perhaps the player can go faster as well, leading to a case where being in the lead makes the entire race go faster (but not giving an advantage or disadvantage to anyone). Or maybe the player in the lead can find better power-ups to compensate for the opponents’ new speed advantage.

## Emergence

Another dynamic that game designers should be aware of is called **emergent gameplay** (or **emergent complexity**, or simply **emergence**). I’ve found this is a difficult thing to describe in my classroom courses, so I would welcome other perspectives on how to teach it. Generally, emergence describes a game with simple mechanics but complex dynamics. "Emergent complexity" can be used to describe *any* system of this nature, even things that are not games.

Some examples of emergence from the world outside of games:

-   In nature, insect colonies (such as ants and bees) show behavior that is so complex, it appears to be intelligent enough that we call it a "hive mind" (much to the exploitation of many sci-fi authors). In reality, each individual insect is following its own very simple set of rules, and it is only in aggregate that the colony displays complex behaviors.

-   [Conway’s Game of Life](http://en.wikipedia.org/wiki/Conway’s_Game_of_Life), though not actually a "game" by most of the definitions in this course, is a simple set of sequential rules for simulating cellular life on a square grid. Each cell is either "alive" or "dead" on the current turn. To progress to the next turn, all living cells that are adjacent to either zero or one other living cells are killed (from isolation), and living cells adjacent to four or more other living cells are also killed (from overcrowding); all dead cells adjacent to exactly three living cells are "born" and changed to living cells on the next turn; and any cell adjacent to exactly two living cells stays exactly as it is. Those are the only rules. You start with an initial setup of your choice, and then modify the board to see what happens. And yet, you can get incredibly complex behaviors: structures can move, mutate, spawn new structures, and any number of other things.

-   [Boid’s Algorithm](http://www.red3d.com/cwr/boids/), a way to simulate crowd and flocking behavior that is used in some CG-based movies as well as games. There are only three simple rules that individuals in a flock must each follow. First, if there are a lot of your companions on one side of you and few on the other, it means you’re probably at the edge of the flock; move towards your companions. Second, if you are close to your companions, give them room so you don’t crowd them. Third, adjust your speed and direction to be the average of your nearby companions. From these three rules you can get some pretty complex, detailed and realistic crowd behavior.

Here are some examples of emergent gameplay:

-   In fighting games like the *Street Fighter* or *Tekken* series, "combos" arise from the collision of several simple rules: connecting with certain attacks momentarily stuns the opponent so that they cannot respond, and other attacks can be executed quickly enough to connect before the opponent recovers. Designers may or may not intentionally put combos in their games (the earliest examples were not intended, and indeed were not discovered until the games had been out for awhile), but it is the mechanics of stunning and attack speed that create complex series of moves that are unblockable after the first move in the series connects.

-   In the sport of *Basketball*, the concept of "dribbling" was not explicitly part of the rules. As originally written, the designer had intended the game to be similar to how *Ultimate Frisbee* is played: the player with the ball is not allowed to move, and must either throw the ball towards the basket (in an attempt to score), or "pass" the ball to a teammate (either through the air, or by bouncing it on the ground). There was simply no rule that prevented a player from passing to himself.

-   Book openings in *Chess*. The rules of this game are pretty simple, with only six different piece types and a handful of special-case moves, but a set of common opening moves has emerged from repeated play.

Why do we care about emergent dynamics? It is often desired for practical reasons, especially in the video game world, because you can get a lot of varied and deep gameplay out of relatively simple mechanics. In video games (and to a lesser extent, board games) it is the *mechanics* that must be implemented. If you are programming a video game, emergent gameplay gives you a great ratio of hours-of-gameplay to lines-of-code. Because of this apparent cost savings, "emergence" as a buzzword was all the rage a few years ago, and I still hear it mentioned from time to time.

It’s important to note that emergence is not always planned for, and for that matter it is not always desirable. Here are two examples of emergence, both from the *Grand Theft Auto* series of games, where unintended emergent gameplay led to questionable results:

-   Consider these two rules. First, running over a pedestrian in a vehicle causes them to drop the money they are carrying. Second, hiring a prostitute refills the player’s health, but costs the player money. From these two unrelated rules, we get the emergent strategy that has been affectionately termed the "hooker exploit": sleep with a prostitute, then run her over to regain the money you spent. This caused a bit of a scandal in the press back in the day, from people who interpreted this dynamic as an intentional design that glorified violence against sex workers. Simply saying "it’s emergent gameplay!" is not sufficient to explain to a layperson why this was not intentional.

-   Perhaps more amusing was the combination of two other rules. First, if the player causes damage to an innocent bystander, the person will (understandably) defend themselves by attacking the player. Second, if a vehicle has taken sufficient damage, it will eventually explode, damaging everything in the vicinity (and of course, nearly killing the driver). These led to the following highly unrealistic scenario: a player, driving a damaged vehicle, crashes near a group of bystanders. The car explodes. The player crawls from the wreckage, barely alive… until the nearby crowd of "Samaritans" decides that the player damaged them from the explosion, and they descend in a group to finish the player off!

As you can see, emergence is not always a good thing. More to the point, it is not *necessarily* cheaper to develop a game with emergent properties. Because of the complex nature of the dynamics, emergent games require a lot more playtesting and iteration than games that are more straightforward in their relationships between mechanics and dynamics. A game with emergence may be easier to program, but it is much harder to design; there is no cost savings, but rather a *shift* in cost from programmers to game designers.

## From Emergence to Intentionality

Player intentionality, the concept from Church’s *Formal Abstract Design Tools* mentioned earlier in this course, is related in some ways to emergence. Generally, you get emergence by having lots of small, simple, interconnected systems. If the player is able to figure out these systems and use them to form complicated chains of events intentionally, that is one way to have a higher degree of player intention.

## Another Reading

-   [*Designing to Promote Intentional Play*](http://clicknothing.typepad.com/Design/hockingc_GDC06_Intentionality.zip) by Clint Hocking. This was a lecture given live at GDC in 2006, but Clint has kindly made his Powerpoint slides and speaker notes publicly available for download from his blog. It covers the concept of player intentionality and its relation to emergence, far better than I can cover here. The link goes to a Zip file that contains a number of files inside it; start with the Powerpoint and the companion Word doc, and the presentation will make it clear when the other things like the videos come into play. I will warn you that, like many video game developers, Clint tends to use a lot of profanity; also, the presentation opens with a joke about Jesus and Moses. It may be best to skip this one if you are around people who are easily offended by such things.

## Lessons Learned

The most important takeaway from today is that game design is not a trivial task. It is difficult, mainly because of the nature of MDA. The designer creates rules, which create play, which create the player experience. Every rule created has a doubly-indirect effect on the player, and this is hard to predict and control. This also explains why making one small rules change in a game can have ripple effects that drastically alter how the game is played. And yet, a designer’s task is to create a favorable player experience.

This is why playtesting is so important. It is the most effective way to gauge the effects of rules changes when you are uncertain.

## Homeplay

Today we will practice iterating on an existing design, rather than starting from scratch. I want you to see first-hand the effects on a game when you change the mechanics.

Here are the rules for a simplified variant of the dice game called *Bluff* (also called *Liar’s Dice*, but known to most people as *that weird dice game that they played in the second Pirates of the Caribbean movie*):

-   Players: 2 or more, best with a small group of 4 to 6.

-   Objective: Be the last player with any dice remaining.

-   Setup: All players take 5 six-sided dice. It may also help if each player has something to hide their dice with, such as an opaque cup, but players may just shield their dice with their own hands. All players roll their dice, in such a way that each player can see their own dice but no one else’s. Choose a player to go first. That player must make a bid:

-   Bids: A "bid" is a player’s guess as to how many dice are showing a certain face, *among all players*. Dice showing the number 1 are "wild" and count as *all* other numbers. You cannot bid any number of 1s, only 2s through 6s. For example, "three 4s" would mean that between every player’s dice, there are *at least* three dice showing the number 1 or 4.

-   Increasing a bid: To raise a bid, the new bid must be *higher* than the previous. Increasing the number of dice is *always* a higher bid, regardless of rank (nine 2s is a higher bid than eight 6s). Increasing the rank is a higher bid if the number of dice is the *same or higher* (eight 6s is a higher bid than eight 5s, both of which are higher than eight 4s).

-   Progression of Play: On a player’s turn, that player may either raise the current bid, or if they think the most recent bid is incorrect, they can challenge the previous bid. If they raise the bid, play passes to the next player in clockwise order. If they challenge, the current round ends; all players reveal their dice, and the result is resolved.

-   Resolution of a round: If a bid is challenged but found to be correct (for example, if the bid was "nine 5s" and there are actually eleven 1s and 5s among all players, so there were indeed at least nine of them), the player who challenged the bid loses one of their dice. On subsequent rounds, that player will then have fewer dice to roll. If the bid is challenged *correctly* (suppose on that bid of "nine 5s" there were actually only eight 1s and 5s among all players), the player who made the incorrect bid loses one of their dice instead. Then, all players re-roll all of their remaining dice, and play continues with a new opening bid, starting with the player who won the previous challenge.

-   Game resolution: When a player has lost all of their dice, they are eliminated from the game. When all players (except one) have lost all of their dice, the one player remaining is the winner.

If you don’t have enough dice to play this game, you can use a variant: dealing cards from a deck, for example, or drawing slips of paper numbered 1 through 6 out of a container with many such slips of paper thrown in.

If you don’t have any friends, spend some time finding them. It will make it much easier for you to playtest your projects later in this course if you have people who are willing to play games with you.

At any rate, your first "assignment" here is to **play the game**. Take particular note of the dynamics and how they emerge from the mechanics. Do you see players bluffing, calling unrealistically high numbers in an effort to convince their opponents that they have more of a certain number than they actually do? Are players hesitant to challenge, knowing that any challenge is a risk and it is therefore safer to *not* challenge as long as you are not challenged yourself? Do any players calculate the odds, and use that information to influence their bid? Do you notice any feedback loops in the game as play progresses – that is, as a player starts making mistakes and losing dice, are they *more* or *less* likely to lose again in future rounds, given that they receive fewer dice and therefore have less information to bid on?

Okay, that last question kind of gave it away – yes, there is a positive feedback loop in this game. The effect is small, and noticeable mostly in an end-game situation where one player has three or more dice and their one or two remaining opponents only have a single die. Still, this gives us an opportunity to fiddle with things as designers.

Your next step is to **add, remove, or change one rule in order to remove the effect of the positive feedback loop**. Why did you choose the particular change that you did? What do you expect will happen – how will the dynamics change in response to your modified mechanic? Write down your prediction.

Then, **play the game again** with your rules modification. Did it work? Did it have any other side effects that you didn’t anticipate? How did the dynamics *actually* change? Be honest, and don’t be afraid if your prediction wasn’t accurate. The whole *point* of this is so you can see for yourself how hard it is to predict gameplay changes from a simple rules change, without actually playing.

Next, **share what you learned** with the community. [I have created a new page on the course Wiki](http://gamedesignconcepts.pbworks.com/L5-Homeplay). On that page, write the following:

1.  What was your rules change?

2.  How did you expect the dynamics of the game to change?

3.  How did they *really* change?

You don’t need to include much detail; a sentence or two for each of the three points is fine.

Finally, your last assignment (this is mandatory!) is to **read at least three other responses**. Read the rules change first, and without reading further, ask yourself how you think that rule change would modify gameplay. Then read the other person’s prediction, and see if it matches yours. Lastly, read what actually happened, and see how close you were.

You may leave your name, or you may post anonymously.

## Mini-Challenge

Take your favorite physical sport. Identify a positive or negative feedback loop in the game. Most sports have at *least* one of these. Propose a rule change that would eliminate it. Find a way to express it in less than 135 characters, and post to Twitter with the \#GDCU tag. You have until Thursday. One sport per participant, please!

