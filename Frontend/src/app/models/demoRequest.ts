export interface DemoRequest {
  client: {
    firstName: string
    lastName: string;
    phone: string;
    email: string;
  };
  demo: {
    service: string;
    date: string;
    event_id: string;
  };
}
