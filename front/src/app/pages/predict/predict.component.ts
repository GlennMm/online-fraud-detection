import { Component, OnDestroy, OnInit } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Papa } from 'ngx-papaparse';
import { PredictionsService } from 'src/app/core/service/predictions.service';

@Component({
  selector: 'app-predict',
  templateUrl: './predict.component.html',
  styleUrls: ['./predict.component.css']
})
export class PredictComponent implements OnInit, OnDestroy {

  dataset: File = null;
  headers: string[] = []
  recs: any[] = []
  csvData: Array<any[]> = []
  loading = false
  
  constructor(
    private snackbar: MatSnackBar,
    private papa: Papa,
    private pred: PredictionsService) { }
  
  ngOnInit(): void {  }

  ngOnDestroy() {
    delete this.headers
    delete this.recs
    delete this.csvData
    delete this.dataset
  }

  selectFile(event): void {
    this.dataset = event.target.files[0]
    this.readCsv()
  }

  clear(): void {
    this.dataset = null
    this.csvData = []
  }

  readCsv() {
    if (this.dataset === null) return
    this.csvData = []
    this.headers = []
    this.recs = []
    this.loading = true
    return this.papa.parse(this.dataset,{
      complete: (result) => {
        this.headers = result.data[0]
        this.csvData = result.data
        for(let i = 0; i < result.data.length;i++) {
          if (i == 0) {}
          else {
            this.recs.push(result.data[i])
          }
        }
        this.recs.splice(this.recs.length-1, 1)
        // console.log(result.data[0])
        this.loading = false
      },
      error: (error) => {
        console.log(error)
        this.loading = false
      }
    });
  }

  predictOne(index: number) {
    const rec = this.recs[index]
    const form = new FormData()
    form.append('record', rec)
    this.pred.predictOne(form).subscribe(
      (data) => {
        // console.log(data)
        this.recs[index].push(data['classification'])
      },
      (err) => {
        console.log(err)
        this.snackbar.open(`${err.message}`, null, { duration: 5000 })
      }
    )
  }

}
