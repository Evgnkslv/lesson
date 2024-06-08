from your_module import String_utils

def test_capitilize():
    utils = String_utils()
    assert utils.capitalize("skypro") == "Skypro"

def test_trim():
    utils = String_utils()
    assert utils.trim("   skypro") == "skypro"

def test_to_list():
    utils = String_utils()
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]

def test_contains():
    utils = String_utils()
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "U") is False

def test_delete_symbol():
    utils = String_utils()
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

def test_starts_with():
    utils = String_utils()
    assert utils.starts_with("SkyPro", "S") is True
    assert utils.starts_with("SkyPro", "P") is False

def test_end_with():
    utils = String_utils()
    assert utils.end_with("SkyPro", "o") is True
    assert utils.end_with("SkyPro", "y") is False

def test_is_empty():
    utils = String_utils()
    assert utils.is_empty("") is True
    assert utils.is_empty(" ") is True
    assert utils.is_empty("SkyPro") is False

def test_list_to_string():
    utils = String_utils()
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"