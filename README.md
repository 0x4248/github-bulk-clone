# Github Bulk Clone

Quickly Download all of a users or organisations public repository's.

Forget the hassle of cloning one by one.

## Usage

Downloading a users or organisations public repository's is really simple. When you start the downloading git will download each project in the current working directory.

```
 - main.py
 /repo 1 <-- This would be the name of the repo.
 /repo 2
```


### Downloading a users or organisations public repository's

```bash
python3 main.py -u <username>
```

### Downloading a organisations public repository's

```bash
python3 main.py -o <organisation>
```

### Exclude

With exclude you can exclude certain repository's from being downloaded by git.

```bash
python3 main.py -u <username> --exclude=<repository>
```

Note: You can use a comma separated list of repository's to exclude. e.g: `--exclude=linux,git,vim`

## Dependencies
- Python 3.8+
- Git
- A working internet connection
- A working git configuration
- Your api.github.com rate limit is not going to be exceeded. (if it is you will get an error)