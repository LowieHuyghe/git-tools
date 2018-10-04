import * as program from 'commander'

program
  .version('1.0.0')
  .command('checkout', 'Switch branches or restore working tree files')
  .command('commit', 'Record changes to the repository')
  .command('pick', 'Pick various types of objects')
  .command('show', 'Show various types of objects')
  .parse(process.argv)
