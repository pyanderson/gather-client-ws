import types
from random import randint

from gather_client_ws.helpers import camel_to_snake, snake_to_camel

from .events_pb2 import ClientServerAction


def get_txn_id():
    return randint(0, 4294967295)


def get_type(descriptor):
    if descriptor.type == descriptor.TYPE_BOOL:
        return bool
    if descriptor.type == descriptor.TYPE_STRING:
        return str
    if descriptor.type == descriptor.TYPE_BYTES:
        return bytes
    if descriptor.type in [descriptor.TYPE_DOUBLE, descriptor.TYPE_FLOAT]:
        return float
    return int


def get_available_actions():
    actions = []
    fields = ClientServerAction.DESCRIPTOR.fields_by_name
    for field_name, field_descriptor in fields.items():
        # The only primitive field is the txnId, it is safe to ignore it here
        if field_descriptor.message_type is None:
            continue
        action_args = []
        action_descriptor = field_descriptor.message_type
        for name, descriptor in action_descriptor.fields_by_name.items():
            if descriptor.message_type is None:  # is primitive
                action_args.append({name: get_type(descriptor)})
                continue
            action_args.append({name: descriptor.message_type._concrete_class})
        actions.append(
            {
                "name": field_name,
                "args": action_args,
                "class": field_descriptor.message_type._concrete_class,
            }
        )
    return actions


def create_action_method(action):
    async def method(client, *args, **kwargs):
        params = {}
        for value, arg in zip(args, action["args"]):
            params[next(iter(arg))] = value
        for key, value in kwargs.items():
            params[snake_to_camel(key)] = value
        data = action["class"](**params)
        _action = ClientServerAction(
            txnId=get_txn_id(), **{action["name"]: data}
        )
        await client._ws.send(_action.SerializeToString())

    args_doc = "\n".join(
        f"\t{camel_to_snake(name)} ({_type.__name__})"
        for arg in action["args"]
        for name, _type in arg.items()
    )

    method.__doc__ = f"{camel_to_snake(action['name'])}\nArgs:\n{args_doc}"

    return method


def set_actions_methods(client):
    actions = get_available_actions()
    actions_names = []
    for action in actions:
        name = camel_to_snake(action["name"])
        actions_names.append(name)
        setattr(
            client,
            name,
            types.MethodType(create_action_method(action), client),
        )
    client.available_actions = actions_names
