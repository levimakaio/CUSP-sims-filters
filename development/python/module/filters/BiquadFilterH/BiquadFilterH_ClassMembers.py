from ..projectHeader                    import *                                #project Header Script


biquadFilterTDF2_typ._fields_ = [('dimension'                             , I                                          ),
                                 ('pY'                                    , P(D)                                       ),
                                 ('pS1'                                   , P(D)                                       ),
                                 ('pS2'                                   , P(D)                                       ),
                                 ('coef'                                  , D * 6                                      ),
                                 ('isInit'                                , B                                          )]

