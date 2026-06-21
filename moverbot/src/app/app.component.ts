import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'Moverbot';

  navItems = [
    'About',
    'Services',
    'Technology',
    'Projects',
    'Contact'
  ];

  services = [
    {
      title: 'Autonomous Mobile Robots (AMRs)',
      description:
        'Smart robots capable of navigating dynamic environments without human intervention.'
    },
    {
      title: 'Industrial Automation',
      description:
        'Robotic systems designed to streamline manufacturing and operational workflows.'
    },
    {
      title: 'AI-Powered Robotics',
      description:
        'Machine learning integration for decision-making, predictive behavior, and adaptive performance.'
    },
    {
      title: 'Custom Robotics Solutions',
      description:
        'Tailor-made autonomous systems built to solve unique business challenges.'
    }
  ];

  technologies = [
    'Artificial Intelligence',
    'Machine Learning',
    'Computer Vision',
    'Embedded Systems',
    'IoT Integration',
    'SLAM Navigation',
    'ROS Development',
    'Edge Computing'
  ];

  projects = [
    {
      name: 'Warehouse Navigator',
      description: 'Autonomous warehouse transportation robot.'
    },
    {
      name: 'Smart Inspection Bot',
      description: 'Computer vision-powered industrial inspection robot.'
    },
    {
      name: 'Delivery Rover',
      description: 'Autonomous last-mile delivery platform.'
    },
    {
      name: 'Agricultural Assistant',
      description: 'Precision farming and crop monitoring robot.'
    }
  ];

  stats = [
    { value: '50+', label: 'Projects Delivered' },
    { value: '15+', label: 'Industry Partners' },
    { value: '99.5%', label: 'System Reliability' },
    { value: '24/7', label: 'Autonomous Operations' }
  ];

  benefits = [
    'Advanced AI Integration',
    'Industry-Grade Reliability',
    'Custom Engineering Expertise',
    'Scalable Automation Solutions',
    'Continuous Innovation'
  ];

  testimonials = [
    {
      quote:
        'Moverbot transformed our warehouse operations through intelligent automation.'
    },
    {
      quote:
        "The team's expertise in autonomous robotics exceeded our expectations."
    }
  ];
}
