(function(clientId, clientSecret, owner, repo) {
  var issuesMap = {}
  var issuesIdList = []
  var locationHash = location.hash
  fetch('https://api.github.com/repos/' + owner + '/' + repo + '/issues?client_id=' + clientId + '&client_secret=' + clientSecret)
    .then(function (res) {
      return res.json()
    })
    .then(function (data) {
      data.map(function(issue) {
        var issueId = String(issue.id)
        issuesIdList.push(issueId)
        issuesMap[issueId] = issue
      })

      console.log(issuesIdList, issuesMap, locationHash)
    })
    .then(function () {
      var directory = []
      issuesIdList.map(function (id, index) {
        var thisIssue = issuesMap[id]
        directory.push('<div class=""><a class="list-group-item" id="' + thisIssue.id + '" href="#' + thisIssue.id + '" onclick=changeArticle(' + thisIssue.id + ')>' + (index+1) + '. ' + thisIssue.title + '</a></div>')
      })
      document.getElementById('blogs').innerHTML = directory.join('')
    })
    .then(function () {
      var hashId = !!locationHash ? locationHash.split('#')[1] : issuesIdList[0]
      var labelsList = issuesMap[hashId].labels.map(function (label) { return label.name })
      var options = {
        id: labelsList.join(','),
        owner: owner,
        title: issuesMap[hashId].title || '',
        link: issuesMap[hashId].html_url,
        labels: labelsList,
        repo: repo,
        issueId: hashId,
        oauth: {
          client_id: clientId,
          client_secret: clientSecret,
        },
        maxCommentHeight: 99999
      }
      return renderGitment(options, 'blog-container')
    })

    var changeArticle = window.changeArticle = function (issueId) {
      var hashId = String(issueId)
      var labelsList = issuesMap[hashId].labels.map(function (label) { return label.name })
      var options = {
        id: labelsList.join(','),
        issueId: hashId,
        owner: owner,
        title: issuesMap[hashId].title,
        link: issuesMap[hashId].html_url,
        labels: labelsList,
        repo: repo,
        oauth: {
          client_id: clientId,
          client_secret: clientSecret,
        },
        maxCommentHeight: 99999
      }
      return renderGitment(options, 'blog-container')
    }
})(
  '716e41ff2cdca481c655', // client_id
  '3a6d744d2ceb91399dc853ddf46d1c0286fbf189',  // client_secret
  'synbe', // owner
  'issue'  // repo
)

function renderGitment(options, containerId) {
  var gitment = new Gitment(options)
  gitment.render(containerId)
  return gitment
}

