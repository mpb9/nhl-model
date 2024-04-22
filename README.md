# NHL Model

## _Personalized Complex Data_

### Power Ranks
_Power Ranks return values for each team at a given date_

_Each Power Rank can be transformed into a numerical ranking (ex. 1-32) if desired_

* **Implied**: Each team's average odds vs. every other team. Initially calculates average odds across all games against each particular opponent, sums those calculated averages, and divides by number of opponents faced over the given sample's timespan.

* **Implied Matchup**: Each team's average of their _ranked_ average odds vs. every other team. Initially ranks the calculated average odds across all games against each particular opponent compared to other teams, sums those calculated ranks, and divides by number of opponents faced over the given sample's timespan.

* **Implied Home/Away**: Similar to _Implied_, but only accounts for games where each team is Home or Away. _(can specify to use Implied Matchup)_

* **Home Ice Adjusted**: The difference between each team's base _Implied Home Rank_ from the mean _Implied Home Rank_ is added to the _Implied Rank_. _(can specify to use Implied Matchup)_

* **Home Ice Adjusted Matchup**: Similar to _Home Ice Adv_, but only takes into account games where each team plays eachother both Home and Away in the sample for determining _Implied Home Rank_

* **Strength of Schdule Adjusted Ranking Over Expectation**: The difference between each team's _Implied Rank_ and their Expected Rank based on their _SoS_. _(can specify to use Implied Matchup)_


### Home / Away Advantage

* **Implied**: Each team's _Implied Home/Away Rank_ subtracted by their base _Implied Rank_

_(method using Implied Matchup also available)_

### Strength of Schedule

* **Implied**: Sum of each team's number of games played against each opponent multiplied by that opponent's _Implied Rank_, then divided by their total games played.

_(method using Implied Matchup also available)_


## _Initalizing Datasets_

### Rolling Averages
```python
def rolling_avgs(
    df, num_games, include_null_next=True, suffix=True, add_objs=["season", "game_number", "is_home", "iceTime"],
):
```
```python
def season_avgs(
    df, suffix=True, add_objs=["season", "game_number", "is_home", "iceTime"],
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
    df, recent_num, past_num, add_objs=["season", "game_number", "is_home", "iceTime"], suffix=False,
):
```
```python
def trajectory_season(
    df, recent_num, add_objs=["season", "game_number", "is_home", "iceTime"], suffix=False,
):
```
```python
def trajectory_quick(
    recent_df, past_df, recent_num, past_num, is_season=False, add_objs=["season", "game_number", "is_home", "iceTime"], suffix=False,
):
```
```python
def trajectory_linear(
    df, num_games, add_objs=["season", "game_number", "is_home", "iceTime"], suffix=False,
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
