import { Component, OnInit, Inject } from '@angular/core';
import { DOCUMENT } from '@angular/common'; 
import {NgbModal, ModalDismissReasons} from '@ng-bootstrap/ng-bootstrap';
import { FormBuilder } from '@angular/forms';
import { DeviceService } from '../services/device.service';
import { ActivatedRoute } from '@angular/router';
import { toNumber } from 'ng-zorro-antd';


@Component({
  selector: 'app-deviceconfig',
  templateUrl: './deviceconfig.component.html',
  styleUrls: ['./deviceconfig.component.css'],
})
export class DeviceconfigComponent implements OnInit {
  closeResult: string;
  public id: string;	
  public flowid: string;	
  checkoutForm;	
  
  constructor(
    private modalService:NgbModal,
    private formBuilder: FormBuilder,
    private device: DeviceService,
    private route: ActivatedRoute,
    @Inject(DOCUMENT) document
  ) {
      this.checkoutForm = this.formBuilder.group({
        deviceid: '',
        ipAddress: '',
        host: '',
        projectid: ''
      });
    }

    deviceDetail: object;  
    flows: object;  
    ProjectName: string;

  ngOnInit() {
    //this.listDevices();
    this.id = this.route.snapshot.paramMap.get('id');
    this.ProjectName = this.route.snapshot.paramMap.get('id');
    this.listDevicesByproject();
    console.log("id is " + this.id);
    this.getFlowJsonFile()
  }

  
  open(content) {
    this.modalService.open(content, {ariaLabelledBy: 'modal-basic-title'}).result.then((result) => {
      this.closeResult = `Closed with: ${result}`;
    }, (reason) => {
      this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
    });
  }

  startbutton(_id){
    this.flowid = document.getElementById(_id).value; 
    console.log("id is " + _id + ' and flowid is '+ this.flowid);
  }

  stopbutton(_id){
    this.flowid = document.getElementById(_id).value; 
    console.log("id is " + _id + ' and flowid is '+ this.flowid);
  }

  resetbutton(_id){
    this.flowid = document.getElementById(_id).value; 
    console.log("id is " + _id + ' and flowid is '+ this.flowid);
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return  `with: ${reason}`;
    }
  }

  onSubmit(customerData) {
    console.log("Form Submitted 1!");
    console.log('projectid is ' + customerData['projectid']);
    customerData['projectid'] = this.id;
    this.device.createDevice(customerData); 
    //this.listDevices();
    //this.checkoutForm.reset();
  }


  listDevices() {
    this.device.getDevicesList().subscribe(devices => {
      //console.log(devices.json());
      //console.log('all' + typeof(devices.json()));
      if(devices){
        this.deviceDetail = devices.json();
      }else{
        this.deviceDetail = [];
      }
    });
  }

  listDevicesByproject() {
    this.device.getDevicesListByproject(this.id).subscribe(devices => {
      if(devices){
        this.deviceDetail = devices.json();
      }else{
        this.deviceDetail = [];
      }
    });
  }

  getFlowJsonFile(){
    var i;
    var j = 0;
    var k = [];
    this.device.getFlowJsonFile(this.id).subscribe(flows => {
      //console.log("flows are "+flows.json().length);
      //console.log("flows are " + typeof(flows.json().length));
      for(i=0;i<flows.json().length;i++){
        //console.log('list is '+flows.json()[i]['id']);
        if(flows.json()[i]['label'] !== undefined){
          //console.log('label is '+flows.json()[i]['label']);
          k[j] = {};
          k[j]['id'] = flows.json()[i]['id'];
          k[j]['flow'] = flows.json()[i]['label'];
          //console.log(k[j]);
          j++;
        }
      }
      console.log("final k is" + k)
      if(k.length !== 0){
        this.flows = k;
      }else{
        this.flows = [];
      }
    });
  }
}
