#include "colors.inc"  
#include "finish.inc"  

global_settings{SAR_Output_Data 1 SAR_Intersection 0}


// orthographic projection using parallel camera rays
// Could be used to render a planar image map, for example
#declare Cam = camera {
  orthographic
  location <0, 10, -10>    // position & direction of view
  look_at  <0,0,0>
  right 25*x            // horizontal size of view
  up 25*y               // vertical size of view
}

camera{Cam} 

// create a point "spotlight" (cylindrical directed) light source
light_source {
  0*x                     // light's position (translated below)
  color rgb <1,1,1>       // light's color
  parallel               // this variation
  translate <0, 10, -10> // <x y z> position of light
  point_at <0, 0, 0>      // direction of spotlight
}   

plane {
  <0,1,0> // <X Y Z> unit surface normal, vector points "away from surface"
   0 // distance from the origin in the direction of the surface normal
  //hollow on // has an inside pigment?       
  pigment {color White}
  finish {reflection {0.0} ambient 0 diffuse 0 specular 0.7 roughness 0.2}
}  
   
   
#declare box_dummy = box{  

        // create a box that extends between the 2 specified points
         <-2, 10, -2>  // one corner position <X1 Y1 Z1>
        <2, 0, 2>  // other corner position <X2 Y2 Z2>  
        pigment {color White} 
        finish {reflection {0.5} ambient 0 diffuse 0.3}
}     
  
object {box_dummy
       rotate <0,0,0>
       translate <0,0,0>
}
 


     







   



