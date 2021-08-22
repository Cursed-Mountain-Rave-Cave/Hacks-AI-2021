export default interface ILink {
  title: string;
  to?: string;
  icon: string;
  child?: ILink[];
  disable: boolean;
}
