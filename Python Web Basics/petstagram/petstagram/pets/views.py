from django.shortcuts import render, redirect
from petstagram.pets.models import Pet, Like
from petstagram.pets.create_pet_form import CreatePetForm


# Create your views here.


def list_pets(request):
    all_pets = Pet.objects.all()

    context = {
        "pets": all_pets,
    }

    return render(request, 'pets_page_template/index.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet_likes_count = pet.like_set.count

    context = {
        "pet": pet,
        "pet_likes_count": pet_likes_count,
    }

    return render(request, 'pets_details_template/index.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    like = Like(
        pet=pet
                )
    like.save()

    return redirect('pet details', pet.id)


def create_pet(request):
    if request.method == 'GET':
        form = CreatePetForm()
        context = {
            'form': form,
        }

        return render(request, 'pet_create.html', context)
    else:
        form = CreatePetForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list pets')


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = CreatePetForm(initial=pet.__dict__)
        context = {
            'form': form,
        }

        return render(request, 'pet_edit.html', context)
    else:
        form = CreatePetForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            return redirect('pet details', pet.id)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'pet_name': pet.name,
        }

        return render(request, 'pet_delete.html', context)

    else:
        pet.delete()
        return redirect('list pets')

