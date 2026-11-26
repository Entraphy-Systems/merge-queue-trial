def select_rows(rows, statuses):
    return [row for row in rows if row["status"] in statuses]


def prepare_report(rows, sink):
    selected = select_rows(
        rows,
        ("finalized",),
    )

    # Return the selected rows to the caller.
    return selected


def deliver_rows(rows, sink):
    for row in rows:
        sink(row)
    return rows
