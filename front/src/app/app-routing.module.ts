import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DashboardComponent } from "./pages/dashboard/dashboard.component";
import { HomeComponent } from './pages/home/home.component';
import { InvestigateComponent } from './pages/investigate/investigate.component';
import { PredictComponent } from './pages/predict/predict.component';
import { TestComponent } from './pages/test/test.component';
import { TrainComponent } from './pages/train/train.component';

const routes: Routes = [
  { path: "", redirectTo: "dashboard", pathMatch: "full" },
  {
    path: "dashboard", component: DashboardComponent, children: [
      {
        path: '', redirectTo: 'home', pathMatch: 'full'
      },
      {
        path: 'home',
        component: HomeComponent
      },
      {
        path: 'investigate',
        component: InvestigateComponent
      },
      {
        path: 'test',
        component: TestComponent
      },
      {
        path: 'train',
        component: TrainComponent
      },
      {
        path: 'predict',
        component: PredictComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
