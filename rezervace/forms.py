# -*- coding: utf-8 -*-
from django import forms

SHOW_CHOICES = (
    ('', u'vyberte představení'),
    (u'LISTOPAD', [(show, show) for show in (
        u'3. 11. Romeo a Julie',
        u'4. 11. Stráže! Stráže!',
        u'6. 11. Viking Vike',
        u'9. 11. Experiment',
        u'14. 11. Blázníček a Jeleňovití',
        u'15. 11. Tři mušketýři',
        u'16. 11. Frank Pátý',
        u'20. 11. Dr. Jekyll a Mr. Hyde',
        u'21. 11. Romeo a Julie',
        u'24. 11. Dr. Jekyll a Mr. Hyde',
        u'29. 11. Don Juan',
        u'30. 11. A nezbyl ani jeden',
    )]),
    (u'PROSINEC', [(show, show) for show in (
        u'2. 12. Romeo a Julie',
        u'4. 12. Rakovnická hra vánoční',
        u'6. 12. Nesem vám noviny',
        u'7. 12. Tři mušketýři',
        u'8. 12. Dr. Jekyll a Mr. Hyde',
        u'12. 12. Raskolnikov',
        u'13. 12. A nezbyl ani jeden',
        u'14. 12. Experiment',
        u'15. 12. Nesem vám noviny',
        u'18. 12. Stráže! Stráže!',
        u'19. 12. Romeo a Julie',
        u'21. 12. Dr. Jekyll a Mr. Hyde',
    )]),
)

NUMBER_OF_TICKETS_CHOICES = (
    ('', 'vyberte'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

class ReserveTicketsForm(forms.Form):
    show = forms.ChoiceField(label=u'Představení', choices=SHOW_CHOICES)
    name = forms.CharField(label=u'Vaše jméno')
    email = forms.EmailField(label=u'Váš e-mail')
    number_of_tickets = forms.ChoiceField(label=u'Počet vstupenek', choices=NUMBER_OF_TICKETS_CHOICES)
