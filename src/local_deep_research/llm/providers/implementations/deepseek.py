"""DeepSeek LLM provider for Local Deep Research.

Supports deepseek-v4-flash (fast, cost-effective) and deepseek-v4-pro
(premium reasoning) models, plus legacy deepseek-chat and deepseek-reasoner.
"""

from ..openai_base import OpenAICompatibleProvider


class DeepseekProvider(OpenAICompatibleProvider):
    """DeepSeek provider using OpenAI-compatible endpoint.

    Recommended models:
    - deepseek-v4-flash: Fast, cost-effective model for most research tasks
    - deepseek-v4-pro: Premium model for complex reasoning
    - deepseek-reasoner: Legacy DeepSeek-R1 reasoning model
    - deepseek-chat: Legacy DeepSeek-V3 chat model
    """

    provider_name = "DeepSeek"
    api_key_setting = "llm.deepseek.api_key"
    default_base_url = "https://api.deepseek.com/v1"
    default_model = "deepseek-v4-flash"

    # Metadata for auto-discovery
    provider_key = "DEEPSEEK"
    company_name = "DeepSeek"
    is_cloud = True

    @classmethod
    def requires_auth_for_models(cls):
        """DeepSeek requires authentication for listing models."""
        return True
