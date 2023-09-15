import { Component, OnInit } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { PredictionsService } from 'src/app/core/service/predictions.service';

@Component({
  selector: 'app-investigate',
  templateUrl: './investigate.component.html',
  styleUrls: ['./investigate.component.css']
})
export class InvestigateComponent implements OnInit {

  dataset: File = null
  loading = false

  result: any

  constructor(
    private snackbar: MatSnackBar,
    private predictions: PredictionsService) { }

  ngOnInit(): void {
  }

  selectFile(event) {
    this.dataset = event.target.files[0]
  }

  resetTrain(){
    this.dataset = null
    this.clearResults()
  }

  clearResults() {
    this.result = null
  }

  predict() {
    this.loading = true
    const form = new FormData()
    form.append('dataset', this.dataset)
    this.predictions.predict_batch(form).subscribe(
      (data) => {
        console.log(data)
        this.result = data
        this.loading = false
      },
      (err) => {
        console.log(err)
        this.loading = false
        return this.snackbar.open(`${err.statusText} ${err.error.message || ""}`, null, { duration: 5000 })
      })
  }

}
