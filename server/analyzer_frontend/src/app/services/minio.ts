import { Client } from 'minio';
import Bucket from "../models/bucket"

export default class MinioService {

    constructor() {
        this.minioClient = new Client({
            endPoint: 's3',
            port: 9000,
            useSSL: false,
            accessKey: process.env.S3_ACCESS_KEY,
            secretKey: process.env.S3_SECRET_KEY,
        })
    }

    async get_buckets() {
        return (await this.minioClient.listBuckets() ).map(bucket => new Bucket(bucket))
    }

}
