# Classes

# • User

## methods

| method   | params | return  |
|----------|--------|---------|
| sign_up  |        | SignUp  | |
| sign_in  |        | SignIn  | |
| sign_out |        | SignOut | |
| device   |        | Device  | |

## `SignUp`

## methods

| method  | params                             | return |
|---------|------------------------------------|--------|
| execute | username: string, password: string |        | |

## properties

| property    | return  |
|-------------|---------|
| status_code | integer | |

## `SignIn`

## methods

| method  | params                                                  | return |
|---------|---------------------------------------------------------|--------|
| execute | username: string, password: string, expiration: integer |        | |

## properties

| property    | return  |
|-------------|---------|
| status_code | integer | |
| get_token   | integer | |

## `SignOut`

## methods

| method  | params        | return |
|---------|---------------|--------|
| execute | token: string |        | |

## properties

| property    | return  |
|-------------|---------|
| status_code | integer | |

# • Report

## methods

| method | params | return |
|--------|--------|--------|
| create |        | Create | |

## `Create`

## methods

| method  | params                                              | return |
|---------|-----------------------------------------------------|--------|
| execute | token: string, issue: string, inventory_number: int |        | |

## properties

| property    | return  |
|-------------|---------|
| status_code | integer | |

# • Device

## methods

| method                  | params | return                     |
|-------------------------|--------|----------------------------|
| get_by_inventory_number |        | DeviceGetByInventoryNumber | |

## `DeviceGetByInventoryNumber`

## methods

| method  | params                   | return |
|---------|--------------------------|--------|
| execute | inventory_number: string |        | |

## properties

| property                  | return   |
|---------------------------|----------|
| status_code               | integer  | |
| response.id               | integer  | |
| response.inventory_number | string   | |
| response.object_name      | string   | |
| response.year_issue       | datetime | |
| response.floor            | integer  | |
| response.office_number    | string   | |

## Example:

```python
from src.core.classes.user import User

def sign_up():
    user_obj = User().sign_up()
    user_obj.execute(USERNAME, PASSWORD)
    user_obj.status_code

def sign_in():
    user_obj = User().sign_in()
    user_obj.execute(USERNAME, PASSWORD, EXPIRATION)
    user_obj.status_code
    user_obj.get_token

def sign_out():
    user_obj = User().sign_out()
    user_obj.execute(TOKEN)
    user_obj.status_code

def report_create():
    obj = Report().create()
    obj.execute(TOKEN, ISSUE, INVENTORY_NUMBER)
    obj.status_code

def device():
    obj = User().device().get_by_inventory_number()
    obj.execute(INVENTORY_NUMBER)
    obj.status_code
    obj.response.id
    obj.response.inventory_number
    obj.response.object_name
    obj.response.year_issue
    obj.response.floor
    obj.response.office_number
```

# • TemplateIssue
## methods

| method   | params | return  |
|----------|--------|---------|
| get |        | TemplateIssueGet | |

## `TemplateIssueGet`

## methods

| method  | params                             | return |
|---------|------------------------------------|--------|
| execute | username: string, password: string |        | |

## properties

| property    | return  |
|-------------|---------|
| status_code | integer | |
| response | string (json) | |

```python
from src.core.classes.template_issue import TemplateIssue

def template_issue():
    __obj = TemplateIssue()
    obj = __obj.get()
    obj.execute()
    obj.status_code
    obj.response
```

```json
{
    "categories": [
        {
            "category": "Text",
            "list": [
                "issue_id": 1,
                "issue": "Text",
                "solution": "Text"
            ]
        }
    ]
}
```
