
export default class ConversationFile {
    name: String;
    content: BinaryData;

    constructor({name, content}) {
        this.name = name;
        this.content = content;
    }
}
