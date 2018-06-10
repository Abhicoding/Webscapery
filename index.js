const cheerio = require('cheerio')
const request = require('request')

const link = process.argv[2]

request(link, function (err, res, html) {
  if (!err && res.statusCode === 200) {
    let $ = cheerio.load(html)
    $('div.mw-parser-output')
      .each(function (i, element) {
        var name = $(this).find('.sortable wikitable plainrowheaders jquery-tablesorter').find('tbody').children()
        console.log(name)
      })
  }
})
