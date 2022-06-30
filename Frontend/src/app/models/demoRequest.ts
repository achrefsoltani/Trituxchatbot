export interface DemoRequest {
  client: {
    firstName: string
    lastName: string;
    phone: string;
    email: string;
  };
  demo: {
    service: string;
    event_id: string;
  };
}
