import npyscreen


# TODO: Allow dynamic tasks and rewards #
tasks = [
    {"name": "Read a book chapter", "value": 30}, {
        "name": "Complete a khan academy section", "value": 20}]

rewards = [
    {"name": "20 minutes discord call", "price": 20}
]


class RewardButton(npyscreen.ButtonPress):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price = kwargs.get('price')

    def whenPressed(self):
        if self.price > self.parent.balance:
            return

        self.parent.balance -= self.price
        self.parent.balance_widget.value = f'${self.parent.balance}'
        self.parent.display()


class TaskButton(npyscreen.ButtonPress):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reward = kwargs.get('reward')

    def whenPressed(self):
        self.parent.balance += self.reward
        self.parent.balance_widget.value = f'${self.parent.balance}'
        self.parent.display()


class Trackamot(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MainForm())


# TODO: Maybe use a sqlite database for storing data #
def load_balance():
    return 0


class MainForm(npyscreen.Form):
    balance_widget = None

    def create(self):
        self.balance = load_balance()

        self.balance_widget = self.add(
            npyscreen.TitleText,
            name='Balance',
            editable=False,
            value=f'${self.balance}'
        )

        self.nextrely += 1
        self.add(npyscreen.TitleText,
                 name='Tasks', editable=False)

        for task in tasks:
            reward = task["value"]
            name = task["name"]
            self.add(TaskButton, name=f'{name} - ${reward}', reward=reward)

        self.nextrely += 1
        self.add(npyscreen.TitleText, name='Rewards', editable=False)

        for reward in rewards:
            price = reward["price"]
            name = reward["name"]
            self.add(RewardButton, name=f'{name} - ${price}', price=price)


if __name__ == "__main__":
    Trackamot().run()
