#include <webots/DistanceSensor.hpp>
#include <webots/Motor.hpp>
#include <webots/Robot.hpp>
#include <webots/Keyboard.hpp>
#include <webots/GPS.hpp>
#include <webots/InertialUnit.hpp>

#define TIME_STEP 64
using namespace webots;

int main(int argc, char **argv) {
  Robot *robot = new Robot();
  Keyboard kb;

  Motor *wheels[4];
  char wheels_names[4][8] = {"Motor1", "Motor2", "Motor3", "Motor4"};
  for (int i = 0; i < 4; i++) {
    wheels[i] = robot->getMotor(wheels_names[i]);
    wheels[i]->setPosition(INFINITY);
    wheels[i]->setVelocity(0.0);
  }
  
  std::cout<<"pradzia"<< std::endl;
  
  kb.enable(TIME_STEP);
  double leftSpeed = 0.0;
  double rightSpeed = 0.0;
  while (robot->step(TIME_STEP) != -1) {
    int key=kb.getKey();
    
    if (key==315){
    leftSpeed = 1.0;
    rightSpeed = 1.0;
    } else if (key==317){
    leftSpeed = -1.0;
    rightSpeed = -1.0;
    }else if (key==316){
    leftSpeed = 1.0;
    rightSpeed = -1.0;
    }else if (key==314){
    leftSpeed = -1.0;
    rightSpeed = 1.0;
    }else {
    leftSpeed = 0.0;
    rightSpeed = 0.0;
    }
    wheels[0]->setVelocity(leftSpeed);
    wheels[1]->setVelocity(rightSpeed);
    wheels[2]->setVelocity(leftSpeed);
    wheels[3]->setVelocity(rightSpeed);
  }
  delete robot;
  return 0;  // EXIT_SUCCESS
}