import React from 'react';
import Link from 'next/link';

const Hero = () => {
  return (
    <section className="text-gray-600 body-font">
      <div className="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
        <div className="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 mb-10 md:mb-0">
          <img
            className="object-cover object-center rounded h-[600px]"
            alt="hero"
            src="/e7image.jpeg"
          />
        </div>
        <div className="lg:flex-grow md:w-1/2 lg:pl-24 md:pl-16 flex flex-col md:items-start md:text-left items-center text-center">
          <h1 className="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">
            <br className="hidden lg:inline-block" />A free, open source lecture
            summarizer
          </h1>
          <p className="mb-8 leading-relaxed">
            Simply drag and drop your audio file or find it from your computer,
            and your summary will generate very shortly. 😈
          </p>
          <div className="flex justify-center">
            {/* <FileUploader /> */}
            <Link href="/how">
              <button className="inline-flex text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg">
                How it works
              </button>
            </Link>
            <Link href="/dashboard">
              <button className="ml-4 inline-flex text-gray-700 bg-gray-100 border-0 py-2 px-6 focus:outline-none hover:bg-gray-200 rounded text-lg">
                Go to Dashboard
              </button>
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
