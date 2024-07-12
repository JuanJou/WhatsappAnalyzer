import Link from "next/link";
import { withService } from "../services"
import { ServiceProps } from "../services/dependency_injection";

async function InnerHome({ minio }: ServiceProps) {
    const buckets = await minio.get_buckets()
    console.log(`Buckets - MINIO: ${JSON.stringify(buckets)}`)

    return (
        <div className="">
            <ul>
                {buckets.map((bucket) =>
                    <Link href={`/bucket/${bucket.name}`}>
                        <li key={bucket.name}>{bucket.name}</li>
                    </Link>)}
            </ul>
        </div>
    );
}

export default withService(InnerHome, ["minio"])
