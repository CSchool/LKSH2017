(function() {
	var sess = "";
	var width = Math.floor((document.getElementById("term").clientWidth - 16) / 9.00146484375);
	var $term = document.getElementById('term');
	var inp = "";
	var quit = false;

	function sendData(input) {
		var data = new FormData();
		data.append('input', input);
		data.append('sess', sess);
		data.append('width', width);
		data.append('achievments', window.localStorage.preyAchievments || '');
		var xmlHttp = new XMLHttpRequest();
		xmlHttp.onreadystatechange = function() {
			if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
				var dat = xmlHttp.responseText.split("~~SEPARATOR~~");
				if (!dat)
					return;
				var t = dat[0];
				if (dat.length == 3) {
					sess = dat[0];
					window.localStorage.preyAchievments = dat[1];
					t = dat[2];
				}
				if (t.slice(0, "\\cmd::quit".length) == "\\cmd::quit") {
					// quit
					$term.innerText += t.slice("\\cmd::quit".length);
					$term.innerHTML += "\n\n<b>[Inferior 1 (process 26273 'Prey') exited normally]</b>";
					quit = true;
						inp = "";
					$term.scrollTop = $term.scrollHeight - $term.clientHeight;
					return;
				}
				$term.innerText += t + "█";
				$term.scrollTop = $term.scrollHeight - $term.clientHeight;
				inp = "";
			}
		}
		xmlHttp.open("post", "/server");
		xmlHttp.send(data);
	}

	sendData('start');

	window.onbeforeunload = function() {
		sendData('unload');
		return null;
	}

	window.onkeydown = function(key) {
		if (quit) return;
		if (key.keyCode == 8 && inp.length > 0) {
			$term.innerText = $term.innerText.slice(0, -2) + "█";
			inp = inp.slice(0, -1);
		}
		if (key.keyCode == 13) {
			$term.innerText = $term.innerText.slice(0, -1);
			$term.innerText += "\n\n";
			sendData(inp);
		}
	}

	window.onkeypress = function(key) {
		if (quit) return;
		if (key.key.length == 1) {
			$term.innerText = $term.innerText.slice(0, -1) + key.key + "█";
			inp += key.key;
		}
	}
})();