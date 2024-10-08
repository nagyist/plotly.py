import _plotly_utils.basevalidators


class DomainValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="domain", parent_name="layout.map", **kwargs):
        super(DomainValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Domain"),
            data_docs=kwargs.pop(
                "data_docs",
                """
            column
                If there is a layout grid, use the domain for
                this column in the grid for this map subplot .
            row
                If there is a layout grid, use the domain for
                this row in the grid for this map subplot .
            x
                Sets the horizontal domain of this map subplot
                (in plot fraction).
            y
                Sets the vertical domain of this map subplot
                (in plot fraction).
""",
            ),
            **kwargs,
        )
