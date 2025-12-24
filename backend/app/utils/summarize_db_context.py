from langchain_core.messages import HumanMessage, SystemMessage, AnyMessage
from ..llm.model import get_llm

MAX_RECENT_MESSAGES = 7
SUMMARIZE_AFTER = 10

def summarize_messages(
    old_messages: list[AnyMessage],
    existing_summary: str | None
) -> str:
    llm = get_llm()

    system = SystemMessage(
        content="Summarize the conversation for long-term memory. Be concise."
    )

    human = HumanMessage(
        content=(
            f"Existing summary:\n{existing_summary or 'None'}\n\n"
            f"New messages:\n" +
            "\n".join(
                f"{m.type}: {m.content}" for m in old_messages
            )
        )
    )

    return llm.invoke([system, human]).content
