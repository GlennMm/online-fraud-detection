import { Component, OnInit } from '@angular/core';
import { ModelResultsService } from 'src/app/core/service/model-results.service';
import { ModelService } from 'src/app/core/service/model.service';

@Component({
  selector: 'app-train',
  templateUrl: './train.component.html',
  styleUrls: ['./train.component.css']
})
export class TrainComponent implements OnInit {

  train_dataset: File = null
  test_dataset: File = null

  loading_train = false
  loading_test = false

  constructor(private model: ModelService, public result: ModelResultsService) { }

  ngOnInit(): void {}

  onTrainChange(event: any) {
    this.train_dataset = event.target.files[0]
  }

  onTestChange(event: any) {
    this.test_dataset = event.target.files[0]
  }

  resetTrain() {
    this.train_dataset = null
  }

  resetTest() {
    this.test_dataset = null
  }

  train() {
    if (!this.train_dataset) {
      return alert('Select training dataset first')
    }
    this.loading_train = true
    const form = new FormData()
    form.append('dataset', this.train_dataset)
    this.model.train(form).subscribe(
      (data) => {
        this.result.training_result = data
        this.loading_train = false
      },
      (err) => {
        console.log(err)
        this.loading_train = false
      }
    )
  }

  test() {
    if (!this.test_dataset) {
      return alert('Select test dataset first')
    }
    this.loading_test = true
    const form = new FormData()
    form.append('dataset', this.test_dataset)
    this.model.test(form).subscribe(
      (data) => {
        this.result.test_result = data
        console.log(data)
        this.loading_test = false
      },
      (err) => {
        console.log(err)
        this.loading_test = false
      }
    )
  }
  
}
