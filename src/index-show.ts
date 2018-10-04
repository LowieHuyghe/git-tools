import * as inquirer from 'inquirer'
import * as childProcess from 'child_process'
import Commit from './models/commit'
import 'colors'

(async () => {
  const commits = Commit.all(50)
  const commitMapping: { [key: string]: Commit } = {}
  for (const commit of commits) {
  	const message = `${commit.shortHash.gray} ${commit.author.green} ${('on ' + commit.formattedDate).gray} ${commit.message}`
    commitMapping[message] = commit
  }

  const input = await inquirer.prompt<{ commit: string }>({
    name: 'commit',
    type: 'list',
    message: 'Pick your commit:',
    choices: [...Object.keys(commitMapping), new inquirer.Separator()]
  })
  if (!input.commit || !commitMapping[input.commit]) {
    console.error('No commit specified')
    process.exit(1)
  }

  const theChosenCommit = commitMapping[input.commit]
  childProcess.spawnSync('git' , ['show', theChosenCommit.fullHash], { stdio: 'inherit' })
})()
