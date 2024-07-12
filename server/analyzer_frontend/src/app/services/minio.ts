import { BucketItem, Client } from 'minio';
import Bucket from "../models/bucket"
import ConversationFile from '../models/file';

export default class MinioService {
    minioClient: Client;

    constructor() {
        this.minioClient = new Client({
            endPoint: 's3',
            port: 9000,
            useSSL: false,
            accessKey: process.env.S3_ACCESS_KEY || "",
            secretKey: process.env.S3_SECRET_KEY || "",
        })
    }

    async get_buckets() {
        return (await this.minioClient.listBuckets() ).map((bucket:any) => new Bucket(bucket))
    }

    async get_files_from_bucket(bucket_name: string): Promise<ConversationFile[]> {
        const promise = new Promise<ConversationFile[]>((reject,resolve) => {
            const stream = this.minioClient.listObjects(bucket_name)
            const files: BucketItem[] = []

            stream.on("data", (obj) => {
                files.push(obj)
            })
            stream.on("end", () => {
                resolve(files)
            })
            stream.on("error", reject)
        })
        return promise;
    }

}
