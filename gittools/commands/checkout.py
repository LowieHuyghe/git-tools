
from scriptcore.console.cuiscript import CuiScript
from gittools.models.branch import Branch


class Checkout(CuiScript):

    def __init__(self, base_path, arguments=None):
        """
        Construct the script
        :param base_path:   The base path
        :param arguments:   The arguments
        """

        title = 'Git checkout'
        description = 'Switch branches'

        super(Checkout, self).__init__(base_path, title, description, arguments=arguments)

    def _run(self):
        """
        Actually run the script
        """

        branches = Branch.all()
        branches.sort(key=lambda branch: branch.name)
        branch_names = []
        for branch in branches:
            if branch.current:
                branch_name = self.output.color(branch.name, 'blue')
            else:
                branch_name = self.output.color(branch.name, 'green')
            branch_names.append(branch_name)

        index = self.input.pick(branch_names, 'Which branch would you like to checkout?')

        if index is not None:
            self.execute('git checkout %s' % branches[index].name)
        else:
            self.output('Invalid input given', 'error')
