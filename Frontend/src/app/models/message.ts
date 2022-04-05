import {Chat} from './chat';

export interface Message {
  sender: string;
  chat: number;
  type: string;
  content?: string;
  choice_id?: number;
}
