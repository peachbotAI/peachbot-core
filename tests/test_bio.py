from core.engine.runner import execute


def test_bio_gnn_detection():
    result = execute("bio", {"text": "gnn protein interaction"})

    assert "state" in result
    assert "alert" in result
    assert result["alert"]["level"] == "INFO"
    assert "graph" in result["alert"]["message"].lower()


def test_bio_gene_signal():
    result = execute("bio", {"text": "gene expression analysis"})

    assert result["state"]["entity_type"] == "gene"
    assert "gene" in result["alert"]["message"].lower()


def test_bio_no_signal():
    result = execute("bio", {"text": "random text"})

    assert result["alert"]["level"] == "INFO"