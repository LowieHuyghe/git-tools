import * as childProcess from 'child_process'
import * as osLocale from 'os-locale'

export default class Commit {
  fullHash: string
  shortHash: string
  author: string
  message: string
  datetime: string

  static all (limit: number): Commit[] {
    const output = childProcess.execSync(`git log -n ${limit} --pretty=format:"%H | %h | %ai | %an <%ae> | %s"`).toString()

    return output.split('\n')
      .map(line => {
        const parts = line.split(' | ')
        return new Commit(parts[0], parts[1], parts[3], parts[4], parts[2])
      })
  }

  static where (where: string, limit: number): Commit[] {
    const output = childProcess.execSync(`git log -n ${limit} ${where} --pretty=format:"%H | %h | %ai | %an <%ae> | %s"`).toString()

    return output.split('\n')
      .map(line => {
        const parts = line.split(' | ')
        return new Commit(parts[0], parts[1], parts[3], parts[4], parts[2])
      })
  }

  constructor (fullHash: string, shortHash: string, author: string, message: string, datetime: string) {
    this.fullHash = fullHash
    this.shortHash = shortHash
    this.author = author
    this.message = message
    this.datetime = datetime
  }

  get date (): Date {
    return new Date(this.datetime)
  }

  get formattedDate (): string {
    const locale = osLocale.sync().replace('_', '-')
    return this.date.toLocaleTimeString(locale)
  }
}
