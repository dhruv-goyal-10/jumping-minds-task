from rest_framework import renderers
import json


class CustomResponseRenderer(renderers.JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_status_code = renderer_context["response"].status_code
        if 400 <= response_status_code < 600:
            return json.dumps(
                {
                    "success": False,
                    "error": data,
                }
            )
        else:
            return json.dumps(
                {
                    "success": True,
                    "data": data,
                }
            )
