# JFlask
> ❄️ JFlask: Template for Flask RESTful API and management

## Server
>  RESTful API server with a systematic structure separated by resources for rapid development

- `flask-common`: common settings
- `flask-cors`: CORS 설정
- `flask-jwt-extended`: JWT 관리(Bearer)
- `flask-restplus`: REST API 구축과 Swagger 문서화
- `flask-pymongo`: MongoDB 데이터베이스 연동
- `validators`: 데이터 검증

### Structure

```
namespaces
├── test
│   ├── __init__.py
│   ├── models.py
│   └── resources
│       └── test.py
└── __init__.py
```

- `server.namespaces` 아래에는 API의 각 `Namespace`(네임스페이스)에 대한 모듈이 위치합니다.
- 하위 네임스페이스에서 리소스를 추가하기 위해서 `extend_namespace`로 `Namespace`를 확장한 뒤 `add_resources` 메소드를 사용합니다.
- `extend_namespace` 확장에 존재하는 `validate` 메소드는 `validator`에 따라 `ns.payload`의 필드를 검증합니다(실패 시 400).
  - `resources`는 `Resource`(리소스)에 대한 각각의 모듈을 가집니다.
  - `models`는 해당 네임스페이스의 리소스에서 사용하는 `Namespace.model`들을 가집니다.

## App for management
> Admin app with Vue.js
