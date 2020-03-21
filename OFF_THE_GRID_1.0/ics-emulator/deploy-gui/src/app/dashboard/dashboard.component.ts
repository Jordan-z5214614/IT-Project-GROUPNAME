import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NoderedService } from '../services/nodered.service';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  constructor(private _router: Router, private _nodered: NoderedService) {}

  projectDetails: object;

  ngOnInit() {
    this.listProjects();
  }

  createScenario() {
    this._router.navigate(['createscenario']);
  }

  devicesConfig(project) {
    this._router.navigate(['deviceconfig' , project ]);
  }
 
  listProjects() {
    this._nodered.getProjectsList().subscribe(projects => {
      console.log(projects);
      this.projectDetails = projects;
    });
  }

  getProjectsMeataDeta() {}
}
