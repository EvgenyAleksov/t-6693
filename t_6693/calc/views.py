from django.core.cache import cache  # type: ignore
from django.shortcuts import render  # type: ignore
from django.views.generic import TemplateView  # type: ignore
from django_renderpdf.views import PDFView  # type: ignore

from .calc import calc_num, get_comp  # type: ignore
from .forms import CalcForm_1, CalcForm_2


class Calc_1_View(TemplateView):
    template_name = "calc/calc_1.html"

    def get(self, request, *args, **kwargs):
        form = CalcForm_1()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            submitbutton = request.POST.get("submit")
            resetbutton = request.POST.get("reset")

            form = CalcForm_1(request.POST or None)
            if form.is_valid():
                sex = form.cleaned_data.get("sex")
                sex = "Мужчина" if sex == 1 else "Женщина"
                name = form.cleaned_data.get("name")
                bd = form.cleaned_data.get("birthday")
                res = calc_num(bd)
                context = {
                    "form": form,
                    "sex": sex,
                    "name": name,
                    "res": res,
                    "submitbutton": submitbutton,
                    "resetbutton": resetbutton,
                }
                cache.set("sex", sex)
                cache.set("name", name)
                cache.set("res", res)
                return render(request, self.template_name, context)
        else:
            form = CalcForm_1()
        return render(request, self.template_name, {"form": form})


class Calc_1_PDF_View(PDFView):
    template_name = "calc/calc_1_pdf.html"

    def get_context_data(self):
        context = {
            "sex": cache.get("sex"),
            "name": cache.get("name"),
            "res": cache.get("res"),
            }
        return context


class Calc_2_View(TemplateView):
    template_name = "calc/calc_2.html"

    def get(self, request, *args, **kwargs):
        form = CalcForm_2()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            submitbutton = request.POST.get("submit")
            resetbutton = request.POST.get("reset")

            form = CalcForm_2(request.POST or None)
            if form.is_valid():
                name_1 = form.cleaned_data.get("name_1")
                name_1 = "Партнёр 1" if name_1 == "" else name_1
                name_2 = form.cleaned_data.get("name_2")
                name_2 = "Партнёр 2" if name_2 == "" else name_2
                bd_1 = form.cleaned_data.get("birthday_1")
                bd_2 = form.cleaned_data.get("birthday_2")
                res_1 = calc_num(bd_1)
                res_2 = calc_num(bd_2)
                res_comp_comm = (
                    ""
                    if res_1["comm"] is None or res_2["comm"] is None
                    else get_comp(str(res_1["comm"].id) + str(res_2["comm"].id))
                )
                res_comp_miss = (
                    ""
                    if res_1["miss"] is None or res_2["miss"] is None
                    else get_comp(str(res_1["miss"].id) + str(res_2["miss"].id))
                )
                context = {
                    "form": form,
                    "name_1": name_1,
                    "name_2": name_2,
                    "res_1": res_1,
                    "res_2": res_2,
                    "res_comp_comm": res_comp_comm,
                    "res_comp_miss": res_comp_miss,
                    "submitbutton": submitbutton,
                    "resetbutton": resetbutton,
                }
                if request.user.is_authenticated is True:
                    cache.set("status", True)
                else:
                    cache.set("status", False)
                cache.set("name_1", name_1)
                print("name_1 = ", name_1) 
                cache.set("name_2", name_2)
                cache.set("res_1", res_1)
                cache.set("res_2", res_2)
                cache.set("res_comp_comm", res_comp_comm)
                cache.set("res_comp_miss", res_comp_miss)
                return render(request, self.template_name, context)
        else:
            form = CalcForm_2()
        return render(request, self.template_name, {"form": form})


class Calc_2_PDF_View(PDFView):
    template_name = "calc/calc_2_pdf.html"

    def get_context_data(self):
        context = {
            "status": cache.get("status"),
            "name_1": cache.get("name_1"),
            "name_2": cache.get("name_2"),
            "res_1": cache.get("res_1"),
            "res_2": cache.get("res_2"),
            "res_comp_comm": cache.get("res_comp_comm"),
            "res_comp_miss": cache.get("res_comp_miss"),
            }
        return context
