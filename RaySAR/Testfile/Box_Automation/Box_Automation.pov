#include "colors.inc"
#include "finish.inc"

global_settings {SAR_Output_Data 1 SAR_Intersection 0}

#declare Cam = camera {
  orthographic
  look_at <0,0,0>
  location <-1.0708686428919791,1.2774995800839535,-9.860082919152152>
  right 25 *x
  up 25 *y
}

camera{Cam}

light_source {
  0*x
  color rgb <1,1,1>
  parallel
  translate <-1.0708686428919791,1.2774995800839535,-9.860082919152152>
  point_at <0,0,0>
}

plane {
  <0,1,0> // <X Y Z> unit surface normal, vector points "away from surface"
   0 // distance from the origin in the direction of the surface normal
  //hollow on // has an inside pigment?       
  pigment {color White}
  finish {reflection {0.3} ambient 0 diffuse 0 specular 0.7 roughness 0.2}
}  
   
#declare box_dummy = box{  

        // create a box that extends between the 2 specified points
         <-2, 4, -2>  // one corner position <X1 Y1 Z1>
        <2, 0, 2>  // other corner position <X2 Y2 Z2>  
        pigment {color White} 
        finish {reflection {0.5} ambient 0 diffuse 0.3}
}     
      
#declare building = union{ 

        polygon {
        5, // number of points
        <0,0,0>, <0,0,2>, <0, 2,2>, <0, 2,0>, <0, 0,0> 
  
         pigment {color White}  
        
         finish {reflection {0.5} ambient 0 diffuse 0.3} 
         
        }    

        polygon {
         6, // number of points
         <0, 0,0>, <0, 2,0>, <1,3,0>, <2, 2,0>, <2, 0,0>, <0, 0,0> 
  
         pigment {color White}
         finish {reflection {0.5} ambient 0 diffuse 0.3} 
        }

        polygon {
          5, // number of points
         <2,0,0>, <2,0,2>, <2, 2,2>, <2, 2,0>, <2, 0,0> 
  
         pigment {color White} 
         finish {reflection {0.5} ambient 0 diffuse 0.3}  
        }    

        polygon {
          6, // number of points
         <0, 0,2>, <0, 2,2>, <1,3,2>, <2, 2,2>, <2, 0,2>, <0, 0,2> 
  
         pigment {color White}
         finish {reflection {0.5} ambient 0 diffuse 0.3} 
        }   

        // Roof  

        polygon {
         5, // number of points
         <0, 2,0>, <0, 2,2>, <1,3,2>, <1, 3,0>, <0, 2,0> 
  
        pigment {color White}  
        finish {reflection {0.5} ambient 0 diffuse 0.3} 
        }

        polygon {
         5, // number of points
        <2, 2,0>, <2, 2,2>, <1,3,2>, <1, 3,0>, <2, 2,0> 
  
        pigment {color White}           
        finish {reflection {0.5} ambient 0 diffuse 0.3}         
        }   
}  

// building
object {building
       scale <3,3,3>
       rotate <0,-45,0>
       //rotate <0,-90,0>
       translate <0,0,-3>
       finish {reflection {0.8} ambient 0 diffuse 0 specular 0.9 roughness 0.005}
}  
 


     







   





