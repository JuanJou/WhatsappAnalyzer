"use server"

import Image from "next/image";
import MinioService from './services/minio'

const minioService = new MinioService()

export default async function Home() {
  const files = await minioService.get_buckets()
  console.log(`Files - MINIO: ${JSON.stringify( files )}`)

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
        <ul>
            {files.map((file) => <li key={ file.name }>{file.name}</li>)}
        </ul>
    </main>
  );
}
