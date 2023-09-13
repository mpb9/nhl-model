# NHL Model

## _Initalizing Datasets_

### Rolling Averages
```python
def rolling_avgs(
    df, num_games, include_null_next=True, suffix=True, add_objs=["season", "game_number"],
):
```
```python
def season_avgs(
    df, suffix=True, add_objs=["season", "game_number"],
):
```
> _previous **X** games_
```python
rolling_avgs(df, num_games)
```
> _season to date_
```python
season_avgs(df)
```

### Trajectory
```python
def trajectory(
    df, recent_num, past_num, add_objs=["season", "game_number"], suffix=False,
):
```
```python
def trajectory_season(
    df, recent_num, add_objs=["season", "game_number"], suffix=False,
):
```
```python
def trajectory_quick(
    recent_df, past_df, recent_num, past_num, is_season=False, add_objs=["season", "game_number"], suffix=False,
):
```
>  _previous **X** VS. **Y** games_
```python
trajectory(df, recent_num, past_num)
```
```python
trajectory_quick(df_X, df_Y, recent_num, past_num, False)
```
> _previous **X** games VS. season to date_
  ```python
trajectory_season(df, recent_num)
  ```
```python
trajectory_quick(df_X, df_szn, recent_num, past_num, False)  
```

## _Command Line_
> _Virtual Environment_:
```console
myenv\Scripts\activate
```
```console
deactivate
```
> _Jupyter Notebook_:
```console
jupyter notebook
```
