from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    TemplateView,
    View,
)
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from . import models
from django import forms
from django.http import HttpResponseRedirect


class FormMixin:
    def form_valid(self, form):
        if form.is_valid() and not self.request.up.validate:
            return super().form_valid(form)
        return self.render_to_response(self.get_context_data(form=form))

    def get_initial(self):
        initial = super().get_initial()

        initial.update(self.request.GET.dict())
        return initial


class CompanyListView(ListView):
    model = models.Company


class CompanyDetailView(DetailView):
    model = models.Company


class CompanyCreateView(FormMixin, CreateView):
    model = models.Company
    fields = ["name", "address"]


class CompanyUpdateView(FormMixin, UpdateView):
    model = models.Company
    fields = ["name", "address"]


class ProjectDetailView(DetailView):
    model = models.Project


class ProjectCreateView(FormMixin, CreateView):
    model = models.Project
    fields = ["name", "budget", "company"]


class ProjectUpdateView(FormMixin, UpdateView):
    model = models.Project
    fields = ["name", "budget", "company"]


class ProjectListView(ListView):
    model = models.Project


class ProjectSuggestNameView(TemplateView):
    template_name = "core/project_suggest_name.html"

    def get_context_data(self, **kwargs):
        import random

        ctx = super().get_context_data(**kwargs)
        names = []
        random.shuffle(ANIMALS)
        for i in range(10):
            names.append("-".join(ANIMALS[i * 3 : (i + 1) * 3]))
        ctx["names"] = names

        return ctx


class TaskListView(ListView):
    model = models.Task


class TaskForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 40}))

    class Meta:
        model = models.Task
        fields = ["text"]


class TaskCreateView(FormMixin, CreateView):
    model = models.Task
    form_class = TaskForm

    def form_valid(self, form):
        if form.is_valid() and not self.request.up.validate:
            super().form_valid(form)
            self.request.up.layer.accept()
            return self.render_to_response(self.get_context_data(form=form))
        return self.render_to_response(self.get_context_data(form=form))


class TaskDetailView(DetailView):
    model = models.Task


class TaskUpdateView(FormMixin, UpdateView):
    model = models.Task
    form_class = TaskForm


class TaskDoneView(SingleObjectMixin, View):
    model = models.Task

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.done = not self.object.done
        self.object.save()
        return HttpResponseRedirect(self.object.get_absolute_url())


class ClearTasksView(View):
    def post(self, request, *args, **kwargs):
        models.Task.objects.filter(done=True).delete()
        return HttpResponseRedirect(reverse("task-list"))


