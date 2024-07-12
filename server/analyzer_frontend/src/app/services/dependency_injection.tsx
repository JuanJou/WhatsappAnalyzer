import MinioService from "./minio"

type ServiceType = {
    name: string,
    Class: typeof MinioService
}

const services: ServiceType[] = [
    {
        "name": "minio",
        "Class": MinioService
    }
]

export type ServiceProps = {
    minio: Readonly<MinioService>
}


export function withService<T>(OriginalComponent: React.ElementType, services_to_inject: String[]) {

    type ExtendedProps = T & ServiceProps

    return function EnhancedComponent(props: T): React.ReactElement<ExtendedProps> {
        const set_of_services_to_inject = new Set(services_to_inject)
        const services_to_pass: ServiceProps = services.filter(
            service => set_of_services_to_inject.has(service.name)
        ).reduce((acc, service) => {
            acc[`${service.name}`] = new service.Class();
            return acc;
        }, {})
        return <OriginalComponent {...props} {...services_to_pass} />
    }
}
