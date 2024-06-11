// Angular import
import { Component, Input, OnDestroy, Inject, ViewEncapsulation } from '@angular/core';
import { Router, NavigationStart, NavigationEnd, NavigationCancel, NavigationError } from '@angular/router';
import { DOCUMENT } from '@angular/common';

// project import
import { Spinkit } from './spinkits';
import { HttpConfigInterceptor } from 'src/app/interceptors/http/http-config-interceptor.interceptor';

@Component({
  selector: 'app-spinner',
  templateUrl: './spinner.component.html',
  styleUrls: ['./spinner.component.scss', './spinkit-css/sk-line-material.scss'],
  encapsulation: ViewEncapsulation.None
})
export class SpinnerComponent implements OnDestroy {
  // public props
  isSpinnerVisible = true;
  Spinkit = Spinkit;
  @Input() backgroundColor = '#2689E2';
  @Input() spinner = Spinkit.skLine;

  // Constructor
  constructor(
    private router: Router,
    @Inject(DOCUMENT) private document: Document,
    private httpInterceptor: HttpConfigInterceptor
  ) {
    this.router.events.subscribe(
      (event) => {
        if (event instanceof NavigationStart) {
          this.isSpinnerVisible = true;
        } else if (event instanceof NavigationEnd || event instanceof NavigationCancel || event instanceof NavigationError) {
          this.isSpinnerVisible = false;
        }
      },
      () => {
        this.isSpinnerVisible = false;
      }
    );

    //subscribe httpclient events
    httpInterceptor.loadingSubject.subscribe(
      (isLoading)=>{
        this.isSpinnerVisible = isLoading
      }
    )
  }

  // life cycle event
  ngOnDestroy(): void {
    this.httpInterceptor.loadingSubject.unsubscribe();
    this.isSpinnerVisible = false;

  }
}
