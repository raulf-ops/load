player_info =  { "name":"brice","age": 25,"hp": 100
    
}

ai_info =  { "name":"AI","age": 30,"hp": 150
     }
print(f"Player: {player_info['name']} | HP: {player_info['hp']}")
print(f"AI: {ai_info['name']} | HP: {ai_info['hp']}")

if player_info['hp'] > ai_info['hp']:
    print(f"{player_info['name']} wins!")
else:
    print(f"{ai_info['name']} wins!")
