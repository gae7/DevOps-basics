import app
from click.testing import CliRunner



def test_app():
    runner = CliRunner()
    result = runner.invoke(app.make_set_operations, "1,2,3 4,5,6")
    assert "intersection: set()" in result.output