import * as inquirer from 'inquirer'
import * as childProcess from 'child_process'
import Branch from './models/branch'

(async () => {
  const branches = Branch.all()
  const branchMapping: { [key: string]: Branch } = {}
  for (const branch of branches) {
    branchMapping[`${branch.current ? '* ' : ''}${branch.name}`] = branch
  }

  const input = await inquirer.prompt<{ branch: string }>({
    name: 'branch',
    type: 'list',
    message: 'Which branch would you like to checkout?',
    choices: [...Object.keys(branchMapping), new inquirer.Separator()]
  })
  if (!input.branch || !branchMapping[input.branch]) {
    console.error('No branch specified')
    process.exit(1)
  }

  const theChosenBranch = branchMapping[input.branch]
  childProcess.execSync(`git checkout ${theChosenBranch.name}`)
})()
