### Pretty JSON responses from ROS2

I found ROS2 responses difficult to read during development on command-line.

Install requirements using:
```
pip3 install -r requirements.txt
```

Set an alias (e.g. in ~/.bashrc) as
```
alias pr='python3 ${path_to_pretty_ros2_responses_dir}'
```

Then pipe ROS2 service calls as:
```
ros2 service call /service/list msgs/srv/ServiceList '{}' | pr
```

Instead of the default response formatting:
```
...
response:
msgs.srv.Srv_Response(loaded=[], backups=[msgs.msg.Msg(id='171', updated_at='2024-05-31 17:14:45', path='/backup/path/1.db3'), msgs.msg.Msg(id='171', updated_at='2024-06-03 11:00:38', path='/backup/path/2.db3')], error=msgs.msg.ErrorMsg(error_code=0, error_msg=''))
```

Yielding formatted response:
```
{
  "loaded": [],
  "backups": [
    {
      "id": "171",
      "updated_at": "2024-05-31 17:14:45",
      "path": "/backup/path/1.db3"
    },
    {
      "id": "171",
      "updated_at": "2024-06-03 11:00:38",
      "path": "/backup/path/2.db3"
    }
  ],
  "error": {
    "error_code": 0,
    "error_msg": ""
  }
}
```

Is there another way to achieve this. Probably. I personally feel JSON should be default.