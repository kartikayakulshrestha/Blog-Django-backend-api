<h1>Blogging Restfull API </h1>

<h2> BASE API </h2>

```markdown
| METHODS | Routes                         |
| GET     | http://127.0.0.1:8000/api/v1   | 

```
<h2> USER CREATION / DELETION / UPDATION / READING  </h2>

```markdown
| METHODS | Routes                                         |
| GET     | http://127.0.0.1:8000/api/v1/users             | List of all users
| GET     | http://127.0.0.1:8000/api/v1/users/{id}        | Unique user which are registered
| DELETE  | http://127.0.0.1:8000/api/v1/users             | Delete User
| GET     | http://127.0.0.1:8000/api/v1/users/{id}/blogs/ | Blogs which are related to userid
| POST    | http://127.0.0.1:8000/api/v1/users/            | CREATION OF USER
| PUT     | http://127.0.0.1:8000/api/v1/users/{id}/       | to change anything in users
| POST    | http://127.0.0.1:8000/api/v1/users/login       | cookies creation
| GET     | http://127.0.0.1:8000/api/v1/users/logout      | deletion of cookie
```

<h2> Blog (PAGINATION UNABLED)</h2>

```markdown
| METHODS | Routes                                           |
| GET     | http://127.0.0.1:8000/api/v1/blog/               | READ BLOGS (with pagination + like count + comment count )
| POST    | http://127.0.0.1:8000/api/v1/blog/               | CREATE OF BLOG
| PUT     | http://127.0.0.1:8000/api/v1/blog/{id}           | MODIFICATION of Blog
| DELETE  | http://127.0.0.1:8000/api/v1/blog/{id}           | DELETION OF BLOG
| GET     | http://127.0.0.1:8000/api/v1/blog/{id}           | (5 latest comment)
| POST    | http://127.0.0.1:8000/api/v1/blog/{id}/likes/    | like or unlike (you need to be logged in)
| GET     | http://127.0.0.1:8000/api/v1/blog/{id}/likes/    | list of user ids  (you need to be logged in)
| POST    | http://127.0.0.1:8000/api/v1/blog/{id}/comments/ | comments creation to specific blog id  (you need to be logged in)
| GET     | http://127.0.0.1:8000/api/v1/blog/{id}/comments/ | comments lists to specific blog id    (you need to be logged in) 
```







