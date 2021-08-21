interface IInfo {
  title: string;
  description: string;
}

export interface ICase extends IInfo {
  additional: string;
}

export interface ICard extends IInfo {
  color: string;
  class: string;
  to: string;
}
