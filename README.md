# NHL Model

## _Initalizing Datasets_

### Rolling Averages
> METHODS
```python
def rolling_avgs(
    df, num_games, include_null_next=True, suffix=True, add_objs=["season", "game_number"],
):
```
```python
def season_avgs(
    df, suffix=True, add_objs=["season", "game_number"]
):
```

> PREVIOUS X GAMES  
```python
get_rolling_avgs(df, number of games, include_null_next=True, suffix=True, add_objs=["season", "game_number"])
```

> SEASON TO DATE  
```python
get_season_avgs(df, suffix=True, add_objs=["season", "game_number"])
```

### Trajectory
> METHODS
```python
def trajectory(
    df, recent_num, past_num, add_objs=["season", "game_number"], suffix=True,
):
```
```python
def trajectory_season(
    df, recent_num, add_objs=["season", "game_number"], suffix=True,
):
```
```python
def trajectory_quick(
    recent_df, past_df, recent_num, past_num, is_season=False, add_objs=["season", "game_number"], suffix=False,
):
```

> PREVIOUS X GAMES vs. PREVIOUS Y GAMES
```python
trajectory(df, recent_num, past_num)
```
```python
trajectory_quick(df_X, df_Y, recent_num, past_num, False)
```

> PREVIOUS X GAMES vs. SEASON TO DATE
```python
trajectory_season(df, recent_num)
```
```python
trajectory_quick(df_X, df_szn, recent_num, past_num, True)  
```

## _Command Line_
> _Virtual Environment_:
```console
myenv\Scripts\activate
```
> _Jupyter Notebook_:
```console
jupyter notebook
```
