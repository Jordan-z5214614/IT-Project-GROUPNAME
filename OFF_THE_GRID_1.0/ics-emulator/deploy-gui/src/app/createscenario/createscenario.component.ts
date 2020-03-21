import { Component, OnInit } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { NoderedService } from '../services/nodered.service';

@Component({
  selector: 'app-createscenario',
  templateUrl: './createscenario.component.html',
  styleUrls: ['./createscenario.component.css']
})
export class CreatescenarioComponent implements OnInit {
  isrc: SafeResourceUrl;
  constructor(
    private sanitizer: DomSanitizer,
    private _nodeRed: NoderedService
  ) {}

  ngOnInit() {
    this.isrc = this.sanitizer.bypassSecurityTrustResourceUrl(
      `${this._nodeRed.baseUrl}/red/`
    );
  }
}
