# NHL Model
## Initalizing Datasets
### **_Rolling Averages_**
* PREVIOUS X GAMES 
  
  **get_rolling_avgs**(df, _number of games, include_null_next=True, suffix=True, add_objs=["season", "game_number"]_)

* SEASON TO DATE

  **get_season_avgs**(df, _suffix=True, add_objs=["season", "game_number"]_)

### **_Trajectory_**
* PREVIOUS X GAMES vs. SEASON TO DATE

  **get_trajectory_quick**(df_rolling, df_szn, _recent_num, past_num, is_season=**True**, add_objs=["season", "game_number"], suffix=False_)

* PREVIOUS X GAMES vs. PREVIOUS Y GAMES

  **get_trajectory_quick**(df_rolling_X, df_rolling_Y, _recent_num, past_num, is_season=**False**, add_objs=["season", "game_number"], suffix=False_)
## Python Info
* _Virtual Environment_: **myenv\Scripts\activate**
* _Jupyter Notebook_: **jupyter notebook**
