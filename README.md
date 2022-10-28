# work_time_calculator
## Usage
```
$ docker build . -t work_time_calculator
$ docker run -it -v ${PWD}:/work work_time_calculator /bin/bash
$ cd work/
$ python -m work_time_calculator

所定労働日数: 20 day
月規定労働時間: 160 h
実働日数: 19 day
必須労働時間: 152 h


$ python -m work_time_calculator --hour 153 --time 35

所定労働日数: 20 day
月規定労働時間: 160 h
実働日数: 19 day
必須労働時間: 152 h
差分: +1時間35分
```
