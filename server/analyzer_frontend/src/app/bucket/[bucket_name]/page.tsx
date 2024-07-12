import BucketList from "@/app/bucket/[bucket_name]/bucket-list";


export default function Bucket({ params: { bucket_name } }: { params: { bucket_name: string }}) {
    console.log(`Bucket name: ${bucket_name}`)

    return <BucketList bucket_name={bucket_name} />
}
