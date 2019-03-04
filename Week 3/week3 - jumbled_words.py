import random
def read_words_from_file():
    s = [];
    with open('words.txt') as file:
        for line in file:
            s.append(line.strip());
    return s;

def choose(words):
    return random.choice(words);

def jumble(s):
    return ''.join(random.sample(s,len(s)));

def check_answer(player,score,word):
    print(player, 'Your turn.');
    ans = input("What's on your mind? ");
    if(ans == word):
        print('Wow, You guessed it correct.');
        score += 1;
        print('Your score is ', score);
    else:
        print('I am afraid, You are wrong.');
        print('The correct answer is ',word);
        print('Your score is', score);
    return score;

def play(words):
    player1 = input('Player1 name? ');
    player2 = input('Player2 name? ');
    player1_score,player2_score = 0,0;
    turn = 0;
    repeat = True;
    while(repeat):
        word = choose(words);
        jumbled_word = jumble(word);
        print('\nJumbled word is ',jumbled_word);
        if not turn%2:
            player1_score = check_answer(player1,player1_score,word);
        else:
            player2_score = check_answer(player2,player2_score,word);
        turn += 1;
        print();
        repeat = int(input('Press 0 to quit and 1 to continue! '));
    print();
    print(player1 + ' is the winner' if player1_score > player2_score\
          else player2+ ' is the winner' if player1_score != player2_score\
          else "It's a tie, What a game!!");
    print(player1, ', Your score is ',player1_score);
    print(player2, ', Your score is ',player2_score);
            
words = read_words_from_file();
play(words);
