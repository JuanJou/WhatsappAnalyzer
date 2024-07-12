"use server"
import MinioService from './services/minio'
import Home from "./home"

const minioService = new MinioService()

export default async function Main() {
  const files = await minioService.get_buckets()
  console.log(`Files - MINIO: ${JSON.stringify( files )}`)

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
    </main>
  );
}
