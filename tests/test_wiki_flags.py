from flaggart.wiki_flags import selectpage
import pytest

def test_selectpage_basic():
    assert selectpage("Scotland", ['Flag of Scotland']) == 'Flag of Scotland'