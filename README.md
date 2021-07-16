# supervisord-spike
`프로세스`의 감시 기능과 관리 기능을 갖는 Superviord를 활용해 보자.

![purple-octopus-tattoo-design](https://user-images.githubusercontent.com/87116570/125969727-6640736c-7430-4bf3-bdb0-cdc0b033471b.jpeg)

## Acceptance Critieria 🧑‍⚖️
  - Supervisord 설정 정보를 이해한다.
  - 로컬에서 해당 테스트를 할 수 있고 확인할 수 있다.



## Getting Started
프로세스를 뛰어서 Supervisord의 설정방법을 익혀보자.
### Running dockerfile

- Building docker image
```
$ docker build -t supervisord .
```

- Running docker
```
$ docker run --rm -d -p 23233:23233 --name supervisord supervisord
```

- Accessing bash 
```
$ docker exec -it supervisord /bin/bash
$ ps -eaf
```

### Setup virtual environment
```
# set up virtual environment
$ PIPENV_VENV_IN_PROJECT=true pipenv install --three

# activate
$ pipenv shell
```

### Up & Running process for testing
```
$ python ./src/process_1.py
```

## Functionality
  - 시스템 죽을 때 재시작
  - 시스템이 죽을 때를 대비한 로깅
  - 백그라운드 옵션

## Reference
- [supervisord blog](https://medium.com/coinmonks/when-you-throw-a-web-crawler-to-a-devops-supervisord-562765606f7b)
- [supervisord docs](http://supervisord.org/introduction.html#overview)
- [supervisord github](https://github.com/Supervisor/supervisor)
