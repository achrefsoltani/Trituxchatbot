import {Chat} from './chat';

export interface Message {
  sender: string;
  chat: Chat;
  type: string;
  content?: string;
  choice_id?: number;
}
