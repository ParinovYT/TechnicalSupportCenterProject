# Classes

# • User
## methods
| method | params | return |
| - | - | - |
| sign_up | | SignUp | |
| sign_in | | SignIn | |

## `SignUp`
## methods
| method | params | return |
| - | - | - |
| execute | username: string, password: string | | |

## properties
| property | return |
| - | - |
| status_code | integer | |

## `SignIn`
## methods
| method | params | return |
| - | - | - |
| execute | username: string, password: string, expiration: integer | | |

## properties
| property | return |
| - | - |
| status_code | integer | |
| get_token | integer | |

## Example:
```python
def sign_up():
    user_obj = User().sign_up()
    user_obj.execute(USERNAME, PASSWORD)
    user_obj.status_code

def sign_in():
    user_obj = User().sign_in()
    user_obj.execute(USERNAME, PASSWORD, EXPIRATION)
    user_obj.status_code
    user_obj.get_token
```
