export interface Choice {
  id?: number;
  title_en: string;
  title_fr: string;
  response_en: string;
  response_fr: string;
  link_en: string;
  link_fr: string;
  next_choices: number[];
  previous_choices: number[];

}
