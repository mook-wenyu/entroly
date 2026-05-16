from entroly.dashboard import _cogops_unavailable_snapshot


def test_cogops_unavailable_snapshot_is_dashboard_safe():
    snap = _cogops_unavailable_snapshot("No module named 'entroly_core'")

    assert snap["engine"] == "unavailable"
    assert snap["status"] == "native_module_missing"
    assert snap["total_beliefs"] == 0
    assert "entroly-core" in snap["hint"]
