# rosgraph_yaml


## How To run

- command
```bash
python3 ./rosgraph_parse.py "$(for node in $(rosnode list); do rosnode info -q ${node}; done)"
```

- result
```
/rosout:
  publish:
  - name: /rosout_agg
    type: rosgraph_msgs/Log
  subscribe:
  - name: /rosout
    type: rosgraph_msgs/Log
/static_transform_publisher_1681132769971738643:
  publish:
  - name: /rosout
    type: rosgraph_msgs/Log
  - name: /tf
    type: tf2_msgs/TFMessage
  subscribe: []
```

- test
```
./main.py "$(cat ./test_input.txt)"
```