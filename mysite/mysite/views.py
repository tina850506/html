from django.shortcuts import render_to_response

def menu(request):
	food1 = {'name':'番茄炒蛋' , 'price':60 , 'comment':'delicious'}
	food2 = {'name':'蒜泥白肉' , 'price':100 , 'comment': 'hito'}
	food3 = {'name':'椒麻雞腿排' , 'price':180 , 'comment': 'spicy'}
	foods = [food1 , food2 , food3]
	return render_to_response('menu.html' , locals())

