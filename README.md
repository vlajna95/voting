# Voting API 

A simple yet hopefully useful voting API, with Djoser used to handle authentication. 

Every poll can have many questions, and any question can have many choices/options. 

**Note: There is no frontend!** 


## Instructions 

After creating and activating your virtual environment, you should clone this repo, enter the newly created directory and install the requirements from the provided file. 

```bash
git clone https://github.com/vlajna95/voting.git
cd voting/
python -m pip install -r requirements.txt
```

Then execute the standard Django commands to create the database and add a super user. The polls app comes with the initial migration, so you can skip the _makemigrations_ command. 

```bash
python manage.py migrate
python manage.py createsuperuser
```

If you're lazy to add data on the admin site or lacking creativity :wink: you can use the fixtures provided in the polls app. 

```bash
python -Xutf8 manage.py loaddata polls_sr
```

As the name of the fixtures file suggests, the data is in serbian. You can change the language of the project in the settings file, but the data will still be in serbian. 
There are three polls, any of them has a few questions and different choices per question. 

For those who like the admin panel forms, there's an installed third-party app. It's name is [django-nested-inline](https://github.com/s-block/django-nested-inline/) and it provides... well, nested inlines. :grin: 
This will allow you to create the poll with both the questions and question choices in just one form, quickening the process. 


## Available endpoints 

### /api/auth/... 

Djoser authentication URLs (token authentication implemented) 

### /api/polls/create/ 

Create a new poll 

Allowed methods: POST 

### /api/polls/ 

List the available polls (with questions, including the choices for every question) 

Allowed methods: GET 

### /api/polls/vote/<choice_id>/ 

Vote for a choice 

Allowed method: PATCH 

### /api/polls/<poll_id>/ 

See voting results and update the poll (poll author only) 

Allowed methods: GET, PUT, PATCH, DELETE 


## Example request to the polls API 

Here's a request to create a poll, with nested questions and choices. The data is in JSON format. 

POST /api/polls/create/ 

```json
{
	"title": "A poll",
	"description": "Something about the poll",
	"questions": [
		{
			"question_text": "Coffee or tea?",
			"choices": [
				{"choice_text": "Coffee"},
				{"choice_text": "Tea"}
			]
		}
	]
}
```

Both the questions and the choices are optional. You can create a poll without questions and add the questions later, with a PATCH request to the last endpoint. 
The same applies to the questions. You can create a poll with empty questions (without choices), and add some choices later with a PATCH request to the API. 


## To do 

I may add endpoints to directly access the questions and choices, but I considered it unnecessary at this moment.
