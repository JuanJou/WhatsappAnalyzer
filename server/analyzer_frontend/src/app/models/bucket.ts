
export default class Bucket {
    constructor(bucket) {
        this.name = bucket.name
        this.creationDate = bucket.creationDate
        this.objects = []
    }
}
