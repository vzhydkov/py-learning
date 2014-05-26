<!DOCTYPE html>
<html>
<head>
<title>Hello World!</title>
</head>
<body>
<p>Welcome {{username}}</p>
<ul>
% for thing in things:
<li>{{thing["username"]}}</li>
%end
</ul>

</body>
</html