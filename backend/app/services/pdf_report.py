from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import os


def generate_pdf_report(
    filename,
    analysis,
    ai_report,
    output_path
):

    doc = SimpleDocTemplate(
        output_path
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Network Troubleshooter Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Filename: {filename}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Packet Count: {analysis['packet_count']}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Protocols",
            styles["Heading2"]
        )
    )

    for proto, count in analysis["protocols"].items():

        content.append(
            Paragraph(
                f"{proto}: {count}",
                styles["Normal"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "AI Diagnostic Report",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            ai_report.replace(
                "\n",
                "<br/>"
            ),
            styles["BodyText"]
        )
    )

    doc.build(content)

    return output_path