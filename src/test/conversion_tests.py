import pytest

from src.methods import convert_ros2_response_to_json_s as to_json_s
from src.methods import format_json

@pytest.mark.parametrize(
    ("input", "expected_output"),
    [
        ("()", "{}"),
        ("(a=123)", '{"a": 123}'),
        ("type.a(key='value')", '{"key": "value"}'),
        ("a.b(x=1, y='2', z=1.0)", '{"x": 1, "y": "2", "z": 1.0}'),
        ("a.b(x=c.d(y=123, z='a'))", '{"x": {"y": 123, "z": "a"}}'),
        ("c.d(a=[])", '{"a": []}'),
        ("c.d(a=[error.type(code=1, message='failed')])", '{"a": [{"code": 1, "message": "failed"}]}'),
        ("a.b(key=\"Don't do it.\")", '{"key": "Don\'t do it."}'),
        ("a.b(key='This seems \"odd\".')", '{"key": "This seems \\"odd\\"."}'),
        ("a.b(key='Don\\'t this seem \"odd\".')", '{"key": "Don\'t this seem \\"odd\\"."}'),
        (
                "msgs.srv.Srv_Response(loaded=[], backups=[msgs.msg.Msg(id='171', updated_at='2024-05-31 17:14:45', "
                "path='/backup/path/1.db3'), msgs.msg.Msg(id='171', updated_at='2024-06-03 11:00:38', "
                "path='/backup/path/2.db3')], error=msgs.msg.ErrorMsg(error_code=0, error_msg=''))",
                '{"loaded": [], "backups": [{"id": "171", "updated_at": "2024-05-31 17:14:45", '
                '"path": "/backup/path/1.db3"}, {"id": "171", "updated_at": "2024-06-03 11:00:38", '
                '"path": "/backup/path/2.db3"}], "error": {"error_code": 0, "error_msg": ""}}'
        )
    ]
)
class TestConversionAndFormat:

    def test_conversion_and_format(self, input, expected_output):
        json_s = to_json_s(input)
        if not json_s == expected_output:
            raise AssertionError(json_s, expected_output)
        print(format_json(json_s))