ANIMALS = [
    "aardvark",
    "aardwolf",
    "albatross",
    "alligator",
    "alpaca",
    "amphibian",
    "anaconda",
    "angelfish",
    "anglerfish",
    "ant",
    "anteater",
    "antelope",
    "antlion",
    "ape",
    "aphid",
    "armadillo",
    "asp",
    "baboon",
    "badger",
    "bandicoot",
    "barnacle",
    "barracuda",
    "basilisk",
    "bass",
    "bat",
    "bear",
    "beaver",
    "bedbug",
    "bee",
    "beetle",
    "bird",
    "bison",
    "blackbird",
    "boa",
    "boar",
    "bobcat",
    "bobolink",
    "bonobo",
    "booby",
    "bovid",
    "bug",
    "butterfly",
    "buzzard",
    "camel",
    "canid",
    "canidae",
    "capybara",
    "cardinal",
    "caribou",
    "carp",
    "cat",
    "caterpillar",
    "catfish",
    "catshark",
    "cattle",
    "centipede",
    "cephalopod",
    "chameleon",
    "cheetah",
    "chickadee",
    "chicken",
    "chimpanzee",
    "chinchilla",
    "chipmunk",
    "cicada",
    "clam",
    "clownfish",
    "cobra",
    "cockroach",
    "cod",
    "condor",
    "constrictor",
    "coral",
    "cougar",
    "cow",
    "coyote",
    "crab",
    "crane",
    "crawdad",
    "crayfish",
    "cricket",
    "crocodile",
    "crow",
    "cuckoo",
    "damselfly",
    "deer",
    "dingo",
    "dinosaur",
    "dog",
    "dolphin",
    "dormouse",
    "dove",
    "dragon",
    "dragonfly",
    "duck",
    "eagle",
    "earthworm",
    "earwig",
    "echidna",
    "eel",
    "egret",
    "elephant",
    "elk",
    "emu",
    "ermine",
    "falcon",
    "felidae",
    "ferret",
    "finch",
    "firefly",
    "fish",
    "flamingo",
    "flea",
    "fly",
    "flyingfish",
    "fowl",
    "fox",
    "frog",
    "galliform",
    "gamefowl",
    "gayal",
    "gazelle",
    "gecko",
    "gerbil",
    "gibbon",
    "giraffe",
    "goat",
    "goldfish",
    "goose",
    "gopher",
    "gorilla",
    "grasshopper",
    "grouse",
    "guan",
    "guanaco",
    "guineafowl",
    "gull",
    "guppy",
    "haddock",
    "halibut",
    "hamster",
    "hare",
    "harrier",
    "hawk",
    "hedgehog",
    "heron",
    "herring",
    "hippopotamus",
    "hookworm",
    "hornet",
    "horse",
    "hoverfly",
    "hummingbird",
    "hyena",
    "iguana",
    "impala",
    "jackal",
    "jaguar",
    "jay",
    "jellyfish",
    "junglefowl",
    "kangaroo",
    "kingfisher",
    "kite",
    "kiwi",
    "koala",
    "koi",
    "krill",
    "ladybug",
    "lamprey",
    "landfowl",
    "lark",
    "leech",
    "lemming",
    "lemur",
    "leopard",
    "leopon",
    "limpet",
    "lion",
    "lizard",
    "llama",
    "lobster",
    "locust",
    "loon",
    "louse",
    "lungfish",
    "lynx",
    "macaw",
    "mackerel",
    "magpie",
    "mammal",
    "manatee",
    "mandrill",
    "marlin",
    "marmoset",
    "marmot",
    "marsupial",
    "marten",
    "mastodon",
    "meadowlark",
    "meerkat",
    "mink",
    "minnow",
    "mite",
    "mockingbird",
    "mole",
    "mollusk",
    "mongoose",
    "moose",
    "mosquito",
    "moth",
    "mouse",
    "mule",
    "muskox",
    "narwhal",
    "newt",
    "nightingale",
    "ocelot",
    "octopus",
    "opossum",
    "orangutan",
    "orca",
    "ostrich",
    "otter",
    "owl",
    "ox",
    "panda",
    "panther",
    "parakeet",
    "parrot",
    "parrotfish",
    "partridge",
    "peacock",
    "peafowl",
    "pelican",
    "penguin",
    "perch",
    "pheasant",
    "pigeon",
    "pike",
    "pinniped",
    "piranha",
    "planarian",
    "platypus",
    "pony",
    "porcupine",
    "porpoise",
    "possum",
    "prawn",
    "primate",
    "ptarmigan",
    "puffin",
    "puma",
    "python",
    "quail",
    "quelea",
    "quokka",
    "rabbit",
    "raccoon",
    "rat",
    "rattlesnake",
    "raven",
    "reindeer",
    "reptile",
    "rhinoceros",
    "roadrunner",
    "rodent",
    "rook",
    "rooster",
    "roundworm",
    "sailfish",
    "salamander",
    "salmon",
    "sawfish",
    "scallop",
    "scorpion",
    "seahorse",
    "shark",
    "sheep",
    "shrew",
    "shrimp",
    "silkworm",
    "silverfish",
    "skink",
    "skunk",
    "sloth",
    "slug",
    "smelt",
    "snail",
    "snake",
    "snipe",
    "sole",
    "sparrow",
    "spider",
    "spoonbill",
    "squid",
    "squirrel",
    "starfish",
    "stingray",
    "stoat",
    "stork",
    "sturgeon",
    "swallow",
    "swan",
    "swift",
    "swordfish",
    "swordtail",
    "tahr",
    "takin",
    "tapir",
    "tarantula",
    "tarsier",
    "termite",
    "tern",
    "thrush",
    "tick",
    "tiger",
    "tiglon",
    "toad",
    "tortoise",
    "toucan",
    "trout",
    "tuna",
    "turkey",
    "turtle",
    "tyrannosaurus",
    "unicorn",
    "urial",
    "vicuna",
    "viper",
    "vole",
    "vulture",
    "wallaby",
    "walrus",
    "warbler",
    "wasp",
    "weasel",
    "whale",
    "whippet",
    "whitefish",
    "wildcat",
    "wildebeest",
    "wildfowl",
    "wolf",
    "wolverine",
    "wombat",
    "woodpecker",
    "worm",
    "wren",
    "xerinae",
    "yak",
    "zebra",
]
