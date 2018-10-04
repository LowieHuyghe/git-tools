import * as childProcess from 'child_process'

export default class Branch {
  name: string
  current: boolean

  static all (): Branch[] {
    const output = childProcess.execSync('git branch').toString()

    return output.split('\n')
      .map(line => {
        const match = /^(\*?)\s*(.+)$/.exec(line)
        if (match) {
          const name = match[2]
          const current = !!match[1]
          return new Branch(name, current)
        }
      })
      .filter(branch => !!branch) as Branch[]
  }

  constructor (name: string, current: boolean) {
    this.name = name
    this.current = current
  }
}
