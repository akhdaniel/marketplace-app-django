from django.shortcuts import render, render_to_response, RequestContext, Http404

from .models import Product, Category, ProductImage


def list_all(request):
    products = Product.objects.filter(active=True)
    return render_to_response("products/all.html", locals(), context_instance=RequestContext(request))


def edit_product(request, slug):
    instance = Product.objects.get(slug=slug)
    if request.user == instance.user:
        return render_to_response("products/edit.html", locals(), content_instance=RequestContext(request))
    else:
        raise Http404

def single(request, slug):
    product = Product.objects.get(slug=slug)

    images = product.productimage_set.all()

    categories = product.category_set.all()
    context = {
        "product": product,
        "categories": categories,
        "edit": True,
        "images": images,
    }


    return render_to_response("products/single.html", context, context_instance=RequestContext(request))