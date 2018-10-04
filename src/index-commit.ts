import * as inquirer from 'inquirer'
import * as childProcess from 'child_process'

(async () => {
  if (!childProcess.execSync('git diff --cached').toString()) {
    console.error('No changes added to commit')
    process.exit(1)
  }

  const input = await inquirer.prompt<{ message: string }>({
    name: 'message',
    message: 'Message:'
  })
  if (!input.message) {
    console.error('No message specified')
    process.exit(1)
  }

  const message = input.message.replace(/"/, '\\"')
  childProcess.execSync(`git commit -m "${message}"`)
})()
