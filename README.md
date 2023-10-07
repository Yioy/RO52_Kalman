# RO52_Kalman

Mise en application du filtre de Kalman pour améliorer la trajectoire détecté des robots EV3 de LEGO.
Nous avons utilisés plusieurs méthodes pour récupérer les coordonnées en X et Y du robot à chaque instant dans l'objectif de construire la trajectoire finale du robot sur un circuit donné.

Mise en application d'une commande P, PI et PID sur le robot pour réaliser une suivi de ligne. 
Pour cela, nous avions un capteur de couleur donnant un pourcentage de luminosité détecté par celui-ci. Ainsi si la luminosité était supérieur à 50%, nous pouvions dire que le robot était entrain de sortir du tracés noir au sol. Nous avons réaliser un asservissement de l'angle de rotation du robot à chaque instant afin que celui-ci suive correctement le tracé donné.

Mise en application d'un système de freinage anticipé en utilisant un robot leader et suiveur.
Nous avons implémenté 3 méthodes : 
  - 1ère : arrêt d'urgence du robot dès qu'une certaine distance leader-suiveur à été franchie.
  - 2ème : arrêt anticipé en utilisant le distance précédente.
  - 3ème : arrêt anticipé amélioré en prenant en compte l'accélération du robot.


