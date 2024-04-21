from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Chat
from accounts.models import CustomUser


def chat(request):
    return render(request, 'chat.html')

def connect_contact(request, pk):
    user = CustomUser.objects.get(pk = pk)
    Chat.objects.create(
        from_user = request.user,
        to_user = user,
        message = f"{request.user} - sizni kontaktga qo`shdi"
    ).save()
    return redirect('chat')
    
def your_view(request):
    if request.method == 'POST':
        
        data = request.POST
        message = data.get("message", None)
        partner = data.get("partner", None)
        
        to_user = CustomUser.objects.get(id = partner)
        Chat.objects.create(from_user = request.user, to_user = to_user, message=message).save()
        
        response_data = { 'message': 'Data received successfully!', 'data': "Salomde"}
        return JsonResponse(response_data)
    elif request.method == 'GET':
        
        pass

    else:
        return JsonResponse({'error': 'Unsupported method'}, status=405)  # Handle invalid methods


def get_history(request, pk):
    data = Chat.objects.filter(from_user = request.user, to_user__id = pk) | Chat.objects.filter(from_user__id = pk, to_user = request.user)
    partner = CustomUser.objects.get(pk = pk)
    return render(request, 'chat.html', context={"chats": data, "partner":partner}, )

def get_history_js(request, pk):
    data = Chat.objects.filter(from_user = request.user, to_user__id = pk) | Chat.objects.filter(from_user__id = pk, to_user = request.user)
    partner = CustomUser.objects.get(pk = pk)
    res = []
    for d in data:
        res.append({
            d.id : {
                "from_user" : d.from_user.fullname,
                "to_user" : d.to_user.fullname,
                "message" : d.message,
                "created_at" : d.created_at
            }}
        )
    return JsonResponse({"status":200, "message_list": res})

def get_chat_list(request):
    if request.method =='GET':
        data = Chat.objects.filter(to_user=request.user) | Chat.objects.filter(from_user=request.user)
    
        res = []
        keyss = []
        for item in data:
            if item.to_user == request.user:
                user = item.from_user
            else:
                user = item.to_user
            
            
            if not user.id in keyss:
                keyss.append(user.id)
                res.append({
                user.id: {
                    "phonenumber": user.phonenumber,
                    "fullname": user.fullname
                }
            })
        
        return JsonResponse({'message': "200", "chat_list": res})
        
        
def connect_new_user(request):
    return render(request, 'user_list.html', context={"users": CustomUser.objects.all()})