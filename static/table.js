const resultsTable = document.querySelector('#resultsTable');

// fetch('/allbasewordings')
// 	.then(response => response.json())
// 	.then(data => {
// 		data.forEach(result => {
// 			const row = document.createElement('tr');
// 			const baseWording = document.createElement('td');
// 			const theme = document.createElement('td');
// 			const tone = document.createElement('td');
// 			const length = document.createElement('td');
// 			const learningObjective = document.createElement('td');
// 			baseWording.textContent = result.base_wording;
// 			theme.textContent = result.theme;
// 			tone.textContent = result.tone;
// 			length.textContent = result.length;
// 			learningObjective.textContent = result.learning_objective;
// 			row.appendChild(baseWording);
// 			row.appendChild(theme);
// 			row.appendChild(tone);
// 			row.appendChild(length);
// 			row.appendChild(learningObjective);
// 			resultsTable.appendChild(row);
// 		});
// 	})
// 	.catch(error => console.error(error));

fetch('/allbasewordings')
	.then(response => print(response))
	
