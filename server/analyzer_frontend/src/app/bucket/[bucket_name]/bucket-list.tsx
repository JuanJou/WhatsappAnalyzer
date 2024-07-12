import ConversationFile from "@/app/models/file"
import { withService } from "@/app/services"
import { ServiceProps } from "@/app/services/dependency_injection"

type BucketProps = {
    bucket_name: string
}


async function InnerBucketList({bucket_name, minio}: BucketProps & ServiceProps) {
    const files: ConversationFile[] = await minio.get_files_from_bucket(bucket_name)
    return <p></p>
    return <ul>
            {files.map((file) => <li>{file.name}</li>)}
        </ul>
}

export default withService<BucketProps>(InnerBucketList, ["minio"])
