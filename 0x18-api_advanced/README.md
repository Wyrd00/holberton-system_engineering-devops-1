
# 0x18. API advanced

This project is about using Reddit's public API to find endpoints, deal with pagination, parse JSON results and use recursion to make API calls.

## Environment
The python files have been tested on Ubuntu 14.05.5 LTS with Python3 and style checked with Pep8.

Tests done in VirtualBox on [Ubuntu](https://atlas.hashicorp.com/ubuntu/boxes/trusty64) via [Vagrant](https://www.vagrantup.com/)(1.9.1)

## Repository Breakdown
Once cloned over, the repository will contain the following files:

|   **File**    |  **Decription**                       |
|---------------|---------------------------------------|
| 0-subs.py   | Function that queries api and returns the number of subscribers for a given subreddit |
| 1-top_ten.py | Function that queries api and prints the titles of the first 10 hot posts listed for a given subreddit |
| 2-recurse.py | Recursive function that queries api and return a list of the titles of all hot articles for a given subreddit |
| 100-count.py | Recurise function that queries the api, parses the titles of all hot articles and prints a sorted count of given keywords *Not yet implemented* |
| Test Folder | Contains test files to run each function |


## How to Use
### How many subs?
#### 0-subs.py
To use the `def number_of_subscribers(subreddit)` function, run the `0-main.py` file and pass in a valid subreddit:
```
$ python3 0-main.py programming
$ 756024 
```
If the subreddit passed in is not a valid subreddit, function returns 0

```
$ python3 0-main.py this_is_a_fake_subreddit
$ 0
```
### Top Ten
#### 1-top_ten.py
To use the `def top_ten(subreddit)` function, run the `1-main.py` file and pass in a valid subreddit:
```
$ python3 1-main.py programming
$ Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
Spend effort on your Git commits
It's a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
From the D Blog: Introspection, Introspection Everywhere
Do MVC like it’s 1979
GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
Google Bug Bounty - The 5k Error Page
PyCon 2017 Talk Videos 
```
If the subreddit passed in is not a valid subreddit, function prints `None`.

```
$ python3 1-main.py this_is_a_fake_subreddit
$ None
```
### Recurse It!
#### 2-recuse.py
To use the `def recurse(subreddit, hot_list=[])` function, run the `2-main.py` file and pass in a valid subreddit:
*Main file counts the number of elements in the hot_list*
```
$ python3 2-main.py programming
$ 932
```
If the subreddit passed in is not a valid subreddit, function prints `None`.

```
$ python3 2-main.py this_is_a_fake_subreddit
$ None
```

## Known Bugs
There are no known bugs at the time.

### Author
*Kimberly Wong* - [Github](https://github.com/kjowong) || [Twitter](https://twitter.com/kjowong) || [email](kimberly.wong@holbertonschool.com)


#### Feedback and contributors welcomed.
