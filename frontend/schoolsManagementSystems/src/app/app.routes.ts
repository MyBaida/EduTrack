import { Routes } from '@angular/router';

export const routes: Routes = [
    {path: '', 
    loadChildren: ()=> import('./pages/home/home.module').then(
        m=>m.HomeModule
    ),
    pathMatch: 'full'
 },
 {
    path: 'dashboard',
    loadChildren: ()=> import('./pages/dashboard/dashboard.module').then(
        m => m.DashboardModule
    ),
    pathMatch: 'full'
 }
];
