from django.shortcuts import render


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Supplier


@csrf_exempt
def register_supplier(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body)

        supplier = Supplier.objects.create(
            verification_code=data.get("verificationCode"),
            company_name=data.get("companyName"),
            country=data.get("country"),
            state=data.get("state"),
            city=data.get("city"),
            company_type=data.get("companyType"),
            website=data.get("website"),

            sales_name=data.get("salesName"),
            email=data.get("email"),
            country_code=data.get("countryCode"),
            phone=data.get("phone"),

            categories=data.get("categories", []),
            other_category=data.get("otherCategory"),
            description=data.get("description"),

            catalog_url=data.get("catalogUrl"),
            catalog_files=data.get("catalogFiles"),

            moq=data.get("moq"),

            certifications=data.get("certifications", []),
            other_certs=data.get("otherCerts"),

            buyer_intent=data.get("buyerIntent", []),

            consent=data.get("consent", False)
        )

        return JsonResponse({"status": "success", "id": supplier.id})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
