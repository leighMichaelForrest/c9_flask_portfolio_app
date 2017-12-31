import requests
import wikipedia

class Astronauts(object):
    url = 'http://api.open-notify.org/astros.json'

    @classmethod
    def _get(self):
        """Get json from the request."""
        response = requests.get(url=self.url)
        return response.json()

    @classmethod
    def get_astros(self):
        """Get a sanitized list of astronauts/cosmonauts from remote API."""
        astro_list = []
        # get the remote list
        remote_list = self._get()['people']

        # sanitize list
        for astro in remote_list:
            name = astro['name'].replace('kiy', 'ky').replace(' ', '_').lower()
            astro_list.append(name)
        # return list
        return astro_list

    @classmethod
    def get_astro_wikipedia(self, astro):
        """Get a dictionary with appropriate data."""
        # get wikipedia name and url
        astro_data = wikipedia.page(astro)

        # return that data
        return {'name': astro, 'url': astro_data.url}

    @classmethod
    def get_astro_data(self):
        data = []

        # get astronauts
        astros = self.get_astros()

        # get wikipedia data on each
        for astro in astros:
            datum = self.get_astro_wikipedia(astro)
            # add proper name
            datum['name'] = datum['name'].replace('_', ' ').title()
            data.append(datum)

        return data
