import React from 'react';

import Navbar from '../components/Navbar';
import Hero from '../components/Hero';

const navigation = [
  { name: 'Product', href: '#' },
  { name: 'Features', href: '#' },
  { name: 'Marketplace', href: '#' },
  { name: 'Company', href: '#' },
];

export default function Home() {
  return (
    <>
      <Hero />
    </>
  );
}
