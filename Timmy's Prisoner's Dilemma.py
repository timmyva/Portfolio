    elif player == 5:
        if getting_team_name:
            return 'The Bomb Squad - Kristen and Timothy'
        else:
            if len(opponent_history)==0: #In the first round: collude
                return 'c'
            elif opponent_history[-1]=='c':
                    return 'b'
            else:
                return 'b' # colludes unless I was betrayed.
            if opponent_history == 'c':
                return 'c'
            # if the oponent betrays, I betray to lose them pionts to. 