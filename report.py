def select_rows(rows, statuses):
    return [row for row in rows if row["status"] in statuses]


def prepare_report(rows, sink):
    selected = select_rows(
        rows,
        ("finalized",),
    )

    # Deliver the selected rows to the fixture sink.
    return deliver_rows(selected, sink)


def deliver_rows(rows, sink):
    for row in rows:
        sink(row)
    return rows
