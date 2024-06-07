import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { authService } from 'src/app/services/auth/auth.service';

export const authGuard: CanActivateFn = (route, state) => {
  const auth = inject(authService);
  const router = inject(Router);

    if (auth.isLoggedIn) {
      return true;
    }
  
    return router.parseUrl('/guest/login');


};
